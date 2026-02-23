**THE GAMBIA**

**NATIONAL ENTERPRISE ARCHITECTURE FRAMEWORK**

*Establishing the Foundation for Whole-of-Government Digital Transformation*

**Prepared for:**

Government of The Gambia

Ministry of Communications and Digital Economy (MoCDE)

Gambia Information and Communications Technology Agency (GICTA)

**Prepared by:**

International Telecommunication Union (ITU)

Enterprise Architecture Advisory Team

Contract Reference: WARDIP/C4.13.2/2024/DC009

Funded by: World Bank — Western Africa Regional Digital Integration Programme (WARDIP)

D2 — Enterprise Architecture Framework | Version 1.0 | February 2026

Classification: Official — Unrestricted | Validity Period: 2026–2033

# Document Control

## Version History

| **Version** | **Date**   | **Author**  | **Description**                                                |
|-------------|------------|-------------|----------------------------------------------------------------|
| 0.1         | 2026-02-10 | ITU EA Team | Initial draft — Chapters 1–5                                   |
| 0.2         | 2026-02-15 | ITU EA Team | Added Chapters 6–7, Methodology and EA Services                |
| 0.3         | 2026-02-18 | ITU EA Team | Added Chapters 8–9, Repository and Maturity Roadmap            |
| 0.4         | 2026-02-20 | ITU EA Team | Added Appendices A–F; full draft complete                      |
| 0.5         | 2026-02-22 | ITU EA Team | Integration review, consistency corrections, Executive Summary |
| 1.0         | 2026-02-XX | ITU EA Team | Final version incorporating stakeholder review comments        |

## Document Roles

| **Role**               | **Name**                                         | **Organisation**                               |
|------------------------|--------------------------------------------------|------------------------------------------------|
| **Author**             | ITU Enterprise Architecture Advisory Team        | International Telecommunication Union          |
| **Technical Reviewer** | Prof. Abdou Karim Jallow, Director General       | GICTA                                          |
| **Technical Reviewer** | Ministry EA Focal Points                         | MoFEA, GRA, MoH, MoCDE                         |
| **Approver**           | Permanent Secretary                              | Ministry of Communications and Digital Economy |
| **Endorsement**        | Digital Transformation Steering Committee (DTSC) | Government of The Gambia                       |

## Distribution

| **Recipient**              | **Organisation**  | **Copy Type** |
|----------------------------|-------------------|---------------|
| Director General           | GICTA             | Controlled    |
| Permanent Secretary        | MoCDE             | Controlled    |
| Permanent Secretary        | MoFEA             | Controlled    |
| Commissioner General       | GRA               | Controlled    |
| Permanent Secretary        | MoH               | Controlled    |
| WARDIP Project Coordinator | World Bank        | Controlled    |
| EA Board Members           | Tier 1 Ministries | Controlled    |
| Ministry EA Focal Points   | Tier 1 Ministries | Controlled    |

# Executive Summary

## The Gambia’s Digital Transformation Challenge

The Gambia aspires to become a digitally empowered society, with the Digital Economy Master Plan (DEMP) 2024–2034 setting a target of 70% government service digitisation by 2033. Achieving this ambition requires more than deploying individual technology systems — it demands a coordinated, whole-of-government approach that ensures investments are aligned, systems can communicate, data is shared securely, and limited resources deliver maximum impact.

Today, The Gambia’s government digital landscape is characterised by pockets of capability within a largely fragmented environment. The Gambia Revenue Authority (GRA) has achieved 98% server virtualisation and operates a modern tax administration system (GamTax Net). The GamPay payment gateway demonstrates API maturity at Level 4. The Ministry of Health (MoH) runs the DHIS2 health information system across more than 700 facilities. Yet these capable systems exist alongside fundamental gaps: no formal enterprise architecture governance, no data governance framework, no operational integration platform, and inter-ministry data exchange that relies primarily on email and manual processes.

The national EA maturity assessment confirms this picture, establishing a baseline score of **2.19 out of 5.0** — placing The Gambia in the upper range of “Developing” on the international maturity scale. The constraints are real: approximately 62% national electricity access, a single submarine cable (ACE) for international connectivity, IT teams of 3–5 staff per ministry, and heavy reliance on donor funding through WARDIP and other programmes.

## What This Framework Provides

This Enterprise Architecture Framework (Deliverable 2 under Contract WARDIP/C4.13.2/2024/DC009) establishes the authoritative foundation for The Gambia’s government-wide digital transformation. It defines the principles, governance structures, standards, methodology, and institutional arrangements that will guide all architecture decisions across government for the validity period 2026–2033.

The Framework is built on five pillars:

**1. Strategic Direction (Chapter 3)** — 33 binding EA principles across five categories (Business Architecture, Data Architecture, Application Architecture, Technology Architecture, and Cross-Cutting), adapted from the Government Enterprise Architecture Target Development Method (GEATDM) to The Gambia’s specific context, constraints, and ambitions.

**2. Governance (Chapter 4)** — A three-tier governance model leveraging existing Gambian institutions: the Digital Transformation Steering Committee (DTSC) for strategic oversight (chaired by the Cabinet Secretary), the Enterprise Architecture Board for technical decisions (chaired by the Permanent Secretary of MoCDE), and the National EA Office within GICTA for day-to-day operations. Ministry EA Focal Points provide the essential link between central governance and ministry-level implementation.

**3. Metamodel and Notation (Chapter 5)** — A standardised vocabulary of architecture objects, attributes, and relationships spanning six portfolio domains (Strategy, Service, Business, Application, Data, Technology), enabling consistent documentation across all ministries and making architectures from different institutions comparable and composable.

**4. Methodology (Chapter 6)** — The GEATDM five-phase approach (DISCOVER → ASSESS → ADAPT → PLAN → EXECUTE & GOVERN) tailored to The Gambia, including the classification of all four Tier 1 institutions (MoCDE and MoFEA as Policy Development Units; GRA and MoH as Service Delivery Agencies) and a Digital Public Infrastructure readiness assessment establishing a national DPI score of 36.25%.

**5. EA Services (Chapter 7)** — A 12-service catalogue to be delivered by the National EA Office, with a phased activation plan: 6 core services in Year 1, expanding to 10 services in Year 2, and the full 12-service catalogue by Year 3.

Two supporting components complete the Framework: an EA Repository and Tooling strategy (Chapter 8) recommending a pragmatic open-source approach (DokuWiki + Archi) appropriate to current maturity, and an EA Maturity Roadmap (Chapter 9) defining the progressive journey from Level 2.19 to the target of Level 4.1 by 2030.

## The Path Forward

| **Stage**    | **Period** | **Target Maturity** | **Key Outcomes**                                                                                                                               |
|--------------|------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Foundation   | 2025–2026  | 2.19 → 2.5          | EA governance bodies operational; As-Is and To-Be architectures documented; EA repository launched; first 5 standards published                |
| Integration  | 2027–2028  | 2.5 → 3.0           | Government Interoperability Platform (GIP) operational; G-Cloud in production; 30–40 services digitised; EA compliance embedded in procurement |
| Optimisation | 2029–2031  | 3.0 → 4.1           | Event-driven architecture operational; Master Data Management deployed; 60–80% cloud-based; EA self-sustaining                                 |
| Aspiration   | 2032–2033  | 4.1 → 4.5+          | Innovation-led; 70% service digitisation achieved; regional integration mature                                                                 |

This trajectory requires sustained investment, estimated at \$8–12M for the Foundation stage (primarily WARDIP-funded), scaling to \$18–25M for Integration and \$20–30M for Optimisation, with an increasing share from the government’s own budget as donor dependency decreases.

## Critical Success Factors

Five factors will determine whether this Framework translates into real digital transformation:

**1. Executive Sponsorship** — The DTSC must actively champion EA governance and hold ministries accountable for compliance.

**2. Institutional Capacity** — Recruiting a Chief Enterprise Architect and establishing the National EA Office within GICTA is the single most critical near-term action.

**3. Phased Compliance** — Enforcement must grow with maturity: advisory in Year 1, binding for major investments in Year 2, full enforcement from Year 4.

**4. Interoperability as Priority** — The Government Interoperability Platform (GIP) is the lynchpin of cross-ministry integration; its operationalisation must be treated as foundational infrastructure.

**5. Financial Sustainability** — The transition from donor-funded EA operations to government budget allocation must begin in Year 1 through budget advocacy and demonstrated value.

## Call to Action

This Framework is presented to the Digital Transformation Steering Committee for endorsement. Upon endorsement, it becomes the binding normative reference for all government architecture decisions and the foundation upon which all subsequent project deliverables (D3 through D13) are built. The immediate next steps are:

**1.** DTSC endorsement of this Framework

**2.** Recruitment of the Chief Enterprise Architect

**3.** Formal designation of Ministry EA Focal Points

**4.** EA Board inaugural session

**5.** Commencement of EA Repository establishment (Deliverable 3)

The Gambia’s digital transformation journey starts with this Framework. It provides the common language, shared governance, and structured methodology that ensure the government’s digital investments work together — not in isolation — to deliver the Digital Economy Master Plan 2033 vision.

# Table of Contents

