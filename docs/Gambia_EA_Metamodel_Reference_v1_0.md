# Gambia National EA Metamodel Reference v1.0

> Companion to D2: Enterprise Architecture Framework v1.0, Chapter 5
> Source specification: GEATDM WP1-T11 Metamodel v1.0
> Date: February 2026

---

## 1. Metamodel Summary

| Component | Count | Detail |
|-----------|-------|--------|
| Core Object Types | 31 | GEATDM standard across 7 domains |
| Building Block Types | 2 | ABB (specification), SBB (implementation) |
| Governance Types | 1 + 6 | Standard + 6 controlled vocabularies |
| **Total Concepts** | **40** | |
| Relationship Types | 28 | 9 core + 16 extended + 3 property-type |
| Allowed Triples | 70 | Valid subject–relationship–object combinations |
| Architecture Domains | 7 | Strategy, Service, Business, Application, Data, Technology, Investment |

---

## 2. Architecture Domains

| Domain | Objects | Focus | Key Question |
|--------|---------|-------|--------------|
| **Strategy** | 4 | National direction and priorities | Where are we going and why? |
| **Service** | 2 | What government delivers to citizens | What services do we provide? |
| **Business** | 7 | How government operates | Who does what, and how? |
| **Application** | 4 | Software systems used | What systems support the work? |
| **Data** | 4 | Information managed | What data exists and where does it flow? |
| **Technology** | 7 | Physical and virtual infrastructure | What hardware and networks run it all? |
| **Investment** | 3 | Budgets, projects, and demands | How do we fund and deliver change? |

Plus: 2 Building Block types (ABB, SBB), 1 Governance type (Standard), 6 controlled vocabularies.

---

## 3. Complete Object Catalogue

### 3.1 Strategy Domain (4 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **Vision** | Long-term aspiration. Example: "Digital Gambia 2033." | ID, Name, Description, Time Horizon, Owner, Status | Realised by → Goal |
| **Goal** | Qualitative intent from Vision. Example: "Improve public service delivery through digital channels." | ID, Name, Description, Owner | Supports → Vision; Achieved through → Objective |
| **Objective** | Measurable, time-bound target. Example: "70% of services online by 2030." | ID, Name, Description, Measure, Target, Target Date, Owner | Supports → Goal; Realised by → Initiative |
| **Initiative** | Structured programme. Example: "Government Payment Gateway Expansion." | ID, Name, Description, Status, Start/End Date, Owner | Realises → Objective; Delivered by → Project |

### 3.2 Service Domain (2 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **BusinessService** | External service to citizens/businesses. Examples: "Tax Return Filing," "Birth Certificate Issuance," "Drug Registration." | ID, Name, Description, Type, Status, Owning Unit | Serves → Customer; Realised by → Business Process |
| **SupportService** | Internal enabling service. Examples: "Payroll Processing," "IT Helpdesk." | ID, Name, Description, Type, Status | Supports → BusinessService; Realised by → Business Process |

### 3.3 Business Domain (7 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **Customer** | Person/org served by government. Examples: "Taxpayer," "Health Facility," "Importer." | ID, Name, Description, Type (Citizen/Business/Government) | Receives → BusinessService |
| **BusinessProcess** | Ordered activities delivering a service. Examples: "Tax Registration Process," "HMIS Data Collection." | ID, Name, Description, Type, Owner, Status | Realises → Service; Contains → Workflow; Supported by → Application |
| **Workflow** | Detailed steps within one org unit. Example: "Taxpayer Verification Workflow." | ID, Name, Description, Sequence, Owner | Part of → BusinessProcess; Supported by → ApplicationFunction |
| **Capability** | Organisational ability (people + process + tech). Examples: "Revenue Collection," "Disease Surveillance." Levels 1–3. | ID, Name, Description, Level (1–3) | Enabled by → Process; Supported by → Application; Owned by → OrganisationUnit |
| **OrganisationUnit** | Ministry, department, division, unit. Examples: "GRA Domestic Tax Division," "MoH Directorate of Health Services." | ID, Name, Description, Type | Performs → Process; Owns → Capability; Contains → OrganisationUnit |
| **Role** | Named function performed by a person. Examples: "Tax Officer," "District Health Officer," "IT Focal Point." | ID, Name, Description | Assigned to → OrganisationUnit |
| **Actor** | Entity filling a Role. Examples: "Customs Officer Jallow," "GamTax Net (automated actor)." | ID, Name, Description, Type (Person/System/External) | Fills → Role; Executes → Workflow |

