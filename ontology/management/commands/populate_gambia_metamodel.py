"""
Management command to populate the Gambia National EA Metamodel in OpenEA.

Implements Step 3 from the OpenEA adoption plan:
  "Configure a Gambian-government metamodel in OpenEA"

Based on:
  - D2 EA Framework v1.0, Chapter 5: Enterprise Architecture Metamodel
  - GEATDM WP1-T11 Metamodel v1.0 (31 object types, 9 relationship types)

Usage:
  python manage.py populate_gambia_metamodel --org <organisation_name>

  If --org is not provided, defaults to 'GICTA'.

This command is idempotent - running it multiple times will not create
duplicates (uses get_or_create pattern).

Cross-reference verification:
  - 31 core GEATDM object types (GEATDM-WP1-T11 §2.2–2.8)
  - 2 building block types (D2 §5.3.5–5.3.7: ABB, SBB)
  - 1 governance type (Standard)
  - 6 controlled-vocabulary value types
  - 9 core + 16 extended relationship types
  - ~65 predicate triples covering all 4 traceability chains

Author: Aare Laponin, ITU Lead Architect
Date: 2025
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from ontology.models import (
    OConcept, OInstance, OModel, OPredicate, ORelation, OSlot, Repository
)
from organisation.models import Organisation


# =============================================================================
# METAMODEL DEFINITIONS
# =============================================================================

# Repository and Model names
REPOSITORY_NAME = "Gambia National EA Repository"
REPOSITORY_DESC = (
    "Authoritative repository for all architecture artefacts produced and "
    "maintained under the Gambia National Enterprise Architecture Framework. "
    "Operationalises the metamodel defined in D2 EA Framework Chapter 5."
)
MODEL_NAME = "Gambia National EA Metamodel"
MODEL_VERSION = "1.0"
MODEL_DESC = (
    "Core metamodel with 31 object types spanning Strategy, Service, Business, "
    "Application, Data, Technology, and Investment portfolio domains "
    "(per GEATDM WP1-T11), plus ABB/SBB building block types and governance "
    "value types (per D2 EA Framework Chapter 5)."
)

# =============================================================================
# CONCEPTS
# Organised by the 7 architecture domains per GEATDM-WP1-T11 §2.2–2.8
# =============================================================================
CONCEPTS = [
    # =========================================================================
    # STRATEGY DOMAIN (4 objects) — GEATDM-WP1-T11 §2.2
    # =========================================================================
    ("Vision",
     "A high-level aspirational description of what the organisation seeks to "
     "achieve in the long term. Time-bound with a defined horizon.",
     "Strategy"),
    ("Goal",
     "A qualitative statement of intent derived from the vision, providing "
     "direction for the organisation.",
     "Strategy"),
    ("Objective",
     "A time-bound, measurable target that supports achievement of a goal. "
     "Includes measure, target value, and target date.",
     "Strategy"),
    ("Initiative",
     "A coordinated programme of work designed to achieve one or more "
     "strategic objectives. Has status, start/end dates, and owner.",
     "Strategy"),

    # =========================================================================
    # SERVICE PORTFOLIO DOMAIN (2 objects) — GEATDM-WP1-T11 §2.3
    # =========================================================================
    ("BusinessService",
     "A defined performance that meets external customer or citizen needs. "
     "Represents what the organisation delivers to its external stakeholders. "
     "Attributes: Type, Status, Owning Unit.",
     "Service"),
    ("SupportService",
     "An internal service that enables business operations and supports the "
     "delivery of business services.",
     "Service"),

    # =========================================================================
    # BUSINESS PORTFOLIO DOMAIN (7 objects) — GEATDM-WP1-T11 §2.4
    # =========================================================================
    ("Customer",
     "A person, organisation, or group served by the public administration. "
     "Includes citizens, businesses, and other government entities.",
     "Business"),
    ("BusinessProcess",
     "An ordered series of activities that collectively deliver a business "
     "service or support service. Contains workflows. Supported by applications.",
     "Business"),
    ("Workflow",
     "An ordered series of process steps within an organisational unit, "
     "representing the detailed operational flow within a business process.",
     "Business"),
    ("Capability",
     "An organisational ability to perform a particular kind of work, "
     "combining people, process, and technology. Levelled 1–3.",
     "Business"),
    ("OrganisationUnit",
     "A structural grouping within the organisation: ministry, department, "
     "division, or unit. Performs processes and owns capabilities.",
     "Business"),
    ("Role",
     "A named specific behaviour of an individual participating in a "
     "particular context. Assigned to Organisation Units.",
     "Business"),
    ("Actor",
     "An entity that performs actions — can be a person, system, or external "
     "organisation. Fills Roles and executes Workflows.",
     "Business"),

    # =========================================================================
    # APPLICATION PORTFOLIO DOMAIN (4 objects) — GEATDM-WP1-T11 §2.5
    # =========================================================================
    ("Application",
     "A logical grouping of application functionality deployed as a coherent "
     "unit. Contains Application Components. Supports Business Processes. "
     "Examples: GamTax Net, DHIS2, IFMIS.",
     "Application"),
    ("ApplicationComponent",
     "A deployable software unit that delivers specific application "
     "functionality. Types: Module, Service, Library, Container. "
     "Provides Application Functions. Deployed on Technology Components.",
     "Application"),
    ("ApplicationFunction",
     "A grouping of related functionality offered by an application component. "
     "Types: User Interface, Processing, Data, Integration. "
     "Supports Workflows and Business Activities.",
     "Application"),
    ("ApplicationService",
     "An externally visible unit of functionality exposed by an application "
     "component, typically via an API. Has interface type, status, version.",
     "Application"),

    # =========================================================================
    # DATA (INFORMATION) PORTFOLIO DOMAIN (4 objects) — GEATDM-WP1-T11 §2.6
    # =========================================================================
    ("DataEntity",
     "A distinguishable real-world or abstract object about which data is "
     "stored. Types: Master, Reference, Transactional. Has classification "
     "and data steward. Examples: Taxpayer, License, Transaction.",
     "Data"),
    ("DataObject",
     "A passive element suitable for automated processing that stores or "
     "conveys information. An instance of a Data Entity processed by "
     "Applications.",
     "Data"),
    ("InformationFlow",
     "The exchange of data between processes or applications. Characterised "
     "by source, target, frequency (Real-time/Batch/Event-driven), and "
     "protocol.",
     "Data"),
    ("DataDomain",
     "A logical grouping of related data entities under common governance. "
     "Owned by Organisation Units. Examples: Revenue Data, Health Data.",
     "Data"),

    # =========================================================================
    # TECHNOLOGY PORTFOLIO DOMAIN (7 objects) — GEATDM-WP1-T11 §2.7
    # =========================================================================
    ("TechnologyComponent",
     "An infrastructure element such as a server, network device, storage "
     "system, or security appliance. Types: Server, Network, Storage, "
     "Security, Platform. Has vendor, model, location.",
     "Technology"),
    ("Server",
     "A computing resource providing processing capability. A specialised "
     "type of Technology Component. Hosts Application Components.",
     "Technology"),
    ("Network",
     "Communication infrastructure connecting technology components. "
     "Includes LAN, WAN, Internet links, VPN tunnels.",
     "Technology"),
    ("Location",
     "A physical or logical place where technology components are situated. "
     "Data centres, offices, cloud regions.",
     "Technology"),
    ("Deployment",
     "The assignment of an application component to a technology component "
     "in a specific environment (Development, Test, Production). "
     "Has deployment date.",
     "Technology"),
    ("Vendor",
     "An external provider of technology products or services.",
     "Technology"),
    ("ITCapability",
     "A technical ability provided by infrastructure, such as compute, "
     "storage, networking, or security services.",
     "Technology"),

    # =========================================================================
    # INVESTMENT PORTFOLIO DOMAIN (3 objects) — GEATDM-WP1-T11 §2.8
    # =========================================================================
    ("Project",
     "A temporary endeavour with defined start/end dates to create a unique "
     "product, service, or result. Implements Initiatives. Delivers Building "
     "Blocks. Has status and compliance outcome.",
     "Investment"),
    ("Demand",
     "A request for new or changed IT capability originating from business "
     "needs. Triggers Projects.",
     "Investment"),
    ("Budget",
     "Financial resources allocated for IT activities, linked to projects "
     "and programmes.",
     "Investment"),

    # =========================================================================
    # BUILDING BLOCKS (2 objects) — D2 §5.3.5–5.3.7
    # Not in GEATDM-WP1-T11 core 31, but committed to GICTA in D2 deliverable
    # =========================================================================
    ("ABB",
     "Architecture Building Block — a reusable, specification-level component "
     "that realises a Capability. Domain-aligned (Business, Data, Application, "
     "Technology). Implemented by SBBs.",
     "BuildingBlock"),
    ("SBB",
     "Solution Building Block — a concrete, implementation-level component "
     "that implements an ABB. Deployed as an Application Component. "
     "Has deployment status.",
     "BuildingBlock"),

    # =========================================================================
    # GOVERNANCE (1 object)
    # =========================================================================
    ("Standard",
     "A normative specification or guideline governing architecture decisions. "
     "Includes API standards, data standards, security standards, technology "
     "standards.",
     "Governance"),
]

# =============================================================================
# CONTROLLED-VOCABULARY VALUE TYPES
# Used as target concepts for property-style predicates
# =============================================================================
NATIVE_VALUE_CONCEPTS = [
    ("LifecycleStatus",
     "Controlled vocabulary for lifecycle states: Planned | InDevelopment | "
     "Pilot | Operational | Deprecated | Retired.",
     "Governance"),
    ("HealthRating",
     "Assessment of an element's condition: Green (healthy) | Amber "
     "(needs attention) | Red (critical).",
     "Governance"),
    ("ComplianceStatus",
     "Compliance review outcome: Compliant | ConditionallyCompliant | "
     "NonCompliant.",
     "Governance"),
    ("DeliveryStatus",
     "Project delivery status: NotStarted | InProgress | Delivered | "
     "Deferred | Cancelled.",
     "Governance"),
    ("Environment",
     "Deployment environment: Development | Test | Staging | Production | DR.",
     "Technology"),
    ("DataClassification",
     "Data sensitivity classification: Public | Internal | Confidential | "
     "Restricted.",
     "Governance"),
]

# =============================================================================
# RELATIONS
# 9 core types from GEATDM-WP1-T11 §3.1 + D2 §5.4.1
# Plus extended types for full metamodel coverage
# =============================================================================
RELATIONS = [
    # --- 9 Core relationship types (GEATDM-WP1-T11 §3.1 + D2 §5.4.1) ---
    ("realizes",
     "One element makes another element effective or brings it into "
     "existence. Example: Process realizes Service.",
     "PROP"),
    ("supports",
     "One element assists or enables another element. "
     "Example: Application supports Process.",
     "PROP"),
    ("uses",
     "One element employs or consumes another element. "
     "Example: Process uses Data Entity.",
     "PROP"),
    ("contains",
     "One element is composed of other elements (aggregation). "
     "Example: Application contains Application Components.",
     "PROP"),
    ("assignedTo",
     "Allocation of responsibility or ownership. "
     "Example: Role assigned to Organisation Unit.",
     "PROP"),
    ("serves",
     "Provision of functionality or value to another element. "
     "Example: Business Service serves Customer.",
     "PROP"),
    ("triggers",
     "One element initiates or causes the start of another. "
     "Example: Demand triggers Project.",
     "PROP"),
    ("flowsTo",
     "Movement of data or information from one element to another. "
     "Example: Information flows from Application A to Application B.",
     "PROP"),
    ("hosts",
     "Infrastructure provides runtime for software. "
     "Example: Server hosts Application Component. (D2 §5.4.1)",
     "PROP"),

    # --- Extended structural relationships ---
    ("isPartOf",
     "Hierarchical composition relationship. "
     "Example: Workflow is part of Business Process.",
     "PROP"),
    ("delivers",
     "A project or initiative produces an architecture building block. "
     "Example: Project delivers SBB.",
     "PROP"),
    ("implements",
     "A concrete element realises an abstract specification. "
     "Example: SBB implements ABB; Project implements Initiative. (D2 §5.4.1)",
     "PROP"),
    ("ownedBy",
     "Institutional ownership of an architecture element. "
     "Example: Application owned by OrganisationUnit.",
     "PROP"),
    ("hostedOn",
     "An application component runs on a technology component (inverse of hosts). "
     "Example: DHIS2 hosted on Ubuntu Server.",
     "PROP"),
    ("locatedAt",
     "A technology component is situated at a location. "
     "Example: Server located at GICTA Data Centre.",
     "PROP"),
    ("connectedTo",
     "Network connectivity between technology components.",
     "PROP"),
    ("suppliedBy",
     "A technology component or service is provided by a vendor.",
     "PROP"),
    ("funds",
     "A budget provides financial resources for a project.",
     "PROP"),
    ("compliesWith",
     "An element conforms to a standard or policy.",
     "PROP"),
    ("replaces",
     "One element supersedes another (lifecycle transition). "
     "Example: New Application replaces Legacy Application.",
     "PROP"),
    ("dependsOn",
     "An element requires another element to function. "
     "Example: IFMIS depends on Oracle Database.",
     "PROP"),
    ("carries",
     "An information flow transports a data entity. "
     "Example: InformationFlow carries DataEntity.",
     "PROP"),
    ("manages",
     "An application manages (is responsible for) a data entity. "
     "Example: ITAS manages TaxpayerRecord.",
     "PROP"),
    ("exposedBy",
     "An application service is exposed by an application component. "
     "Example: Tax Filing API exposed by GamTax Net.",
     "PROP"),

    # --- Inheritance relationship ---
    ("isA",
     "Subtype/specialisation relationship. "
     "Example: Server is-a Technology Component.",
     "HESR"),

    # --- Property-type relationships ---
    ("hasLifecycleStatus",
     "An element has a lifecycle state: Planned, In Development, Pilot, "
     "Operational, Deprecated, Retired.",
     "PROP"),
    ("hasComplianceStatus",
     "A project linkage has a compliance review outcome: Compliant, "
     "Conditionally Compliant, Non-Compliant.",
     "PROP"),
    ("hasProperty",
     "An element has a named property or attribute value.",
     "PROP"),
]

# =============================================================================
# PREDICATES (ONTOLOGY TRIPLES)
# Define allowed relationships between concept types
# Verified against all 4 traceability chains from D2 §5.4.4 and
# per-object "Key Relationships" from GEATDM-WP1-T11 §2.2–2.8
# =============================================================================
PREDICATES = [
    # =========================================================================
    # CHAIN 1: Strategy to Execution
    # D2 §5.4.4: Vision → Goal → Objective → Initiative → Project → BB → Deployment
    #
    # Per D2 §5.3.1:
    #   Vision: "Realised by → Goal"    → Goal realizes Vision
    #   Goal: "Supports → Vision; Achieved through → Objective"
    #   Objective: "Supports → Goal; Realised by → Initiative"
    #   Initiative: "Realises → Objective; Delivered by → Project"
    # =========================================================================
    ("Goal", "realizes", "Vision"),
    ("Goal", "supports", "Vision"),
    ("Objective", "supports", "Goal"),
    ("Initiative", "realizes", "Objective"),
    ("Project", "implements", "Initiative"),
    ("Project", "delivers", "SBB"),
    ("Project", "delivers", "ApplicationComponent"),
    ("Project", "delivers", "TechnologyComponent"),

    # =========================================================================
    # CHAIN 2: Service to Technology
    # D2 §5.4.4: Customer → Service → Process → Application Component → Technology Component
    #
    # Per D2 §5.3.2–5.3.3 and GEATDM-WP1-T11 §2.3–2.4:
    #   Business Service: "Serves → Customer; Realised by → Process"
    #   Support Service: "Supports → Business Service; Realised by → Process"
    #   Business Process: "Realises → Service; Contains → Workflow; Supported by → Application"
    #   Workflow: "Part of → Business Process; Supported by → Application Functions"
    # =========================================================================
    ("BusinessService", "serves", "Customer"),
    ("SupportService", "supports", "BusinessService"),
    ("BusinessProcess", "realizes", "BusinessService"),
    ("BusinessProcess", "realizes", "SupportService"),
    ("BusinessProcess", "contains", "Workflow"),
    ("Application", "supports", "BusinessProcess"),
    ("ApplicationComponent", "supports", "Workflow"),
    ("ApplicationFunction", "supports", "Workflow"),

    # =========================================================================
    # CHAIN 4: Capability Realisation
    # D2 §5.4.4: Capability → Process → Application Function → Application Component
    #
    # Per D2 §5.3.2–5.3.3:
    #   Capability: "Enabled by → Process; Supported by → Application"
    #   Organisation Unit: "Performs → Process; Owns → Capability"
    # =========================================================================
    ("BusinessProcess", "realizes", "Capability"),
    ("Application", "supports", "Capability"),
    ("ApplicationFunction", "realizes", "Capability"),

    # =========================================================================
    # Organisation & Roles — GEATDM-WP1-T11 §2.4
    # =========================================================================
    ("OrganisationUnit", "contains", "OrganisationUnit"),  # hierarchy
    ("Role", "assignedTo", "OrganisationUnit"),
    ("Actor", "assignedTo", "Role"),
    ("BusinessProcess", "assignedTo", "OrganisationUnit"),
    ("Capability", "ownedBy", "OrganisationUnit"),

    # =========================================================================
    # Application Landscape — GEATDM-WP1-T11 §2.5
    #   Application: "Contains App Components; Supports Processes"
    #   App Component: "Part of Application; Provides App Functions"
    #   App Function: "Provided by App Components"
    #   App Service: "Exposed by App Components; Used by Processes"
    # =========================================================================
    ("Application", "contains", "ApplicationComponent"),
    ("ApplicationComponent", "contains", "ApplicationFunction"),
    ("ApplicationService", "exposedBy", "ApplicationComponent"),
    ("ApplicationComponent", "hostedOn", "TechnologyComponent"),

    # =========================================================================
    # CHAIN 3: Data Lineage
    # D2 §5.4.4: Data Entity → Data Object → Application Component → Information Flow → Process
    #
    # Per D2 §5.3.5–5.3.7 and GEATDM-WP1-T11 §2.6:
    #   Data Entity: "Used by → Process; Managed by → Application"
    #   Data Object: "Instance of → Data Entity; Processed by → Applications"
    #   Information Flow: "From/To → App Component/Process; Carries → Data Entity"
    #   Data Domain: "Contains → Data Entities; Owned by → Org Units"
    # =========================================================================
    ("DataDomain", "contains", "DataEntity"),
    ("DataObject", "isPartOf", "DataEntity"),
    ("BusinessProcess", "uses", "DataEntity"),
    ("Application", "manages", "DataEntity"),
    ("ApplicationComponent", "uses", "DataObject"),
    ("InformationFlow", "carries", "DataEntity"),
    ("InformationFlow", "flowsTo", "ApplicationComponent"),
    ("InformationFlow", "flowsTo", "BusinessProcess"),
    ("DataEntity", "ownedBy", "OrganisationUnit"),
    ("DataDomain", "ownedBy", "OrganisationUnit"),

    # =========================================================================
    # Technology Infrastructure — GEATDM-WP1-T11 §2.7
    #   Technology Component: "Hosts → App Component; Located at → Location"
    #   Server: "Type of → Technology Component; Hosts → App Component"
    #   Network: "Connects → Technology Components"
    #   Location: "Contains → Technology Components"
    #   Deployment: "Maps App Component → Technology Component"
    #   Vendor: "Supplies → Technology Components"
    #   IT Capability: "Enabled by → Technology Components"
    # =========================================================================
    ("Server", "isA", "TechnologyComponent"),
    ("TechnologyComponent", "hosts", "ApplicationComponent"),
    ("TechnologyComponent", "locatedAt", "Location"),
    ("Location", "contains", "TechnologyComponent"),
    ("Network", "connectedTo", "TechnologyComponent"),
    ("TechnologyComponent", "suppliedBy", "Vendor"),
    ("TechnologyComponent", "supports", "ITCapability"),
    ("Deployment", "uses", "ApplicationComponent"),
    ("Deployment", "hostedOn", "TechnologyComponent"),

    # =========================================================================
    # Investment Management — GEATDM-WP1-T11 §2.8
    # =========================================================================
    ("Demand", "triggers", "Project"),
    ("Budget", "funds", "Project"),

    # =========================================================================
    # Building Blocks — D2 §5.3.5–5.3.7
    #   ABB: "Realises → Capability; Implemented by → SBB"
    #   SBB: "Implements → ABB; Deployed as → App Component"
    # =========================================================================
    ("ABB", "realizes", "Capability"),
    ("SBB", "implements", "ABB"),
    ("SBB", "contains", "ApplicationComponent"),

    # =========================================================================
    # Cross-Domain Governance & Ownership
    # =========================================================================
    ("Application", "ownedBy", "OrganisationUnit"),
    ("TechnologyComponent", "ownedBy", "OrganisationUnit"),
    ("ApplicationComponent", "compliesWith", "Standard"),
    ("TechnologyComponent", "compliesWith", "Standard"),
    ("Application", "replaces", "Application"),
    ("TechnologyComponent", "replaces", "TechnologyComponent"),
    ("Application", "dependsOn", "Application"),
    ("ApplicationComponent", "dependsOn", "ApplicationComponent"),
    ("TechnologyComponent", "dependsOn", "TechnologyComponent"),

    # =========================================================================
    # Lifecycle & Status Properties
    # Per D2 §8.1.2 (Repository Functional Requirements)
    # =========================================================================
    ("Application", "hasLifecycleStatus", "LifecycleStatus"),
    ("ApplicationComponent", "hasLifecycleStatus", "LifecycleStatus"),
    ("TechnologyComponent", "hasLifecycleStatus", "LifecycleStatus"),
    ("Project", "hasLifecycleStatus", "DeliveryStatus"),
    ("Application", "hasProperty", "HealthRating"),
    ("TechnologyComponent", "hasProperty", "HealthRating"),
    ("Project", "hasComplianceStatus", "ComplianceStatus"),
    ("DataEntity", "hasProperty", "DataClassification"),
    ("Deployment", "hasProperty", "Environment"),
]


class Command(BaseCommand):
    help = (
        "Populate the Gambia National EA Metamodel in OpenEA. "
        "Creates Repository, Model, Concepts (31+2+1+6 = 40 types), "
        "Relations (28 relationship types), and Predicates (ontology triples). "
        "Idempotent: safe to run multiple times."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--org',
            type=str,
            default='GICTA',
            help='Organisation name in OpenEA (default: GICTA)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Print what would be created without making changes.',
        )

    def handle(self, *args, **options):
        org_name = options['org']
        dry_run = options['dry_run']

        # Resolve organisation
        try:
            organisation = Organisation.objects.get(name=org_name)
        except Organisation.DoesNotExist:
            raise CommandError(
                f"Organisation '{org_name}' not found. "
                f"Create it first with: python manage.py create_organisation "
                f"{org_name} --users <username>"
            )

        if dry_run:
            self._print_plan()
            return

        with transaction.atomic():
            # 1. Create Repository
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 1: Repository ==="
            ))
            repository, created = Repository.objects.get_or_create(
                name=REPOSITORY_NAME,
                organisation=organisation,
                defaults={'description': REPOSITORY_DESC}
            )
            if not created:
                repository.description = REPOSITORY_DESC
                repository.save()
            self._report("Repository", REPOSITORY_NAME, created)

            # 2. Create Model
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 2: Model ==="
            ))
            model, created = OModel.objects.get_or_create(
                name=MODEL_NAME,
                version=MODEL_VERSION,
                repository=repository,
                organisation=organisation,
                defaults={'description': MODEL_DESC}
            )
            if not created:
                model.description = MODEL_DESC
                model.save()
            self._report("Model", f"{MODEL_NAME} v{MODEL_VERSION}", created)

            # 3. Create Concepts
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 3: Concepts ==="
            ))
            concept_map = {}
            all_concepts = CONCEPTS + NATIVE_VALUE_CONCEPTS

            for name, description, domain in all_concepts:
                concept, created = OConcept.objects.get_or_create(
                    name=name,
                    model=model,
                    organisation=organisation,
                    defaults={'description': description}
                )
                if not created:
                    concept.description = description
                    concept.save()
                concept_map[name] = concept
                self._report("Concept", f"[{domain}] {name}", created)

            # 4. Create Relations
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 4: Relations ==="
            ))
            relation_map = {}

            for name, description, rel_type in RELATIONS:
                relation, created = ORelation.objects.get_or_create(
                    name=name,
                    model=model,
                    organisation=organisation,
                    defaults={
                        'description': description,
                        'type': rel_type,
                    }
                )
                if not created:
                    relation.description = description
                    relation.type = rel_type
                    relation.save()
                relation_map[name] = relation
                self._report("Relation", f"{name} ({rel_type})", created)

            # 5. Create Predicates (ontology triples)
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 5: Predicates (Ontology Triples) ==="
            ))
            predicate_count = 0
            created_count = 0
            skip_count = 0

            for subject_name, relation_name, object_name in PREDICATES:
                subject = concept_map.get(subject_name)
                relation = relation_map.get(relation_name)
                obj = concept_map.get(object_name)

                if not subject:
                    self.stderr.write(
                        f"  WARNING: Subject concept '{subject_name}' "
                        f"not found, skipping."
                    )
                    skip_count += 1
                    continue
                if not relation:
                    self.stderr.write(
                        f"  WARNING: Relation '{relation_name}' "
                        f"not found, skipping."
                    )
                    skip_count += 1
                    continue
                if not obj:
                    self.stderr.write(
                        f"  WARNING: Object concept '{object_name}' "
                        f"not found, skipping."
                    )
                    skip_count += 1
                    continue

                predicate, was_created = OPredicate.objects.get_or_create(
                    subject=subject,
                    relation=relation,
                    object=obj,
                    model=model,
                    organisation=organisation,
                    defaults={
                        'description': (
                            f"{subject_name} {relation_name} {object_name}"
                        )
                    }
                )
                predicate_count += 1
                if was_created:
                    created_count += 1
                triple = f"{subject_name} → {relation_name} → {object_name}"
                self._report("Predicate", triple, was_created)

            # Summary
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n" + "=" * 60
            ))
            self.stdout.write(self.style.MIGRATE_HEADING(
                "  SUMMARY"
            ))
            self.stdout.write(self.style.MIGRATE_HEADING(
                "=" * 60
            ))
            self.stdout.write(
                f"  Repository : {REPOSITORY_NAME}"
            )
            self.stdout.write(
                f"  Model      : {MODEL_NAME} v{MODEL_VERSION}"
            )
            self.stdout.write(
                f"  Concepts   : {len(all_concepts)} "
                f"(31 core GEATDM + 2 BB + 1 governance + 6 value types)"
            )
            self.stdout.write(
                f"  Relations  : {len(RELATIONS)}"
            )
            self.stdout.write(
                f"  Predicates : {predicate_count} verified "
                f"({created_count} new, {skip_count} skipped)"
            )
            self.stdout.write("")

            self._verify_traceability_chains(concept_map, relation_map, model)

            self.stdout.write(self.style.SUCCESS(
                "\n✓ Gambia National EA Metamodel populated successfully!\n"
            ))
            self.stdout.write(
                "Next steps:\n"
                "  1. Open OpenEA and navigate to the model's Ontology Diagram.\n"
                "  2. Verify all 4 traceability chains are visible.\n"
                "  3. Proceed to Step 4: populate As-Is instances "
                "(ministries, apps, etc.).\n"
            )

    def _report(self, obj_type, name, created):
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"  ✓ Created {obj_type}: {name}")
            )
        else:
            self.stdout.write(f"  · Updated {obj_type}: {name}")

    def _verify_traceability_chains(self, concept_map, relation_map, model):
        """Verify the 4 critical traceability chains from D2 §5.4.4."""
        self.stdout.write(self.style.MIGRATE_HEADING(
            "\n  Traceability Chain Verification:"
        ))

        chains = {
            "Chain 1 (Strategy→Execution)": [
                ("Goal", "realizes", "Vision"),
                ("Objective", "supports", "Goal"),
                ("Initiative", "realizes", "Objective"),
                ("Project", "implements", "Initiative"),
                ("Project", "delivers", "SBB"),
            ],
            "Chain 2 (Service→Technology)": [
                ("BusinessService", "serves", "Customer"),
                ("BusinessProcess", "realizes", "BusinessService"),
                ("Application", "supports", "BusinessProcess"),
                ("ApplicationComponent", "hostedOn", "TechnologyComponent"),
            ],
            "Chain 3 (Data Lineage)": [
                ("DataObject", "isPartOf", "DataEntity"),
                ("ApplicationComponent", "uses", "DataObject"),
                ("InformationFlow", "carries", "DataEntity"),
                ("InformationFlow", "flowsTo", "BusinessProcess"),
            ],
            "Chain 4 (Capability Realisation)": [
                ("BusinessProcess", "realizes", "Capability"),
                ("ApplicationFunction", "realizes", "Capability"),
                ("ApplicationComponent", "contains", "ApplicationFunction"),
            ],
        }

        all_ok = True
        for chain_name, links in chains.items():
            chain_ok = True
            for s, r, o in links:
                subject = concept_map.get(s)
                relation = relation_map.get(r)
                obj = concept_map.get(o)
                if subject and relation and obj:
                    exists = OPredicate.objects.filter(
                        subject=subject,
                        relation=relation,
                        object=obj,
                        model=model,
                    ).exists()
                    if not exists:
                        chain_ok = False
                        all_ok = False
                else:
                    chain_ok = False
                    all_ok = False

            status = "✓" if chain_ok else "✗"
            style = self.style.SUCCESS if chain_ok else self.style.ERROR
            self.stdout.write(style(f"    {status} {chain_name}"))

        if all_ok:
            self.stdout.write(self.style.SUCCESS(
                "    All 4 traceability chains verified."
            ))

    def _print_plan(self):
        self.stdout.write(self.style.MIGRATE_HEADING(
            "\n=== DRY RUN: Gambia National EA Metamodel ===\n"
        ))

        self.stdout.write(f"Repository: {REPOSITORY_NAME}")
        self.stdout.write(f"Model: {MODEL_NAME} v{MODEL_VERSION}\n")

        all_concepts = CONCEPTS + NATIVE_VALUE_CONCEPTS

        self.stdout.write(self.style.MIGRATE_HEADING("Concepts to create:"))
        current_domain = None
        domain_counts = {}
        for name, desc, domain in all_concepts:
            if domain != current_domain:
                self.stdout.write(f"\n  [{domain}]")
                current_domain = domain
            self.stdout.write(f"    - {name}")
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\n  Domain breakdown: {domain_counts}"
        ))

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nRelations to create ({len(RELATIONS)}):"
        ))
        for name, desc, rel_type in RELATIONS:
            self.stdout.write(f"    - {name} ({rel_type})")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nPredicates to create ({len(PREDICATES)}):"
        ))
        for s, r, o in PREDICATES:
            self.stdout.write(f"    {s} → {r} → {o}")

        # Check for duplicate predicates
        seen = set()
        dupes = []
        for p in PREDICATES:
            if p in seen:
                dupes.append(p)
            seen.add(p)
        if dupes:
            self.stderr.write(self.style.ERROR(
                f"\n  WARNING: {len(dupes)} duplicate predicate(s) found:"
            ))
            for d in dupes:
                self.stderr.write(f"    {d[0]} → {d[1]} → {d[2]}")
        else:
            self.stdout.write(self.style.SUCCESS(
                "\n  ✓ No duplicate predicates."
            ))

        self.stdout.write(
            f"\n  TOTALS: {len(all_concepts)} concepts, "
            f"{len(RELATIONS)} relations, "
            f"{len(PREDICATES)} predicates\n"
        )