[Document Control [2](#document-control)](#document-control)

[Version History [2](#version-history)](#version-history)

[Document Roles [2](#document-roles)](#document-roles)

[Distribution [2](#distribution)](#distribution)

[Executive Summary [4](#executive-summary)](#executive-summary)

[The Gambia’s Digital Transformation Challenge [4](#the-gambias-digital-transformation-challenge)](#the-gambias-digital-transformation-challenge)

[What This Framework Provides [4](#what-this-framework-provides)](#what-this-framework-provides)

[The Path Forward [5](#the-path-forward)](#the-path-forward)

[Critical Success Factors [5](#critical-success-factors)](#critical-success-factors)

[Call to Action [6](#call-to-action)](#call-to-action)

[Table of Contents [7](#table-of-contents)](#table-of-contents)

[Abbreviations and Acronyms [15](#abbreviations-and-acronyms)](#abbreviations-and-acronyms)

[Chapter 1: Introduction [18](#chapter-1-introduction)](#chapter-1-introduction)

[1.1 Purpose [18](#purpose)](#purpose)

[1.2 Scope [18](#scope)](#scope)

[In Scope [18](#in-scope)](#in-scope)

[Out of Scope [19](#out-of-scope)](#out-of-scope)

[Scope Boundaries and Extensions [19](#scope-boundaries-and-extensions)](#scope-boundaries-and-extensions)

[1.3 Reference Frameworks [19](#reference-frameworks)](#reference-frameworks)

[TOGAF 9.2 — The Open Group Architecture Framework [20](#togaf-9.2-the-open-group-architecture-framework)](#togaf-9.2-the-open-group-architecture-framework)

[PAERA — Public Administration Ecosystem Reference Architecture [20](#paera-public-administration-ecosystem-reference-architecture)](#paera-public-administration-ecosystem-reference-architecture)

[GovStack — Building Block Specifications [20](#govstack-building-block-specifications)](#govstack-building-block-specifications)

[GEATDM — Government Enterprise Architecture Target Development Method [20](#geatdm-government-enterprise-architecture-target-development-method)](#geatdm-government-enterprise-architecture-target-development-method)

[1.4 Relationship to National Strategies [20](#relationship-to-national-strategies)](#relationship-to-national-strategies)

[Digital Economy Master Plan (DEMP) 2024–2034 [20](#digital-economy-master-plan-demp-20242034)](#digital-economy-master-plan-demp-20242034)

[West Africa Regional Digital Integration Programme (WARDIP) [21](#west-africa-regional-digital-integration-programme-wardip)](#west-africa-regional-digital-integration-programme-wardip)

[National Development Plan (NDP) [21](#national-development-plan-ndp)](#national-development-plan-ndp)

[National ICT Policy and Cybersecurity Strategy [21](#national-ict-policy-and-cybersecurity-strategy)](#national-ict-policy-and-cybersecurity-strategy)

[1.5 Document Structure Guide [21](#document-structure-guide)](#document-structure-guide)

[Chapter Overview [21](#chapter-overview)](#chapter-overview)

[Audience Navigation Guide [22](#audience-navigation-guide)](#audience-navigation-guide)

[Document Conventions [22](#document-conventions)](#document-conventions)

[Chapter 2: EA Framework Structure [23](#chapter-2-ea-framework-structure)](#chapter-2-ea-framework-structure)

[2.1 Framework Components Overview [23](#framework-components-overview)](#framework-components-overview)

[The Five Pillars [23](#the-five-pillars)](#the-five-pillars)

[Supporting Components [23](#supporting-components)](#supporting-components)

[2.2 Relationship Between Components [23](#relationship-between-components)](#relationship-between-components)

[Key Interaction Patterns [24](#key-interaction-patterns)](#key-interaction-patterns)

[The Two-Layer Architecture [24](#the-two-layer-architecture)](#the-two-layer-architecture)

[2.3 How This Framework Relates to GEATDM [24](#how-this-framework-relates-to-geatdm)](#how-this-framework-relates-to-geatdm)

[GEATDM Structure and This Framework’s Position [25](#geatdm-structure-and-this-frameworks-position)](#geatdm-structure-and-this-frameworks-position)

[Nature of Adaptation [25](#nature-of-adaptation)](#nature-of-adaptation)

[2.4 Framework Applicability and Compliance Expectations [25](#framework-applicability-and-compliance-expectations)](#framework-applicability-and-compliance-expectations)

[Applicability Tiers [25](#applicability-tiers)](#applicability-tiers)

[Mandatory vs. Advisory Content [26](#mandatory-vs.-advisory-content)](#mandatory-vs.-advisory-content)

[Enforcement Timeline [26](#enforcement-timeline)](#enforcement-timeline)

[Chapter 3: EA Principles [27](#chapter-3-ea-principles)](#chapter-3-ea-principles)

[3.1 Architecture Vision for The Gambia [27](#architecture-vision-for-the-gambia)](#architecture-vision-for-the-gambia)

[3.2 Principle Structure [27](#principles-structure)](#principles-structure)

[3.3 Business Architecture Principles [27](#business-architecture-principles)](#business-architecture-principles)

[BA-01: Customer-Centric Service Design [28](#ba-01-customer-centric-service-design)](#ba-01-customer-centric-service-design)

[BA-02: Process Standardisation and Automation [28](#ba-02-process-standardisation-and-automation)](#ba-02-process-standardisation-and-automation)

[BA-03: Capability-Based Planning [28](#ba-03-capability-based-planning)](#ba-03-capability-based-planning)

[BA-04: Service Orientation [29](#ba-04-service-orientation)](#ba-04-service-orientation)

[BA-05: Regulatory Compliance by Design [29](#ba-05-regulatory-compliance-by-design)](#ba-05-regulatory-compliance-by-design)

[BA-06: Channel Choice and Consistency [30](#ba-06-channel-choice-and-consistency)](#ba-06-channel-choice-and-consistency)

[BA-07: Natural Digital Environment Integration [30](#ba-07-natural-digital-environment-integration)](#ba-07-natural-digital-environment-integration)

[3.4 Data Architecture Principles [31](#data-architecture-principles)](#data-architecture-principles)

[DA-01: Data as a Strategic Asset [31](#da-01-data-as-a-strategic-asset)](#da-01-data-as-a-strategic-asset)

[DA-02: Once-Only Data Collection [31](#da-02-once-only-data-collection)](#da-02-once-only-data-collection)

[DA-03: Single Source of Truth [32](#da-03-single-source-of-truth)](#da-03-single-source-of-truth)

[DA-04: Data Quality Management [32](#da-04-data-quality-management)](#da-04-data-quality-management)

[DA-05: Privacy and Data Protection by Design [32](#da-05-privacy-and-data-protection-by-design)](#da-05-privacy-and-data-protection-by-design)

[DA-06: Data Sharing and Interoperability [33](#da-06-data-sharing-and-interoperability)](#da-06-data-sharing-and-interoperability)

[DA-07: Analytics-Ready Data [33](#da-07-analytics-ready-data)](#da-07-analytics-ready-data)

[3.5 Application Architecture Principles [34](#application-architecture-principles)](#application-architecture-principles)

[APP-01: Building Block Orientation [34](#app-01-building-block-orientation)](#app-01-building-block-orientation)

[APP-02: Loose Coupling and High Cohesion [34](#app-02-loose-coupling-and-high-cohesion)](#app-02-loose-coupling-and-high-cohesion)

[APP-03: Integration Through National DPI [35](#app-03-integration-through-national-dpi)](#app-03-integration-through-national-dpi)

[APP-04: No Legacy by Design [35](#app-04-no-legacy-by-design)](#app-04-no-legacy-by-design)

[APP-05: API-First Design [35](#app-05-api-first-design)](#app-05-api-first-design)

[APP-06: Cloud-Ready and Platform-Neutral [36](#app-06-cloud-ready-and-platform-neutral)](#app-06-cloud-ready-and-platform-neutral)

[APP-07: Modularity and Incremental Delivery [36](#app-07-modularity-and-incremental-delivery)](#app-07-modularity-and-incremental-delivery)

[3.6 Technology Architecture Principles [36](#technology-architecture-principles)](#technology-architecture-principles)

[TECH-01: Security by Design [37](#tech-01-security-by-design)](#tech-01-security-by-design)

[TECH-02: Resilience and Business Continuity [37](#tech-02-resilience-and-business-continuity)](#tech-02-resilience-and-business-continuity)

[TECH-03: Scalability and Performance [37](#tech-03-scalability-and-performance)](#tech-03-scalability-and-performance)

[TECH-04: Standardisation and Simplification [38](#tech-04-standardisation-and-simplification)](#tech-04-standardisation-and-simplification)

[TECH-05: Infrastructure as Code [38](#tech-05-infrastructure-as-code)](#tech-05-infrastructure-as-code)

[TECH-06: Observability and Monitoring [38](#tech-06-observability-and-monitoring)](#tech-06-observability-and-monitoring)

[TECH-07: Sustainable and Responsible Technology [39](#tech-07-sustainable-and-responsible-technology)](#tech-07-sustainable-and-responsible-technology)

[3.7 Cross-Cutting Principles [39](#cross-cutting-principles)](#cross-cutting-principles)

[CC-01: Whole-of-Government Alignment [39](#cc-01-whole-of-government-alignment)](#cc-01-whole-of-government-alignment)

[CC-02: Digital by Default, Inclusive by Design [39](#cc-02-digital-by-default-inclusive-by-design)](#cc-02-digital-by-default-inclusive-by-design)

[CC-03: Continuous Improvement and Innovation [40](#cc-03-continuous-improvement-and-innovation)](#cc-03-continuous-improvement-and-innovation)

[CC-04: Transparency and Accountability [40](#cc-04-transparency-and-accountability)](#cc-04-transparency-and-accountability)

[CC-05: Value for Money and Sustainability [41](#cc-05-value-for-money-and-sustainability)](#cc-05-value-for-money-and-sustainability)

[3.8 Principle Application and Compliance Guidance [41](#principle-application-and-compliance-guidance)](#principle-application-and-compliance-guidance)

[3.8.1 How Principles Are Applied [41](#how-principles-are-applied)](#how-principles-are-applied)

[3.8.2 Principle Compliance Assessment [41](#principle-compliance-assessment)](#principle-compliance-assessment)

[3.8.3 Dispensation Process [41](#dispensation-process)](#dispensation-process)

[3.8.4 Principle Review Cycle [42](#principle-review-cycle)](#principle-review-cycle)

[3.8.5 Principle Priority in Conflict Situations [42](#principle-priority-in-conflict-situations)](#principle-priority-in-conflict-situations)

[Chapter 4: Enterprise Architecture Governance [43](#chapter-4-enterprise-architecture-governance)](#chapter-4-enterprise-architecture-governance)

[4.1 Governance Hierarchy Overview [43](#governance-hierarchy-overview)](#governance-hierarchy-overview)

[4.1.1 Governance Objectives [43](#governance-objectives)](#governance-objectives)

[4.1.2 Governance Scope [43](#governance-scope)](#governance-scope)

[4.1.3 Three-Tier Governance Structure [43](#three-tier-governance-structure)](#three-tier-governance-structure)

[4.2 Digital Transformation Steering Committee (DTSC) [44](#digital-transformation-steering-committee-dtsc)](#digital-transformation-steering-committee-dtsc)

[4.2.2 Membership [44](#membership)](#membership)

[4.3 Enterprise Architecture Board (EA Board) [44](#enterprise-architecture-board-ea-board)](#enterprise-architecture-board-ea-board)

[4.3.3 Decision Authority Matrix [44](#decision-authority-matrix)](#decision-authority-matrix)

[4.4 National EA Office [44](#national-ea-office)](#national-ea-office)

[4.4.3 Staffing Plan [45](#staffing-plan)](#staffing-plan)

[4.5 Ministry EA Focal Points [45](#ministry-ea-focal-points)](#ministry-ea-focal-points)

[4.6 Governance Processes [45](#governance-processes)](#governance-processes)

[4.6.1 Solution Architecture Compliance Review [45](#solution-architecture-compliance-review)](#solution-architecture-compliance-review)

[4.6.2 Architecture Change Request Management [46](#architecture-change-request-management)](#architecture-change-request-management)

[4.6.3 Architecture Dispensation Management [46](#architecture-dispensation-management)](#architecture-dispensation-management)

[4.6.4 EA Framework Maintenance [46](#ea-framework-maintenance)](#ea-framework-maintenance)

[4.6.5 Investment Review Process [46](#investment-review-process)](#investment-review-process)

[4.7 RACI Matrix for Governance Activities [47](#raci-matrix-for-governance-activities)](#raci-matrix-for-governance-activities)

[4.7.1 Compliance Review RACI [47](#compliance-review-raci)](#compliance-review-raci)

[4.8 Decision Escalation and Dispute Resolution [47](#decision-escalation-and-dispute-resolution)](#decision-escalation-and-dispute-resolution)

[4.9 Governance KPIs and Performance Monitoring [47](#governance-kpis-and-performance-monitoring)](#governance-kpis-and-performance-monitoring)

[Chapter 5: Enterprise Architecture Metamodel [49](#chapter-5-enterprise-architecture-metamodel)](#chapter-5-enterprise-architecture-metamodel)

[5.1 Metamodel Purpose and Value [49](#metamodel-purpose-and-value)](#metamodel-purpose-and-value)

[5.1.2 Value Proposition [49](#value-proposition)](#value-proposition)

[5.2 Architecture Domains [49](#architecture-domains)](#architecture-domains)

[5.3 Core Objects Catalogue [50](#core-objects-catalogue)](#core-objects-catalogue)

[5.3.1 Strategy Domain Objects [50](#strategy-domain-objects)](#strategy-domain-objects)

[5.3.2–5.3.3 Service and Business Domain Objects [50](#service-and-business-domain-objects)](#service-and-business-domain-objects)

[5.3.4 Application Domain Objects [50](#application-domain-objects)](#application-domain-objects)

[5.3.5–5.3.7 Data, Technology, and Investment Domain Objects [51](#data-technology-and-investment-domain-objects)](#data-technology-and-investment-domain-objects)

[5.4 Cross-Domain Relationships [51](#cross-domain-relationships)](#cross-domain-relationships)

[5.4.1 Relationship Types [51](#relationship-types)](#relationship-types)

[5.4.4 Critical Traceability Chains [52](#critical-traceability-chains)](#critical-traceability-chains)

[5.5 Architecture Viewpoints [52](#architecture-viewpoints)](#architecture-viewpoints)

[5.6 Notation Standard [52](#notation-standard)](#notation-standard)

[5.6.4 Naming Conventions [52](#naming-conventions)](#naming-conventions)

[5.6.5 ID Convention [53](#id-convention)](#id-convention)

[5.7 Metamodel Implementation Approach [53](#metamodel-implementation-approach)](#metamodel-implementation-approach)

[Chapter 6: EA Methodology [53](#chapter-6-ea-methodology)](#chapter-6-ea-methodology)

[6.1 GEATDM Overview [53](#geatdm-overview)](#geatdm-overview)

[6.1.1 Introduction [53](#introduction)](#introduction)

[6.1.2 Core Principles [54](#core-principles)](#core-principles)

[6.1.3 The Five Phases [54](#the-five-phases)](#the-five-phases)

[6.1.4 Decision Points [55](#decision-points)](#decision-points)

[6.2 Organisation Classification [57](#organisation-classification)](#organisation-classification)

[6.2.1 The Three Organisation Types [57](#the-three-organisation-types)](#the-three-organisation-types)

[6.2.2 Classification of Gambian Tier 1 Institutions [57](#classification-of-gambian-tier-1-institutions)](#classification-of-gambian-tier-1-institutions)

[6.2.3 Classification Implications [58](#classification-implications)](#classification-implications)

[6.3 Phase Descriptions [59](#phase-descriptions)](#phase-descriptions)

[6.3.1 DISCOVER Phase [59](#discover-phase)](#discover-phase)

[6.3.2 ASSESS Phase [59](#assess-phase)](#assess-phase)

[6.3.3 ADAPT Phase [59](#adapt-phase)](#adapt-phase)

[6.3.4 PLAN Phase [60](#plan-phase)](#plan-phase)

[6.3.5 EXECUTE & GOVERN Phase [60](#execute-govern-phase)](#execute-govern-phase)

[6.4 DPI Readiness Assessment for Gambia [62](#dpi-readiness-assessment-for-gambia)](#dpi-readiness-assessment-for-gambia)

[6.4.1 Five Pillars Assessment [62](#five-pillars-assessment)](#five-pillars-assessment)

[6.4.2 Overall DPI Readiness Score [62](#overall-dpi-readiness-score)](#overall-dpi-readiness-score)

[6.4.3 Implications by Organisation Type [62](#implications-by-organisation-type)](#implications-by-organisation-type)

[6.4.4 Mitigation Strategies [63](#mitigation-strategies)](#mitigation-strategies)

[6.5 Reference Architecture Selection and Application [64](#reference-architecture-selection-and-application)](#reference-architecture-selection-and-application)

[6.5.1 RA Selection Matrix for Gambia [64](#ra-selection-matrix-for-gambia)](#ra-selection-matrix-for-gambia)

[6.5.2 Reference Architecture Inheritance [64](#reference-architecture-inheritance)](#reference-architecture-inheritance)

[6.5.3 Application by Institution [64](#application-by-institution)](#application-by-institution)

[6.6 Methodology Application in This Project [66](#methodology-application-in-this-project)](#methodology-application-in-this-project)

[6.6.1 Deliverable Chain to Phase Mapping [66](#deliverable-chain-to-phase-mapping)](#deliverable-chain-to-phase-mapping)

[6.6.2 Project Timeline Alignment [66](#project-timeline-alignment)](#project-timeline-alignment)

[6.6.3 Toolkit Application [66](#toolkit-application)](#toolkit-application)

[6.6.4 Cross-Deliverable Consistency [67](#cross-deliverable-consistency)](#cross-deliverable-consistency)

[Chapter 7: Enterprise Architecture Services [68](#chapter-7-enterprise-architecture-services)](#chapter-7-enterprise-architecture-services)

[7.1 National EA Office Establishment Plan [68](#national-ea-office-establishment-plan)](#national-ea-office-establishment-plan)

[7.1.1 Purpose and Mandate [68](#purpose-and-mandate)](#purpose-and-mandate)

[7.1.2 Placement Within GICTA [68](#placement-within-gicta)](#placement-within-gicta)

[7.1.3 Phased Establishment [68](#phased-establishment)](#phased-establishment)

[7.2 Staffing Model [69](#staffing-model)](#staffing-model)

[7.2.1 Target Organisational Structure [69](#target-organisational-structure)](#target-organisational-structure)

[7.2.2 Staffing Budget Estimate [69](#staffing-budget-estimate)](#staffing-budget-estimate)

[7.3 Service Catalogue [71](#service-catalogue)](#service-catalogue)

[7.3.1 Service Portfolio Overview [71](#service-portfolio-overview)](#service-portfolio-overview)

[7.3.2 Service Summary Cards [71](#service-summary-cards)](#service-summary-cards)

[7.4 Service Delivery Processes [73](#service-delivery-processes)](#service-delivery-processes)

[7.4.1 Service Request Process [73](#service-request-process)](#service-request-process)

[7.4.2 Mandate-Driven Service Scheduling [73](#mandate-driven-service-scheduling)](#mandate-driven-service-scheduling)

[7.5 Service Performance Metrics and KPIs [73](#service-performance-metrics-and-kpis)](#service-performance-metrics-and-kpis)

[7.5.1 Portfolio-Level KPIs [73](#portfolio-level-kpis)](#portfolio-level-kpis)

[7.6 Phased Service Rollout [74](#phased-service-rollout)](#phased-service-rollout)

[7.6.1 Rollout Overview [74](#rollout-overview)](#rollout-overview)

[7.6.2 Phase 1 — Foundation (Year 1: 2026–2027) [74](#phase-1-foundation-year-1-20262027)](#phase-1-foundation-year-1-20262027)

[7.6.3 Phase 2 — Governance (Year 2: 2027–2028) [74](#phase-2-governance-year-2-20272028)](#phase-2-governance-year-2-20272028)

[7.6.4 Phase 3 — Full Catalogue (Year 3: 2028–2029) [74](#phase-3-full-catalogue-year-3-20282029)](#phase-3-full-catalogue-year-3-20282029)

[Chapter 8: EA Repository and Tooling [75](#chapter-8-ea-repository-and-tooling)](#chapter-8-ea-repository-and-tooling)

[8.1 Repository Requirements [75](#repository-requirements)](#repository-requirements)

[8.1.1 Purpose [75](#purpose-1)](#purpose-1)

[8.1.2 Functional Requirements [75](#functional-requirements)](#functional-requirements)

[8.1.3 Non-Functional Requirements [75](#non-functional-requirements)](#non-functional-requirements)

[8.2 Tool Selection Rationale [75](#tool-selection-rationale)](#tool-selection-rationale)

[8.2.1 Selection Approach [75](#selection-approach)](#selection-approach)

[8.2.2 Evaluation Criteria [76](#evaluation-criteria)](#evaluation-criteria)

[8.2.3 Recommended Tooling Stack [76](#recommended-tooling-stack)](#recommended-tooling-stack)

[8.3 Repository Structure and Namespace Design [77](#repository-structure-and-namespace-design)](#repository-structure-and-namespace-design)

[8.3.1 DokuWiki Namespace Hierarchy [77](#dokuwiki-namespace-hierarchy)](#dokuwiki-namespace-hierarchy)

[8.3.2 Naming Conventions [77](#naming-conventions-1)](#naming-conventions-1)

[8.4 Content Management Processes [77](#content-management-processes)](#content-management-processes)

[8.5 Access Control and Security [77](#access-control-and-security)](#access-control-and-security)

[8.6 Migration Path to Commercial Tools [78](#migration-path-to-commercial-tools)](#migration-path-to-commercial-tools)

[Chapter 9: EA Maturity Roadmap [79](#chapter-9-ea-maturity-roadmap)](#chapter-9-ea-maturity-roadmap)

[9.1 Current Maturity Assessment [79](#current-maturity-assessment)](#current-maturity-assessment)

[9.1.1 Assessment Methodology [79](#assessment-methodology)](#assessment-methodology)

[9.1.2 Baseline Results (2025) [79](#baseline-results-2025)](#baseline-results-2025)

[9.2 Target Maturity Trajectory [80](#target-maturity-trajectory)](#target-maturity-trajectory)

[9.3 Maturity Dimensions and Assessment Criteria [81](#maturity-dimensions-and-assessment-criteria)](#maturity-dimensions-and-assessment-criteria)

[9.4 Year 1–3 Implementation Roadmap [83](#year-13-implementation-roadmap)](#year-13-implementation-roadmap)

[9.4.1 Year 1 (2026): Establish Foundations [83](#year-1-2026-establish-foundations)](#year-1-2026-establish-foundations)

[9.4.2 Year 2 (2027): Build Operational Capability [83](#year-2-2027-build-operational-capability)](#year-2-2027-build-operational-capability)

[9.4.3 Year 3 (2028): Transition to Integration Stage [83](#year-3-2028-transition-to-integration-stage)](#year-3-2028-transition-to-integration-stage)

[9.5 Critical Success Factors [83](#critical-success-factors-1)](#critical-success-factors-1)

[9.6 Risk Register [85](#risk-register)](#risk-register)

[Appendix A: Glossary [86](#appendix-a-glossary)](#appendix-a-glossary)

[Appendix B: Full Principles Catalogue [88](#appendix-b-full-principles-catalogue)](#appendix-b-full-principles-catalogue)

[B.1 Business Architecture Principles (7 Principles) [88](#b.1-business-architecture-principles-7-principles)](#b.1-business-architecture-principles-7-principles)

[B.2 Data Architecture Principles (7 Principles) [88](#b.2-data-architecture-principles-7-principles)](#b.2-data-architecture-principles-7-principles)

[B.3 Application Architecture Principles (7 Principles) [89](#b.3-application-architecture-principles-7-principles)](#b.3-application-architecture-principles-7-principles)

[B.4 Technology Architecture Principles (7 Principles) [89](#b.4-technology-architecture-principles-7-principles)](#b.4-technology-architecture-principles-7-principles)

[B.5 Cross-Cutting Principles (5 Principles) [90](#b.5-cross-cutting-principles-5-principles)](#b.5-cross-cutting-principles-5-principles)

[Appendix C: Governance Body Terms of Reference [91](#appendix-c-governance-body-terms-of-reference)](#appendix-c-governance-body-terms-of-reference)

[C.1 Digital Transformation Steering Committee (DTSC) [91](#c.1-digital-transformation-steering-committee-dtsc)](#c.1-digital-transformation-steering-committee-dtsc)

[Membership [91](#membership-1)](#membership-1)

[C.2 Enterprise Architecture Board (EA Board) [91](#c.2-enterprise-architecture-board-ea-board)](#c.2-enterprise-architecture-board-ea-board)

[Membership [91](#membership-2)](#membership-2)

[C.3 National Enterprise Architecture Office (NEAO) [92](#c.3-national-enterprise-architecture-office-neao)](#c.3-national-enterprise-architecture-office-neao)

[C.4 Ministry EA Focal Points [92](#c.4-ministry-ea-focal-points)](#c.4-ministry-ea-focal-points)

[Appendix D: Metamodel Object Catalogue [93](#appendix-d-metamodel-object-catalogue)](#appendix-d-metamodel-object-catalogue)

[D.1 Object Summary [93](#d.1-object-summary)](#d.1-object-summary)

[D.2 Validation Rules [93](#d.2-validation-rules)](#d.2-validation-rules)

[D.3 Gambia-Specific Extensions [93](#d.3-gambia-specific-extensions)](#d.3-gambia-specific-extensions)

[Appendix E: EA Tool Evaluation Matrix [95](#appendix-e-ea-tool-evaluation-matrix)](#appendix-e-ea-tool-evaluation-matrix)

[Appendix F: References [96](#appendix-f-references)](#appendix-f-references)

[F.1 International Frameworks and Standards [96](#f.1-international-frameworks-and-standards)](#f.1-international-frameworks-and-standards)

[F.2 GEATDM Document Suite [96](#f.2-geatdm-document-suite)](#f.2-geatdm-document-suite)

[F.3 Gambia National Strategies and Project Documents [96](#f.3-gambia-national-strategies-and-project-documents)](#f.3-gambia-national-strategies-and-project-documents)

[F.4 International Best Practice and Tools [97](#f.4-international-best-practice-and-tools)](#f.4-international-best-practice-and-tools)

# Abbreviations and Acronyms

| **Abbreviation** | **Full Form**                                                              |
|------------------|----------------------------------------------------------------------------|
| ABB              | Architecture Building Block                                                |
| ACE              | Africa Coast to Europe (submarine cable)                                   |
| ADM              | Architecture Development Method                                            |
| ADR              | Architecture Decision Record                                               |
| API              | Application Programming Interface                                          |
| ASYCUDA          | Automated System for Customs Data                                          |
| BA               | Business Architecture (principle category)                                 |
| BB               | Building Block                                                             |
| BDAT             | Business, Data, Application, Technology                                    |
| CC               | Cross-Cutting (principle category)                                         |
| CERT             | Computer Emergency Response Team                                           |
| COBIT            | Control Objectives for Information Technologies                            |
| DA               | Data Architecture (principle category)                                     |
| DEMP             | Digital Economy Master Plan (2024–2034)                                    |
| DHIS2            | District Health Information Software 2                                     |
| DG               | Director General                                                           |
| DIAL             | Digital Impact Alliance                                                    |
| DPI              | Digital Public Infrastructure                                              |
| DTSC             | Digital Transformation Steering Committee                                  |
| EA               | Enterprise Architecture                                                    |
| ECOWAS           | Economic Community of West African States                                  |
| eCRVS            | Electronic Civil Registration and Vital Statistics                         |
| e-NHIS           | Electronic National Health Insurance System                                |
| FTE              | Full-Time Equivalent                                                       |
| G-Cloud          | Government Cloud                                                           |
| GamPay           | Gambia Government Payment Gateway                                          |
| GamTax Net       | Gambia Tax Administration System (also ITAS)                               |
| GAVI             | Global Alliance for Vaccines and Immunisation                              |
| GEATDM           | Government Enterprise Architecture Target Development Method               |
| GICTA            | Gambia Information and Communications Technology Agency                    |
| GIP              | Government Interoperability Platform                                       |
| GIZ              | Deutsche Gesellschaft für Internationale Zusammenarbeit                    |
| gmCSIRT          | Gambia Computer Security Incident Response Team                            |
| GovStack         | International initiative for digital public infrastructure building blocks |
| GRA              | Gambia Revenue Authority                                                   |
| HTTPS            | Hypertext Transfer Protocol Secure                                         |
| IaC              | Infrastructure as Code                                                     |
| ICT              | Information and Communications Technology                                  |
| IDA              | International Development Association (World Bank)                         |
| IFMIS            | Integrated Financial Management Information System                         |
| IMF              | International Monetary Fund                                                |
| ISO              | International Organization for Standardization                             |
| ITAS             | Integrated Tax Administration System (GamTax Net)                          |
| ITIL             | Information Technology Infrastructure Library                              |
| ITU              | International Telecommunication Union                                      |
| KPI              | Key Performance Indicator                                                  |
| MDA              | Ministry, Department, or Agency                                            |
| MDM              | Master Data Management                                                     |
| MoCDE            | Ministry of Communications and Digital Economy                             |
| MoFEA            | Ministry of Finance and Economic Affairs                                   |
| MoH              | Ministry of Health                                                         |
| MOSIP            | Modular Open Source Identity Platform                                      |
| NDP              | National Development Plan                                                  |
| NEAO             | National EA Office                                                         |
| OECD             | Organisation for Economic Co-operation and Development                     |
| OpenIMIS         | Open Insurance Management Information System                               |
| OpenMRS          | Open Medical Records System                                                |
| PAERA            | Public Administration Ecosystem Reference Architecture                     |
| PDU              | Policy Development Unit (PAERA classification)                             |
| PFM              | Public Financial Management                                                |
| PS               | Permanent Secretary                                                        |
| RA               | Reference Architecture; also Revenue Authority (PAERA classification)      |
| RACI             | Responsible, Accountable, Consulted, Informed                              |
| RBAC             | Role-Based Access Control                                                  |
| RFC              | Request for Change                                                         |
| SBB              | Solution Building Block                                                    |
| SDA              | Service Delivery Agency (PAERA classification)                             |
| SLA              | Service Level Agreement                                                    |
| SOC              | Security Operations Centre                                                 |
| TCO              | Total Cost of Ownership                                                    |
| TOGAF            | The Open Group Architecture Framework                                      |
| UNCTAD           | United Nations Conference on Trade and Development                         |
| USD              | United States Dollar                                                       |
| WAHO             | West African Health Organisation                                           |
| WARDIP           | Western Africa Regional Digital Integration Programme                      |
| WCAG             | Web Content Accessibility Guidelines                                       |
| WCO              | World Customs Organization                                                 |
| WHO              | World Health Organization                                                  |
| WP               | Work Package (GEATDM)                                                      |
| XML              | Extensible Markup Language                                                 |

# Chapter 1: Introduction

## 1.1 Purpose

The Gambia is undergoing a significant digital transformation journey, guided by the Digital Economy Master Plan (DEMP) 2024–2034 vision of a digitally empowered society and a target of 70% government service digitisation by 2033. Achieving this ambition requires more than individual technology projects — it demands a coherent, whole-of-government approach to planning, building, and governing digital capabilities.

This Enterprise Architecture (EA) Framework establishes that coherent approach. It provides the authoritative set of principles, governance structures, standards, and methods that guide all architecture decisions across The Gambia’s government. The Framework serves as the normative foundation upon which all subsequent architecture deliverables — from current-state assessments to target architectures and implementation roadmaps — are built.

The specific purposes of this Framework are to:

**Establish a common language** for describing government business capabilities, applications, data, and technology infrastructure, enabling meaningful communication across ministries and with development partners.

**Define decision rights and accountability** for architecture governance, ensuring that investment decisions are coordinated and aligned with national priorities rather than pursued in isolation.

**Provide a structured methodology** for developing, validating, and evolving enterprise architectures across government organisations, calibrated to The Gambia’s current capacity and maturity level.

**Enable interoperability by design** by embedding integration, data sharing, and standards compliance as foundational principles rather than afterthoughts.

**Create a sustainable institutional capability** for EA management that can outlast individual projects and donor funding cycles.

This Framework is developed under Contract WARDIP/C4.13.2/2024/DC009 between the International Telecommunication Union (ITU) and the Government of The Gambia, represented by the Gambia Information and Communications Technology Agency (GICTA), within the Ministry of Communications and Digital Economy (MoCDE). The work is funded through the West Africa Regional Digital Integration Programme (WARDIP) with World Bank financing.

## 1.2 Scope

### In Scope

**Tier 1 Government Organisations.** This Framework applies directly to the four organisations designated as Tier 1 stakeholders under the current project:

| **Organisation**                                       | **Abbreviation** | **Domain**                                              |
|--------------------------------------------------------|------------------|---------------------------------------------------------|
| Ministry of Finance and Economic Affairs               | MoFEA            | Public financial management, budget, treasury           |
| Gambia Revenue Authority                               | GRA              | Tax administration, customs, border management          |
| Ministry of Health                                     | MoH              | Health service delivery, surveillance, health financing |
| Ministry of Communications and Digital Economy / GICTA | MoCDE / GICTA    | Digital infrastructure, shared services, EA governance  |

**Shared Digital Services.** The Framework governs cross-government shared services and platforms, including the Government Interoperability Platform (GIP), GamPay payment gateway, digital identity systems, and any future shared infrastructure components.

**Cross-Government Architecture Standards.** The principles, metamodel, governance processes, and methodology defined in this Framework apply to all government architecture work, whether conducted by Tier 1 organisations or extended to additional ministries in subsequent phases.

**EA Capability Establishment.** The Framework covers the organisational structures, services, and maturity progression required to establish and sustain EA as an institutional capability within GICTA and participating ministries.

### Out of Scope

**Detailed Technical Specifications.** This Framework defines what architecture components exist and how they relate; detailed technical designs for specific systems are addressed in target architecture deliverables (D6) and implementation roadmaps (D7).

**Non-Tier 1 Organisations.** While the Framework’s principles and standards are designed for whole-of-government applicability, detailed architecture assessments for organisations beyond Tier 1 are planned for subsequent project phases.

**Commercial and Private Sector Systems.** The Framework does not govern private sector IT systems, though it defines interface standards for government-to-business interactions.

**Procurement Decisions.** While the Framework informs technology selection criteria, specific vendor or product procurement decisions are outside its scope and follow government procurement regulations.

### Scope Boundaries and Extensions

The Framework is designed with explicit extension points. As The Gambia’s EA maturity progresses from the current Level 2.19 toward the target of Level 4.1 by 2030, additional organisations will be onboarded using the methodology and standards defined herein. The two-layer architecture (Generic Cross-Sectoral layer and Sector-Specific layer) supports this progressive extension without requiring Framework revision.

## 1.3 Reference Frameworks

This Framework does not create a new architecture methodology from scratch. Instead, it instantiates and adapts four internationally recognised frameworks, each contributing specific capabilities to The Gambia’s context.

### TOGAF 9.2 — The Open Group Architecture Framework

TOGAF provides the foundational architecture development method and vocabulary. Its Architecture Development Method (ADM) cycle establishes the iterative process for creating and governing enterprise architectures. The Gambia Framework adopts TOGAF’s domain decomposition into Business, Data, Application, and Technology (BDAT) architecture domains, its content metamodel structure, and its governance framework concepts.

**Contribution to this Framework:** Architecture domain structure (Chapter 5), development lifecycle concepts (Chapter 6), governance process patterns (Chapter 4), metamodel foundations (Chapter 5).

### PAERA — Public Administration Ecosystem Reference Architecture

PAERA provides a government-specific reference architecture that extends TOGAF’s generic approach with public administration patterns. It defines standard building blocks for government services, interoperability layers, and cross-agency coordination mechanisms.

**Contribution to this Framework:** Government ecosystem perspective (Chapter 2), public administration reference patterns (Chapter 6), cross-agency coordination models (Chapter 4), service-oriented architecture principles (Chapter 3).

### GovStack — Building Block Specifications

GovStack provides concrete, implementation-ready specifications for common digital government capabilities — digital identity, payments, data exchange, messaging, and other foundational components. Where TOGAF and PAERA operate at the architecture and design level, GovStack bridges to implementation.

**Contribution to this Framework:** Building Block specifications informing the metamodel (Chapter 5), shared services design patterns (Chapter 7), interoperability standards (Chapter 3), digital public infrastructure assessment criteria (Chapter 6).

### GEATDM — Government Enterprise Architecture Target Development Method

GEATDM is the project methodology that guides the overall EA development process for this engagement. It provides a comprehensive method repository with specific guidance on principle formulation, governance establishment, metamodel design, EA services definition, and organisational classification. GEATDM’s five-phase approach (DISCOVER → ASSESS → ADAPT → PLAN → EXECUTE & GOVERN) structures the entire project delivery.

**Contribution to this Framework:** Principles catalogue (Chapter 3), governance templates (Chapter 4), metamodel specifications (Chapter 5), methodology phases (Chapter 6), EA services catalogue (Chapter 7), maturity assessment approach (Chapter 8).

## 1.4 Relationship to National Strategies

This Framework operates within and supports a hierarchy of national strategic instruments. It translates high-level national aspirations into actionable architecture standards and governance mechanisms.

### Digital Economy Master Plan (DEMP) 2024–2034

The DEMP 2033 establishes The Gambia’s overarching digital transformation vision, including the target of 70% government service digitisation. This Framework directly supports DEMP implementation by providing the architecture standards that ensure digitisation efforts are coordinated, defining interoperability requirements, establishing governance mechanisms that align IT investments with DEMP priorities, and creating the maturity assessment approach that measures progress toward DEMP goals.

### West Africa Regional Digital Integration Programme (WARDIP)

WARDIP provides the primary funding mechanism for this EA initiative and establishes the regional integration context. This Framework ensures that Gambia’s architecture decisions are compatible with regional digital integration objectives, particularly in areas of cross-border data exchange, harmonised digital identity, and regional payment interoperability.

### National Development Plan (NDP)

The NDP sets broader development priorities within which digital transformation operates. This Framework supports NDP objectives by ensuring that government IT investments deliver measurable development outcomes, particularly in service delivery improvement, revenue mobilisation, and administrative efficiency.

### National ICT Policy and Cybersecurity Strategy

The ICT Policy establishes the regulatory and institutional framework within which this EA Framework operates. The Framework’s security governance provisions (Chapter 4) and security architecture principles (Chapter 3) align with and operationalise the Cybersecurity Strategy’s requirements within the EA context.

## 1.5 Document Structure Guide

This Framework document is organised into nine chapters, progressing from strategic context through normative content to implementation guidance.

### Chapter Overview

| **Chapter** | **Title**                 | **Content Summary**                                                                                                                                                                                                |
|-------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1           | Introduction              | Purpose, scope, reference frameworks, strategic alignment (this chapter)                                                                                                                                           |
| 2           | EA Framework Structure    | Component overview, relationships, GEATDM mapping, compliance expectations                                                                                                                                         |
| 3           | EA Principles             | 33 architecture principles across five categories (Business Architecture, Data Architecture, Application Architecture, Technology Architecture, Cross-Cutting) with Gambia-specific rationale and compliance tests |
| 4           | EA Governance             | Governance bodies, decision rights, processes, RACI matrix, security governance, KPIs                                                                                                                              |
| 5           | EA Metamodel              | Architecture domains, core objects catalogue, relationships, viewpoints, notation standards                                                                                                                        |
| 6           | EA Methodology            | GEATDM five-phase approach, organisation classification, DPI readiness, project mapping                                                                                                                            |
| 7           | EA Services               | National EA Office establishment, 12-service catalogue, delivery processes, phased rollout                                                                                                                         |
| 8           | EA Repository and Tooling | Repository implementation, tooling selection, data management, integration                                                                                                                                         |
| 9           | EA Maturity Roadmap       | Capability maturity progression from Level 2.19 to 4.1, phased investment plan                                                                                                                                     |

### Audience Navigation Guide

| **Audience**                                    | **Primary Chapters**             | **Purpose**                                                                |
|-------------------------------------------------|----------------------------------|----------------------------------------------------------------------------|
| DTSC Members (Ministers, Permanent Secretaries) | 1, 2, 4 (§4.1–4.3), 9            | Strategic understanding, governance roles, investment decisions            |
| EA Board Members                                | 3, 4, 5 (overview), 6 (overview) | Compliance review, standards enforcement, methodology oversight            |
| National EA Office Staff                        | All chapters                     | Operational reference for day-to-day EA management                         |
| Ministry EA Focal Points                        | 3, 5, 6                          | Principles to follow, how to document architecture, methodology to apply   |
| Ministry IT Staff                               | 3, 5, 7                          | Principles, metamodel for documentation, services available from EA Office |
| Development Partners                            | 1, 2, 9                          | Alignment context, investment opportunities, maturity progression          |
| World Bank / WARDIP                             | 1, 4, 9                          | Contract compliance, governance accountability, progress monitoring        |

### Document Conventions

Throughout this document, the following conventions are used:

**“Shall”** indicates mandatory requirements that must be followed.

**“Should”** indicates recommended practices that apply unless a documented dispensation is granted.

**“May”** indicates optional guidance that organisations can choose to adopt.

***[Gambia-Specific]*** markers identify content adapted specifically for The Gambia’s context.

Architecture object names follow the naming convention defined in Chapter 5, Section 5.7.

# Chapter 2: EA Framework Structure

## 2.1 Framework Components Overview

### The Five Pillars

The Gambia’s Enterprise Architecture Framework is organised around five interconnected pillars, each addressing a distinct aspect of architecture capability. Together, these pillars form a complete system for planning, governing, and evolving the government’s digital landscape.

**Pillar 1: Strategic Direction (Chapter 3)** defines what we believe — the principles, vision, and values that constrain and guide all architecture decisions. The 33 EA principles across five categories (Business Architecture, Data Architecture, Application Architecture, Technology Architecture, Cross-Cutting) provide the normative foundation. Every architecture proposal, system acquisition, and technology investment must demonstrate alignment with these principles.

**Pillar 2: Governance (Chapter 4)** defines who decides and how — the bodies, processes, and decision rights that ensure architecture compliance and coordinated investment. The governance model establishes four tiers: the Digital Transformation Steering Committee (DTSC) for strategic oversight, the EA Board for compliance and standards, the National EA Office for operational management, and Ministry EA Focal Points for domain ownership.

**Pillar 3: Metamodel and Notation (Chapter 5)** defines what we document and how — the standardised objects, attributes, relationships, and viewpoints used to describe architectures. The metamodel provides the common vocabulary that makes architectures from different ministries comparable and composable. It spans six portfolio domains (Strategy, Service, Business, Application, Data, Technology) plus an Investment portfolio for project management and GovStack Building Block alignment.

**Pillar 4: Methodology (Chapter 6)** defines how we work — the phased approach to developing, validating, and evolving enterprise architectures. Based on the GEATDM five-phase method (DISCOVER → ASSESS → ADAPT → PLAN → EXECUTE & GOVERN), the methodology includes organisation classification, reference architecture selection, DPI readiness assessment, and project delivery mapping.

**Pillar 5: EA Services (Chapter 7)** defines what we deliver — the operational services provided by the National EA Office to government organisations. The 12-service catalogue spans architecture development, compliance review, standards management, training, and repository operations, with a phased activation plan that matches The Gambia’s growing EA maturity.

### Supporting Components

Two additional chapters complete the Framework without constituting separate pillars:

**Repository and Tooling (Chapter 8)** addresses the practical infrastructure for managing architecture artefacts — the EA repository, selected tooling, data management practices, and integration with governance processes.

**Maturity Roadmap (Chapter 9)** defines the progressive improvement path from the current EA maturity level (2.19) to the target level (4.1 by 2030), with investment requirements, milestones, and success metrics.

## 2.2 Relationship Between Components

The five pillars do not operate independently. They form a reinforcing system where each component both depends on and enables others. Understanding these relationships is essential for implementing the Framework effectively.

### Key Interaction Patterns

**Principles → Governance.** Principles define what compliance means; governance enforces it. When the EA Board reviews an architecture proposal, it assesses conformance against the 33 principles. The dispensation process (Chapter 4, Section 4.6.3) provides a governed mechanism for exception management when strict principle adherence is impractical.

**Principles → Methodology.** Each phase of the GEATDM methodology incorporates principle validation checkpoints. Architecture outputs from the ASSESS and ADAPT phases are evaluated against principles before progressing to the next phase.

**Metamodel → All Components.** The metamodel provides the shared vocabulary that makes the entire Framework operational. Governance reviews assess metamodel-documented artefacts. The methodology produces metamodel-structured outputs. EA Services deliver metamodel-compliant documentation. Without a shared metamodel, the Framework would lack coherence.

**Governance → EA Services.** Governance bodies commission and authorise EA Services activities. The National EA Office reports to the EA Board on service delivery performance. Service escalation paths lead through governance tiers when standard service delivery cannot resolve issues.

**Methodology → EA Services.** The methodology defines the process; EA Services provide the people and capabilities to execute that process. Each GEATDM phase maps to specific EA services — architecture development services in ADAPT, compliance review services in PLAN, monitoring services in EXECUTE & GOVERN.

**Maturity Roadmap → Progressive Activation.** Not all Framework components activate simultaneously. The maturity roadmap (Chapter 9) sequences component activation based on institutional readiness.

### The Two-Layer Architecture

A critical structural principle of this Framework is the separation between the Generic Cross-Sectoral Layer and the Sector-Specific Layer:

**The Generic Cross-Sectoral Layer** is governed by this Framework and applies universally. It includes the principles (Chapter 3), metamodel (Chapter 5), governance structures (Chapter 4), and shared digital infrastructure. All organisations must comply with this layer.

**The Sector-Specific Layer** extends the generic layer with domain-specific reference architectures, business objects, and application patterns. Each Tier 1 organisation operates within its sector layer while inheriting all cross-sectoral standards. The organisation classification in Chapter 6 (Policy Development Units, Revenue Authorities, Service Delivery Agencies) determines which sector-specific reference architecture applies.

This separation enables the Framework to scale: new organisations are onboarded by connecting them to the generic layer and assigning the appropriate sector-specific reference architecture, without modifying the core Framework.

## 2.3 How This Framework Relates to GEATDM

The Government Enterprise Architecture Target Development Method (GEATDM) is a comprehensive methodology with a full method repository covering all aspects of EA development for government organisations. This Framework is The Gambia’s country-specific instantiation of GEATDM — it takes the generic method and tailors it to the specific context, constraints, and ambitions of The Gambia’s government.

### GEATDM Structure and This Framework’s Position

| **GEATDM Work Package**         | **Content**                                   | **Gambia Framework Chapter** |
|---------------------------------|-----------------------------------------------|------------------------------|
| WP1-T11: Metamodel              | Entity model for EA repository                | Chapter 5                    |
| WP1-T12: EA Principles          | Principle catalogue and governance            | Chapter 3                    |
| WP1-T13: Governance             | Governance bodies, processes, decision rights | Chapter 4                    |
| WP1-T14: EA Services            | EA Office operations and service catalogue    | Chapter 7                    |
| WP2: PDU Reference Architecture | Policy Development Unit patterns              | Chapter 6 (classification)   |
| WP3: RA Reference Architecture  | Revenue Authority patterns                    | Chapter 6 (classification)   |
| WP4: SDA Reference Architecture | Service Delivery Agency patterns              | Chapter 6 (classification)   |
| WP5: Method Guide               | Step-by-step methodology                      | Chapter 6                    |
| WP6-T61: Toolkit                | Templates and tools for EA work               | Chapter 6 (mapping)          |
| WP6-T62: Main Document          | Country-level framework assembly guidance     | This entire document         |

### Nature of Adaptation

The adaptation from GEATDM to The Gambia’s Framework involves three types of change:

**Contextualisation** — Generic guidance is grounded in Gambia-specific institutional names, system names, and organisational structures. For example, GEATDM’s generic “Central EA Authority” becomes GICTA’s National EA Office; generic “government payment platform” becomes GamPay.

**Calibration** — Maturity targets, staffing models, and timeline expectations are calibrated to The Gambia’s starting position (Level 2.19 maturity, 3–5 IT staff per ministry, donor-dependent funding).

**Prioritisation** — From GEATDM’s comprehensive menu of governance processes, EA services, and metamodel elements, The Gambia Framework selects and sequences those that are achievable given current constraints.

## 2.4 Framework Applicability and Compliance Expectations

### Applicability Tiers

| **Tier**                            | **Organisations**                           | **Obligation**                                                                               | **Timeline**                        |
|-------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------|
| **Tier 1 — Full Compliance**        | MoFEA, GRA, MoH, MoCDE/GICTA                | Must comply with all Framework components; architecture artefacts subject to EA Board review | Immediate (upon Framework adoption) |
| **Tier 2 — Progressive Compliance** | Ministries onboarded in Phase 2 (2027–2029) | Must adopt principles and governance; architecture development follows GEATDM methodology    | Within 12 months of onboarding      |
| **Tier 3 — Voluntary Adoption**     | All other government organisations          | Encouraged to adopt principles; may request EA Services                                      | No mandatory timeline               |

### Mandatory vs. Advisory Content

**Mandatory (“Shall”) Requirements:** EA principles (Chapter 3) — all 33 principles are binding for Tier 1 organisations. Governance participation (Chapter 4) — Tier 1 organisations shall designate an EA Focal Point, participate in EA Board reviews, and submit architectures through the compliance process. Metamodel compliance (Chapter 5) — architecture artefacts shall use the defined objects, attributes, and naming conventions. Methodology adherence (Chapter 6) — architecture development shall follow the GEATDM phase structure with defined decision points.

**Advisory (“Should”) Recommendations:** Specific tooling selections (Chapter 8) — tooling recommendations guide but do not mandate specific products. Service-level targets (Chapter 7) — advisory until the National EA Office reaches operational maturity. Extended metamodel viewpoints (Chapter 5) — beyond core mandatory viewpoints, additional analytical viewpoints are recommended but not required.

### Enforcement Timeline

**Phase 1 — Foundation (Year 1, 2026):** Focus on governance establishment and awareness. Compliance reviews are advisory — findings are documented but non-compliance does not block investment. Emphasis on building understanding and habits.

**Phase 2 — Transition (Years 2–3, 2027–2028):** Compliance reviews become binding for major investments. Dispensation process is fully operational. Annual health checks begin. EA Board has authority to require architectural changes.

**Phase 3 — Full Operation (Years 4+, 2029 onwards):** Full compliance enforcement across all Tier 1 organisations. Extension to Tier 2 organisations begins. Performance metrics and KPIs are actively tracked and reported to DTSC.

# Chapter 3: EA Principles

## 3.1 Architecture Vision for The Gambia

The Gambia’s Enterprise Architecture principles provide the foundational guidelines that will inform and govern all architecture and technology decisions across government ministries, departments, and agencies for the architecture validity period 2026–2033. These principles translate The Gambia’s national ambitions — articulated in the Digital Economy Master Plan (DEMP) 2024–2034, the Western Africa Regional Digital Integration Project (WARDIP), and the broader vision to become “the most advanced digital society and IT innovation hub in Africa” — into concrete, actionable decision criteria.

The principles are grounded in The Gambia’s current reality: an EA maturity level of 2.19 on a 5.0 scale, approximately 62% national electricity access, a single submarine cable (ACE) providing international connectivity, IT teams of 3–5 staff per ministry, and heavy reliance on donor funding. They are calibrated to guide a progressive transformation towards an integrated, whole-of-government digital ecosystem targeting EA maturity level 4.1 by 2030.

These principles are binding on all Tier 1 ministries — MoFEA, GRA, MoH, and MoCDE/GICTA — and serve as the normative reference for all subsequent deliverables (D3 through D13).

## 3.2 Principle’s Structure

Each principle is documented using the GEATDM standard structure to ensure clarity, traceability, and actionability:

| **Element**      | **Description**                                                         |
|------------------|-------------------------------------------------------------------------|
| **ID**           | Domain identifier (BA, DA, APP, TECH, CC) followed by a sequence number |
| **Name**         | Short, memorable name that captures the essence of the principle        |
| **Statement**    | Clear, actionable principle statement written in imperative form        |
| **Rationale**    | Why this principle matters for The Gambia’s digital transformation      |
| **Implications** | Concrete consequences and requirements for architecture decisions       |

Principles are organised into five categories:

| **Category**                   | **Count** | **Focus**                                  |
|--------------------------------|-----------|--------------------------------------------|
| Business Architecture (BA)     | 7         | Services, processes, customer experience   |
| Data Architecture (DA)         | 7         | Data management, quality, sharing          |
| Application Architecture (APP) | 7         | Applications, integration, building blocks |
| Technology Architecture (TECH) | 7         | Infrastructure, security, operations       |
| Cross-Cutting (CC)             | 5         | Principles spanning all domains            |
| **Total**                      | **33**    |                                            |

## 3.3 Business Architecture Principles

Business Architecture Principles guide the design of government services, business processes, and organisational capabilities to meet the needs of Gambian citizens, businesses, and government stakeholders.

### BA-01: Customer-Centric Service Design

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>BA-01</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Customer-Centric Service Design</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>All government services shall be designed from the perspective of the needs of Gambian citizens and businesses, prioritising user experience, accessibility, and outcomes over internal administrative convenience.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia’s DEMP 2024–2034 targets 70% service digitisation by 2033. With varying levels of digital literacy, multiple languages, and limited internet access in rural areas, an outside-in design perspective is essential. The planned MyGov citizen portal will serve as the primary digital channel and must be built around citizen needs from inception.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> User research involving Gambian citizens and businesses must inform the design of all digital services.<br />
<strong>(2)</strong> Services must be tested with actual users before full deployment.<br />
<strong>(3)</strong> Service performance must be measured from the customer perspective.<br />
<strong>(4)</strong> Accessibility standards must be applied across all digital touchpoints, accounting for The Gambia’s multilingual context.<br />
<strong>(5)</strong> The DTSC shall review service designs for citizen-centricity as part of the architecture compliance process.</td>
</tr>
</tbody>
</table>

### BA-02: Process Standardisation and Automation

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>BA-02</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Process Standardisation and Automation</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Core government business processes shall be standardised, documented, and automated where feasible, reducing manual intervention and ensuring consistent outcomes across all ministries.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Current state assessment reveals significant process fragmentation across Tier 1 ministries. With IT teams of only 3–5 staff per ministry, standardised, automated processes free limited staff for higher-value activities. GRA’s experience with GamTax Net demonstrates that automation significantly reduces processing time.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Business processes must be documented in a standard notation before automation.<br />
<strong>(2)</strong> Process variations between ministries must be minimised and formally justified.<br />
<strong>(3)</strong> Workflow automation shall be prioritised for high-volume, rule-based processes.<br />
<strong>(4)</strong> Exception handling processes must be defined.<br />
<strong>(5)</strong> Process performance metrics must be established and monitored.</td>
</tr>
</tbody>
</table>

### BA-03: Capability-Based Planning

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>BA-03</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Capability-Based Planning</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>IT investments across The Gambia’s government shall be prioritised based on their contribution to organisational capabilities required to deliver public services and achieve national strategic objectives.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>With heavy dependence on donor funding and constrained national budgets, The Gambia must ensure every technology investment directly strengthens government capacity. Capability-based planning provides a stable framework that transcends individual ministry restructuring, technology changes, and donor programme cycles.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> A national government capability map must be developed and maintained by the National EA Office.<br />
<strong>(2)</strong> Business cases must demonstrate which capabilities will be enhanced and their link to DEMP 2033.<br />
<strong>(3)</strong> Investment prioritisation must consider capability gaps identified in the As-Is assessment (D5).<br />
<strong>(4)</strong> The application portfolio must be mapped to the capability model.<br />
<strong>(5)</strong> Capability maturity shall be assessed periodically.</td>
</tr>
</tbody>
</table>

### BA-04: Service Orientation

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>BA-04</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Service Orientation</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government functions shall be organised and delivered as discrete, well-defined services with clear interfaces, enabling composition, reuse, and measurement across The Gambia’s public administration.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Service orientation enables shared services that multiple ministries can consume. GamPay is an early example. This approach maximises impact per investment dollar and aligns with GovStack Building Block specifications.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> A government service catalogue must be established with clear ownership.<br />
<strong>(2)</strong> Services must have defined scope, interfaces, and service level targets.<br />
<strong>(3)</strong> Shared services must be consumed by all ministries rather than duplicated.<br />
<strong>(4)</strong> New service development must assess whether an existing shared service can be extended.<br />
<strong>(5)</strong> Service performance must be monitored and reported to the EA Board.</td>
</tr>
</tbody>
</table>

### BA-05: Regulatory Compliance by Design

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>BA-05</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Regulatory Compliance by Design</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government business processes and services shall be designed with compliance requirements built in from inception, reflecting The Gambia’s legal and regulatory framework.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia’s regulatory landscape is evolving, with a Data Protection Act under development and cybersecurity legislation pending. Building compliance into system design from the outset is essential for building citizen trust.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Regulatory requirements must be captured during requirements analysis.<br />
<strong>(2)</strong> Compliance validation shall be automated where feasible.<br />
<strong>(3)</strong> Audit trails must be built into all government systems.<br />
<strong>(4)</strong> A regulatory change management process must be established.<br />
<strong>(5)</strong> Systems must accommodate The Gambia’s pending Data Protection Act requirements from inception.</td>
</tr>
</tbody>
</table>

### BA-06: Channel Choice and Consistency

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>BA-06</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Channel Choice and Consistency</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government services shall be accessible through multiple channels appropriate to the Gambian population, delivering consistent information and outcomes regardless of the channel used.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia’s infrastructure reality — 62% electricity access, limited broadband outside urban areas — means digital-only service delivery would exclude a significant portion of the population. Digital-first does not mean digital-only.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Digital channels shall be the primary option but physical service counters must remain available during transition.<br />
<strong>(2)</strong> Service logic must be channel-agnostic.<br />
<strong>(3)</strong> Information must be synchronised across channels.<br />
<strong>(4)</strong> Channel analytics must inform service design improvements.<br />
<strong>(5)</strong> Assisted digital options must be available at ministry offices.</td>
</tr>
</tbody>
</table>

### BA-07: Natural Digital Environment Integration

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>BA-07</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Natural Digital Environment Integration</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Where feasible, government services shall be delivered directly to stakeholders’ existing digital environments rather than requiring interaction exclusively through government portals.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>GRA’s API-based integration with GamPay demonstrates this principle: businesses can initiate tax payments from their own systems. Extending this pattern improves compliance rates.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> APIs must be provided for all appropriate government services.<br />
<strong>(2)</strong> Integration patterns must support common business software used in The Gambia.<br />
<strong>(3)</strong> Standards must align with regional and international practices.<br />
<strong>(4)</strong> Third-party service providers may be authorised through approved APIs.<br />
<strong>(5)</strong> Security and liability frameworks must be established for API-based service delivery.</td>
</tr>
</tbody>
</table>

## 3.4 Data Architecture Principles

Data Architecture Principles guide the management, governance, quality, and use of government data as a strategic national asset.

### DA-01: Data as a Strategic Asset

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>DA-01</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Data as a Strategic Asset</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government data shall be managed as a strategic national asset, with defined ownership, quality standards, lifecycle management, and governance appropriate to its value and sensitivity.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia’s government generates significant data through its operational systems. IFMIS processes financial transactions for approximately 41,958 civil servants, GRA collects revenue from thousands of taxpayers, DHIS2 aggregates data from over 700 facilities. This data, if properly managed, provides the foundation for evidence-based policy making.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Data ownership must be formally assigned for all significant government data domains.<br />
<strong>(2)</strong> Data quality metrics must be established and monitored.<br />
<strong>(3)</strong> Data lifecycle policies must govern creation, use, archival, and disposal.<br />
<strong>(4)</strong> A national data catalogue shall be developed as part of the GIP.<br />
<strong>(5)</strong> Data valuation should inform investment decisions.</td>
</tr>
</tbody>
</table>

### DA-02: Once-Only Data Collection

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>DA-02</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Once-Only Data Collection</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>The Government of The Gambia shall collect data from citizens and businesses only once, enabling authorised reuse across government systems through integration with authoritative sources.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Current assessment reveals multiple agencies independently collecting the same information. This duplication burdens citizens, creates data inconsistencies, and increases administrative costs. The once-only principle is foundational to integrated digital government.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Systems must integrate with authoritative data sources rather than collecting duplicate data.<br />
<strong>(2)</strong> Data sharing agreements must be established between ministries.<br />
<strong>(3)</strong> Master data entities must be identified and managed through designated authoritative systems.<br />
<strong>(4)</strong> Consent management mechanisms must be implemented.<br />
<strong>(5)</strong> The GIP shall serve as the primary infrastructure for once-only data exchange.</td>
</tr>
</tbody>
</table>

### DA-03: Single Source of Truth

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>DA-03</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Single Source of Truth</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Each government data entity shall have one authoritative source system that serves as the system of record.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia currently operates multiple systems maintaining independent copies of the same data. Designating a single authoritative source for each data entity is essential for data integrity and for enabling the GIP.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Authoritative sources must be formally designated — IFMIS for financial data, GamTax Net for tax data, ASYCUDA World for customs data, DHIS2 for health programme data.<br />
<strong>(2)</strong> Data integration flows must run from authoritative sources to consuming systems.<br />
<strong>(3)</strong> Data updates must be made in the designated source system.<br />
<strong>(4)</strong> The EA Board shall maintain the authoritative source registry.</td>
</tr>
</tbody>
</table>

### DA-04: Data Quality Management

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>DA-04</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Data Quality Management</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government data quality shall be actively managed through defined standards, profiling, validation, cleansing, and continuous monitoring.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Poor data quality undermines every aspect of digital transformation. As the government moves towards integrated digital services, data quality management transitions from a nice-to-have to a critical capability.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Data quality dimensions must be defined for all key government datasets.<br />
<strong>(2)</strong> Quality validation rules must be implemented at the point of data capture.<br />
<strong>(3)</strong> Quality metrics must be measured periodically and reported.<br />
<strong>(4)</strong> Remediation processes must be established.<br />
<strong>(5)</strong> Data profiling exercises shall be conducted as part of D3 establishment.</td>
</tr>
</tbody>
</table>

### DA-05: Privacy and Data Protection by Design

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>DA-05</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Privacy and Data Protection by Design</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Privacy and data protection requirements shall be incorporated into the design of all government systems from inception, implementing data minimisation, purpose limitation, and appropriate safeguards.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Government systems hold some of the most sensitive personal data in the country. Building privacy into system design from inception is essential and far less costly than retrofitting once the Data Protection Act is enacted.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Privacy impact assessments must be conducted for all new system developments involving personal data.<br />
<strong>(2)</strong> Data minimisation must be enforced.<br />
<strong>(3)</strong> Purpose limitation must prevent unauthorised reuse.<br />
<strong>(4)</strong> Data subject rights must be technically supported.<br />
<strong>(5)</strong> Health data systems must implement controls compliant with international standards.</td>
</tr>
</tbody>
</table>

### DA-06: Data Sharing and Interoperability

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>DA-06</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Data Sharing and Interoperability</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government data shall be structured, documented, and exposed through standard interfaces to enable authorised sharing through the Government Interoperability Platform (GIP).</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The value of government data multiplies when shared appropriately. The planned GIP, based on the Information Mediator (X-Road) pattern, will provide secure infrastructure for automated data exchange.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> All cross-ministry data exchange must use the GIP once operational.<br />
<strong>(2)</strong> Data formats must follow national and international standards.<br />
<strong>(3)</strong> APIs must be provided by all authoritative source systems.<br />
<strong>(4)</strong> Data sharing agreements must be formalised and approved by the EA Board.<br />
<strong>(5)</strong> GamPay’s existing API-based integration pattern shall serve as the reference model.</td>
</tr>
</tbody>
</table>

### DA-07: Analytics-Ready Data

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>DA-07</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Analytics-Ready Data</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government data shall be captured, structured, and managed to support both operational needs and analytical use cases.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia’s national development priorities require evidence-based policy making. As the government integrates data through the GIP, the opportunity to establish whole-of-government analytical capability becomes viable.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> A government analytical data platform shall be planned as a Phase 2/3 initiative.<br />
<strong>(2)</strong> ETL/ELT processes must be designed for transforming operational data.<br />
<strong>(3)</strong> Historical data must be retained for a minimum of 5 years.<br />
<strong>(4)</strong> Self-service analytics capabilities should be prioritised.</td>
</tr>
</tbody>
</table>

## 3.5 Application Architecture Principles

Application Architecture Principles guide the design, selection, integration, and management of government applications.

### APP-01: Building Block Orientation

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>APP-01</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Building Block Orientation</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>The Gambia’s government application architecture shall be constructed from standardised, interoperable building blocks aligned with GovStack specifications, favouring reuse over custom development.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>With limited IT staff and constrained budgets, The Gambia cannot afford to custom-build every application. GovStack Building Block specifications provide proven patterns. Existing systems already demonstrate building block patterns: GamPay (Payments BB), DHIS2 (Digital Registries), ASYCUDA World (customs blocks).</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> GovStack BB specifications must be the primary reference for evaluating solutions.<br />
<strong>(2)</strong> Available national DPI building blocks must be leveraged.<br />
<strong>(3)</strong> Build-vs-buy-vs-reuse decisions must justify why an existing BB cannot meet the requirement.<br />
<strong>(4)</strong> All building blocks must integrate through standard GovStack interoperability patterns.</td>
</tr>
</tbody>
</table>

### APP-02: Loose Coupling and High Cohesion

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>APP-02</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Loose Coupling and High Cohesion</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government applications shall be designed with loose coupling between components and high cohesion within components, enabling independent change.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Tight coupling means upgrading one system risks disrupting others. Loose coupling enables each system to evolve independently, essential for a government that must modernise incrementally within budget constraints.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Integration must use well-defined APIs — direct database access between applications is prohibited.<br />
<strong>(2)</strong> Applications must encapsulate their data behind service interfaces.<br />
<strong>(3)</strong> Event-driven patterns should be adopted where appropriate.<br />
<strong>(4)</strong> Shared databases between independent applications must be avoided.<br />
<strong>(5)</strong> The GIP shall serve as the preferred integration layer.</td>
</tr>
</tbody>
</table>

### APP-03: Integration Through National DPI

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>APP-03</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Integration Through National DPI</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Inter-system integration shall utilise national Digital Public Infrastructure components — the GIP, GamPay, and the National Digital Identity Platform — rather than point-to-point connections.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Point-to-point connections proliferate rapidly. The current IFMIS-GRA integration via manual email illustrates the inefficiency of ad-hoc approaches. GamPay already demonstrates this principle as the single payment integration point.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> All new inter-ministry integration must be planned for the GIP from inception.<br />
<strong>(2)</strong> Existing point-to-point connections must be migrated to the GIP per the roadmap (D7).<br />
<strong>(3)</strong> Integration patterns must follow national standards approved by the EA Board.<br />
<strong>(4)</strong> Exception handling must address DPI unavailability.</td>
</tr>
</tbody>
</table>

### APP-04: No Legacy by Design

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>APP-04</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>No Legacy by Design</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government applications shall be designed for maintainability and continuous evolution, with regular updates and periodic technology refresh planned from inception.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Every application deployed must include a sustainability plan from inception. Prevention of legacy is far more cost-effective than legacy remediation.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> All applications must receive regular updates — at minimum annual security patches.<br />
<strong>(2)</strong> Technology platforms must have defined refresh cycles (5–7 years) planned and budgeted from procurement.<br />
<strong>(3)</strong> Technical debt must be tracked in the EA Repository.<br />
<strong>(4)</strong> Exit strategies must be defined for all applications.</td>
</tr>
</tbody>
</table>

### APP-05: API-First Design

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>APP-05</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>API-First Design</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government applications shall expose functionality through well-documented APIs as the primary integration mechanism.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>APIs decouple functionality from presentation. GamPay’s API-based architecture has proven this approach in The Gambia. Extending API-first design is essential for the GIP.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> APIs must be designed before user interfaces for all new development.<br />
<strong>(2)</strong> API documentation must be comprehensive and published.<br />
<strong>(3)</strong> API versioning must be implemented.<br />
<strong>(4)</strong> API security must include authentication, authorisation, rate limiting, and encryption.<br />
<strong>(5)</strong> All APIs exposed through the GIP must conform to nationally defined standards.</td>
</tr>
</tbody>
</table>

### APP-06: Cloud-Ready and Platform-Neutral

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>APP-06</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Cloud-Ready and Platform-Neutral</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Government applications shall be designed for deployment flexibility, capable of running on-premises, in the G-Cloud, or in authorised commercial cloud environments without vendor lock-in.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Vendor lock-in is particularly dangerous for a country with limited negotiating leverage. Open-source solutions and platform-neutral designs protect The Gambia’s long-term flexibility.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Containerisation should be adopted where appropriate.<br />
<strong>(2)</strong> Proprietary cloud services must be abstracted.<br />
<strong>(3)</strong> Infrastructure as Code must enable reproducible deployments.<br />
<strong>(4)</strong> Data portability must be ensured — all government data extractable in standard formats.<br />
<strong>(5)</strong> Open-source solutions must be actively considered.</td>
</tr>
</tbody>
</table>

### APP-07: Modularity and Incremental Delivery

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>APP-07</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Modularity and Incremental Delivery</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Application development shall follow modular architectures that support incremental delivery of value.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Large monolithic IT projects have high failure rates, amplified in The Gambia’s resource-constrained environment. MoFEA’s planned approach of extending IFMIS through modular satellite applications demonstrates this principle.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Solutions must be decomposed into independently deliverable modules.<br />
<strong>(2)</strong> Dependencies between modules must be minimised.<br />
<strong>(3)</strong> Minimum viable products must be defined for initial releases.<br />
<strong>(4)</strong> Each increment must deliver measurable value to users.</td>
</tr>
</tbody>
</table>

## 3.6 Technology Architecture Principles

Technology Architecture Principles guide infrastructure, security, and operational decisions.

### TECH-01: Security by Design

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>TECH-01</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Security by Design</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Security shall be integrated into all aspects of The Gambia’s government technology architecture from inception, implementing defence in depth, least privilege, and zero trust principles.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Security is a contract-prioritised area. Government systems process sensitive data — financial records in IFMIS, taxpayer data in GamTax Net, patient health records in DHIS2. The Gambia’s GCI score of 32.12 underscores the urgency of systematic improvement.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Threat modelling must inform architecture decisions.<br />
<strong>(2)</strong> Defence in depth must layer multiple security controls.<br />
<strong>(3)</strong> Least privilege must limit access to the minimum necessary.<br />
<strong>(4)</strong> Zero trust principles must be progressively adopted.<br />
<strong>(5)</strong> Security testing must be continuous.<br />
<strong>(6)</strong> Encryption: AES-256 at rest, TLS 1.3 in transit.<br />
<strong>(7)</strong> The EA Board must include security review as a mandatory gate.</td>
</tr>
</tbody>
</table>

### TECH-02: Resilience and Business Continuity

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>TECH-02</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Resilience and Business Continuity</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Technology infrastructure shall be designed for resilience, with redundancy, failover, disaster recovery, and business continuity capabilities appropriate to criticality and The Gambia’s infrastructure constraints.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia faces amplified resilience requirements: single submarine cable (ACE), unreliable power supply (62% access), limited data centre capacity. IFMIS unavailability directly impacts 41,958+ government employees.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Service criticality must be assessed and classified.<br />
<strong>(2)</strong> RTO and RPO must be defined per criticality tier.<br />
<strong>(3)</strong> Redundancy must eliminate single points of failure for critical systems.<br />
<strong>(4)</strong> Business continuity plans must be documented and tested annually.<br />
<strong>(5)</strong> The second submarine cable investment under WARDIP must be prioritised.</td>
</tr>
</tbody>
</table>

### TECH-03: Scalability and Performance

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>TECH-03</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Scalability and Performance</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Technology infrastructure shall be designed for scalability and performance optimised for user experience under constrained network conditions.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Government service demand peaks unpredictably. Performance must be optimised for The Gambia’s network realities: lower bandwidth, higher latency, mobile-first access.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Capacity planning must anticipate growth aligned with DEMP 2033 targets.<br />
<strong>(2)</strong> Horizontal scaling must be enabled where feasible.<br />
<strong>(3)</strong> Performance baselines and targets must be established.<br />
<strong>(4)</strong> Applications must be optimised for low-bandwidth conditions.</td>
</tr>
</tbody>
</table>

### TECH-04: Standardisation and Simplification

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>TECH-04</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Standardisation and Simplification</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Technology choices shall be standardised to minimise complexity, reduce skill requirements, and enable operational efficiency.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>With IT teams of only 3–5 staff per ministry, The Gambia cannot afford technology proliferation. Reducing the portfolio to managed standards enables deeper expertise.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> A government technology standards register must be established.<br />
<strong>(2)</strong> Standard technology offerings must be defined for common requirements.<br />
<strong>(3)</strong> Non-standard selections must be formally justified and approved by the EA Board.<br />
<strong>(4)</strong> Open-source technologies shall be preferred where suitable.</td>
</tr>
</tbody>
</table>

### TECH-05: Infrastructure as Code

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>TECH-05</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Infrastructure as Code</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Infrastructure provisioning and configuration shall be defined as version-controlled code.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Manual infrastructure configuration is error-prone. IaC is a force multiplier for limited IT staff and directly supports disaster recovery.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Infrastructure configurations must be defined in code.<br />
<strong>(2)</strong> Infrastructure code must be version-controlled.<br />
<strong>(3)</strong> Manual configuration changes in production are prohibited for IaC-managed systems.<br />
<strong>(4)</strong> IaC adoption shall be phased: G-Cloud first, then existing critical systems.</td>
</tr>
</tbody>
</table>

### TECH-06: Observability and Monitoring

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>TECH-06</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Observability and Monitoring</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>All government systems shall implement comprehensive observability — logging, metrics, and tracing.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Current monitoring capabilities are limited. Proactive monitoring is essential: detecting issues before they impact citizens is far more efficient than reactive firefighting.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Logging standards must be defined nationally.<br />
<strong>(2)</strong> Metrics must cover technical and business dimensions.<br />
<strong>(3)</strong> Centralised monitoring must aggregate observability data from all Tier 1 systems.<br />
<strong>(4)</strong> Alerting must notify operations staff based on defined thresholds.</td>
</tr>
</tbody>
</table>

### TECH-07: Sustainable and Responsible Technology

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>TECH-07</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Sustainable and Responsible Technology</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Technology choices shall consider environmental sustainability, energy efficiency, and responsible resource utilisation.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia is particularly vulnerable to climate change impacts. Government technology must be as energy-efficient as possible. Cloud consolidation, virtualisation, and efficient hardware selection directly reduce energy consumption.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Energy efficiency must be a scored criterion in procurement evaluations.<br />
<strong>(2)</strong> The G-Cloud strategy must incorporate energy-efficient design.<br />
<strong>(3)</strong> Virtualisation and containerisation must minimise physical hardware footprint.<br />
<strong>(4)</strong> Hardware lifecycle management must include responsible disposal.</td>
</tr>
</tbody>
</table>

## 3.7 Cross-Cutting Principles

Cross-Cutting Principles span all architecture domains and reflect The Gambia’s fundamental values for digital government transformation.

### CC-01: Whole-of-Government Alignment

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>CC-01</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Whole-of-Government Alignment</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Architecture decisions across all ministries shall align with whole-of-government strategies, national standards, and shared services.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>The Gambia’s small size and limited resources make whole-of-government alignment essential. The DEMP 2033 explicitly calls for a unified digital government approach.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> National strategies must inform all ministry-level architecture decisions.<br />
<strong>(2)</strong> Shared services must be consumed by all ministries — building alternatives is prohibited without EA Board dispensation.<br />
<strong>(3)</strong> Citizen identity must be consistent across all government services.<br />
<strong>(4)</strong> ECOWAS and regional integration commitments must inform national standards.</td>
</tr>
</tbody>
</table>

### CC-02: Digital by Default, Inclusive by Design

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>CC-02</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Digital by Default, Inclusive by Design</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Digital channels shall be the primary means of government service delivery while ensuring inclusive access for all Gambians.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Digital by default drives efficiency and transparency; inclusive design ensures equity. The transition must be managed to avoid creating a two-tier society.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Digital must be the primary channel but alternative access must remain available during transition.<br />
<strong>(2)</strong> Accessibility standards (WCAG 2.1 Level AA minimum) must be implemented.<br />
<strong>(3)</strong> Assisted digital options must be available.<br />
<strong>(4)</strong> Offline-capable and low-bandwidth design patterns must be adopted.<br />
<strong>(5)</strong> Digital literacy support must be embedded in capacity building programmes.</td>
</tr>
</tbody>
</table>

### CC-03: Continuous Improvement and Innovation

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>CC-03</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Continuous Improvement and Innovation</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Architecture shall enable continuous improvement and responsible innovation within The Gambia’s capacity constraints.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Countries at The Gambia’s maturity level benefit most from adopting proven innovations rather than experimenting with unproven approaches.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Performance metrics must be established for all major systems.<br />
<strong>(2)</strong> Feedback loops must capture input from system users.<br />
<strong>(3)</strong> Pilot programmes must be used to test new approaches safely.<br />
<strong>(4)</strong> Knowledge sharing mechanisms must disseminate lessons learned.</td>
</tr>
</tbody>
</table>

### CC-04: Transparency and Accountability

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>CC-04</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Transparency and Accountability</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Architecture shall support transparency in government operations and clear accountability for decisions.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Public trust in government is essential for digital service adoption. Audit trails in IFMIS, GamTax Net, and health systems are governance requirements, not optional features.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Audit trails must track all significant actions in government systems.<br />
<strong>(2)</strong> Decision rationale must be documented through Architecture Decision Records.<br />
<strong>(3)</strong> Open data must be published where appropriate.<br />
<strong>(4)</strong> Performance information for digital services must be published.</td>
</tr>
</tbody>
</table>

### CC-05: Value for Money and Sustainability

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>CC-05</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Value for Money and Sustainability</td>
</tr>
<tr class="odd">
<td><strong>Statement</strong></td>
<td>Architecture decisions shall demonstrate clear value for public investment, with lifecycle costs considered, duplication avoided, and long-term operational sustainability ensured beyond initial donor funding periods.</td>
</tr>
<tr class="even">
<td><strong>Rationale</strong></td>
<td>Donor-funded systems that cannot be sustained from domestic resources after project completion become liabilities. Every decision must demonstrate not only initial value but long-term sustainability.</td>
</tr>
<tr class="odd">
<td><strong>Implications</strong></td>
<td><strong>(1)</strong> Business cases must quantify expected benefits over the architecture validity period.<br />
<strong>(2)</strong> Total cost of ownership must be calculated for all proposed solutions.<br />
<strong>(3)</strong> Benefits realisation must be tracked.<br />
<strong>(4)</strong> Open-source solutions must be actively considered and preferred.<br />
<strong>(5)</strong> Reuse of existing investments must be prioritised over replacement.</td>
</tr>
</tbody>
</table>

## 3.8 Principle Application and Compliance Guidance

### 3.8.1 How Principles Are Applied

**Strategic Level (DTSC):** Principles inform investment prioritisation, programme design, and strategic direction.

**Solution Level (EA Board):** Principles serve as the primary evaluation criteria in architecture compliance reviews.

**Implementation Level (Ministry EA Focal Points):** Principles guide day-to-day technology decisions within ministries.

### 3.8.2 Principle Compliance Assessment

| **Classification**                  | **Definition**                                                                                                   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Compliant**                       | The proposed solution fully satisfies the principle requirements                                                 |
| **Partially Compliant**             | The solution satisfies the principle in some respects but has identified gaps with a documented remediation plan |
| **Non-Compliant with Dispensation** | The solution does not satisfy the principle, but a formal dispensation has been approved                         |
| **Non-Compliant**                   | The solution does not satisfy the principle and no dispensation has been granted                                 |

### 3.8.3 Dispensation Process

When a proposed solution cannot comply with one or more principles, the proposing ministry must submit a formal dispensation request to the EA Board including: specific principles affected, reason compliance cannot be achieved, risk assessment, mitigation approach, and remediation timeline. The detailed dispensation management process, including approval categories and escalation, is defined in Chapter 4, Section 4.6.3.

### 3.8.4 Principle Review Cycle

Principles shall be reviewed annually by the EA Board to assess continued relevance, consistency with updated national and international frameworks, effectiveness based on compliance experience, and completeness. Changes follow the formal change management process defined in Chapter 4.

### 3.8.5 Principle Priority in Conflict Situations

When principles conflict, the following priority guidance applies:

**1.** Security and privacy principles (TECH-01, DA-05) take priority in cases involving personal data or critical systems.

**2.** Whole-of-government alignment (CC-01) takes priority over ministry-specific optimisation.

**3.** Sustainability (CC-05) takes priority over feature richness.

**4.** The EA Board is the arbiter of principle conflicts and must document the rationale.

# Chapter 4: Enterprise Architecture Governance

## 4.1 Governance Hierarchy Overview

Enterprise Architecture governance provides the organisational structure, processes, and decision-making frameworks that ensure ICT investments and solutions across The Gambia’s government align with the national digital transformation strategy, comply with EA principles and standards, and deliver measurable value.

### 4.1.1 Governance Objectives

**1. Strategic Alignment** — Ensure all architectural decisions support the DEMP 2033, the NDP, and ministry-level business strategies.

**2. Standards Compliance** — Maintain adherence to the EA principles, technology standards, and integration patterns.

**3. Investment Optimisation** — Guide IT portfolio decisions to maximise value, reduce duplication, and direct scarce resources toward highest-impact initiatives.

**4. Risk Management** — Identify and mitigate architectural risks before they affect operations.

**5. Continuous Improvement** — Drive evolution of EA practices targeting Level 4.1 by 2030.

### 4.1.2 Governance Scope

EA governance encompasses all ICT-related investment and change activities across Tier 1 ministries (MoFEA, GRA, MoH, MoCDE/GICTA) and, progressively, all MDAs. The scope includes architecture vision and standards enforcement, architecture development and maintenance, solution design review and compliance assessment, change management and dispensation handling, IT portfolio oversight and investment approval, benefits realisation tracking, and security architecture governance (contract-prioritised).

### 4.1.3 Three-Tier Governance Structure

| **Tier** | **Body**                                         | **Chair**                  | **Cadence**      | **Primary Role**                                   |
|----------|--------------------------------------------------|----------------------------|------------------|----------------------------------------------------|
| Tier 1   | Digital Transformation Steering Committee (DTSC) | Cabinet Secretary          | Quarterly        | Strategic direction and executive sponsorship      |
| Tier 2   | Enterprise Architecture Board (EA Board)         | PS, MoCDE                  | Monthly          | Architecture decisions and standards approval      |
| Tier 3   | National EA Office (within GICTA)                | Chief Enterprise Architect | Continuous       | Day-to-day governance and implementation           |
| —        | Ministry EA Focal Points (federated)             | Ministry ICT Directors     | Part-time (~25%) | Domain architecture ownership within each ministry |

The three-tier structure leverages existing institutions, implements a federated model appropriate for resource-constrained ministries (3–5 IT staff each), and supports progressive expansion from Tier 1 to all MDAs.

## 4.2 Digital Transformation Steering Committee (DTSC)

The DTSC is the apex governance body. It provides strategic direction, approves major investment decisions, resolves cross-ministry conflicts, and ensures digital transformation delivers on strategic priorities.

### 4.2.2 Membership

| **Role**                                    | **Institution**         | **Participation**          |
|---------------------------------------------|-------------------------|----------------------------|
| Cabinet Secretary                           | Office of the President | Chairman                   |
| Permanent Secretary                         | MoCDE                   | Vice Chairman              |
| Permanent Secretary                         | MoFEA                   | Member                     |
| Commissioner General                        | GRA                     | Member                     |
| Permanent Secretary                         | MoH                     | Member                     |
| Director General (Prof. Abdou Karim Jallow) | GICTA                   | Member & Technical Adviser |
| Representative                              | WARDIP / World Bank     | Observer                   |
| Chief Enterprise Architect                  | National EA Office      | Secretary (non-voting)     |

## 4.3 Enterprise Architecture Board (EA Board)

The EA Board is the primary technical governance body for EA compliance and standards. It operates under the DTSC’s strategic authority and is supported by the National EA Office.

### 4.3.3 Decision Authority Matrix

| **Decision Type**                            | **EA Board Authority**  | **Escalation** |
|----------------------------------------------|-------------------------|----------------|
| Architecture principles and standards        | Approve                 | —              |
| Target architecture artefacts                | Approve                 | —              |
| Technology standard selections               | Approve                 | —              |
| Minor dispensation requests                  | Approve                 | —              |
| Major dispensation requests (cross-ministry) | Recommend               | DTSC           |
| IT investments USD 50,000 – 250,000          | Approve                 | —              |
| IT investments USD 250,001 – 1,000,000       | Approve with conditions | —              |
| IT investments \> USD 1,000,000              | Recommend               | DTSC           |

## 4.4 National EA Office

The National EA Office is the operational arm of EA governance, housed within GICTA, reporting to the Director General. It executes day-to-day governance activities, maintains the EA repository, conducts compliance reviews, and provides architectural guidance.

### 4.4.3 Staffing Plan

| **Phase**           | **Position**                              | **FTE** | **Timing** |
|---------------------|-------------------------------------------|---------|------------|
| Phase 1 (2026–2027) | Chief Enterprise Architect                | 1.0     | Immediate  |
| Phase 1 (2026–2027) | Domain Architect (Business/Data)          | 1.0     | Month 3    |
| Phase 1 (2026–2027) | Domain Architect (Application/Technology) | 1.0     | Month 6    |
| Phase 2 (2028–2030) | Dedicated Business Architect              | 1.0     | Year 3     |
| Phase 2 (2028–2030) | Dedicated Data Architect                  | 1.0     | Year 3     |
| Phase 2 (2028–2030) | EA Repository / Tools Specialist          | 1.0     | Year 3     |
| Phase 3 (2030–2033) | Additional Domain Architects              | 2.0     | Year 5+    |

**Phase 1 minimum viable team: 3 FTE** (Chief EA + 2 combined Domain Architects). The Chief EA position may initially be filled through ITU/World Bank technical assistance, with knowledge transfer to a Gambian counterpart.

## 4.5 Ministry EA Focal Points

Ministry EA Focal Points are the critical link between the National EA Office and each ministry’s ICT operations. The role is a part-time designation (~25% of time) assigned to an existing senior ICT staff member.

| **Ministry** | **Suggested Designee**             | **Rationale**                               |
|--------------|------------------------------------|---------------------------------------------|
| MoFEA        | IFMIS Team Lead or AGD IT Head     | Deepest technical knowledge of PFM systems  |
| GRA          | Head of IT / Systems Administrator | Knowledge of GamTax Net, ASYCUDA World      |
| MoH          | DHIS2 Focal Point or eHealth Lead  | Familiarity with health information systems |
| MoCDE/GICTA  | Senior Systems Officer             | Proximity to shared platform operations     |

## 4.6 Governance Processes

The EA governance model defines five processes that together ensure disciplined management of the architecture lifecycle.

### 4.6.1 Solution Architecture Compliance Review

Process Owner: Chief Enterprise Architect. The review is triggered by new ICT project initiation (all projects above USD 10,000), major changes to existing systems, solution design completion, system go-live readiness, and scheduled periodic assessments.

| **Outcome**             | **Action**                                                 | **Authority** |
|-------------------------|------------------------------------------------------------|---------------|
| Fully Compliant         | Proceed with implementation                                | Chief EA      |
| Minor Non-Compliance    | Implement with conditions; remediation plan within 90 days | Chief EA      |
| Major Non-Compliance    | Trigger dispensation; implementation paused                | EA Board      |
| Critical Non-Compliance | Block implementation; redesign required                    | EA Board      |

**Security-Specific Compliance:** Every compliance review must include a dedicated security architecture assessment covering data classification, authentication, encryption standards, audit trail requirements, and alignment with national cybersecurity policies.

### 4.6.2 Architecture Change Request Management

The process manages and responds to architecture change requests through: receive and validate RFC, impact assessment across BDAT domains, decision based on impact (minor: Chief EA approves; major: EA Board decides), develop implementation plan, execute changes, and communicate updates.

### 4.6.3 Architecture Dispensation Management

| **Category** | **Duration** | **Authority** | **Examples**                                    |
|--------------|--------------|---------------|-------------------------------------------------|
| Temporary    | ≤ 12 months  | Chief EA      | Legacy system bridge pending replacement        |
| Extended     | 12–36 months | EA Board      | Donor-funded system with incompatible standards |
| Permanent    | Indefinite   | DTSC          | Regulatory requirement conflict                 |

**Dispensation Limit:** No ministry may hold more than three active dispensations simultaneously without DTSC review.

### 4.6.4 EA Framework Maintenance

The Framework is continuously improved through: ongoing stakeholder feedback collection, quarterly lessons learned reviews, quarterly identification of enhancement areas, drafting of updates by Domain Architects, and semi-annual publication of updated framework versions.

### 4.6.5 Investment Review Process

| **Tier**             | **Value Range (USD)** | **Review Level**                                   | **Approval Authority**   |
|----------------------|-----------------------|----------------------------------------------------|--------------------------|
| Tier 4 (Routine)     | \< 10,000             | No formal EA review                                | Ministry ICT Director    |
| Tier 3 (Standard)    | 10,000 – 50,000       | Desk review by EA Office                           | Chief EA                 |
| Tier 2 (Significant) | 50,001 – 250,000      | Full compliance review                             | EA Board                 |
| Tier 1A (Major)      | 250,001 – 1,000,000   | Full review + business case                        | EA Board (DTSC notified) |
| Tier 1B (Strategic)  | \> 1,000,000          | Full review + business case + strategic assessment | DTSC                     |

## 4.7 RACI Matrix for Governance Activities

The RACI matrix defines accountability across all governance activities. Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed.

### 4.7.1 Compliance Review RACI

| **Activity**                       | **Chief EA** | **Domain Architects** | **EA Board** | **Focal Points** |
|------------------------------------|--------------|-----------------------|--------------|------------------|
| Customise architecture checklist   | A            | R                     | —            | C                |
| Conduct compliance check           | A            | R                     | —            | C                |
| Develop compliance report          | A            | R                     | —            | C                |
| Publish results & archive decision | A/R          | I                     | I            | I                |

## 4.8 Decision Escalation and Dispute Resolution

| **Level** | **Body**  | **Target Resolution**  | **Scope**                                             |
|-----------|-----------|------------------------|-------------------------------------------------------|
| Level 1   | EA Office | 5 business days        | Technical disagreements, minor compliance findings    |
| Level 2   | EA Board  | 10 business days       | Major compliance disputes, cross-ministry conflicts   |
| Level 3   | DTSC      | Next quarterly session | Strategic direction disputes, permanent dispensations |

**Security Governance Escalation:** Critical vulnerabilities block implementation immediately. Major security non-compliance triggers emergency EA Board session within 5 business days. Data protection violation risks are notified to PS MoCDE and GICTA DG within 48 hours.

## 4.9 Governance KPIs and Performance Monitoring

| **KPI**                  | **Description**                                             | **Baseline (2026)** | **Target (Year 3)** | **Target (Year 5)** |
|--------------------------|-------------------------------------------------------------|---------------------|---------------------|---------------------|
| EA Service Utilisation   | % of ICT projects above USD 10,000 that undergo EA review   | 0%                  | \> 60%              | \> 80%              |
| Compliance Rate          | % of projects passing compliance review on first submission | N/A                 | \> 50%              | \> 70%              |
| EA-Traced Benefits       | % of project benefits traced to architecture involvement    | 0%                  | \> 30%              | \> 60%              |
| Stakeholder Satisfaction | Ministry feedback rating on EA engagement quality           | N/A                 | \> 3.5/5.0          | \> 4.0/5.0          |
| Review Turnaround        | Average time to complete compliance review                  | —                   | \< 10 days          | \< 5 days           |

# Chapter 5: Enterprise Architecture Metamodel

## 5.1 Metamodel Purpose and Value

The Enterprise Architecture Metamodel defines the set of entities (objects), their attributes, and relationships that allow architectural concepts to be captured, stored, filtered, queried, and represented consistently across The Gambia’s government. It serves as the foundation for the EA Repository (Deliverable 3) and ensures that all architecture artifacts use a common vocabulary and structure.

***Contract Activity 2.3:*** “Define the entity model (objects, attributes, relationships) for the EA repository and agree on tooling for repository management and documentation.”

### 5.1.2 Value Proposition

| **Benefit**       | **Description**                                             | **Gambia Relevance**                                                                          |
|-------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Abstraction**   | Provides an abstraction of a complex organisational system  | Enables the four Tier 1 ministries to describe architectures using a shared model             |
| **Visualisation** | Enables depiction using formalised notation (ArchiMate 3.1) | Allows complex cross-ministry integration patterns to be represented visually                 |
| **Communication** | Provides a common vocabulary for stakeholders               | Ensures ministry focal points, EA Board, and development partners reference the same concepts |

## 5.2 Architecture Domains

The metamodel organises objects across six architecture domains following the BDAT structure extended with Strategy Management and Investment Portfolio domains:

| **Domain**                   | **Key Objects**                                       | **Gambia Examples**                                   |
|------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Strategy Management          | Vision, Goal, Objective, Initiative                   | DEMP 2033 goals and initiatives                       |
| Service Portfolio            | Business Service, Support Service                     | Tax Filing, Birth Registration, Health Reporting      |
| Business Portfolio           | Process, Capability, Organisation, Role, Workflow     | Tax Assessment Process, Revenue Collection Capability |
| Application Portfolio        | Application, App Component, App Function, App Service | GamTax Net, DHIS2, IFMIS, GamPay                      |
| Data (Information) Portfolio | Data Entity, Information Flow, Data Domain            | Taxpayer, Patient, Revenue Reconciliation Flow        |
| Technology Portfolio         | Server, Network, Location, Deployment, Vendor         | GICTA Data Centre, ACE submarine cable                |
| Investment Portfolio         | Project, Demand, Budget, Building Block (ABB/SBB)     | WARDIP EA Project, G-Cloud Deployment                 |

## 5.3 Core Objects Catalogue

The following is an overview of main objects of the EA metamodel:

![A diagram of a software company AI-generated content may be incorrect.](./media/image1.png)

Figure - The Gambia National Enterprise Architecture - Conceptual Metamodel

The complete attribute catalogue defines the data model for the EA Repository (D3). Objects are classified as Required (must be documented) or Optional (documented when available). The following tables present key objects by domain.

### 5.3.1 Strategy Domain Objects

| **Object** | **Required Attributes**                                    | **Key Relationships**                           |
|------------|------------------------------------------------------------|-------------------------------------------------|
| Vision     | ID, Name, Description, Time Horizon, Owner, Status         | Realised by → Goal                              |
| Goal       | ID, Name, Description, Owner                               | Supports → Vision; Achieved through → Objective |
| Objective  | ID, Name, Description, Measure, Target, Target Date, Owner | Supports → Goal; Realised by → Initiative       |
| Initiative | ID, Name, Description, Status, Start/End Date, Owner       | Realises → Objective; Delivered by → Project    |

### 5.3.2–5.3.3 Service and Business Domain Objects

| **Object**        | **Required Attributes**                          | **Key Relationships**                                               |
|-------------------|--------------------------------------------------|---------------------------------------------------------------------|
| Business Service  | ID, Name, Description, Type, Status, Owning Unit | Serves → Customer; Realised by → Process                            |
| Business Process  | ID, Name, Description, Type, Owner, Status       | Realises → Service; Contains → Workflow; Supported by → Application |
| Capability        | ID, Name, Description, Level (1–3)               | Enabled by → Process; Supported by → Application                    |
| Organisation Unit | ID, Name, Description, Type                      | Performs → Process; Owns → Capability                               |
| Role              | ID, Name, Description, Organisation Unit         | Assigned to → Organisation Unit; Performs → Workflow                |
| Customer          | ID, Name, Type, Description                      | Receives → Business Service                                         |
| Workflow          | ID, Name, Description, Parent Process, Owner     | Part of → Business Process                                          |

### 5.3.4 Application Domain Objects

| **Object**                | **Required Attributes**                       | **Key Relationships**                               |
|---------------------------|-----------------------------------------------|-----------------------------------------------------|
| Application               | ID, Name, Description, Type, Status           | Contains → App Component; Supports → Process        |
| Application Component     | ID, Name, Description, Type                   | Part of → Application; Provides → App Function      |
| Application Function      | ID, Name, Description                         | Provided by → App Component; Supports → Workflow    |
| Application Service (API) | ID, Name, Description, Interface Type, Status | Exposed by → App Component; Used by → App Component |

### 5.3.5–5.3.7 Data, Technology, and Investment Domain Objects

| **Object**           | **Required Attributes**                                    | **Key Relationships**                                |
|----------------------|------------------------------------------------------------|------------------------------------------------------|
| Data Entity          | ID, Name, Description, Domain, Type, Owner, Classification | Used by → Process; Managed by → Application          |
| Information Flow     | ID, Name, Source, Target, Frequency                        | From/To → Application/Process; Carries → Data Entity |
| Technology Component | ID, Name, Description, Type, Status                        | Hosts → App Component; Located at → Location         |
| Server               | ID, Name, Type, Status                                     | Hosts → Application Component                        |
| Network              | ID, Name, Type, Status                                     | Connects → Technology Components                     |
| Location             | ID, Name, Type                                             | Contains → Technology Components                     |
| Project              | ID, Name, Description, Status, Start/End, Owner            | Implements → Initiative; Delivers → SBB              |
| ABB                  | ID, Name, Description, Domain, Type                        | Realises → Capability; Implemented by → SBB          |
| SBB                  | ID, Name, Description, ABB Reference, Deployment Status    | Implements → ABB; Deployed as → App Component        |

## 5.4 Cross-Domain Relationships

### 5.4.1 Relationship Types

| **Relationship** | **Description**                     | **Example**                            |
|------------------|-------------------------------------|----------------------------------------|
| Realises         | One element makes another effective | Process realises Service               |
| Supports         | One element assists another         | Application supports Process           |
| Uses             | One element employs another         | Process uses Data Entity               |
| Contains         | Composition relationship            | Application contains App Components    |
| Assigned To      | Allocation of responsibility        | Role assigned to Organisation Unit     |
| Triggers         | One element initiates another       | Demand triggers Project                |
| Flows To         | Movement of data or information     | Information flows between Applications |
| Hosts            | Infrastructure provides runtime     | Server hosts Application Component     |
| Implements       | Concrete realises abstract          | SBB implements ABB                     |

### 5.4.4 Critical Traceability Chains

**Chain 1: Strategy to Execution —** Vision → Goal → Objective → Initiative → Project → Building Block → Deployment

**Chain 2: Service to Technology —** Customer → Business Service → Business Process → Application Component → Technology Component

**Chain 3: Data Lineage —** Data Entity → Data Object → Application Component → Information Flow → Process

**Chain 4: Capability Realisation —** Capability → Business Process → Application Function → Application Component

## 5.5 Architecture Viewpoints

| **ID** | **Viewpoint**         | **Primary Audience**          | **Key Question**                                   |
|--------|-----------------------|-------------------------------|----------------------------------------------------|
| V-01   | Strategic Alignment   | Ministers, DTSC               | How does EA support national priorities?           |
| V-02   | Service Blueprint     | Service Delivery Managers     | How are services delivered end-to-end?             |
| V-03   | Application Portfolio | ICT Directors, EA Board       | What applications exist and what is their health?  |
| V-04   | Integration Landscape | Integration Specialists, NEAO | How do systems connect across ministries?          |
| V-05   | Data Lineage          | Data Stewards, Focal Points   | Where does data originate, flow, and get consumed? |
| V-06   | Infrastructure        | GICTA Operations              | What infrastructure supports government systems?   |
| V-07   | Security              | CISO, Auditors                | What is the security posture?                      |
| V-08   | Investment            | PMO, DTSC, Dev Partners       | How are IT investments managed?                    |

## 5.6 Notation Standard

The Gambia National EA adopts ArchiMate 3.1 as the recommended notation standard for architecture diagrams. ArchiMate is an open, vendor-neutral modelling language maintained by The Open Group.

### 5.6.4 Naming Conventions

| **Object Type**       | **Convention**                   | **Example**                               |
|-----------------------|----------------------------------|-------------------------------------------|
| Business Service      | \<Action\> \<Subject\>           | Process Tax Return, Register Birth        |
| Capability            | \<Verb\> \<Noun\>                | Manage Registration, Collect Revenue      |
| Application           | \<System Name\>                  | GamTax Net, DHIS2, IFMIS                  |
| Application Component | \<Application\> \<Module\>       | GamTax Net Registration Module            |
| Data Entity           | \<Singular Noun\>                | Taxpayer, Patient, Transaction            |
| Business Process      | \<Verb\> \<Object\> Process      | Tax Registration Process                  |
| Information Flow      | \<Source\> → \<Target\> \<Desc\> | GamTax Net → IFMIS Revenue Reconciliation |
| Project               | \<Scope\> \<Action\> Project     | GRA E-Filing Portal Enhancement Project   |

### 5.6.5 ID Convention

All objects use the format: \<DOMAIN_PREFIX\>-\<MINISTRY_CODE\>-\<SEQUENTIAL_NUMBER\>. Domain prefixes include VIS, GOAL, OBJ, INIT, BSVC, CAP, BPRC, APP, ACOMP, AFUN, ASVC, DENT, IFLOW, TCOMP, PRJ, ABB, SBB. Ministry codes: NAT (national), MOFEA, GRA, MOH, MOCDE, GICTA.

## 5.7 Metamodel Implementation Approach

| **Phase**             | **Period** | **Scope**                                                                               | **Tools**                                                    |
|-----------------------|------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Phase 1: Foundation   | 2026–2027  | Core objects: Business Service, Application, Data Entity, Technology Component, Project | Excel/spreadsheet catalogues, draw.io/Visio diagrams         |
| Phase 2: Expansion    | 2028–2029  | All BDAT objects with relationships; Building Blocks; Strategy objects                  | Archi (open source EA tool) with repository                  |
| Phase 3: Optimisation | 2030–2033  | Full metamodel with all attributes; automated traceability; impact analysis             | Archi or commercial EA tool with full repository integration |

The metamodel is a living artifact maintained by the National EA Office. Any changes (new objects, modified attributes, new relationships) require EA Board approval. EA focal points are trained on metamodel usage during capacity building (D11/D12).

# Chapter 6: EA Methodology

## 6.1 GEATDM Overview

### 6.1.1 Introduction

The Gambia National Enterprise Architecture adopts the Government Enterprise Architecture Target Development Method (GEATDM) as its primary methodology for developing, implementing, and sustaining enterprise architecture across government institutions. GEATDM is a practical, replicable methodology that enables public sector organisations to develop their target enterprise architecture by leveraging Reference Architectures as the primary instrument.

GEATDM complements the broader framework alignment described in Chapter 2 (TOGAF, PAERA, GovStack) by providing the specific step-by-step process through which Gambian institutions discover, assess, adapt, plan, and execute their digital transformation journeys.

### 6.1.2 Core Principles

The methodology is founded on five core principles that guide all activities:

| **Principle**              | **Description**                                                                                       | **Gambia Relevance**                                                                                                                         |
|----------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **RA-Centric**             | Reference Architectures are the primary tool; the method supports their discovery and application     | Gambia does not design from scratch — it selects proven patterns appropriate to each institution’s function                                  |
| **DPI-First**              | Organisations integrate with national Digital Public Infrastructure; they do not build DPI themselves | GamPay, Government Interoperability Platform (GIP), and National Identity systems form Gambia’s DPI layer; ministries consume these services |
| **Building Block Reuse**   | Maximise reuse of GovStack Building Block specifications                                              | Gambia prioritises open-source, standards-based components aligned with GovStack BB specifications to reduce cost and accelerate deployment  |
| **BDAT Alignment**         | Architecture spans Business, Data, Application, and Technology domains in that order                  | Each Gambian ministry addresses business capabilities first, then derives data, application, and technology requirements                     |
| **Inheritance Compliance** | Reference Architectures inherit: PDU ⊂ RA ⊂ SDA                                                       | Government-wide coherence is ensured because shared capabilities are defined once at PDU level and inherited by all higher types             |

### 6.1.3 The Five Phases

GEATDM follows a five-phase sequential process. Phases are completed in order, though organisations may revisit earlier phases as they learn more during subsequent phases.

| **Phase** | **Duration** | **Focus**                       |
|-----------|--------------|---------------------------------|
| DISCOVER  | 2–4 weeks    | Classify & Select RA            |
| ASSESS    | 4–8 weeks    | Document AS-IS & Find Gaps      |
| ADAPT     | 4–6 weeks    | Tailor RA to Your Context       |
| PLAN      | 4–6 weeks    | Develop Roadmap & Business Case |
| EXECUTE   | Ongoing      | Implement & Govern              |

| **Phase**    | **Purpose**                                                                                                | **Key Deliverables**                                      | **Key Decision**                                          |
|--------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| **DISCOVER** | Classify organisation, assess DPI readiness, select Reference Architecture                                 | Organisation Profile, DPI Assessment, RA Selection Report | Organisation type (PDU/RA/SDA)                            |
| **ASSESS**   | Document current-state architecture and identify gaps against the selected Reference Architecture          | AS-IS Architecture, Gap Analysis, Readiness Assessment    | Gap priority (Must-have / Should-have / Nice-to-have)     |
| **ADAPT**    | Tailor the Reference Architecture to the organisation’s specific context, creating the target architecture | Target Architecture, Tailoring Decisions, BB Priorities   | Adaptation scope (Minimal / Moderate / Extensive)         |
| **PLAN**     | Transform the target architecture into an actionable implementation roadmap with business case             | Implementation Roadmap, Business Case, Governance Charter | Implementation approach (Big Bang / Phased / Incremental) |
| **EXECUTE**  | Implement projects, govern compliance, and continuously improve the architecture                           | Projects, Compliance Reports, Continuous Improvement      | Project compliance (Compliant / Dispensation Required)    |

### 6.1.4 Decision Points

Seven formal decision points punctuate the methodology, each requiring documented rationale and governance approval:

| **ID** | **Phase** | **Decision**                | **Options**                            |
|--------|-----------|-----------------------------|----------------------------------------|
| DP1    | DISCOVER  | Organisation Classification | PDU / RA / SDA / Hybrid                |
| DP2    | DISCOVER  | DPI Readiness               | Proceed / Address Gaps First           |
| DP3    | ASSESS    | Gap Priority                | Must-have / Should-have / Nice-to-have |
| DP4    | ADAPT     | Adaptation Scope            | Minimal / Moderate / Extensive         |
| DP5    | PLAN      | Implementation Approach     | Big Bang / Phased / Incremental        |
| DP6    | PLAN      | Governance Level            | Light / Standard / Comprehensive       |
| DP7    | EXECUTE   | Project Compliance          | Compliant / Dispensation Required      |

## 6.2 Organisation Classification

### 6.2.1 The Three Organisation Types

GEATDM classifies public sector organisations into three types based on their automation requirements and operational complexity. Classification determines which Reference Architecture applies, what DPI integration level is required, and how long the transformation is expected to take.

| **Characteristic**          | **PDU**              | **RA**               | **SDA**               |
|-----------------------------|----------------------|----------------------|-----------------------|
| **Primary Function**        | Policy & legislation | Sector regulation    | Mass service delivery |
| **Customer Volume**         | Low (consultation)   | Moderate (thousands) | High (millions)       |
| **Transaction Type**        | Documents            | Applications/permits | Filings/payments      |
| **IT Complexity**           | Office automation    | Case management      | Enterprise platforms  |
| **Typical Staff**           | \< 500               | 100–500              | \> 500                |
| **Transformation Timeline** | 9–12 months          | 12–18 months         | 18–36 months          |

### 6.2.2 Classification of Gambian Tier 1 Institutions

Each of the four Tier 1 institutions has been classified using the GEATDM classification questionnaire and decision tree. The classification drives Reference Architecture selection and shapes the scope, timeline, and complexity of each institution’s EA development.

| **Institution**   | **Classification**            | **Rationale**                                                                                                                                                                                                                                                                                                      | **Reference Architecture**                  |
|-------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| **MoCDE / GICTA** | **PDU**                       | Primary function is national ICT policy development, digital strategy coordination, and regulatory oversight. While GICTA has a regulatory mandate (telecommunications licensing), its dominant role is policy formulation and cross-government digital coordination. Low direct transaction volume with citizens. | PDU Reference Architecture (GEATDM-WP2-T25) |
| **MoFEA**         | **PDU** (with PFM extensions) | Primary function is fiscal policy development, budget formulation, and economic planning. The Accountant General’s Directorate (AGD) operates IFMIS with SDA-like transactional characteristics, but MoFEA as a whole is policy-driven.                                                                            | PDU Reference Architecture + PFM Extensions |
| **GRA**           | **SDA**                       | Manages ongoing taxpayer and trader accounts, collects revenue at scale (GamTax Net for domestic tax, ASYCUDA World for customs), conducts risk-based audits, requires real-time transaction processing, processes refunds, and maintains data warehouse for analytics. Meets 6 of 7 SDA criteria.                 | SDA Reference Architecture (GEATDM-WP4-T47) |
| **MoH**           | **SDA**                       | Delivers health services at national scale through 600+ facilities, manages patient records (DHIS2, OpenMRS), operates health insurance scheme (e-NHIS), requires multi-channel service delivery, processes claims and payments, and operates supply chain management systems. Meets 5 of 7 SDA criteria.          | SDA Reference Architecture (GEATDM-WP4-T47) |

### 6.2.3 Classification Implications

The classification results have direct implications for the project approach:

| **Implication**             | **PDU Institutions (MoCDE, MoFEA)**                   | **SDA Institutions (GRA, MoH)**                           |
|-----------------------------|-------------------------------------------------------|-----------------------------------------------------------|
| **DPI Requirement**         | Level 1 (Foundational) acceptable                     | Level 3 (Ready) strongly recommended                      |
| **Architecture Complexity** | 72 capabilities, 20 applications, 25 data sub-domains | 140+ capabilities, 35+ applications, 50+ data sub-domains |
| **Transformation Duration** | 12–18 months per institution                          | 24–36 months per institution                              |
| **Adaptation Scope**        | Minimal to Moderate                                   | Moderate to Extensive                                     |
| **Risk Profile**            | Lower — focused on internal operations                | Higher — external-facing, integration-dependent           |

## 6.3 Phase Descriptions

### 6.3.1 DISCOVER Phase

**Purpose:** Classify the organisation, assess national DPI readiness, and select the appropriate Reference Architecture.

**Duration:** 2–4 weeks per institution

**Key Activities:**

1\. **Organisation Classification** — Apply the 30-question scoring questionnaire or the 4-question decision tree to determine whether the institution is a PDU, RA, or SDA. Validate with stakeholders and document the rationale.

2\. **DPI Readiness Assessment** — Evaluate the availability of national DPI across five pillars (Digital Identity, Interoperability, Data Infrastructure, Digital Access, and Governance), weighted 25%, 25%, 20%, 15%, and 15% respectively.

3\. **Reference Architecture Selection** — Based on the classification result and DPI readiness level, select the implementation approach for the appropriate Reference Architecture (Full, Phased, Basic, or Evolution).

**Gambia Application Notes:** All four Tier 1 classifications have been completed during D5 (As-Is) development and validated during stakeholder sessions. Gambia’s DPI readiness is assessed at approximately Level 1–2 (Foundational to Developing): GamPay exists but is not yet operational for tax payments; Government Interoperability Platform (GIP) is planned but not operational; National Digital Identity is under development.

### 6.3.2 ASSESS Phase

**Purpose:** Document the current-state (AS-IS) architecture and identify gaps against the selected Reference Architecture.

**Duration:** 4–8 weeks per institution

**Key Activities:**

1\. **AS-IS Architecture Documentation** — Document the current state across all four BDAT domains using the Reference Architecture as the assessment framework.

2\. **Gap Analysis** — Compare AS-IS state against the Reference Architecture to identify gaps in capabilities, applications, data management, and technology. Categorise each gap as Must-have, Should-have, or Nice-to-have.

3\. **Readiness Assessment** — Evaluate organisational readiness across dimensions including leadership commitment, technical capacity, change management maturity, and budget availability.

**Gambia Application Notes:** The ASSESS phase has been completed for all four Tier 1 institutions through the D5 deliverable. Key findings include 28 systems across 4 institutions, predominantly donor-funded, with limited integration between ministries. Critical gaps identified include: absence of an operational GIP, limited cross-ministry data sharing, manual processes for inter-agency coordination, and insufficient IT staffing (3–5 technical staff per ministry).

### 6.3.3 ADAPT Phase

**Purpose:** Tailor the Reference Architecture to the institution’s specific context, producing the target (TO-BE) architecture.

**Duration:** 4–6 weeks for PDU; 6–8 weeks for SDA

**Key Activities:**

1\. **Review Gap Analysis** — Examine the prioritised gap register from ASSESS phase.

2\. **Determine Adaptation Scope** — Decide how extensively the RA needs to be tailored: Minimal, Moderate, or Extensive.

3\. **Tailor Across BDAT Domains** — Customise business capabilities, data architecture, application portfolio, and technology platform.

4\. **Specify DPI Integration Points** — Define how the institution will integrate with national DPI services.

5\. **Define Building Block Priorities** — Identify critical GovStack Building Blocks for Phase 1.

6\. **Produce TO-BE Architecture** — Compile the complete target architecture document.

**Gambia Application Notes:** The ADAPT phase is being completed through the D6 deliverable for each Tier 1 institution. For GRA, adaptation is extensive with sector-specific extensions for tax and customs. For MoH, the SDA RA has been adapted for healthcare-specific requirements. For MoFEA and MoCDE, adaptation is moderate.

### 6.3.4 PLAN Phase

**Purpose:** Transform the target architecture into an actionable implementation roadmap with clear phases, milestones, resource requirements, and a compelling business case.

**Duration:** 4–6 weeks

**Key Activities:**

1\. **Define Implementation Approach** — Select the overall strategy: Big Bang, Phased, or Incremental. For Gambia, a Phased approach is mandated given resource constraints.

2\. **Sequence Initiatives** — Order implementation initiatives based on dependency analysis, value-based prioritisation, and risk assessment.

3\. **Define Phases and Milestones** — Structure the transformation into distinct phases with clear objectives and exit criteria.

4\. **Estimate Resources and Timeline** — Develop staffing, skills, and budget requirements by phase.

5\. **Develop Business Case** — Produce cost analysis, benefit analysis, ROI calculations, and risk assessment.

6\. **Create Implementation Roadmap** — Produce the visual multi-year roadmap.

7\. **Obtain Approval** — Submit to EA Board and DTSC for review and funding authorisation.

**Gambia Application Notes:** The PLAN phase is being completed through the D7 deliverable. The Gambian roadmap uses a phased approach across three implementation phases: Phase 1 (Foundation, Months 1–12), Phase 2 (Core Capabilities, Months 13–24), and Phase 3 (Optimisation, Months 25–36+). Investment planning is aligned with WARDIP, bilateral donors, and government recurrent budget allocation.

### 6.3.5 EXECUTE & GOVERN Phase

**Purpose:** Implement the roadmap projects, govern architecture compliance, and continuously improve the architecture based on lessons learned.

**Duration:** Ongoing

**Key Activities:**

1\. **EXECUTE Activities** — Project initiation support, architecture guidance, solution design review, DPI integration support, and implementation monitoring.

2\. **ENGAGE Activities** — Stakeholder communication, training and awareness programmes, architecture consultation services, and change management support.

3\. **GOVERN Activities** — Architecture compliance reviews, dispensation process management, board operations, and portfolio oversight.

4\. **IMPROVE Activities** — Lessons-learned capture, architecture refresh cycles, methodology updates, and maturity advancement tracking.

**Gambia Application Notes:** The EXECUTE phase will be operationalised through the National EA Office (NEAO) within GICTA, as defined in Chapter 7. Given Gambia’s current EA maturity level (2.19), the initial focus will be on establishing basic governance processes, building institutional capacity, and delivering quick-win projects. Dispensation processes are critical — donor-funded projects often arrive with pre-selected technology stacks.

## 6.4 DPI Readiness Assessment for Gambia

### 6.4.1 Five Pillars Assessment

The DPI readiness of The Gambia has been assessed across the five GEATDM pillars:

| **Pillar**              | **Weight** | **Status**   | **Level** | **Key Assessment**                                                                                                             |
|-------------------------|------------|--------------|-----------|--------------------------------------------------------------------------------------------------------------------------------|
| **Digital Identity**    | 25%        | Developing   | Partial   | National ID system under development; biometric enrolment underway but not universal; no national eID for digital transactions |
| **Interoperability**    | 25%        | Foundational | Not Ready | GIP planned but not operational; no national data exchange standard; integration is point-to-point or manual                   |
| **Data Infrastructure** | 20%        | Foundational | Partial   | Limited data governance framework; no national data classification standard; individual systems maintain own standards         |
| **Digital Access**      | 15%        | Developing   | Partial   | ~62% electricity access; single submarine cable (ACE); mobile penetration growing; urban-rural divide significant              |
| **Governance**          | 15%        | Developing   | Partial   | Digital Economy Master Plan (DEMP) 2024–2034 provides direction; GICTA established; Data Protection legislation pending        |

### 6.4.2 Overall DPI Readiness Score

Using GEATDM weighting: Digital Identity: 40% × 25% = 10.0%; Interoperability: 20% × 25% = 5.0%; Data Infrastructure: 35% × 20% = 7.0%; Digital Access: 45% × 15% = 6.75%; Governance: 50% × 15% = 7.5%.

**Overall DPI Score: ~36.25% → Level 1 (Foundational)**

### 6.4.3 Implications by Organisation Type

| **Organisation Type**  | **DPI Level Required**              | **Gap Severity** | **Response**                                                                                                 |
|------------------------|-------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| **PDU** (MoCDE, MoFEA) | Level 1 acceptable                  | Minor            | Proceed with standard PDU RA implementation; DPI gaps are manageable for primarily internal operations       |
| **SDA** (GRA, MoH)     | Level 3 recommended; Level 1 actual | Critical         | Major mitigation required; implement using Phased approach initially, evolving to full SDA RA as DPI matures |

### 6.4.4 Mitigation Strategies

For the SDA institutions (GRA, MoH) operating with Level 1 DPI, the following mitigation strategies apply:

1\. **Interoperability Gap** — Prioritise GIP deployment as a Phase 1 foundation initiative. In the interim, establish bilateral API integrations for the most critical data flows. GamPay’s existing API-based architecture provides a proven integration pattern to replicate.

2\. **Digital Identity Gap** — Use existing institutional identifiers (TIN for GRA, patient IDs for MoH) as interim identity management. Plan for integration with national digital identity system when available.

3\. **Data Infrastructure Gap** — Establish data governance within each institution first. Extend to cross-institutional governance as GIP becomes available.

4\. **Digital Access Gap** — Design services for multiple access channels with graceful degradation. Prioritise mobile-first for citizen-facing services given Gambia’s mobile penetration trajectory.

## 6.5 Reference Architecture Selection and Application

### 6.5.1 RA Selection Matrix for Gambia

| **Institution**   | **Classification** | **DPI Level** | **RA Selection**  | **Approach** |
|-------------------|--------------------|---------------|-------------------|--------------|
| **MoCDE / GICTA** | PDU                | Level 1       | PDU RA (WP2-T25)  | Full         |
| **MoFEA**         | PDU + PFM          | Level 1       | PDU RA + PFM Ext. | Full         |
| **GRA**           | SDA                | Level 1       | SDA RA (WP4-T47)  | Phased       |
| **MoH**           | SDA                | Level 1       | SDA RA (WP4-T47)  | Phased       |

### 6.5.2 Reference Architecture Inheritance

All Gambian target architectures follow the GEATDM inheritance model, ensuring government-wide coherence:

| **Level**   | **RA Type**          | **Capabilities**                       | **Content**                              |
|-------------|----------------------|----------------------------------------|------------------------------------------|
| Base        | **PDU RA** (WP2-T25) | 72 capabilities                        | C1.x Policy + C2.x Support, A0–A5, D1–D5 |
| Extends PDU | **RA RA** (WP3-T35)  | +49 regulatory capabilities            | C3.x Regulatory, A6–A9, D6–D9            |
| Extends RA  | **SDA RA** (WP4-T47) | +Service Delivery & Industrialised Ops | C4.x–C5.x, A10–A15, D10–D14              |

### 6.5.3 Application by Institution

**MoCDE / GICTA (PDU)**

Applies PDU RA in full, covering policy development, stakeholder engagement, knowledge management, and organisational support capabilities. Adds digital coordination extensions for GICTA’s unique role as the national ICT agency. Architecture scope: ~72 capabilities, ~20 applications, ~25 data sub-domains, plus coordination extensions.

**MoFEA (PDU + PFM Extensions)**

Applies PDU RA as the base layer for ministry-wide operations. Extends with PFM-specific capabilities covering budget formulation and execution, treasury operations (AGD), revenue policy, expenditure management, public debt management, aid coordination, procurement oversight, and fiscal reporting. IFMIS is the dominant system integration point. Architecture scope: PDU base (~72 capabilities) + PFM extensions (~30 additional capabilities, ~10 additional applications).

**GRA (SDA)**

Applies full SDA RA with sector-specific adaptations for tax and customs operations. Tax domain: GamTax Net (ITAS) integration, taxpayer account management, risk-based audit selection, returns processing, payment reconciliation, refund management. Customs domain: ASYCUDA World integration, border management, risk-based selectivity, trade facilitation. Unified elements: Single taxpayer view, consolidated reporting, shared risk engine, enterprise data warehouse. Architecture scope: Full SDA RA (~140+ capabilities, ~35+ applications), extensively adapted for dual tax/customs mission.

**MoH (SDA)**

Applies full SDA RA with healthcare-specific adaptations. Health service delivery: DHIS2 integration, facility-based care, community health, referral management, epidemiological surveillance. Health financing: e-NHIS claims processing, provider payment management. Health logistics: pharmaceutical supply chain (mSupply/eLMIS), medical equipment management. Architecture scope: Full SDA RA (~140+ capabilities), adapted for health sector with WHO/GAVI alignment.

## 6.6 Methodology Application in This Project

### 6.6.1 Deliverable Chain to Phase Mapping

| **Deliverable** | **Title**                                    | **GEATDM Phase(s)**            |
|-----------------|----------------------------------------------|--------------------------------|
| D1              | Inception Report                             | Pre-phase (Project Setup)      |
| D2              | EA Framework                                 | DISCOVER (partial)             |
| D3              | EA Repository                                | DISCOVER / ASSESS (supporting) |
| D4              | Architectural Reference Model (ARM)          | DISCOVER                       |
| D5              | Documented Current “As-Is” Architecture      | ASSESS                         |
| D6              | Documented Future State “To-Be” Architecture | ADAPT                          |
| D7              | EA Implementation Roadmap                    | PLAN                           |
| D8              | Review & Approve EA Roadmap                  | PLAN (approval)                |
| D9              | Integration Strategy                         | ADAPT / PLAN                   |
| D10             | Cloud Strategy                               | ADAPT / PLAN                   |
| D11             | Capacity Building Programme                  | EXECUTE (preparation)          |
| D12             | Knowledge Transfer Plan                      | EXECUTE (preparation)          |
| D13             | Governance & Sustainability Framework        | EXECUTE                        |

### 6.6.2 Project Timeline Alignment

The 40-week project timeline maps to GEATDM phases, with multiple phases overlapping due to the compressed timeline and the fact that four institutions are addressed in parallel.

### 6.6.3 Toolkit Application

| **Tool ID** | **Tool Name**                | **Phase** | **Application**                        |
|-------------|------------------------------|-----------|----------------------------------------|
| TK-01       | Classification Questionnaire | DISCOVER  | Applied to all 4 Tier 1 institutions   |
| TK-02       | Classification Decision Tree | DISCOVER  | Rapid validation of TK-01 results      |
| TK-03       | DPI Readiness Checklist      | DISCOVER  | National-level DPI assessment          |
| TK-06       | AS-IS Documentation Template | ASSESS    | Applied across BDAT domains (D5)       |
| TK-07       | Gap Analysis Template        | ASSESS    | Capability gap identification (D5/D7)  |
| TK-12       | Tailoring Guidelines         | ADAPT     | Applied during D6 development          |
| TK-16       | Roadmap Template             | PLAN      | Applied in D7 development              |
| TK-17       | Business Case Template       | PLAN      | Applied in D7 investment justification |
| TK-29       | EA Governance Charter        | EXECUTE   | Incorporated in D2 (Ch 4) and D13      |

### 6.6.4 Cross-Deliverable Consistency

The methodology ensures consistency across deliverables through several mechanisms:

1\. **Shared Metamodel** — All deliverables use the same metamodel (Chapter 5) to describe architecture objects, ensuring consistent terminology and relationships.

2\. **Principles as Constraints** — The 33 EA principles (Chapter 3) serve as binding constraints for all architecture decisions.

3\. **Governance Validation** — Every major deliverable is reviewed through the governance process (Chapter 4).

4\. **Inheritance Verification** — Target architectures (D6) are verified against the RA inheritance model.

5\. **Traceability** — Each initiative in the roadmap (D7) traces back to a gap identified in D5, a target capability in D6, and a principle in D2.

# Chapter 7: Enterprise Architecture Services

## 7.1 National EA Office Establishment Plan

### 7.1.1 Purpose and Mandate

The National EA Office (NEAO) is the operational unit within GICTA responsible for delivering enterprise architecture services to The Gambia’s government ministries, departments, and agencies. The NEAO operationalises the governance framework defined in Chapter 4 and applies the methodology described in Chapter 6 through a defined catalogue of services.

The NEAO’s mandate encompasses three functions: ensuring architectural alignment of government ICT investments with national digital transformation goals; providing expert advisory and compliance services to ministries; and maintaining the national EA repository and standards. The office reports to the Director General of GICTA (Prof. Abdou Karim Jallow) and is accountable to the EA Board for service delivery performance.

### 7.1.2 Placement Within GICTA

The NEAO is established as a dedicated unit within GICTA’s organisational structure, positioned to serve as the government-wide centre of EA expertise. This placement provides three key advantages: institutional continuity beyond project-funded timescales; direct access to GICTA’s mandate over national ICT policy and coordination; and neutrality relative to individual line ministries, enabling cross-government advisory work without perceived bias.

### 7.1.3 Phased Establishment

Given The Gambia’s current EA maturity level (2.19 on a 5.0 scale), limited ICT staffing across government (typically 3–5 per ministry), and dependence on external financing (WARDIP), the NEAO shall be established in three phases aligned with available resources and institutional capacity.

**Phase 1 — Foundation (Year 1: 2026–2027)**

Phase 1 establishes the minimum viable EA function. The focus is on demonstrating value through quick wins while building the institutional foundations for expanded services.

**Staffing:** 3 FTE (Chief Enterprise Architect + 2 combined Domain Architects — one covering Business/Data and one covering Application/Technology), consistent with the governance staffing plan defined in Chapter 4, Section 4.4.3.

**Funding:** WARDIP project budget allocation + GICTA operational budget.

**Key success criteria:** EA governance bodies operational; minimum 3 compliance reviews completed; EA repository populated with As-Is and To-Be architecture artefacts from D5/D6; first Digital Maturity Assessment submitted; initial EA standards catalogue (minimum 5 standards) published.

**Phase 2 — Expansion (Year 2: 2027–2028)**

Phase 2 expands the team and service catalogue to cover the four Tier 1 ministries comprehensively and begins extending to Tier 2 agencies.

**Staffing:** 4–5 positions (Chief EA, 2 Domain Architects, 1 Solutions Architect — may be contracted, 1 EA Administrator).

**Key success criteria:** 11 services operational; all Tier 1 ministries receiving regular EA services; architecture roadmap approved by EA Board; 60% compliance rate achieved.

**Phase 3 — Full Operational Capability (Year 3: 2028–2029)**

Phase 3 brings the NEAO to full operational capacity, delivering the complete service catalogue and demonstrating sustained value that justifies permanent budget allocation.

**Staffing:** 5–6 positions (Chief EA, 2–3 Domain Architects, 1 Solutions Architect, 1 EA Administrator).

**Key success criteria:** Full service catalogue operational with measured KPIs; EA maturity assessment shows measurable improvement; positive stakeholder satisfaction ratings (target: 3.5/5.0 minimum); NEAO included in annual GICTA budget as permanent line item.

## 7.2 Staffing Model

### 7.2.1 Target Organisational Structure

The NEAO target structure comprises the following positions, reporting to the Director General of GICTA:

| **Role**                                  | **Reports To**                                  | **Phase** |
|-------------------------------------------|-------------------------------------------------|-----------|
| Chief Enterprise Architect                | DG-GICTA (admin); EA Board (functional)         | Year 1    |
| Domain Architect (Business & Application) | Chief Enterprise Architect                      | Year 1    |
| Domain Architect (Data & Technology)      | Chief Enterprise Architect                      | Year 1    |
| EA Administrator / Coordinator            | Chief Enterprise Architect                      | Year 2    |
| Solutions Architect (contracted)          | Chief Enterprise Architect                      | Year 2+   |
| Ministry EA Focal Points (4×)             | Ministry IT Director (admin); Chief EA (dotted) | Year 1    |

### 7.2.2 Staffing Budget Estimate

| **Role**                          | **Phase**        | **Annual Cost (USD)** | **Funding Source**        |
|-----------------------------------|------------------|-----------------------|---------------------------|
| Chief Enterprise Architect        | Year 1+          | 45,000–55,000         | WARDIP → GICTA budget     |
| Domain Architect (Business & App) | Year 1+          | 35,000–42,000         | WARDIP → GICTA budget     |
| Domain Architect (Data & Tech)    | Year 1+          | 35,000–42,000         | WARDIP → GICTA budget     |
| EA Administrator                  | Year 2+          | 15,000–20,000         | GICTA budget              |
| Solutions Architect (contracted)  | Year 2+ (ad hoc) | 10,000–15,000/year    | Project-specific          |
| Ministry Focal Points (4×)        | Year 1+          | 0 (existing staff)    | Existing ministry budgets |
| Training & certification          | Annual           | 8,000–12,000          | WARDIP + GICTA            |
| **Total Year 1**                  |                  | **~123,000–151,000**  |                           |
| **Total Year 2**                  |                  | **~148,000–186,000**  |                           |
| **Total Year 3 (steady state)**   |                  | **~148,000–186,000**  |                           |

## 7.3 Service Catalogue

The NEAO delivers 12 services organised into six categories. Each service is documented using a standardised service card format and adapted to The Gambia’s institutional context, capacity constraints, and digital transformation priorities.

### 7.3.1 Service Portfolio Overview

| **Category**                 | **Services**                                                                                 |
|------------------------------|----------------------------------------------------------------------------------------------|
| **Strategic Services**       | EA-SRV-01: IT Strategic Planning Support; EA-SRV-02: Architecture Roadmap Planning           |
| **Project Support Services** | EA-SRV-03: Solution Architecture Review; EA-SRV-04: Procurement Support                      |
| **Advisory Services**        | EA-SRV-05: Technical Architecture Consultation; EA-SRV-06: Domain Architecture Guidance      |
| **Repository Services**      | EA-SRV-07: EA Framework Maintenance; EA-SRV-08: EA Development                               |
| **Governance Services**      | EA-SRV-09: Architecture Compliance & Governance; EA-SRV-10: Change & Dispensation Management |
| **Assessment Services**      | EA-SRV-11: Digital Maturity Assessment; EA-SRV-12: Digital Research & Innovation             |

### 7.3.2 Service Summary Cards

| **Service ID** | **Name**                             | **Category**    | **Trigger**             | **SLA**                  |
|----------------|--------------------------------------|-----------------|-------------------------|--------------------------|
| EA-SRV-01      | IT Strategic Planning Support        | Strategic       | Request-driven          | 2 weeks                  |
| EA-SRV-02      | Architecture Roadmap Planning        | Strategic       | Mandate-driven (annual) | 4 weeks                  |
| EA-SRV-03      | Solution Architecture Review         | Project Support | Mandate/Request-driven  | 1–2 weeks                |
| EA-SRV-04      | Procurement Support                  | Project Support | Request-driven          | 2 weeks                  |
| EA-SRV-05      | Technical Architecture Consultation  | Advisory        | Request-driven          | 1–2 weeks                |
| EA-SRV-06      | Domain Architecture Guidance         | Advisory        | Request-driven          | 1 week                   |
| EA-SRV-07      | EA Framework Maintenance             | Repository      | Mandate-driven (annual) | 4 weeks                  |
| EA-SRV-08      | EA Development                       | Repository      | Mandate/Request-driven  | Continuous               |
| EA-SRV-09      | Architecture Compliance & Governance | Governance      | Mandate-driven          | Continuous               |
| EA-SRV-10      | Change & Dispensation Management     | Governance      | Request-driven          | 1–2 weeks                |
| EA-SRV-11      | Digital Maturity Assessment          | Assessment      | Mandate-driven (annual) | Within assessment period |
| EA-SRV-12      | Digital Research & Innovation        | Assessment      | Mandate/Request-driven  | 4 weeks                  |

## 7.4 Service Delivery Processes

### 7.4.1 Service Request Process

All request-driven services follow a common intake process: (1) Request submission by the requesting ministry; (2) Request triage by the EA Administrator; (3) Scoping by the assigned architect; (4) Execution according to the service-specific process; (5) Delivery and feedback collection; (6) Closure with outputs recorded.

### 7.4.2 Mandate-Driven Service Scheduling

| **Service**                      | **Scheduling**                      | **Calendar Alignment**               |
|----------------------------------|-------------------------------------|--------------------------------------|
| EA-SRV-02: Roadmap Planning      | Annual (Q1)                         | Government budget preparation cycle  |
| EA-SRV-07: Framework Maintenance | Annual (Q4)                         | Full year’s lessons learned          |
| EA-SRV-09: Compliance Governance | Continuous with quarterly reporting | EA Board quarterly                   |
| EA-SRV-11: Maturity Assessment   | Annual (Q2)                         | Results feed into Q3 roadmap review  |
| EA-SRV-12: Research & Innovation | Bi-annual (Q1, Q3)                  | Roadmap planning and mid-year review |

## 7.5 Service Performance Metrics and KPIs

### 7.5.1 Portfolio-Level KPIs

| **KPI**               | **Description**                          | **Year 1** | **Year 2** | **Year 3** |
|-----------------------|------------------------------------------|------------|------------|------------|
| Service utilisation   | % of eligible projects using EA services | 20%        | 50%        | 80%        |
| Customer satisfaction | Average satisfaction rating              | 3.0/5.0    | 3.5/5.0    | 4.0/5.0    |
| SLA compliance        | % services delivered within SLA          | 70%        | 85%        | 90%        |
| Request volume        | Total service requests per quarter       | 5–10       | 15–25      | 30+        |
| EA maturity progress  | National EA maturity score               | 2.3        | 2.5        | 2.7+       |

## 7.6 Phased Service Rollout

### 7.6.1 Rollout Overview

Services are introduced in three phases aligned with the NEAO establishment plan (Section 7.1.3) and institutional readiness.

### 7.6.2 Phase 1 — Foundation (Year 1: 2026–2027)

**Active services (6):** EA-SRV-03 (Solution Review), EA-SRV-05 (Technical Consultation), EA-SRV-06 (Domain Guidance), EA-SRV-07 (Framework Maintenance), EA-SRV-08 (EA Development), EA-SRV-11 (Maturity Assessment — baseline update only).

**Rationale:** Phase 1 prioritises services that demonstrate immediate value (advisory and review services) while building the foundation (repository and framework maintenance). These services require the smallest team and establish the NEAO’s credibility with ministry stakeholders.

### 7.6.3 Phase 2 — Governance (Year 2: 2027–2028)

**Additional services (5):** EA-SRV-01 (IT Strategic Planning), EA-SRV-02 (Roadmap Planning), EA-SRV-04 (Procurement Support), EA-SRV-09 (Compliance & Governance), EA-SRV-10 (Change & Dispensation).

**Active total: 11 services** (6 from Phase 1 + 5 new).

**Rationale:** Phase 2 adds the governance enforcement services (compliance and dispensation management) once the NEAO has established credibility through Phase 1 advisory work. Strategic and procurement services are added as the team grows and has sufficient context from Year 1 operations.

### 7.6.4 Phase 3 — Full Catalogue (Year 3: 2028–2029)

**Service changes (reaching 12 total):** EA-SRV-11 (Maturity Assessment) expands from baseline-only to full-scope assessment across all agencies; EA-SRV-12 (Digital Research & Innovation) is newly activated.

**Active total: 12 services** (all services fully operational).

**Rationale:** The full assessment and innovation services require the most mature EA function and broadest stakeholder relationships. By Year 3, the NEAO has the institutional knowledge, stakeholder trust, and team capacity to conduct comprehensive assessments and meaningful innovation research.

| **Phase**        | **Staff** | **Services** | **Key Changes**                         |
|------------------|-----------|--------------|-----------------------------------------|
| Phase 1 (Year 1) | 3 FTE     | 6 core       | Advisory, review, repository foundation |
| Phase 2 (Year 2) | 4–5 FTE   | 11 expanded  | +5 governance and strategic services    |
| Phase 3 (Year 3) | 5–6 FTE   | 12 complete  | EA-SRV-11 full scope + EA-SRV-12 new    |

# Chapter 8: EA Repository and Tooling

## 8.1 Repository Requirements

### 8.1.1 Purpose

The EA repository is the authoritative store for all architecture artefacts produced and maintained under this framework. It operationalises the metamodel defined in Chapter 5, supports the governance processes defined in Chapter 4, and provides the evidence base for EA services described in Chapter 7. Without a functioning repository, architecture standards cannot be enforced, application landscapes cannot be tracked, and IT investment reviews lack an evidence base.

### 8.1.2 Functional Requirements

**Portfolio lifecycle management**: The repository must track the operational lifecycle of application components and technology components as first-class managed objects, distinct from artefact versioning. Each application and technology component shall carry lifecycle attributes including: current lifecycle state (Planned, In Development, Pilot, Operational, Deprecated, Retired); deployment date; planned retirement date; replacement reference (link to the successor component, if applicable); health assessment rating; and owning institution. The repository must support portfolio views that show component aging, technology currency against defined refresh cycles (per Principle APP-04), and lifecycle transition forecasts. These views shall inform the Architecture Roadmap Planning service (EA-SRV-02) and enable the National EA Office to proactively identify components approaching end-of-life or requiring technology refresh decisions. At minimum, the repository must support filtering and reporting by lifecycle state, by institution, and by architecture domain.

**Implementation tracking and architecture evolution**: The repository must link implementation projects to the target architecture elements they are intended to deliver or modify, enabling traceability from the EA Roadmap (D7) through to actual delivery. For each project-to-architecture linkage, the repository shall record: the compliance review outcome (Compliant, Conditionally Compliant, Non-Compliant) as determined through the Solution Architecture Review service (EA-SRV-03); conditions or dispensations granted; and delivery status (Not Started, In Progress, Delivered, Deferred, Cancelled). The repository must support controlled updates to the target ("To-Be") architecture based on implementation outcomes — recording when delivered solutions refine, extend, or deviate from the originally specified target state, with full change history. The repository must provide dashboard views showing roadmap execution progress: planned versus actual architecture delivery across the portfolio, enabling the EA Board and DTSC to monitor transformation progress. These capabilities operationalise the compliance review process defined in the Gambia National EA (Section 8.5) and the Architecture Compliance & Governance service (EA-SRV-09).

**Content management:** The repository must store and organise the full range of metamodel objects defined in Chapter 5 (31 object types spanning Strategy, Service, Business, Application, Data, and Technology portfolio domains plus the Investment portfolio). Content types include architecture models (ArchiMate diagrams), textual documentation (principles, standards, policies), decision records, assessment artefacts, and reference materials.

**Search and navigation:** Users must be able to locate artefacts by domain, by institution (MoFEA, GRA, MoH, MoCDE/GICTA), by artefact type, and by lifecycle status. Full-text search across all textual content is essential.

**Version control:** All artefacts must maintain version history with timestamps, author attribution, and change descriptions. At minimum, major/minor versioning with the ability to view and restore previous versions.

**Access control:** The repository must enforce role-based access aligned with the governance roles defined in Chapter 4. At minimum, four access tiers: read-only, contributor, reviewer/approver, and administrator.

### 8.1.3 Non-Functional Requirements

**Availability:** Accessible from all Tier 1 ministry locations during business hours. Hosting on GICTA premises initially, migrating to G-Cloud when available (target: Phase 2, 2028–2030).

**Performance:** Page load times under 5 seconds on typical government network connections (1–5 Mbps) for initial user base of 15–25, growing to 50–80 users by 2030.

**Security:** Authentication for all write access, audit logs, encrypted transport (HTTPS), and compliance with the data classification scheme defined in Chapter 3.

**Backup:** Automated daily backups with 30-day point-in-time restore capability on separate physical media.

## 8.2 Tool Selection Rationale

### 8.2.1 Selection Approach

Tool selection follows the “Foundation First, Excellence Later” strategy, prioritising: zero or minimal licence cost; low complexity of installation and maintenance; and proven track record in comparable government contexts.

### 8.2.2 Evaluation Criteria

| **Criterion**              | **Weight** | **Description**                                                        |
|----------------------------|------------|------------------------------------------------------------------------|
| Functionality              | 30%        | Meets required capabilities for EA content storage, search, versioning |
| Cost                       | 20%        | Total cost of ownership over 5 years                                   |
| Integration                | 20%        | Works with existing tools and future tools                             |
| Usability                  | 15%        | Learning curve appropriate for ministry staff                          |
| Vendor/Community Viability | 10%        | Long-term availability of support and updates                          |
| Scalability                | 5%         | Grows from 15–25 to 50–80 users                                        |

### 8.2.3 Recommended Tooling Stack

| **Function**             | **Tool**                | **Role**                         | **Cost**           |
|--------------------------|-------------------------|----------------------------------|--------------------|
| Architecture modelling   | Archi (v5.x)            | Create/maintain ArchiMate models | Free (open-source) |
| Model collaboration      | coArchi plugin + Git    | Shared model access              | Free (open-source) |
| Documentation repository | DokuWiki                | Store non-model artefacts        | Free (open-source) |
| Diagramming              | Draw.io / diagrams.net  | Supplementary diagrams           | Free (open-source) |
| Gap/issue tracking       | Microsoft Excel         | Track gaps, issues, actions      | Existing licence   |
| Collaboration            | Microsoft Teams / email | Communication and review         | Existing licence   |

## 8.3 Repository Structure and Namespace Design

### 8.3.1 DokuWiki Namespace Hierarchy

The repository is organised using a two-dimensional namespace structure: by architecture domain (aligned with the BDAT metamodel in Chapter 5) and by institution.

| **Namespace** | **Content**                                                                    |
|---------------|--------------------------------------------------------------------------------|
| governance/   | Governance artefacts (Ch 4): EA Board, DTSC, compliance, policies              |
| principles/   | EA Principles documentation (Ch 3)                                             |
| standards/    | Architecture standards catalogue: API, data, security, integration, technology |
| architecture/ | Architecture artefacts by domain: business, data, application, technology      |
| institutions/ | Institution-specific content: gicta-mocde, mofea, gra, moh                     |
| methodology/  | GEATDM methodology guidance (Ch 6)                                             |
| services/     | EA Service delivery records: assessments, reviews, advisory                    |
| decisions/    | Architecture Decision Records (ADRs)                                           |
| roadmap/      | Implementation roadmap artefacts (D7)                                          |
| reference/    | Reference materials, international standards                                   |

### 8.3.2 Naming Conventions

**Documents:** [DOMAIN]-[TYPE]-[SUBJECT]-v[MAJOR].[MINOR] (e.g., DATA-STD-classification-v1.0). **Pages:** lowercase with hyphens. **Archi models:** [INSTITUTION]-[SCOPE]-model-v[MAJOR].[MINOR].archimate.

## 8.4 Content Management Processes

All repository content follows a four-stage lifecycle: Create (Draft) → Review (submitted for governance approval) → Publish (Approved, authoritative reference) → Retire (Deprecated, retained for 24 months then archived).

Minor versions (v1.0 → v1.1) require Chief EA approval. Major versions (v1.1 → v2.0) require the same approval level as the original content (typically EA Board for standards and policies).

## 8.5 Access Control and Security

| **Role**      | **Permissions**                              | **Assigned To**                 |
|---------------|----------------------------------------------|---------------------------------|
| Administrator | Full access: create, edit, delete, configure | NEAO technical staff            |
| Approver      | Create, edit, approve/reject, view all       | Chief EA, EA Board Chair        |
| Contributor   | Create, edit own, view all                   | Domain Architects, Focal Points |
| Reviewer      | View all, add comments                       | EA Board, DTSC members          |
| Reader        | View approved content only                   | All government stakeholders     |

## 8.6 Migration Path to Commercial Tools

The tooling strategy follows a deliberate three-phase migration path matching tooling sophistication to organisational maturity:

| **Phase**               | **Period** | **Tooling**                       | **Annual Cost** | **Trigger for Next Phase**                               |
|-------------------------|------------|-----------------------------------|-----------------|----------------------------------------------------------|
| Phase 1: Lightweight    | 2026–2028  | DokuWiki + Archi + Excel          | \$0–500         | 80% artefacts populated; 30 users; 3+ reviews documented |
| Phase 2: Open-Source EA | 2028–2030  | Enhanced Archi + structured wiki  | \$2,000–5,000   | 200+ artefacts; maturity ≥3.0; 50+ users                 |
| Phase 3: Commercial EA  | 2030+      | LeanIX, Ardoq, or equivalent SaaS | \$15,000–40,000 | EA Board approval based on evaluation                    |

# Chapter 9: EA Maturity Roadmap

## 9.1 Current Maturity Assessment

### 9.1.1 Assessment Methodology

The Gambia’s EA maturity baseline was established during the DISCOVER phase using the GEATDM maturity assessment methodology. The assessment evaluates six dimensions of EA practice, each scored on a 1.0 to 5.0 scale.

| **Level** | **Name**   | **Description**                                                       |
|-----------|------------|-----------------------------------------------------------------------|
| 1.0       | Initial    | Ad-hoc, undocumented, inconsistent; EA recognised but not practised   |
| 2.0       | Developing | Architecture activities documented in some areas but not standardised |
| 3.0       | Defined    | Standardised processes, metrics exist; EA governance operational      |
| 4.0       | Managed    | Measured and controlled; EA integrated into decision-making           |
| 5.0       | Optimising | Continuous improvement, data-driven; EA drives strategic innovation   |

### 9.1.2 Baseline Results (2025)

The Gambia’s composite EA maturity score is **2.19 out of 5.0**, placing the country in the upper range of the “Developing” level.

| **Dimension**                        | **Score** | **Key Findings**                                                                           |
|--------------------------------------|-----------|--------------------------------------------------------------------------------------------|
| Governance & Institutional Framework | 1.8       | No formal EA governance bodies; decision rights undefined; no compliance review process    |
| Business Architecture Alignment      | 2.3       | Some documented processes (GRA strongest); no cross-ministry business architecture         |
| Data Management & Standards          | 1.5       | No data governance framework; no classification scheme; inter-ministry exchange manual     |
| Application Portfolio Management     | 2.8       | Application inventory exists for Tier 1; some integration; no formal portfolio governance  |
| Technology Infrastructure            | 2.6       | Mixed: GRA 98% virtualisation; GamPay API maturity Level 4; single cable, no cloud, no SOC |
| Integration & Interoperability       | 2.1       | GIP in early deployment; most exchange manual; no API management standards                 |

**Weighted Composite: 2.19** (Governance 25%, Business 15%, Data 20%, Application 15%, Technology 15%, Integration 10%)

## 9.2 Target Maturity Trajectory

The national target is **EA Maturity Level 4.1 by 2030**, progressing from “EA Initiated” (Developing) to “EA Managed and Measured.” The trajectory is defined in four stages:

| **Stage**         | **Period** | **Target Score** | **Investment** | **Focus**                                              |
|-------------------|------------|------------------|----------------|--------------------------------------------------------|
| 1: Foundation     | 2025–2026  | 2.19 → 2.5       | \$8–12M        | Governance setup, framework, As-Is/To-Be documentation |
| 2: Integration    | 2027–2028  | 2.5 → 3.0        | \$18–25M       | GIP operational, G-Cloud, compliance embedding         |
| 3: Optimisation   | 2029–2031  | 3.0 → 4.1        | \$20–30M       | Event-driven architecture, MDM, advanced analytics     |
| 4: Transformation | 2032–2033  | 4.1 → 4.5+       | \$12–15M       | 70%+ digital services, regional integration, AI        |

## 9.3 Maturity Dimensions and Assessment Criteria

Maturity is assessed across six dimensions with specific criteria at each level, enabling consistent assessment over time and across institutions.

**Governance & Institutional Framework (Weight: 25%)**

| **Level** | **Criteria**                                                                |
|-----------|-----------------------------------------------------------------------------|
| Level 1   | No formal EA governance; ad-hoc decision-making                             |
| Level 3   | EA Board meets regularly; compliance review operational; NEAO fully staffed |
| Level 5   | EA governance proactively shapes strategy; zero non-compliant investments   |

**Business Architecture Alignment (Weight: 15%)**

| **Level** | **Criteria**                                                    |
|-----------|-----------------------------------------------------------------|
| Level 1   | No documented business architecture; processes undocumented     |
| Level 3   | Capability maps for all Tier 1; service catalogue comprehensive |
| Level 5   | Business architecture enables proactive service design          |

**Data Management & Standards (Weight: 20%)**

| **Level** | **Criteria**                                                |
|-----------|-------------------------------------------------------------|
| Level 1   | No data governance; no classification; data quality unknown |
| Level 3   | MDM for 3+ core domains; data quality metrics published     |
| Level 5   | Real-time data quality monitoring; AI/ML in production      |

**Application Portfolio Management (Weight: 15%)**

| **Level** | **Criteria**                                                            |
|-----------|-------------------------------------------------------------------------|
| Level 1   | No application inventory; systems undocumented                          |
| Level 3   | Portfolio managed with lifecycle stages; API-based integration standard |
| Level 5   | Portfolio optimised continuously; modular architecture                  |

**Technology Infrastructure (Weight: 15%)**

| **Level** | **Criteria**                                           |
|-----------|--------------------------------------------------------|
| Level 1   | Fragmented infrastructure; no standards; no cloud      |
| Level 3   | G-Cloud operational; SOC active; 30–50% cloud adoption |
| Level 5   | 80%+ cloud; edge computing; green IT practices         |

**Integration & Interoperability (Weight: 10%)**

| **Level** | **Criteria**                                                       |
|-----------|--------------------------------------------------------------------|
| Level 1   | No integration platform; manual/email data exchange                |
| Level 3   | GIP operational with 30–50 APIs; integration patterns standardised |
| Level 5   | Regional API economy with ECOWAS; 100+ APIs                        |

## 9.4 Year 1–3 Implementation Roadmap

### 9.4.1 Year 1 (2026): Establish Foundations

**Q1–Q2:** DTSC and EA Board established; Chief Enterprise Architect recruited; EA Framework endorsed; DokuWiki repository installed; initial content migration from D1–D7; first 3 architecture standards published.

**Q3–Q4:** First compliance review conducted; EA focal points designated in all Tier 1 ministries; first EA training workshop delivered; draft annual Digital Maturity Assessment prepared.

**Success Criteria:** EA Board met minimum 2 times; repository contains minimum 50 artefacts; at least 1 compliance review; all 4 focal points designated; maturity assessment process tested.

### 9.4.2 Year 2 (2027): Build Operational Capability

**Q1–Q2:** Second Domain Architect recruited; compliance review embedded in procurement; 10 architecture standards published; GIP supporting 10–15 APIs.

**Q3–Q4:** EA Board approving/rejecting proposals in normal governance; first Tier 2 ministry assessed; training extended to 50+ staff.

**Success Criteria:** Maturity assessed at 2.5+; 10 compliance reviews cumulative; 50+ staff trained; EA embedded in Tier 1 procurement.

### 9.4.3 Year 3 (2028): Transition to Integration Stage

**Q1–Q2:** GIP operational with 25–30 APIs; G-Cloud hosting first workloads; second-generation repository evaluated; 20 standards published; 70% compliance rate for Tier 1.

**Q3–Q4:** Real-time GRA–MoFEA revenue integration operational; NEAO at full Phase 2 staffing; EA extended to first Tier 2 ministry; maturity independently verified at 3.0.

**Success Criteria:** Maturity assessed at 3.0; GIP with 25+ APIs; G-Cloud in production; 70% compliance; 150+ staff trained.

## 9.5 Critical Success Factors

**Executive Leadership**

Sustained commitment from the Minister of Communications & Digital Economy and DG-GICTA. EA Board must have genuine decision-making power, not merely advisory status. Embedding EA in legislation or executive regulation provides institutional durability.

**Human Capacity and Retention**

Building and retaining a capable NEAO team is the single greatest implementation risk. Competitive compensation, clear career progression, and professional development are essential. The capacity building programme must be continuous.

**Sustained Funding**

Total investment ~\$58–82M over 8 years. Critical transition occurs in Stage 3 when government budget must absorb operational costs. If allocation does not reach 40% by 2031, the practice will not be sustainable.

**Change Management**

Persistent communication of benefits, quick wins, champion networks within each ministry, and explicit management of parallel manual/digital processes.

**Infrastructure Prerequisites**

ACE cable redundancy, electricity improvements, G-Cloud deployment, and broadband to all government offices. Delays constrain achievable maturity.

## 9.6 Risk Register

| **ID** | **Risk Description**                        | **Impact** | **Prob.** | **Mitigation**                                                    |
|--------|---------------------------------------------|------------|-----------|-------------------------------------------------------------------|
| R-01   | Political transition disrupts EA governance | High       | Med       | Embed in legislation; bipartisan endorsement of DEMP 2033         |
| R-02   | EA Board lacks decision authority           | High       | High      | Explicit mandate linking compliance to procurement approval       |
| R-03   | Donor dependency extends beyond transition  | High       | Med       | Begin budget planning Year 2; cost-recovery mechanisms            |
| R-04   | Key staff turnover in NEAO                  | High       | High      | Competitive compensation; succession planning; knowledge transfer |
| R-05   | Ministry focal points not empowered         | Med        | High      | Formal designation; 20% time allocation; training programme       |
| R-06   | Insufficient training pipeline              | Med        | Med       | Multi-channel delivery; train-the-trainer; UTG partnership        |
| R-07   | Submarine cable failure                     | High       | Low       | On-premises Phase 1; offline capability; satellite backup         |
| R-08   | G-Cloud deployment delayed                  | Med        | Med       | Maintain on-premises fallback; deployment-agnostic Phase 2 tools  |
| R-09   | Electricity constrains regional adoption    | Med        | High      | Prioritise urban locations; offline tools; solar backup           |
| R-10   | Ministry resistance to compliance           | Med        | High      | Demonstrate value through quick wins; streamline reviews          |
| R-11   | Stakeholder fatigue from donor initiatives  | Med        | Med       | Align with ministry priorities; minimise meeting burden           |
| R-12   | Tooling adoption resistance                 | Low        | Med       | User training; make repository easier than alternatives           |

# Appendix A: Glossary

This glossary provides definitions for key terms used throughout the Gambia National Enterprise Architecture Framework.

| **Term**          | **Definition**                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ABB               | Architecture Building Block — A reusable architecture component that defines a required capability at a technology-agnostic level.                                                                                                                                                                                                                                 |
| ACE               | Africa Coast to Europe — The submarine telecommunications cable providing The Gambia’s primary international internet connectivity.                                                                                                                                                                                                                                |
| API               | Application Programming Interface — A defined set of protocols enabling software applications to communicate and exchange data.                                                                                                                                                                                                                                    |
| ArchiMate 3.1     | An open, vendor-neutral modelling language maintained by The Open Group for enterprise architecture.                                                                                                                                                                                                                                                               |
| ASYCUDA World     | Automated System for Customs Data — UNCTAD-provided customs management system used by GRA.                                                                                                                                                                                                                                                                         |
| BDAT              | Business, Data, Application, Technology — the four core architecture domains.                                                                                                                                                                                                                                                                                      |
| DEMP              | Digital Economy Master Plan 2024–2034 — The Gambia’s national strategy guiding digital transformation, with primary targets anchored to 2033.                                                                                                                                                                                                                      |
| DHIS2             | District Health Information Software 2 — Open-source health management information platform used by MoH.                                                                                                                                                                                                                                                           |
| DPI               | Digital Public Infrastructure — Shared digital systems enabling government service delivery at population scale.                                                                                                                                                                                                                                                   |
| DTSC              | Digital Transformation Steering Committee — The apex governance body for digital transformation.                                                                                                                                                                                                                                                                   |
| EA Board          | Enterprise Architecture Board — Technical governance body for architecture compliance and standards.                                                                                                                                                                                                                                                               |
| GEATDM            | Government Enterprise Architecture Target Development Method — Five-phase methodology (DISCOVER, ASSESS, ADAPT, PLAN, EXECUTE).                                                                                                                                                                                                                                    |
| GICTA             | Gambia Information and Communication Technology Agency — Statutory ICT implementing agency; institutional home of NEAO.                                                                                                                                                                                                                                            |
| GIP               | Government Interoperability Platform — Planned secure data exchange platform based on X-Road pattern.                                                                                                                                                                                                                                                              |
| GamPay            | The Gambia’s national government payment gateway enabling electronic payments across multiple channels.                                                                                                                                                                                                                                                            |
| GamTax Net (ITAS) | Integrated Tax Administration System operated by GRA for domestic tax administration.                                                                                                                                                                                                                                                                              |
| IFMIS             | Integrated Financial Management Information System — Core PFM system (Epicor 10) for ~41,958 civil servants.                                                                                                                                                                                                                                                       |
| MoCDE             | Ministry of Communications and Digital Economy — Statutory mandate for ICT policy and digital economy.                                                                                                                                                                                                                                                             |
| MoFEA             | Ministry of Finance and Economic Affairs — Responsible for fiscal policy and IFMIS operations.                                                                                                                                                                                                                                                                     |
| MoH               | Ministry of Health — Responsible for health policy and health information systems.                                                                                                                                                                                                                                                                                 |
| NEAO              | National EA Office — Operational unit within GICTA for day-to-day EA governance.                                                                                                                                                                                                                                                                                   |
| PAERA             | Public Administration Ecosystem Reference Architecture — Framework defining reference architectures for PDU, RA, SDA types.                                                                                                                                                                                                                                        |
| PDU               | Policy Development Unit — PAERA classification for policy-focused entities. MoCDE and MoFEA classified as PDU.                                                                                                                                                                                                                                                     |
| RA                | Revenue Authority — A PAERA organisational classification for entities focused narrowly on revenue collection patterns. Despite GRA’s name, GRA was classified as SDA because its operational scope — including customs administration, taxpayer services, and trade facilitation — aligns more closely with direct service delivery (see Chapter 6, Section 6.2). |
| SDA               | Service Delivery Agency — PAERA classification for direct service delivery entities. GRA and MoH classified as SDA.                                                                                                                                                                                                                                                |
| TOGAF             | The Open Group Architecture Framework — Version 9.2 referenced in this framework.                                                                                                                                                                                                                                                                                  |
| WARDIP            | Western Africa Regional Digital Integration Project — World Bank programme funding this EA initiative (Contract WARDIP/C4.13.2/2024/DC009).                                                                                                                                                                                                                        |
| X-Road            | Open-source data exchange platform (Estonian origin) providing the pattern for The Gambia’s GIP.                                                                                                                                                                                                                                                                   |

Note: The complete glossary of 78 terms is maintained in the EA repository. This appendix presents the essential terms for document readability.

# Appendix B: Full Principles Catalogue

This appendix provides the extended reference for all 33 EA principles across five categories, including compliance examples and related principles for each. The full principles are maintained in the EA repository; this section presents the principle structure and representative examples.

## B.1 Business Architecture Principles (7 Principles)

| **ID** | **Principle**                           | **Summary**                                                                                                                 |
|--------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| BA-01  | Customer-Centric Service Design         | Digital services are redesigned experiences that citizens adopt, not functional replicas of paper forms.                    |
| BA-02  | Process Standardisation and Automation  | Standardisation as a prerequisite to automation; automation of inconsistent processes produces inconsistent results faster. |
| BA-03  | Capability-Based Planning               | A stable capability framework that transcends project boundaries, enabling holistic assessment of government investments.   |
| BA-04  | Service Orientation                     | Single shared services (like GamPay) consumed by multiple agencies rather than each building its own.                       |
| BA-05  | Regulatory Compliance by Design         | Compliance designed in at 5–10% cost versus retrofitting at 30–50% of system value.                                         |
| BA-06  | Channel Choice and Consistency          | Same service logic delivered through channel appropriate to each citizen’s circumstances.                                   |
| BA-07  | Natural Digital Environment Integration | Government services meet businesses where they already work (APIs to accounting software, etc.).                            |

## B.2 Data Architecture Principles (7 Principles)

| **ID** | **Principle**                         | **Summary**                                                                         |
|--------|---------------------------------------|-------------------------------------------------------------------------------------|
| DA-01  | Data as a Strategic Asset             | Government data provides foundation for evidence-based policy making.               |
| DA-02  | Once-Only Data Collection             | Citizens provide information once; subsequent uses draw from authoritative sources. |
| DA-03  | Single Source of Truth                | One designated authoritative source per data entity.                                |
| DA-04  | Data Quality Management               | Quality enforced at point of entry with validation rules.                           |
| DA-05  | Privacy and Data Protection by Design | Role-based access, audit logging, encryption for all personal data.                 |
| DA-06  | Data Sharing and Interoperability     | Formal agreements and standard APIs for inter-ministry data exchange.               |
| DA-07  | Analytics-Ready Data                  | Data models include temporal dimensions enabling trend analysis.                    |

## B.3 Application Architecture Principles (7 Principles)

| **ID** | **Principle**                       | **Summary**                                                                |
|--------|-------------------------------------|----------------------------------------------------------------------------|
| APP-01 | Building Block Orientation          | Assess GovStack BB specs before proprietary options.                       |
| APP-02 | Loose Coupling and High Cohesion    | Systems interact through APIs, enabling independent updates.               |
| APP-03 | Integration Through National DPI    | Route through GIP; design interim integrations for GIP migration.          |
| APP-04 | No Legacy by Design                 | Include maintenance contract, refresh cycle, exit strategy from inception. |
| APP-05 | API-First Design                    | All systems expose documented, versioned APIs.                             |
| APP-06 | Cloud-Ready and Platform-Neutral    | Containerised deployment enabling G-Cloud migration.                       |
| APP-07 | Modularity and Incremental Delivery | Deliver visible benefit at each stage, not only at project end.            |

## B.4 Technology Architecture Principles (7 Principles)

| **ID**  | **Principle**                             | **Summary**                                                                      |
|---------|-------------------------------------------|----------------------------------------------------------------------------------|
| TECH-01 | Security by Design (Contract-Prioritised) | Threat modelling, OAuth 2.0, TLS 1.3, rate limiting for all APIs.                |
| TECH-02 | Resilience and Business Continuity        | Backup, UPS, generator, tested disaster recovery plans.                          |
| TECH-03 | Scalability and Performance               | Load testing before deployment; capacity planning.                               |
| TECH-04 | Standardisation and Simplification        | Approved technology standards register; EA Board dispensation for new platforms. |
| TECH-05 | Infrastructure as Code                    | Environments provisioned from version-controlled scripts.                        |
| TECH-06 | Observability and Monitoring              | Centralised logging, metrics, automated alerting.                                |
| TECH-07 | Sustainable and Responsible Technology    | Energy efficiency evaluated alongside functional requirements.                   |

## B.5 Cross-Cutting Principles (5 Principles)

| **ID** | **Principle**                                 | **Summary**                                                                                    |
|--------|-----------------------------------------------|------------------------------------------------------------------------------------------------|
| CC-01  | Whole-of-Government Alignment                 | GIP integration design from inception even for single-ministry projects.                       |
| CC-02  | Digital by Default, Inclusive by Design       | WCAG 2.1 AA, multilingual, mobile-optimised, low-bandwidth resilient.                          |
| CC-03  | Continuous Improvement and Innovation         | Annual technology radar reviews; pilot before scale.                                           |
| CC-04  | Transparency and Accountability               | All decisions documented in ADRs and published in repository.                                  |
| CC-05  | Value for Money and Sustainability (Critical) | 8-year TCO analysis; sustainability test: can Gambia maintain this after donor programme ends? |

Each principle in the repository includes: extended rationale, detailed implications, compliance examples (compliant, non-compliant, partially compliant), and related principles cross-references.

# Appendix C: Governance Body Terms of Reference

## C.1 Digital Transformation Steering Committee (DTSC)

**Purpose:** Provides strategic direction and executive sponsorship for The Gambia’s national digital transformation programme.

### Membership

| **Role**                   | **Institution**                            | **Type**              |
|----------------------------|--------------------------------------------|-----------------------|
| Chairman                   | Cabinet Secretary, Office of the President | Permanent             |
| Vice Chairman              | Permanent Secretary, MoCDE                 | Permanent             |
| Member                     | Permanent Secretary, MoFEA                 | Permanent             |
| Member                     | Commissioner General, GRA                  | Permanent             |
| Member                     | Permanent Secretary, MoH                   | Permanent             |
| Member & Technical Adviser | Director General, GICTA                    | Permanent             |
| Observer                   | WARDIP / World Bank Representative         | During project period |
| Secretary (non-voting)     | Chief Enterprise Architect                 | Permanent             |

**Meeting Cadence:** Quarterly regular sessions; extraordinary sessions as needed; annual strategy session in Q1.

**Decision Rights:** Final authority on strategic architecture directions; escalation authority; mandate compliance across all MDAs; approve Tier 1B investments (\>USD 1,000,000).

## C.2 Enterprise Architecture Board (EA Board)

**Purpose:** Primary technical governance body for architecture compliance and standards.

### Membership

| **Role**      | **Institution**                               |
|---------------|-----------------------------------------------|
| Chairman      | Permanent Secretary, MoCDE                    |
| Vice Chairman | Director General, GICTA                       |
| Secretary     | Chief Enterprise Architect                    |
| Members       | ICT Directors of MoFEA, GRA, MoH, MoCDE/GICTA |
| Member        | Cybersecurity Focal Point, GICTA              |

**Meeting Cadence:** Monthly regular sessions; working sessions as needed; quarterly review preceding DTSC.

**Decision Rights:** Approve architecture principles, standards, and technology selections; grant/deny dispensations; approve IT investments USD 50,000–1,000,000; recommend larger investments to DTSC.

## C.3 National Enterprise Architecture Office (NEAO)

**Purpose:** Operational arm of EA governance within GICTA, responsible for day-to-day activities.

**KPIs:** \>60% projects undergoing EA review (Phase 1); \<10 business days review turnaround; \>80% repository completeness for Tier 1 systems; 100% focal point training completion.

## C.4 Ministry EA Focal Points

**Purpose:** Critical link between NEAO and each ministry’s ICT operations in the federated governance model. Part-time designation (~25% of working time). Formally appointed by Permanent Secretary.

| **Ministry** | **Suggested Designee**             | **Rationale**                        |
|--------------|------------------------------------|--------------------------------------|
| MoFEA        | IFMIS Team Lead or AGD IT Head     | Deepest PFM systems knowledge        |
| GRA          | Head of IT / Systems Administrator | GamTax Net, ASYCUDA World knowledge  |
| MoH          | DHIS2 Focal Point or eHealth Lead  | Health information systems expertise |
| MoCDE/GICTA  | Senior Systems Officer             | Shared platform operations           |

# Appendix D: Metamodel Object Catalogue

## D.1 Object Summary

| **Domain**            | **Object Count** | **Req. Attributes (avg.)** | **Opt. Attributes (avg.)** |
|-----------------------|------------------|----------------------------|----------------------------|
| Strategy Management   | 4                | 5.5                        | 1.5                        |
| Service Portfolio     | 2                | 5.0                        | 1.5                        |
| Business Portfolio    | 7                | 5.3                        | 1.7                        |
| Application Portfolio | 4                | 5.0                        | 2.5                        |
| Data Portfolio        | 3                | 5.7                        | 1.0                        |
| Technology Portfolio  | 7                | 4.6                        | 2.0                        |
| Investment Portfolio  | 2                | 6.0                        | 1.0                        |
| Building Blocks       | 2                | 5.5                        | 1.5                        |
| **Total**             | **31**           | —                          | —                          |

## D.2 Validation Rules

| **Rule** | **Description**                                                                        |
|----------|----------------------------------------------------------------------------------------|
| VR-01    | Every Application must be linked to at least one Organisation Unit (owner)             |
| VR-02    | Every Business Service must be linked to at least one Business Process                 |
| VR-03    | Every Data Entity must have a designated owner                                         |
| VR-04    | Every Data Entity must have a Classification (Public/Internal/Confidential/Restricted) |
| VR-05    | Every Information Flow must have both Source and Target defined                        |
| VR-06    | Every Project must link to at least one Initiative or Demand                           |
| VR-07    | Every SBB must reference an ABB it implements                                          |
| VR-08    | ID format must follow convention: PREFIX-MINISTRY-NNN                                  |
| VR-09    | Status field must use controlled vocabulary                                            |
| VR-10    | Names must follow naming conventions (Section 5.6.4)                                   |

## D.3 Gambia-Specific Extensions

| **Extension** | **Object**           | **New Attribute**                | **Rationale**                                                   |
|---------------|----------------------|----------------------------------|-----------------------------------------------------------------|
| EXT-01        | Application          | Donor Funding Source             | Track donor-funded applications for sustainability planning     |
| EXT-02        | Application          | Post-Project Sustainability Plan | Document whether recurrent costs are budgeted                   |
| EXT-03        | Technology Component | Power Backup Status              | Track UPS/generator given 62% electricity access                |
| EXT-04        | Location             | Connectivity Type                | Document connection quality for infrastructure planning         |
| EXT-05        | Data Entity          | DPA Applicability                | Flag entities with personal data subject to Data Protection Act |
| EXT-06        | Project              | WARDIP Component Reference       | Map to WARDIP programme components for donor reporting          |

# Appendix E: EA Tool Evaluation Matrix

| **Criterion (Weight)**   | **DokuWiki**           | **Archi**          | **Essential EA**   | **Sparx EA**        |
|--------------------------|------------------------|--------------------|--------------------|---------------------|
| Cost — 5yr TCO (20%)     | 5 — Free               | 5 — Free           | 2 — ~\$75K/5yr     | 2 — ~\$40K/5yr      |
| Open Source (10%)        | 5 — GPL                | 5 — MIT            | 1 — Proprietary    | 1 — Proprietary     |
| Learning Curve (15%)     | 4 — Wiki markup        | 3 — ArchiMate reqd | 3 — Web-based      | 2 — Complex         |
| ArchiMate 3.1 (15%)      | 1 — No native          | 5 — Full native    | 4 — Good           | 5 — Full            |
| Collaboration (10%)      | 4 — Multi-user wiki    | 3 — Git-based      | 5 — Real-time      | 3 — Cloud edition   |
| Maintenance (10%)        | 5 — Flat-file, minimal | 4 — Desktop        | 2 — Vendor-managed | 3 — Server required |
| Offline Capability (10%) | 3 — LAN possible       | 5 — Fully offline  | 1 — Cloud only     | 4 — Desktop offline |
| Scalability (5%)         | 4                      | 4                  | 5                  | 4                   |
| Integration (5%)         | 4                      | 4                  | 4                  | 4                   |
| **Weighted Score**       | **3.85**               | **4.10**           | **2.65**           | **2.80**            |

**Recommendation:** DokuWiki + Archi combination (highest combined score at zero licence cost) for Phase 1–2, with commercial platform evaluation at Phase 3 when maturity reaches 3.0+.

# Appendix F: References

## F.1 International Frameworks and Standards

| **Ref.** | **Document**                                                   | **Publisher**       | **Year** |
|----------|----------------------------------------------------------------|---------------------|----------|
| [1]    | TOGAF Standard, Version 9.2                                    | The Open Group      | 2018     |
| [2]    | ArchiMate 3.1 Specification                                    | The Open Group      | 2019     |
| [3]    | PAERA — Public Administration Ecosystem Reference Architecture | GovStack / ITU      | 2025     |
| [4]    | GovStack Building Block Specifications                         | GovStack Initiative | 2024     |
| [5]    | ISO/IEC/IEEE 42010:2022 — Architecture Description             | ISO                 | 2022     |
| [6]    | ISO/IEC 27001 — Information Security Management                | ISO                 | 2022     |
| [7]    | ISO 38500 — Governance of IT                                   | ISO                 | 2015     |
| [8]    | WCAG 2.1 — Web Content Accessibility Guidelines                | W3C                 | 2018     |
| [9]    | COBIT 2019                                                     | ISACA               | 2019     |
| [10]   | ITIL 4 — IT Service Management                                 | Axelos / PeopleCert | 2019     |

## F.2 GEATDM Document Suite

| **Ref.** | **Document ID**    | **Title**                             |
|----------|--------------------|---------------------------------------|
| [11]   | GEATDM-WP1-T11     | EA Metamodel                          |
| [12]   | GEATDM-WP1-T12     | EA Principles                         |
| [13]   | GEATDM-WP1-T13     | EA Governance                         |
| [14]   | GEATDM-WP1-T14     | EA Services                           |
| [15]   | GEATDM-WP2-T25     | PDU Reference Architecture (Complete) |
| [16]   | GEATDM-WP3-T35     | RA Reference Architecture (Complete)  |
| [17]   | GEATDM-WP4-T47     | SDA Reference Architecture (Complete) |
| [18]   | GEATDM-WP5-T58     | Application Method Guide (Complete)   |
| [19]   | GEATDM-WP6-T61     | Toolkit                               |
| [20]   | GEATDM-WP6-T62     | Main Document (Reference Guide)       |
| [21]   | GEATDM Users Guide | v1.0                                  |

## F.3 Gambia National Strategies and Project Documents

| **Ref.** | **Document**                                                           |
|----------|------------------------------------------------------------------------|
| [22]   | Digital Economy Master Plan (DEMP) 2024–2034, Government of The Gambia |
| [23]   | National Development Plan (NDP), Government of The Gambia              |
| [24]   | ICT Act 2009, Government of The Gambia                                 |
| [25]   | Data Protection Act (Pending)                                          |
| [26]   | Cyber Security Act (Pending)                                           |
| [27]   | Public Financial Management (PFM) Act                                  |
| [28]   | Contract WARDIP/C4.13.2/2024/DC009 (signed 2 May 2025)                 |
| [29]   | D1 — Inception Report                                                  |
| [30]   | D2 — Enterprise Architecture Framework (this document)                 |
| [31]   | Digital Transformation Continuum for The Gambia                        |

## F.4 International Best Practice and Tools

| **Ref.** | **Source**                                                                  |
|----------|-----------------------------------------------------------------------------|
| [33]   | Estonia e-Government architecture (X-Road / Information Mediator reference) |
| [34]   | Rwanda Irembo platform (comparable developing country implementation)       |
| [35]   | Kenya Huduma / M-Pesa ecosystem (mobile-first payment and digital identity) |
| [36]   | OECD Tax Administration 3.0 (digital tax administration standards)          |
| [37]   | IMF Government Finance Statistics Manual 2014                               |
| [38]   | WCO Data Model (customs data standards)                                     |
| [39]   | WHO Digital Health Strategy                                                 |
| [40]   | ECOWAS Regional Trade Protocols                                             |
| [41]   | Archi — Open Source ArchiMate Modelling (archimatetool.com)                 |
| [42]   | DokuWiki (dokuwiki.org)                                                     |
| [43]   | Draw.io / diagrams.net                                                      |
| [44]   | coArchi — Archi Collaboration Plugin                                        |