### 3.4 Application Domain (4 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **Application** | Complete software system. Examples: "GamTax Net (ITAS)," "DHIS2," "IFMIS," "ASYCUDA World." | ID, Name, Description, Type, Status, Version, Owning Unit | Contains → ApplicationComponent; Supports → BusinessProcess; Owned by → OrganisationUnit |
| **ApplicationComponent** | Deployable module. Examples: "GamTax Net — Registration Module," "DHIS2 — Tracker Module." | ID, Name, Description, Type (Module/Service/Container), Status | Part of → Application; Provides → ApplicationFunction; Hosted on → TechnologyComponent |
| **ApplicationFunction** | Grouping of functionality. Examples: "Taxpayer Search Function," "Disease Notification Function." | ID, Name, Description, Type (UI/Processing/Data/Integration) | Provided by → ApplicationComponent; Supports → Workflow |
| **ApplicationService** | Externally visible API/interface. Examples: "GamPay Payment API," "DHIS2 Data Exchange API." | ID, Name, Description, Interface Type, Status, Version | Exposed by → ApplicationComponent |

### 3.5 Data Domain (4 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **DataEntity** | Real-world thing data is stored about. Examples: "Taxpayer," "Health Facility," "Budget Allocation." | ID, Name, Description, Type (Master/Reference/Transactional), Classification, Steward | Used by → BusinessProcess; Managed by → Application; Belongs to → DataDomain |
| **DataObject** | Specific data structure. Examples: "Taxpayer Registration Form," "HMIS Monthly Report." | ID, Name, Description, Format | Instance of → DataEntity; Processed by → ApplicationComponent |
| **InformationFlow** | Data exchange between systems/processes. Example: "Tax payment confirmation from GamPay to GamTax Net." | ID, Name, Description, Source, Target, Frequency (Real-time/Batch/Event), Protocol | From/To → ApplicationComponent or BusinessProcess; Carries → DataEntity |
| **DataDomain** | Logical grouping. Examples: "Revenue Data," "Health Data," "Public Finance Data." | ID, Name, Description, Steward | Contains → DataEntity; Owned by → OrganisationUnit |

### 3.6 Technology Domain (7 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **TechnologyComponent** | Any infrastructure element. Examples: "GICTA Primary DB Server," "Firewall Appliance," "Azure Subscription." | ID, Name, Description, Type (Server/Network/Storage/Security/Platform), Status, Vendor, Model, Location | Hosts → ApplicationComponent; Located at → Location; Supplied by → Vendor |
| **Server** | Computing resource (specialised TechnologyComponent). Example: "HP ProLiant DL380 (GICTA DC)." | ID, Name, Description, Type, Status, OS, CPU, RAM | Is a → TechnologyComponent; Hosts → ApplicationComponent |
| **Network** | Communication links. Examples: "GICTA-MoFEA Fibre Link," "Government VPN." | ID, Name, Description, Type (LAN/WAN/VPN/Internet), Bandwidth, Status | Connected to → TechnologyComponent |
| **Location** | Physical or logical place. Examples: "GICTA Data Centre, Kanifing," "Azure West Europe Region." | ID, Name, Description, Type, Address | Contains → TechnologyComponent |
| **Deployment** | Software-to-infrastructure mapping. Example: "DHIS2 on Ubuntu VM at GICTA DC (Production)." | ID, ApplicationComponent, TechnologyComponent, Environment, Date | Maps → ApplicationComponent to TechnologyComponent |
| **Vendor** | External supplier. Examples: "Crown Agents (ASYCUDA)," "HISP (DHIS2)," "FreeBalance (IFMIS)." | ID, Name, Description, Contact, Contract Status | Supplies → TechnologyComponent |
| **ITCapability** | Technical ability. Examples: "Compute Services," "Backup and Recovery," "Internet Connectivity." | ID, Name, Description | Enabled by → TechnologyComponent |

### 3.7 Investment Domain (3 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **Project** | Funded, time-bound endeavour. Examples: "IFMIS-GRA Integration Project," "GamPay Expansion Phase 2." | ID, Name, Description, Status, Start/End Date, Owner, Budget, Compliance Outcome | Implements → Initiative; Delivers → SBB or ApplicationComponent |
| **Demand** | Request for new/changed capability. Example: "Request for online business registration." | ID, Name, Description, Priority, Requesting Unit, Status | Triggers → Project |
| **Budget** | Allocated financial resources. Examples: "WARDIP Component 4 EA Budget," "GICTA FY2026 ICT Capital." | ID, Name, Amount, Source (GoTG/Donor/PPP), Period | Funds → Project |

### 3.8 Building Block Types (2 objects)

| Object | Description | Key Attributes | Key Relationships |
|--------|-------------|----------------|-------------------|
| **ABB** | Architecture Building Block — specification-level. Examples: "Payment BB," "Registration BB," "Identity BB." | ID, Name, Description, Domain, Type | Realises → Capability; Implemented by → SBB |
| **SBB** | Solution Building Block — implementation-level. Examples: "GamPay (implements Payment BB)." | ID, Name, Description, ABB Reference, Deployment Status | Implements → ABB; Contains → ApplicationComponent |

### 3.9 Governance and Controlled Vocabularies

| Object | Purpose | Allowed Values |
|--------|---------|----------------|
| **Standard** | Normative specification governing architecture decisions | E.g., "REST API Standard," "Data Classification Policy" |
| **LifecycleStatus** | Where an application/technology is in its life | Planned → InDevelopment → Pilot → Operational → Deprecated → Retired |
| **HealthRating** | Condition assessment for portfolio management | Green (healthy), Amber (needs attention), Red (critical) |
| **ComplianceStatus** | EA compliance review outcome for projects | Compliant, Conditionally Compliant, Non-Compliant |
| **DeliveryStatus** | Project delivery progress | Not Started, In Progress, Delivered, Deferred, Cancelled |
| **Environment** | Where software is deployed | Development, Test, Staging, Production, DR |
| **DataClassification** | Data sensitivity level | Public, Internal, Confidential, Restricted |

---

## 4. Relationship Types

### 4.1 Nine Core Relationships

| Relationship | Meaning | Direction Rule | Gambian Example |
|--------------|---------|----------------|-----------------|
| **realizes** | Makes effective | Source brings Target into effect | BusinessProcess realizes BusinessService |
| **supports** | Assists/enables | Source helps Target | Application supports BusinessProcess |
| **uses** | Employs/consumes | Source consumes Target | BusinessProcess uses DataEntity |
| **contains** | Parent–child composition | Source is parent of Target | Application contains ApplicationComponent |
| **assignedTo** | Responsibility allocation | Source is allocated to Target | Role assignedTo OrganisationUnit |
| **serves** | Provides value to | Source provides to Target | BusinessService serves Customer |
| **triggers** | Causes to begin | Source initiates Target | Demand triggers Project |
| **flowsTo** | Data movement | Source sends to Target | InformationFlow flowsTo ApplicationComponent |
| **hosts** | Provides runtime | Source runs Target | TechnologyComponent hosts ApplicationComponent |

### 4.2 Extended Relationships

| Relationship | Meaning | Example |
|--------------|---------|---------|
| **isPartOf** | Hierarchical sub-component | Workflow isPartOf BusinessProcess |
| **delivers** | Project produces element | Project delivers SBB |
| **implements** | Concrete realises abstract | SBB implements ABB |
| **ownedBy** | Institutional ownership | Application ownedBy OrganisationUnit |
| **hostedOn** | Software runs on infra (inverse of hosts) | ApplicationComponent hostedOn TechnologyComponent |
| **locatedAt** | Infrastructure at a place | TechnologyComponent locatedAt Location |
| **connectedTo** | Network link | Network connectedTo TechnologyComponent |
| **suppliedBy** | Provided by vendor | TechnologyComponent suppliedBy Vendor |
| **funds** | Budget finances project | Budget funds Project |
| **compliesWith** | Conforms to standard | ApplicationComponent compliesWith Standard |
| **replaces** | Lifecycle succession | Application replaces Application |
| **dependsOn** | Requires another element | GamTax Net dependsOn Oracle Database |
| **carries** | Info flow transports data | InformationFlow carries DataEntity |
| **manages** | App responsible for data | Application manages DataEntity |
| **exposedBy** | API provided by component | ApplicationService exposedBy ApplicationComponent |
| **isA** | Specialisation/subtype | Server isA TechnologyComponent |

### 4.3 Property-Type Relationships

| Relationship | Purpose |
|--------------|---------|
| **hasLifecycleStatus** | Links element to LifecycleStatus or DeliveryStatus |
| **hasComplianceStatus** | Links project to ComplianceStatus |
| **hasProperty** | Links element to HealthRating, DataClassification, or Environment |

---

## 5. Four Traceability Chains

### Chain 1: Strategy to Execution
**Question:** "How does this project connect to our national strategy?"

```
Vision → Goal → Objective → Initiative → Project → SBB → Deployment
```

**Gambian example:** Digital Gambia 2033 Vision → Goal: Improve revenue mobilisation → Objective: Tax-to-GDP 15% by 2028 → Initiative: Tax Admin Modernisation → Project: GamTax Net Enhancement → SBB: e-Filing Module → GICTA production server.

### Chain 2: Service to Technology
**Question:** "If this server goes down, which citizen services are affected?"

```
Customer → BusinessService → BusinessProcess → Application → ApplicationComponent → TechnologyComponent
```

**Gambian example:** Taxpayer → Tax Return Filing → Return Processing Process → GamTax Net → Filing Module → HP ProLiant at GICTA DC.

### Chain 3: Data Lineage
**Question:** "Where does this data come from, where does it go, who owns it?"

```
DataEntity → DataObject → ApplicationComponent → InformationFlow → BusinessProcess
```

**Gambian example:** Taxpayer (entity) → Registration Form (object) → GamTax Net Registration Module → TIN Verification Flow to IFMIS → Budget Allocation Process at MoFEA.

### Chain 4: Capability Realisation
**Question:** "How is this organisational capability actually delivered?"

```
Capability → BusinessProcess → ApplicationFunction → ApplicationComponent
```

**Gambian example:** Revenue Collection → Payment Processing Process → Payment Gateway Function → GamPay Gateway Component.

---

## 6. Complete Allowed Triples (70)

### Strategy Domain
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 1 | Goal | realizes | Vision |
| 2 | Goal | supports | Vision |
| 3 | Objective | supports | Goal |
| 4 | Initiative | realizes | Objective |
| 5 | Project | implements | Initiative |
| 6 | Project | delivers | SBB |
| 7 | Project | delivers | ApplicationComponent |
| 8 | Project | delivers | TechnologyComponent |

### Service and Business Domains
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 9 | BusinessService | serves | Customer |
| 10 | SupportService | supports | BusinessService |
| 11 | BusinessProcess | realizes | BusinessService |
| 12 | BusinessProcess | realizes | SupportService |
| 13 | BusinessProcess | contains | Workflow |
| 14 | Application | supports | BusinessProcess |
| 15 | ApplicationComponent | supports | Workflow |
| 16 | ApplicationFunction | supports | Workflow |

### Capability Realisation
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 17 | BusinessProcess | realizes | Capability |
| 18 | Application | supports | Capability |
| 19 | ApplicationFunction | realizes | Capability |

### Organisation and Roles
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 20 | OrganisationUnit | contains | OrganisationUnit |
| 21 | Role | assignedTo | OrganisationUnit |
| 22 | Actor | assignedTo | Role |
| 23 | BusinessProcess | assignedTo | OrganisationUnit |
| 24 | Capability | ownedBy | OrganisationUnit |

### Application Landscape
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 25 | Application | contains | ApplicationComponent |
| 26 | ApplicationComponent | contains | ApplicationFunction |
| 27 | ApplicationService | exposedBy | ApplicationComponent |
| 28 | ApplicationComponent | hostedOn | TechnologyComponent |

### Data and Information Flows
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 29 | DataDomain | contains | DataEntity |
| 30 | DataObject | isPartOf | DataEntity |
| 31 | BusinessProcess | uses | DataEntity |
| 32 | Application | manages | DataEntity |
| 33 | ApplicationComponent | uses | DataObject |
| 34 | InformationFlow | carries | DataEntity |
| 35 | InformationFlow | flowsTo | ApplicationComponent |
| 36 | InformationFlow | flowsTo | BusinessProcess |
| 37 | DataEntity | ownedBy | OrganisationUnit |
| 38 | DataDomain | ownedBy | OrganisationUnit |

### Technology Infrastructure
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 39 | Server | isA | TechnologyComponent |
| 40 | TechnologyComponent | hosts | ApplicationComponent |
| 41 | TechnologyComponent | locatedAt | Location |
| 42 | Location | contains | TechnologyComponent |
| 43 | Network | connectedTo | TechnologyComponent |
| 44 | TechnologyComponent | suppliedBy | Vendor |
| 45 | TechnologyComponent | supports | ITCapability |
| 46 | Deployment | uses | ApplicationComponent |
| 47 | Deployment | hostedOn | TechnologyComponent |

### Investment Management
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 48 | Demand | triggers | Project |
| 49 | Budget | funds | Project |

### Building Blocks
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 50 | ABB | realizes | Capability |
| 51 | SBB | implements | ABB |
| 52 | SBB | contains | ApplicationComponent |

### Cross-Domain Governance
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 53 | Application | ownedBy | OrganisationUnit |
| 54 | TechnologyComponent | ownedBy | OrganisationUnit |
| 55 | ApplicationComponent | compliesWith | Standard |
| 56 | TechnologyComponent | compliesWith | Standard |
| 57 | Application | replaces | Application |
| 58 | TechnologyComponent | replaces | TechnologyComponent |
| 59 | Application | dependsOn | Application |
| 60 | ApplicationComponent | dependsOn | ApplicationComponent |
| 61 | TechnologyComponent | dependsOn | TechnologyComponent |

### Lifecycle and Status Properties
| # | Subject | Relationship | Object |
|---|---------|-------------|--------|
| 62 | Application | hasLifecycleStatus | LifecycleStatus |
| 63 | ApplicationComponent | hasLifecycleStatus | LifecycleStatus |
| 64 | TechnologyComponent | hasLifecycleStatus | LifecycleStatus |
| 65 | Project | hasLifecycleStatus | DeliveryStatus |
| 66 | Application | hasProperty | HealthRating |
| 67 | TechnologyComponent | hasProperty | HealthRating |
| 68 | Project | hasComplianceStatus | ComplianceStatus |
| 69 | DataEntity | hasProperty | DataClassification |
| 70 | Deployment | hasProperty | Environment |

---

## 7. Naming Conventions

### ID Convention: `[DOMAIN]-[TYPE]-[NUMBER]`

| Domain Code | Types | Example |
|-------------|-------|---------|
| STR | VIS, GOL, OBJ, INI | STR-GOL-001 |
| SVC | BSV, SSV | SVC-BSV-012 |
| BUS | CST, PRC, WKF, CAP, ORG, ROL, ACT | BUS-PRC-005 |
| APP | APP, CMP, FUN, SRV | APP-CMP-003 |
| DAT | ENT, OBJ, FLW, DOM | DAT-ENT-008 |
| TEC | CMP, SRV, NET, LOC, DEP, VEN, CAP | TEC-SRV-002 |
| INV | PRJ, DEM, BUD | INV-PRJ-001 |

### Naming Patterns

| Object Type | Pattern | Examples |
|-------------|---------|----------|
| BusinessService | `<Action> <Subject>` | "Process Tax Return," "Issue Business License" |
| Capability | `<Verb> <Noun>` | "Manage Registration," "Collect Revenue" |
| Application | Official system name | "GamTax Net," "DHIS2," "IFMIS" |
| ApplicationComponent | `<App> — <Module>` | "GamTax Net — Registration Module" |
| DataEntity | `<Singular Noun>` | "Taxpayer," "Health Facility," "Transaction" |
| BusinessProcess | `<Verb> <Object> Process` | "Registration Process," "Audit Selection Process" |
| InformationFlow | `<Data> from <Source> to <Target>` | "Payment Confirmation from GamPay to GamTax Net" |
| OrganisationUnit | Official institutional name | "GRA Domestic Tax Division" |

### Documentation Levels

| Level | Required Attributes | When to Use |
|-------|-------------------|-------------|
| **Level 1 — Essential** | ID, Name, Description, Status | Minimum for all objects; initial discovery |
| **Level 2 — Standard** | Level 1 + Type, Owner, Key Relationships | Target architecture (To-Be); normal working level |
| **Level 3 — Comprehensive** | Level 2 + All defined attributes | Detailed solution design and compliance review |

---

## 8. Governance

### Content Lifecycle
Draft → Review → Published → Retired (retained 24 months then archived).

### Access Control

| Role | Permissions | Assigned To |
|------|------------|-------------|
| **Administrator** | Full access: create, edit, delete, configure | NEAO technical staff |
| **Approver** | Create, edit, approve/reject, view all | Chief EA, EA Board Chair |
| **Contributor** | Create, edit own, view all published | Domain Architects, Ministry Focal Points |
| **Reviewer** | View all, add comments | EA Board, DTSC members |
| **Reader** | View approved content only | All government stakeholders |

### Who Documents What

| Role | Responsible For |
|------|----------------|
| MoFEA Focal Point | IFMIS, budget processes, public finance data |
| GRA Focal Point | GamTax Net, ASYCUDA World, taxpayer data |
| MoH Focal Point | DHIS2, OpenMRS, health facility data |
| MoCDE/GICTA Focal Point | GamPay, government network, GICTA infrastructure |
| Domain Architect (Business/App) | Cross-ministry services, capabilities, ABBs/SBBs |
| Domain Architect (Data/Tech) | Data domains, information flows, technology standards |
| Chief Enterprise Architect | Strategy domain, governance, metamodel, cross-cutting |

### Change Control for Metamodel Itself
- **Minor** (adding attributes): Chief EA approval
- **Major** (new object/relationship types): EA Board approval
- **Structural** (removing domains, redefining chains): DTSC endorsement
