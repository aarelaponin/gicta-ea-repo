# D5: Documented Current "As-Is" Architecture

**Prepared for:** Ministry of Communications & Digital Economy (MoCDE);
ITU Contract\
**Assessment Period:** 2025\
**Framework:** TOGAF ADM & PAERA\
**Assessment Scope:** Tier 1 Ministries + Cross-Cutting DPI Initiatives\
**Assessment Organizations:** Ministry of Finance & Economic Affairs
(MoFEA), Gambia Revenue Authority (GRA), Ministry of Health (MoH),
Ministry of Communications & Digital Economy (MoCDE)

---

## DOCUMENT CONTROL

| Version | Date           | Author              | Status           |
|---------|----------------|---------------------|------------------|
| 1.0     | November 2025  | ITU Consultant Team | Draft for Review |

---

## EXECUTIVE SUMMARY

This document provides an assessment of The Gambia's current government
Enterprise Architecture across four Tier 1 ministries and major
cross-cutting Digital Public Infrastructure (DPI) initiatives.

The assessment reveals a government in active digital transformation
with significant investments ($119.5 in the health sector alone, $50M
in regional digital integration), yet facing critical challenges in
interoperability, system fragmentation, and capacity gaps.

**Key Findings:**

- **About 41,958 civil servants** are managed through the integrated
  IFMIS-Payroll system
- **Multiple parallel systems** with limited interoperability create
  data silos
- **Successful integration examples**: GamPay (payment gateway), eCRVS
  (civil registration)
- **1.17M people registered** in the digital birth certificate system
  since 2022
- **EA Maturity Level: 2.19** (Defined but not consistently applied)
- **Fragmented identity systems** with no unified National ID
  integration
- **Limited real-time integration** across government (GamPay is the
  exception)
- **Active development** of the MyGov citizen portal with a Bangladesh
  partnership
- **Critical infrastructure gaps**: Single submarine cable, limited
  data center capacity, inconsistent connectivity

**Strategic Context:**

The Gambia has set an ambitious vision to become "the most advanced
digital society and IT innovation hub in Africa" by 2034, supported by
comprehensive policy frameworks including the Digital Economy Master
Plan 2024-2034, multiple sector-specific strategies, and significant
World Bank/IDA funding.

However, current state analysis reveals that achieving this vision
requires addressing fundamental architectural challenges around
integration, standardisation, capacity building, and sustainable
governance.

---

## TABLE OF CONTENTS

- [DOCUMENT CONTROL](#document-control)
- [EXECUTIVE SUMMARY](#executive-summary)
- [1. METHODOLOGY & CONTEXT](#1-methodology--context)
- [2. BUSINESS ARCHITECTURE](#2-business-architecture)
- [3. APPLICATION ARCHITECTURE](#3-application-architecture)
- [4. DATA ARCHITECTURE](#4-data-architecture)
- [5. INTEGRATION ARCHITECTURE](#5-integration-architecture)
- [6. TECHNOLOGY ARCHITECTURE](#6-technology-architecture)
- [7. CROSS-CUTTING DPI INITIATIVES](#7-cross-cutting-dpi-initiatives)
- [8. SECURITY ARCHITECTURE](#8-security-architecture)
- [9. GAP ANALYSIS SUMMARY](#9-gap-analysis-summary)
- [APPENDICES](#appendices)

---

## 1. METHODOLOGY & CONTEXT

### 1.1 Assessment Approach

The current state architecture assessment was conducted using a
multi-method approach:

- **Document Review**: Analysis of 50+ policy documents, project
  reports, and technical specifications
- **Stakeholder Interviews**: Engagement with ministry focal points,
  ICT staff, project managers
- **System Surveys**: Technical questionnaires completed by 4 Tier 1
  ministries
- **Field Observations**: Site visits to key government facilities and
  data centres
- **Public Source Analysis**: Review of publicly available information
  on DPI initiatives

### 1.2 Assessment Framework

The assessment follows TOGAF ADM and PAERA frameworks, structured across
five architecture domains:

1. **Business Architecture**: Organisational structures, processes,
   governance
2. **Application Architecture**: Systems, applications, technology
   stacks
3. **Data Architecture**: Data sources, management, quality, governance
4. **Integration Architecture**: System interconnections, data flows,
   APIs
5. **Technology Architecture**: Infrastructure, networks, hosting,
   security

### 1.3 Tier 1 Ministries Assessed

| Ministry | Abbreviation | Primary Functions | Digital Maturity |
|----------|-------------|-------------------|-----------------|
| Ministry of Finance & Economic Affairs | MoFEA | Budget, treasury, financial management, IFMIS | High (Mature systems) |
| Gambia Revenue Authority | GRA | Tax collection, customs, revenue management | High (API integration) |
| Ministry of Health | MoH | Health service delivery, public health, NHIS | Medium (Active digital transformation) |
| Ministry of Communications & Digital Economy | MoCDE | ICT policy, digital infrastructure, e-government | Medium (Leading transformation) |

### 1.4 Strategic Context

The Gambia's enterprise architecture development occurs within a
comprehensive strategic framework encompassing regional digital
integration initiatives, national development priorities, and
substantial international funding commitments. This context is critical
for understanding the current state architecture and informing future
roadmap development.

**National Vision and Strategic Goals**

The Gambia has articulated an ambitious national vision to become "the
most advanced digital society and IT innovation hub in Africa" by 2034.
This vision is operationalized through the Digital Economy Master Plan
2024-2034, which identifies ten strategic pillars for digital
transformation:

- Digital government services and e-government platforms
- Digital infrastructure and connectivity
- Digital identity and civil registration systems
- Digital financial services and payment systems
- Cybersecurity and data protection
- Digital skills and capacity building
- Digital entrepreneurship ecosystem
- Open data and transparency initiatives
- Digital health systems
- Smart cities and digital addressing

**Service Digitization Targets**

The Master Plan establishes aggressive digitization targets, with
current government service digitization estimated at 10% and a target of
70% by 2034. This transformation requires extensive system integration,
standardization, and capacity building across all government ministries.

### 1.5 Digital Transformation for Africa/Western Africa Regional Digital Integration Program (DTFA/WARDIP)

**Program Overview and Scope**

The DTFA/WARDIP program represents the primary funding mechanism and
coordination framework for The Gambia's digital transformation
initiatives. This World Bank-funded initiative provides USD $50 million
specifically allocated to The Gambia as part of a larger $266.5 million
regional program covering The Gambia, Guinea, Guinea-Bissau, and
Mauritania.

The program operates in partnership with multiple regional organizations
including the African Union, Smart Africa, and ECOWAS, establishing The
Gambia within a broader West African digital integration ecosystem.

**Core Program Components**

DTFA/WARDIP is structured around four primary components that directly
impact enterprise architecture development:

**1. Connectivity Infrastructure**

- Broadband access expansion to underserved areas
- Second submarine cable deployment to reduce single point of failure
- National fiber optic network enhancement

**2. Digital Market Development**

- Cross-border data flow frameworks with regional partners
- Digital services integration across ECOWAS member states
- Harmonization of digital policies and regulations

**3. Online Services and E-Government Platforms**

- Government service digitization initiatives
- MyGov citizen portal development
- Digital identity infrastructure
- Digital addressing system implementation

**4. Cybersecurity Infrastructure**

- National Cybersecurity Coordination Center (NCSC) establishment
- Computer Security Incident Response Team (gmCSIRT) operationalization
- Cybersecurity capacity building and training programs
- Critical infrastructure protection frameworks

**Implementation Status**

The program is currently in active implementation phase with a dedicated
project coordinator appointed and multiple procurement processes
underway. Key deliverables include:

- GICTA operationalization under DTFA/WARDIP framework
- National Cybersecurity Coordination Center procurement in progress
- Digital addressing system nationwide rollout ongoing
- MyGov portal development with Bangladesh partnership

**EA Implications**

DTFA/WARDIP directly influences enterprise architecture development
through:

- **Funding Certainty:** $50 million allocation provides resource
  foundation for major initiatives
- **Regional Interoperability Requirements:** Cross-border integration
  mandates influence technical standards
- **Infrastructure Dependencies:** Second submarine cable and
  broadband expansion impact architecture decisions
- **Timeline Constraints:** Program milestones create delivery
  pressure for EA implementation

### 1.6 International Funding and Technical Partnerships

**Major Funding Sources**

The Gambia's digital transformation is supported by multiple
international funding streams:

- **World Bank IDA:** $50 million (DTFA/WARDIP), $119.5 million
  (GEHSSP health sector)
- **ECOWAS Commission:** $180,000 grant for digital infrastructure
  strengthening
- **EU AU-EU D4D Hub:** Technical assistance for multiple initiatives
  including Open Data Platform
- **UNDP:** Technical assistance through Bangladesh a2i program for
  MyGov implementation

**Technology Implementation Partners**

Multiple technology partners provide implementation support:

- **Presight (UAE):** Digital identity infrastructure and
  cybersecurity system development
- **OrangeBD (Bangladesh):** MyGov citizen portal implementation,
  leveraging Bangladesh's successful model
- **Google Africa Initiative:** Digital addressing system pilot and
  expansion support
- **Kalp Foundation (India):** Blockchain platform development for
  Gambia One initiative
- **Ecobank Gambia:** Government revenue collection gateway
  implementation (launched August 2024)
- **WCC Group:** HERA eCRVS solution for civil registration and vital
  statistics

---

## 2. BUSINESS ARCHITECTURE

### 2.1 MINISTRY OF FINANCE & ECONOMIC AFFAIRS (MoFEA)

#### 2.1.1 Organisational Structure

**Department Structure:**

- **Accountant General's Department (AGD)**: Manages IFMIS, treasury
  operations, government payments
- **Budget Directorate**: Budget preparation, execution, and
  monitoring via CBMS
- **Revenue Mobilisation and Aid Coordination**: Revenue policy, donor
  coordination, aid flow management, development partner engagement
- **Debt Management Unit**: Loans and debt management, tracking and
  reporting
- **Economic Policy Analysis Unit**: Macroeconomic policy, fiscal
  analysis
- **Internal Audit Department**: Financial controls, compliance
- **Revenue and Tax Policy Unit**: Fiscal policy and analysis
- **Public Finance Management**: Financial management and reporting
- **Directorate of Public Private Partnership**: Coordinates
  concession agreements
- **Aid Coordination**: Coordinates external funding

**Key Units:**

- **IFMIS Unit**: 18 IT professionals managing the IFMIS network,
  database, user support (~2,000+ users across 50 MDAs)
- **Treasury Management System (TMS) Team**: Manages electronic fund
  transfers, cash management
- **Payment Gateway Team**: Oversees GamPay integration and operations

#### 2.1.2 Business Operating Model

**Core Processes:**

1. **Budget Management**
   - Annual budget preparation through CBMS
   - Quarterly budget execution monitoring
   - Performance-based budgeting initiatives
   - Budget approval workflow through National Assembly

2. **Financial Management**
   - Payment processing via IFMIS (fully operational since 2014)
   - Electronic Fund Transfer (EFT) to commercial banks via CBG T24
     integration
   - Treasury Single Account (TSA) framework implementation
   - Accounts payable/receivable management

3. **Revenue Collection**
   - GamPay integration with GRA for tax revenue
   - Non-tax revenue collection (partial integration)
   - Real-time transaction processing for government fees
   - Payment reconciliation and reporting

4. **Payroll Management**
   - Personnel Management Office (PMO) manages 41,958 civil servants
   - HRMIS and Payroll modules integrated with IFMIS
   - Biometric time attendance system (46 devices installed,
     targeting 100)
   - Automated salary processing with ghost worker detection

#### 2.1.3 Governance Framework

**Financial Governance:**

- **The Public Finance Management Act** provides legal framework
- **IFMIS Steering Committee** oversees system operations and upgrades
- **Internal Audit** ensures compliance with financial regulations
- **The PEFA Framework** is used for PFM performance assessment

**Governance Challenges:**

- Limited coordination between AGD and other financial management units
- Manual reconciliation still required between IFMIS and some systems
- Weak enforcement of financial controls in decentralised units
- Delayed financial reporting from some MDAs

#### 2.1.4 Current Business Challenges

**Operational Challenges:**

1. **Ghost Workers**: Despite improvements (3,146 removed in 2017,
   2,611 in 2019), ongoing audits continue to identify fraudulent
   entries (1,424 in 2024 first phase, 679 in the second phase)

2. **System Integration Gaps**: Poor integration between IFMIS and GRA
   systems requires manual data exchange and reconciliation

3. **Capacity Constraints**:
   - Need for continuous training on new HRMIS/Payroll modules
   - Limited access to source code for system maintenance (vendor
     dependency)
   - Dependency on foreign vendors for IFMIS support

4. **Process Inefficiencies**:
   - Manual processes persist for some payment approvals
   - Delayed budget execution in some MDAs
   - Incomplete biometric attendance integration with payroll

**Strategic Challenges:**

- Balancing between foreign IFMIS (Epicor 10) and home-grown system
  development
- Ensuring sustainable funding for system maintenance and upgrades
- Expanding IFMIS coverage to all government entities
- Achieving full Treasury Single Account implementation

---

### 2.2 GAMBIA REVENUE AUTHORITY (GRA)

#### 2.2.1 Organisational Structure

**Department Structure:**

- **Domestic Tax Department**: Income tax (PIT, CIT), VAT, PAYE,
  Environment Tax, Fringe Benefits, Rental Income Tax
- **Customs Department**: Import/export duties, customs compliance
- **ICT Department**: Manages ITAS, ASYCUDA World, GamPay integration
- **Compliance and Enforcement**: Tax audits, investigations,
  prosecutions
- **Taxpayer Services**: Registration, education, customer service
- HR and Administration Department: Manages personnel and provides
  administrative support
- Finance and Accounting Department: Manages financial and accounting
  functions
- Legal and Board Services: Provides legal support in the discharge of
  the Authority's statutory mandate
- Technical Services Department: Provides advice and research on
  revenue policy matters; develops and monitors corporate strategy;
  taxpayer services
- Internal Audit Department: Provides internal control oversight
- Office of the Commissioner General Department: Provides overall
  administration and enforcement of the Authority's mandate

**Key Units:**

- Headquarter Functions Unit: Provides functional support to GamTax Net
- Technical Support and Monitoring Service Unit: Provides functional
  support to ASYCUDA World
- IT Unit: Deploys and maintains ICT systems and services including
  GamTax Net and ASYCUDA World; handles technical matters on API
  integration

Digital Maturity Leadership: GRA demonstrates the highest digital
maturity among Tier 1 ministries (Level 3.0), driven by successful
infrastructure virtualisation (98% of servers virtualised) and pilot API
integrations with GamPay for payment processing (not yet operational).
This positions GRA as the government benchmark for technology
modernisation.

#### 2.2.2 Business Operating Model

**Core Processes:**

1. **Tax Administration**
   - Taxpayer registration and TIN issuance
   - Tax return filing and assessment
   - Payment collection (GamPay integration pilot not operational)
   - Tax refund processing
   - Compliance monitoring and auditing

2. **Customs Operations**
   - Import/export declaration processing via ASYCUDA World (all
     border posts)
   - Duty calculation and collection
   - Risk management and cargo inspection
   - Trade facilitation and single window initiatives

3. **Revenue Management**
   - Daily revenue collection monitoring
   - Revenue forecasting and target setting
   - Debt management and collection
   - Revenue reporting to MoFEA (manual/email-based)

4. **Taxpayer Services**
   - Walk-in service centres
   - Online declaration for ASYCUDA World (no online services for
     GamTax Net)
   - Taxpayer education and outreach programs
   - Dispute resolution mechanisms (independent from GRA)

#### 2.2.3 Integration Status

**Current Integrations:**

1. GamTax Net → GamPay: API integration for domestic tax payments
   (pilot only - NOT operational)
2. ASYCUDA World → GamPay: API integration for customs duties (pilot
   only - NOT operational)
3. GRA Systems → IFMIS: No integration, manual/email data exchange only
4. GRA Systems → Commercial Banks: No system integration; banks have
   remote access to GRA systems
5. ASYCUDA World → Gambia National Single Window (GNSW): Aggregates all
   players for trade facilitation
6. ASYCUDA → GamTax Net: TIN transfer integration from GamTax Net to
   ASYCUDA

**Integration Architecture:**

- GamPay serves as a central hub for payment processing
- Real-time transaction processing for customs payments
- Domestic tax integration still requires completion
- No real-time revenue data flow to IFMIS

#### 2.2.4 Current Business Challenges

**Operational Challenges:**

1. **System Integration**:
   - IFMIS-GRA integration remains weak despite GamPay success
   - Manual revenue reporting to MoFEA
   - No automated reconciliation between tax systems and IFMIS
   - Email-based data exchange creates delays and errors

2. **Technology Limitations**:
   - GamTax Net and ASYCUDA are separate systems with limited
     interoperability
   - Limited online services for taxpayers, i.e. no online services
     for taxpayers on GamTax Net
   - Partial online services for taxpayers on ASYCUDA World
     (declaration only)
   - Mobile payment integration incomplete
   - Point-to-point integration architecture creates spoke-like
     dependencies and maintenance challenges

3. **Capacity Gaps**:
   - Limited ICT staff for system maintenance and development
   - Insufficient training on new API integration features
   - Weak data analytics capabilities for revenue forecasting
   - Limited GIS capabilities for property tax assessment

**Strategic Challenges:**

- Expanding digital tax services to reduce in-person transactions
- Achieving seamless integration with IFMIS for real-time revenue
  tracking
- Modernising legacy tax systems while maintaining operations
- Implementing a risk-based compliance approach requiring better data
  analytics

---

### 2.3 MINISTRY OF HEALTH (MoH)

#### 2.3.1 Organisational Structure

**Department Structure:**

- **Directorate of Health Services**: Clinical service delivery,
  hospitals, health centres
- **Directorate of Public Health Services**: Disease surveillance,
  immunisation, health promotion
- **Directorate of Planning & Information**: HMIS, data management, M&E
- **Directorate of Pharmaceutical Services**: Drug procurement, supply
  chain
- **Directorate of Human Resource**: Health workforce management, HR
  policies
- **Directorate of Laboratory Services**: Laboratory quality,
  diagnostics coordination
- **Directorate of Health Research**: Health research coordination,
  evidence-based policy
- **Directorate of Health Promotion and Education**: Public health
  awareness, health education programs
- **Directorate of Nursing**: Nursing standards, nurse workforce
  coordination
- **National Health Insurance Authority (NHIA) [Department]**: Health
  insurance scheme management
- **Medical Research Council (MRC) Unit**: Research, clinical trials
  (autonomous)

**Digital Health Units:**

- **HMIS Team**: Manages DHIS2, data collection, reporting (custody of
  DHIS2 operations)
- **eCRVS Team**: Electronic civil registration system management
- **NHIS Digital Platform Team**: e-NHIS system operations
- **Laboratory Information Systems**: A-LIS implementation and support

**Health Information Systems Unit**. The following systems fall under
the broader Health Information Systems umbrella:

- DHIS2 (District Health Information System 2): Core health data
  aggregation
- eLMIS (Electronic Logistics Management Information System): Supply
  chain management
- eHRMIS (Electronic Human Resource Management Information System):
  Health workforce management
- A-LIS (Africa Laboratory Information System): Laboratory services data
- IDSR (Integrated Disease Surveillance and Response): Disease
  surveillance
- SPT (Smart Paper Technology): Immunisation tracking

Note: While these systems are conceptually part of the HIS, they are
currently managed by different teams and operate as separate
applications that require integration.

#### 2.3.2 Business Operating Model

**Core Processes:**

1. **Health Service Delivery**
   - Clinical care at 91 health facilities (public, private,
     not-for-profit)
   - Maternal and newborn health services
   - Disease management programs (HIV, TB, malaria, NCDs)
   - Emergency health services
   - Laboratory and diagnostic services

2. **Public Health Programs**
   - Immunization services (Smart Paper Technology for 374,693
     children registered)
   - Disease surveillance (IDSR with weekly reporting)
   - Health promotion and prevention
   - Environmental health services
   - Community-based health programs (Village Health Workers)

3. **Health Information Management**
   - Data collection via DHIS2 from all health facilities
   - Weekly disease surveillance reporting
   - Quarterly HMIS data verification
   - Monthly facility reporting (timeliness: variable, completeness:
     improving)
   - Electronic case-based surveillance for priority diseases

4. **Health Insurance Operations**
   - NHIS enrolment (15,734 beneficiaries as of April 2025, target:
     60,000)
   - Electronic claims processing via e-NHIS platform
   - Fee-for-service reimbursement to 69 contracted facilities
   - Performance-based financing component
   - Coverage of 19 essential health interventions (maternal/newborn
     focus)

5. **Birth Registration**
   - Mass registration campaign (Aug 2022-Feb 2023): 1,167,460 people
     registered
   - Electronic birth certificates with NIN and QR code
   - Simultaneous health insurance card issuance
   - 53.64% of population registered as of March 2023

#### 2.3.3 Governance Framework

**Health Sector Governance:**

- **National Health Sector Policy 2021-2030:** Comprehensive health
  sector strategic framework
- **National Health Sector Strategic Plan (2022-2025)**: Guides health
  priorities
- **Health Management Information System Policy (2017-2025)**: Governs
  data management
- **National Health Laboratory Services Policy (2021-2025)**: Laboratory
  standards
- **Civil Registration and Vital Statistics (CRVS) Bill**: Legal
  framework for birth, death, and vital event registration (pending
  enactment)
- **HMIS Steering Committee**: Oversees data system operations
- **Disease Surveillance Coordination**: Through the Directorate of
  Public Health Services

**Digital Health Governance:**

- **No comprehensive national eHealth strategy** beyond sectoral
  initiatives
- Different teams manage various HIS components (DHIS2, eCRVS, e-NHIS,
  A-LIS)
- Limited coordination across digital health systems
- WHO Country Cooperation Strategy (2024-2028) includes digital health
  priority

#### 2.3.4 Current Business Challenges

**Operational Challenges:**

1. **Data Quality and Completeness**:
   - Un-timely and incomplete facility reporting
   - Parallel reporting systems creating fragmentation
   - Paper-based case management with manual DHIS2 entry
   - Limited data analysis capacity at facility level
   - Monthly reporting not complete and timely

2. **System Interoperability**:
   - Multiple disconnected systems (DHIS2, eCRVS, e-NHIS, A-LIS, SPT)
   - Siloed applications with limited data exchange
   - Different teams managing different systems
   - eCRVS-NHIS interoperability planned but not yet complete
     (target: August 2025)

3. **Infrastructure and Connectivity**:
   - Limited internet connectivity in rural health facilities
   - Unstable electricity supply affecting system availability
   - 92% of facilities use paper-based clinical registers
   - Limited IT equipment and maintenance
   - 62% national electricity access rate

4. **Human Resource Capacity**:
   - Shortage of skilled ICT personnel in health sector
   - Limited DHIS2 advanced skills among health workers
   - Inadequate statistical software capacity
   - Limited supportive supervision for data quality
   - Technology adoption challenges among older health workers

5. **Health Service Coverage**:
   - NHIS enrollment at 26% of target (15,734 vs 60,000 goal)
   - Need for nationwide NHIS expansion beyond urban centers
   - Limited adoption of electronic health records (60%
     unavailability noted)
   - Telemedicine in early stages with minimal implementation

**Strategic Challenges:**

- Transitioning from pilot implementations to nationwide scale (EHR,
  e-NHIS)
- Establishing true interoperability between health information systems
- Ensuring sustainability beyond donor-funded projects (GEHSSP:
  $119.5M total)
- Building local capacity to maintain and evolve digital health systems
- Expanding digital health infrastructure to rural and underserved areas

---

### 2.4 MINISTRY OF COMMUNICATIONS & DIGITAL ECONOMY (MoCDE)

#### 2.4.1 Organisational Structure

**Department Structure:**

- **Directorate of E-Government**: MyGov, digital services,
  e-government policy
- **Directorate of ICT Policy & Regulation**: ICT sector regulation,
  policy development
- **Directorate of Cyber Security**: National cybersecurity
  coordination, NCSC
- **Digital Infrastructure Division**: Broadband, submarine cables,
  data centers
- **Digital Innovation & Entrepreneurship**: Startup support,
  innovation hubs

**Key Agencies:**

- **Gambia ICT Agency (GICTA)**: Technical implementation, digital
  addressing, e-government platforms
- **Gambia Telecommunications Company (GAMTEL)**: State telecom
  provider, infrastructure
- **West Africa Internet Exchange Point**: Internet peering, data
  centre services

#### 2.4.2 Business Operating Model

**Core Processes:**

1. **E-Government Development**
   - MyGov citizen portal development (partnership with Bangladesh
     a2i program)
   - Digital service design and delivery
   - Government website management (gambia.gov.gm)
   - E-government capacity building (Training of Trainers completed
     Feb 2025, 25 officials)
   - Service Process Simplification initiatives

2. **Digital Infrastructure Management**
   - National broadband network expansion
   - Second submarine cable project ($30-35M World Bank allocation)
   - National Data Centre establishment (Tier 4 planned)
   - Digital Services Development (note: Government Cloud is a
     separate initiative, not a WARDIP component)
   - Digital addressing system (133,000+ properties addressed)

3. **Digital Policy & Regulation**
   - Digital Economy Master Plan 2024-2034 implementation
   - ICT sector regulation and licensing
   - Data protection framework development
   - Cybersecurity policy enforcement
   - Universal access and digital inclusion programs

4. **Cybersecurity Coordination**
   - National Cybersecurity Coordination Centre (NCSC) establishment
     is underway
   - Computer Security Incident Response Team (gmCSIRT) operations
   - Cyber Security Bill formulation
   - Government systems security monitoring via SOC

5. **Digital Public Infrastructure (DPI) Coordination**
   - DTFA/WARDIP program coordination ($50M regional program)
   - Digital identity strategy implementation (partnership with
     Presight, UAE)
   - National addressing system rollout (Google Plus Codes)
   - Blockchain platform development (collaboration with Kalp
     Foundation, India)
   - Open Data Platform implementation

#### 2.4.3 Major DPI Initiatives Under MoCDE

**Digital Transformation for Africa/WARDIP ($50M IDA funding):**

Components:

- Connectivity: Broadband expansion, second submarine cable
- Digital Market Development: Cross-border data flows
- Online Services: E-government platforms, digital services
- Cybersecurity: NCSC establishment, security frameworks

**National Digital Addressing System (NDAS):**

Progress:

- Pilot: 2,500 properties in Banjul (complete)
- Phase 1: 33,000 properties in Kanfing Municipality (complete)
- Phase 2: 100,000 properties in the West Coast Region (complete)
- Current: Nationwide rollout to remaining areas
- Technology: Google Plus Codes, GPS/GIS integration
- Governance: National Digital Addressing Steering Committee (NDASC)
  established Oct 2025

**MyGov Citizen Portal:**

Status: Active development and pilot phase (late 2025)

- Initial services: Birth certificate, National ID, Passport,
  Driver's license, Business registration
- Platform: Web and mobile (Android/iOS), multilingual (English,
  French, Portuguese)
- Development partner: OrangeBD (Bangladesh)
- Portal URL: citizen-dev.gm.orangebd.com (development version)
- Training: 25 government officials trained in Service Process
  Simplification (Feb 2025)

**Government Cloud (G-Cloud):**

Policy Framework (2023-2027):

- "Cloud First" policy for government technology procurement
- Tier 4 National Data Center planned
- Centralized governance through principal G-Cloud provider
- Target: G-Cloud platform operational by 2027
- Focus: Cost reduction, enhanced security, shared infrastructure

#### 2.4.4 Governance Framework

**Policy Framework:**

- **Digital Economy Master Plan 2024-2034**: Overarching digital
  transformation strategy
- **E-Government Strategy 2021-2024**: Digital service delivery framework
- **Government Cloud Policy 2023-2027**: Cloud infrastructure standards
- **Cybersecurity Policy & Strategy 2020-2024**: Security governance
- **Government Open Data Strategy 2023-2026**: Data accessibility and
  transparency
- **Digital Government Policy and Roadmap**: A recently validated
  comprehensive blueprint

**Coordination Mechanisms:**

- GICTA coordinates technical implementation across government
- WARDIP Project Coordinator manages the regional integration program
- Digital addressing coordinated through NDASC
- MyGov steering committee for citizen portal development

**EA Governance Mandate:**

GICTA holds the government-wide mandate for Enterprise Architecture
governance, including:

- Setting EA standards and guidelines for all government agencies
- Reviewing and approving major IT investments for EA compliance
- Maintaining the government EA repository
- Coordinating cross-ministry architecture alignment
- Providing EA technical guidance and capacity building

This mandate is established under the ICT Act [reference year] and
operationalized through the EA Framework developed under this initiative.

#### 2.4.5 Current Business Challenges

**Infrastructure Challenges:**

1. **Connectivity Dependency**:
   - Single submarine cable (ACE) with 4 years remaining legal lifespan
   - Frequent cable damage and disruptions
   - Limited terrestrial backup through Senegal
   - 66.5% mobile internet penetration (2022)
   - 57% internet penetration overall

2. **Data Centre Limitations**:
   - No Tier 3/4 National Data Centre yet (planned)
   - Limited government hosting capacity
   - Reliance on private cloud providers
   - Security concerns with external hosting

3. **Digital Divide**:
   - Urban-rural connectivity disparities
   - 62% electricity access nationally
   - Poor connectivity in rural areas
   - Limited digital literacy (targeting 65% by 2024)

**System Integration Challenges:**

1. **Fragmented Systems**:
   - Multiple disconnected digital identity systems (NIN, birth
     certificates, separate numbering)
   - MyGov integration with backend systems incomplete
   - No unified authentication/authorization system
   - Limited interoperability across e-government services

2. **Implementation Complexity**:
   - MyGov depends on National ID unification (not yet complete)
   - Digital addressing integration with other systems ongoing
   - Payment gateway expansion to non-tax revenue incomplete
   - Backend system modernization required for MyGov full launch

**Capacity and Governance Challenges:**

1. **Human Resources**:
   - Limited ICT specialists across government
   - High dependency on foreign consultants and vendors
   - Need for continuous training on new platforms
   - Limited local software development capacity

2. **Governance Gaps**:
   - No comprehensive national eHealth strategy (sector-specific only)
   - Weak coordination across ministries for DPI initiatives
   - Limited enforcement of digital standards
   - Absent national health information exchange standards

3. **Financial Sustainability**:
   - Project-based funding model limits long-term sustainability
   - High costs for system maintenance and upgrades
   - Insufficient government budget for digital transformation scale
   - Dependency on donor funding (World Bank, ECOWAS, EU, etc.)

**Strategic Challenges:**

- Achieving "most advanced digital society in Africa" by 2034
  requires massive acceleration
- Balancing multiple concurrent DPI initiatives with limited capacity
- Ensuring interoperability and avoiding new silos
- Building sustainable governance for long-term digital transformation
- Transitioning from pilot projects to nationwide deployment at scale

---

## 3. APPLICATION ARCHITECTURE

### 3.1 MoFEA Application Portfolio

#### 3.1.1 Core Financial Systems

**Integrated Financial Management Information System (IFMIS)**

Technical Specifications:

- **Platform**: Epicor 10 (upgraded from earlier versions)
- **Hosting**: On-premises government data centre
- **Users**: ~2,000+ users across 50 government MDAs
- **Operational Since**: 2014 (full production)
- **Modules**: General Ledger, Accounts Payable/Receivable, Cash
  Management, Fixed Assets, Budget Execution
- **Integration**: CBG T24 (EFT), GamPay (payment gateway), CBMS
  (budget system), TMS (treasury management)
- **Support**: 18 IT professionals at AGD

Features:

- Real-time financial transaction processing
- Multi-year budget management
- Electronic payment processing
- Automated journal entries and reconciliation
- Financial reporting and analytics
- Audit trail and compliance controls

Limitations:

- Dependency on a foreign vendor (Epicor) for upgrades and support
- High licensing costs
- Limited customization flexibility
- Integration challenges with some government systems
- Requires continuous training for users

**Central Budget Management System (CBMS)**

Technical Specifications:

- **Platform**: Integrated with IFMIS
- **Function**: Budget preparation and monitoring
- **Users**: Ministry budget units, AGD Budget Directorate
- **Integration**: IFMIS (budget execution data)

Features:

- Annual budget preparation workflows
- Budget allocation by ministry/department/program
- Quarterly budget execution monitoring
- Budget vs. actual reporting
- Budget amendment processing

**Treasury Management System (TMS)**

Technical Specifications:

- **Platform**: Integrated with IFMIS
- **Function**: Cash management, electronic fund transfers
- **Integration**: CBG T24 (core banking), IFMIS, GamPay

Features:

- Electronic Fund Transfer (EFT) processing
- Cash flow forecasting
- Bank reconciliation
- Treasury Single Account (TSA) management
- Payment scheduling and processing

**Human Resources Management Information System (HRMIS)**

Technical Specifications:

- **Platform**: Recently integrated with IFMIS
- **Users**: Personnel Management Office (PMO) staff, 41,958 civil
  servants
- **Support**: 20 dedicated PMO staff (newly recruited)
- **Integration**: IFMIS (payroll), Biometric Time Attendance (46
  devices, targeting 100)

Features:

- Employee master data management
- Payroll processing (13 pay grades)
- Leave management
- Performance appraisal tracking
- Training and development records
- Staff audit and ghost worker detection (removed 3,146 in 2017, 2,611
  in 2019, 1,424 in 2024 phase 1, 679 in phase 2)
- Automated salary suspension for absenteeism (>1 month no clock-in)

Limitations:

- Biometric integration not yet complete
- Limited self-service capabilities for employees
- Data analytics dashboard under development (Microsoft Power BI)
- Need for enhanced reporting capabilities

**Electronic Records Management System (ERMS)**

Technical Specifications:

- **Platform**: Deployed at 5 pilot entities (including PMO, MoFEA)
- **Function**: Digital document management for HR records
- **Status**: Pilot phase, planned expansion

Features:

- Digital storage of personnel files
- Easy retrieval of HR documents
- Workflow automation for HR processes
- Document versioning and audit trail

#### 3.1.2 Revenue Collection Systems

**GamPay (Government Payment Gateway)**

Technical Specifications:

- **Owner**: Central Bank of Gambia (CBG) / MoFEA
- **Management**: Accountant General's Department
- **Hosting**: Cloud-based (external provider)
- **Architecture**: Hub-and-spoke model (central gateway)
- **Integration Protocol**: REST APIs
- **Security**: Tokenisation, SSL/TLS encryption, SOC monitoring
- **Status**: Fully operational (production)
- **Maturity**: API Level 4 (Mature) - highest in government

Current Integrations:

1. IFMIS → GamPay: Payment processing (operational)
2. CBG T24 → GamPay: EFT to commercial banks (operational)
3. GRA → GamPay: Domestic tax collection (pilot only, not operational)
4. GRA ASYCUDA World: Customs declarations (integration with GamPay
   pending)
5. Commercial Banks ↔ GamPay: Real-time transaction processing
   (operational)

Features:

- Real-time payment processing (only real-time cross-ministry
  integration)
- Multi-channel payment acceptance (online, mobile, POS)
- Transaction reconciliation and reporting
- Automated settlement to government accounts
- API-based architecture for system integration

Limitations:

- APIs not versioned (backward compatibility issues)
- No SLA monitoring
- Limited documentation
- Non-tax revenue integration incomplete
- Some ministries having integration difficulties
- No citizen feedback collection mechanism
- No standardized transaction success rate monitoring

**Home-Grown Financial System (Under Development)**

Technical Specifications:

- **Status**: Development phase
- **Team**: 10 system developers (in 3-month training)
- **Focus**: Payroll and HR modules as alternatives to Epicor IFMIS
- **Objective**: Eliminate licensing costs, reduce foreign vendor
  dependency
- **Timeline**: Not specified

#### 3.1.3 Supporting Systems

**Microsoft Power BI Analytics Platform**

Technical Specifications:

- **Status**: Under development for HR and payroll data warehouse
- **Partnership**: Ministry of Public Service + AGD
- **Function**: Advanced analytics, dashboard monitoring
- **Data Sources**: HRMIS, Payroll, IFMIS

**Biometric Time Attendance System**

Technical Specifications:

- **Devices**: 46 installed (target: 100)
- **Integration Status**: Partial (not yet fully integrated with HRMIS)
- **Function**: Staff attendance monitoring, automated salary suspension
- **Planned Enhancement**: Direct integration with payroll for
  automated adjustments

### 3.2 GRA Application Portfolio

#### 3.2.1 Tax Administration Systems

**GamTax Net (Integrated Tax Administration System)**

Technical Specifications:

- Function: Domestic tax administration (Income Tax, Corporate Income
  Tax, VAT, PAYE, Environment Tax, Fringe Benefits, Rental Income Tax)
- Users: GRA Domestic Tax Department staff

Technology Stack:

- Database: SQL Server 2019
- Platform: .NET Framework VB.net
- Operating System: Windows
- Hosting: On-premise
- Version: 4.0
- Vendor: TechBiz

Integration: GamPay (pilot only - NOT operational)

Features:

- Taxpayer registration and TIN management
- Tax return filing and processing
- Tax assessment and calculation
- Payment processing via GamPay
- Tax refund management
- Compliance monitoring
- Taxpayer account management

Limitations:

- No online taxpayer services
- No integration with IFMIS (manual/email reporting only)
- No real-time revenue reporting to MoFEA
- Manual reconciliation required
- No mobile accessibility

**ASYCUDA World**

Technical Specifications:

- Platform: UNCTAD customs management system (Version 4.3.3)
- Function: Import/export declaration processing, customs duties
- Users: GRA Customs Department, importers/exporters, clearing agents

Technology Stack:

- Database: PostgreSQL
- Application Server: SO Class
- Platform: SO Class Java
- Operating System: Redhat Linux 7.0
- Hosting: On-premise

Integration Details:

- Declaration Processing: Real-time electronic submission and validation
- Duty Calculation: Real-time assessment upon declaration submission
- TIN integration with GamTax Net only (GamPay integration NOT
  operational)
- Cargo Release: Dependent on payment confirmation

Note: "Real-time" in this context refers to declaration processing and
duty calculation. Payment settlement times depend on banking system
processing.

Features:

- Electronic customs declaration processing
- Duty calculation and tariff application
- Cargo tracking and release management
- Risk management and selectivity
- Trade statistics and reporting
- Single window initiatives

Limitations:

- Separate system from GamTax Net (limited integration on TIN only)
- Integration with IFMIS is missing
- No connection to other trade facilitation systems

### 3.3 MoH Application Portfolio

#### 3.3.1 Health Information Systems

**District Health Information System 2 (DHIS2)**

Technical Specifications:

- **Platform**: Open-source DHIS2
- **Deployment**: National implementation (all health facilities)
- **Hosting**: Central HMIS team custody
- **Implementation**: Progressive expansion since 2010
- **Users**: Health facility staff, HMIS team, public health programs

Features:

- Facility-level data entry with unique client records
- HIV/AIDS patient management (UICs for ART patients)
- Immunisation data integration with Smart Paper Technology
- Disease surveillance reporting (weekly for IDSR)
- Data quality verification (quarterly validation)
- Timeliness and completeness metrics (regional/national)
- Automated HMIS report generation

Limitations:

- Un-timely and incomplete facility reporting
- Parallel reporting systems creating duplication
- Case management still paper-based (manual entry to DHIS2)
- Limited human resource capacity for advanced DHIS2 functions
- Inadequate supportive supervision at facility level

**Electronic Civil Registration and Vital Statistics (eCRVS)**

Technical Specifications:

- **Solution**: WCC Group HERA platform
- **Launch**: August 1, 2022
- **Mass Registration**: Aug 2022 - Feb 2023 (1,167,460 people
  registered)
- **Coverage**: 53.64% of population (as of March 2023)
- **Features**: Birth certificates with NIN, QR code, GIS-based to
  prevent manipulation

Features:

- Electronic birth, death, marriage, divorce registration
- Printed birth certificates with National Identification Number (NIN)
- QR code for verification
- Simultaneous NHIS card issuance
- Supports legal identity foundation

Planned Integration:

- eCRVS ↔ NHIS: Target completion August 2025 (not yet operational)
- eCRVS ↔ National ID System: Planned but not yet implemented

Limitations:

- Currently operates separately from other government systems
- Interoperability with NHIS delayed
- No integration with Immigration Department's NIN system
- Manual processes still required for some certificate types

**National Health Insurance Scheme (e-NHIS) Digital Platform**

Technical Specifications:

- **Launch**: Pilot Phase 1 (July 2023 at Bundung Maternal & Child
  Hospital)
- **National Rollout**: April 1, 2024
- **Contracted Facilities**: 69 (expanded from 13)
- **Beneficiaries**: 15,734 (as of April 2025; target: 60,000 = 26%
  achieved)
- **Platform**: Electronic enrolment and claims processing

Features:

- Electronic enrolment system for females
- Electronic claims processing (fee-for-service model)
- Performance-based financing component
- Access via NHIS card or electronic birth certificate
- Standard Operating Procedures (SOPs) for e-NHIS use
- 19 essential health interventions (maternal/newborn focus)

Performance Metrics (Pilot):

- 538 women enrolled (Phase 1)
- 399 women enrolled (Phase 2)
- 99.1% beneficiary satisfaction
- 92.40% quality of care score

Limitations:

- Low enrolment (26% of target)
- Urban-centric (limited rural coverage)
- No integration with eCRVS yet (planned for August 2025)
- Limited to maternal/newborn services currently
- Expansion to 54 additional facilities planned for March 2025

**Smart Paper Technology (SPT) for Immunisation**

Technical Specifications:

- **Solution**: Shifo Foundation Smart Paper Technology
- **Deployment**: National scale-up (2022) to all 91 health service
  delivery points
- **Technology**: Hybrid paper-digital solution

Features:

- Simplified smart paper forms completed at point of care
- Regional scanning stations for digitization
- Shifo software reads handwritten notes and uploads to central system
- Individual-level immunization data storage
- Integration with DHIS2 for national reporting
- SMS follow-up for missed appointments

Performance Metrics (as of 2024):

- 374,693 children registered
- 125,344 children fully vaccinated
- 245,316 children followed up with SMS
- Over 99% data accuracy
- 60% reduction in administrative time for health workers

Limitations:

- Requires scanning infrastructure at regional level
- Dependency on internet connectivity for uploads
- Paper form supply chain management required

**Africa Laboratory Information System (A-LIS)**

Technical Specifications:

- **Implementation**: Part of Health Laboratory Information Management
  System (HLIMS) Master Plan
- **Guidelines**: Published January 2023
- **Target**: National Public Health Laboratories

Features:

- Electronic laboratory test requests from clinicians
- Electronic laboratory result reports
- Patient laboratory history tracking
- HMIS data values provision
- Supplies management (orders)
- Laboratory information for referral samples
- Hub systems linkage

Limitations:

- Limited national adoption beyond pilot facilities
- Weak laboratory information management systems generally
- Integration with DHIS2 limited
- Not connected to EHR systems

**Electronic Medical Records Systems (EMRS)**

**MRC Unit Gambia EMRS:**

Technical Specifications:

- **Implementation**: March 2015 (Phase 1 complete March 2017)
- **Scope**: MRC Clinical Services Department only
- **Technology**: Custom-built for MRC

Features:

- Gate Clinic automation
- Pharmacy management
- Inventory stock management
- In-patient clinic systems
- Electronic patient cards
- Laboratory request and results management
- Billing integration
- Doctor interface with patient history access

Benefits Achieved:

- Seamless information flow across clinical departments
- Automated validation controls
- Reduced data capture time
- Enhanced efficiency and patient safety
- Improved audit capability

**National EHR Adoption Status:**

- **MRC Gambia**: Full EMRS operational
- **Sharab Hospital**: Private facility with EHR
- **Public Health System**: 60% unavailability of EHR systems
- **Healthcare Professional Readiness**: 87% (2022 survey)

Limitations:

- No widespread adoption across public health system
- Fragmented implementations
- Each facility uses different systems (if any)
- No national EHR standard or interoperability

**Integrated Disease Surveillance and Response (IDSR) - Electronic
Case-Based Surveillance**

Technical Specifications:

- **Strategy Adoption**: 2003 (adapted 3rd edition in 2022)
- **Electronic System**: Established and validated (GEHSSP PDO
  indicator achieved)
- **Surveillance Type**: Indicator-Based Surveillance (IBS) at all
  facilities

Features:

- Electronic case-based surveillance for priority diseases
- Weekly reporting system for notifiable diseases
- Standard case definitions (SCDs) at 90% of facilities
- Detection of diseases within 7 days (100% of target)

Performance Assessment (2023-2024):

- 90% of facilities have standard case definitions
- 88% of facilities have IDSR-trained focal person
- 71% of regions have intermediate FETP-trained focal persons
- 92% of facilities have paper-based clinical registers (8% digital)

Limitations:

- Exclusive reliance on IBS (no Event-Based or Community-Based
  Surveillance)
- Weak enforcement in private facilities (33% lack SCDs)
- Need for updated IDSR guidelines dissemination

#### 3.3.2 Mobile Health (mHealth) Applications

**SMS for Health Project**

Technical Specifications:

- **Launch**: 2010
- **Partnership**: Vodafone, Pfizer, International Health Partners,
  MatsSoft, MoH
- **Coverage**: All 50 health clinics, central and regional medical
  stores (6 regions), 5 major hospitals

Features:

- Medication supply tracking
- Expiry date monitoring
- Disease incidence data monitoring (pre-specified diseases)
- Real-time weekly analysis
- Web-based drug stock level reports across supply chain
- Standard mobile phone technology

**SPT SMS Component:**

As part of Smart Paper Technology:

- Automated SMS reminders for vaccination follow-ups
- 245,316 children followed up with SMS (as of 2024)

**General mHealth Status:**

Limitations:

- Limited mHealth research specific to The Gambia
- No regulatory standards for health apps in sub-Saharan Africa
- Need for a comprehensive national mHealth strategy
- Limited adoption of other mHealth solutions

#### 3.3.3 Near-Future Health Systems (2025 Planned)

**National E-Health Program:**

Status: Establishment planned per WHO Country Cooperation Strategy
2024-2028

- Comprehensive e-health program framework
- Electronic medical records scale-up beyond pilot facilities
- Electronic logistics management information system
- Technology deployment to health facilities

**Telemedicine Platform:**

Status: Planned as part of Digital Economy Master Plan

- E-health network infrastructure
- Telemedicine services for remote consultations
- Remote healthcare training for professionals
- Integration with national health systems

Current State:

- Small-scale telehealth initiatives reaching underserved communities
- Mobile-based platforms offering virtual consultations and digital
  prescriptions
- Limited implementation, high barriers to adoption

**Digital Health Observatory:**

Status: Implementation planned

- Data visualisation platform for health data
- The Gambia Health Observatory
- Enhanced data use for decision-making

### 3.4 MoCDE Application Portfolio

#### 3.4.1 E-Government Platforms

**MyGov Citizen Portal**

Technical Specifications:

- **Development Partner**: Bangladesh Aspire to Innovate (a2i) program
- **Technical Implementation**: OrangeBD (Bangladesh)
- **Status**: Active development and pilot phase (late 2025)
- **Platform**: Web portal and mobile applications (Android/iOS)
- **Languages**: English, French, Portuguese
- **Development URL**: citizen-dev.gm.orangebd.com

Initial Services (5 priority services):

1. Birth Certificate issuance
2. National Identity Card applications
3. Passport applications
4. Driver's License processing
5. Business Registration Services

Technical Architecture:

- Integration with the existing gambia.gov.gm infrastructure
- Backend integration with government systems (planned):
  - National ID system (not yet unified)
  - eCRVS (birth certificates)
  - Immigration Department (passports, ID cards)
  - GICTA/GPPA (business registration)
  - Payment gateway (GamPay for fee collection)
- Government Service Bus for inter-agency data sharing (planned)
- Open Data Platform integration (planned)

Capacity Building:

- Training of Trainers (TOT) on Service Process Simplification (Feb
  2025)
- 25 government officials trained by Bangladesh experts
- Focus on service process review and simplification before
  digitalisation

Limitations:

- Full public launch pending backend system integration
- Dependency on the National ID system unification (not complete)
- Infrastructure upgrades required (National Data Centre, connectivity)
- Limited current functionality (development phase)
- Integration with multiple fragmented backend systems is challenging

**Gambia Government Website (gambia.gov.gm)**

Technical Specifications:

- **Status**: Operational
- **Function**: Government information portal
- **Content**: Ministry information, news, announcements

Features:

- Information about government ministries and agencies
- News and press releases
- Policy documents and reports
- Links to government services

Limitations:

- Limited transactional capabilities
- Not integrated with service delivery systems
- Mainly informational (not service-oriented)

**Digital Addressing Portal (digitaladdressing.gov.gm)**

Technical Specifications:

- **System**: National Digital Addressing System (NDAS)
- **Technology**: Google Plus Codes integrated with GPS/GIS
- **Status**: Operational, nationwide rollout ongoing

Progress:

- Pilot: 2,500 properties in Banjul (complete)
- Phase 1: 33,000 properties in Kanfing Municipality (complete)
- Phase 2: 100,000 properties in West Coast Region (complete)
- Total Addressed: 133,000+ properties
- Current: Nationwide rollout to remaining areas

Features:

- Unique digital addresses for all properties
- GPS/GIS mapping integration
- Address verification and lookup
- Emergency response optimisation
- E-commerce and postal services enablement
- Urban planning and land administration support
- Tax collection improvement (property visibility)

Governance:

- National Digital Addressing Steering Committee (NDASC) - established
  October 2025

#### 3.4.2 Digital Identity Systems

**National Identification System (Fragmented)**

Current Systems:

**1. National Identification Number (NIN) - Immigration Department**

Technical Specifications:

- **System**: Gambia Biometric Identification System (GAMBIS)
- **Department**: Department of Immigration, Ministry of Interior
- **Format**: 11-digit number (first 6 digits = DOB: DD/MM/YY)
- **Status**: Operational since 2009 (biometric ID cards introduced)
- **Eligibility**: All Gambian citizens aged 18+
- **Current Issue**: ID card production suspended (contract ended with
  Semlex 2024)

Features:

- Biometric data capture
- Used on national ID cards, driver's licenses, resident permits
- Digital chip embedded in cards (not fully enabled)

**2. Birth Certificate System - Ministry of Health**

Technical Specifications:

- **System**: Electronic Civil Registration and Vital Statistics (eCRVS)
- **Solution**: WCC Group HERA platform
- **Format**: 10-digit certificate number (separate from NIN)
- **Status**: Operational since August 2022

Features:

- Electronic birth certificates with QR code
- NIN included for adults, but children under 18 do NOT have NIN
- Mass registration: 1,167,460 people registered (Aug 2022 - Feb 2023)

**Integration Challenge:**

Current State:

- **No direct correlation** between Immigration NIN and Health birth
  certificate system
- Different authorities issue different identification numbers
- No synchronization between systems
- Children under 18 have birth certificate numbers but no NIN

**Planned Unified System (2025 Announcement):**

Government Initiative:

- Single NIN from birth to death announced in 2025
- Integration between NHIA, MoCDE, and GICTA
- Coverage of both Gambians and legal residents
- Timeline: Unclear, depends on system integration and ID card
  production resolution

**Digital Identity Strategy:**

Technical Specifications:

- **Framework**: National Digital Identity Strategy 2023-2028
- **Validation**: Partnership with UN Economic Commission for Africa
- **Implementation Partner**: Presight (UAE) for digital ID and
  cybersecurity

Objectives:

- Unified digital ID system linking all government services
- Maintain the existing NIN structure while adding digital identifiers
- Real-time authentication and verification
- Support online and offline service delivery

#### 3.4.3 Digital Infrastructure Management Systems

**GovStack Platform (Planned)**

Technical Specifications:

- **Framework**: GovStack Architecture Framework approach
- **Status**: Planning and design phase
- **Partnership**: ITU GovStack initiative

Objectives:

- Building block-based architecture
- Reusable components for government services
- Standardised interoperability layer
- National Digital Public Infrastructure Foundation

**Government Service Bus (Planned)**

Technical Specifications:

- **Function**: Central integration layer for data exchange
- **Status**: Design phase (Digital Economy Master Plan)
- **Purpose**: Enable interoperability across government systems

**Open Data Platform**

Technical Specifications:

- **Policy Framework**: Government Open Data Strategy 2023-2026
- **Development Partner**: e-Governance Academy (eGA) via AU-EU
  Digital for Development Hub
- **Status**: Implementation phase

Objectives:

- Public data accessibility
- Transparency enhancement
- Economic development through data-driven innovation
- Citizen engagement in governance

**Gambia One Blockchain Platform**

Technical Specifications:

- **Partnership**: MoCDE with Kalp Foundation (India)
- **Status**: Development phase
- **Platform Vision**: Blockchain-powered DPI for government services

Features:

- Secure data exchange using blockchain
- Government service digitalization with enhanced transparency
- Youth empowerment through blockchain training
- Citizen data ownership on blockchain

Limitations:

- Development phase, not yet operational
- Unclear integration with existing systems
- Pilot use cases not yet defined

#### 3.4.4 Cybersecurity Systems

**National Cybersecurity Coordination Centre (NCSC)**

Technical Specifications:

- **Status**: Establishment underway (DTFA/WARDIP component)
- **Funding**: Part of $50M WARDIP program
- **Function**: National cybersecurity coordination and incident response

**Computer Security Incident Response Team (gmCSIRT)**

Technical Specifications:

- **Status**: Operational
- **Function**: Government cybersecurity incident response
- **Directorate**: Cyber Security under MoCDE

**Security Operations Centre (SOC)**

Technical Specifications:

- **Status**: Operational
- **Function**: API security monitoring, threat detection
- **Coverage**: Government systems including GamPay APIs

**Cybersecurity Framework:**

Policy Documents:

- Cyber Security Bill (in formulation)
- National Cyber Security Strategy (operational)
- Cybersecurity Policy & Strategy 2020-2024
- 2019 Malao Convention provisions

Performance:

- ITU Global Cybersecurity Index: 107th globally
- Score: 32.12
- Africa ranking: 20th position

#### 3.4.5 Supporting Systems

**National Data Centre Infrastructure**

Current State:

- GAMTEL Private Cloud Data Centre (operational)
- Government e-Government Mini Data Center (operational)
- West Africa Internet Exchange Point Data Center (operational)

Planned:

- Tier 4 National Data Center (top priority)
- Secure hosting for public and private sector
- Regional hub positioning for transnational firms

**Connectivity Infrastructure:**

Current:

- Africa-Coast-to-Europe (ACE) submarine fibre optic cable (5.12
  Tbit/s)
- ACE cable at halfway point of technical lifespan (4 years legal
  lifespan remaining)
- Terrestrial network through Senegal (backup)
- Frequent cable damage and disruptions

Planned:

- Second submarine cable ($30-35M World Bank allocation)
- Enhanced digital sovereignty
- Redundancy for the existing ACE cable

---

## 4. DATA ARCHITECTURE

### 4.1 MoFEA Data Architecture

#### 4.1.1 Data Sources

**Primary Data Systems:**

1. **IFMIS (Epicor 10)**
   - Financial transactions (all government payments, receipts)
   - Budget data (allocations, commitments, expenditures)
   - Fixed asset registry
   - Vendor/supplier master data
   - Chart of accounts
   - Financial statements

2. **HRMIS/Payroll**
   - Employee master data (41,958 civil servants)
   - Payroll transactions
   - Leave records
   - Performance appraisal data
   - Training records
   - Staff audit data (ghost worker detection results)

3. **Biometric Time Attendance**
   - Employee clock-in/clock-out records
   - Attendance patterns
   - Absenteeism data
   - 46 devices generating data (targeting 100)

4. **GamPay Transaction Data** (GamPay is not connected to GRA for tax
   revenue collection - this integration is not operational)
   - Payment transactions (real-time)
   - Revenue collection data (tax and non-tax)
   - Bank settlement records
   - Transaction reconciliation data

5. **CBMS (Budget System)**
   - Budget proposals from ministries
   - Budget allocations and revisions
   - Budget execution tracking
   - Performance-based budgeting metrics

#### 4.1.2 Data Ownership

**Clear Data Ownership:**

- **Accountant General's Department**: Owns financial transaction
  data, IFMIS master data
- **Budget Directorate**: Owns budget data and forecasts
- **Personnel Management Office**: Owns employee data, payroll records
- **Central Bank of Gambia**: Owns GamPay transaction data (shared
  access with AGD)

**Data Governance Challenges:**

- Limited data stewardship roles defined
- No comprehensive data governance framework
- Data quality responsibility unclear for some datasets
- Limited data lineage documentation

#### 4.1.3 Data Storage and Management

**Storage Systems:**

1. **IFMIS Database**
   - Platform: Epicor 10 relational database
   - Hosting: On-premises government data centre
   - Backup: Regular backups (frequency not specified)
   - Retention: Multi-year retention for financial records
   - Access: Role-based access control (~2,000+ users)

2. **HRMIS Database**
   - Platform: Integrated with IFMIS
   - Storage: Personnel records, payroll history
   - Backup: Part of IFMIS backup procedures

3. **GamPay Transaction Database**
   - Hosting: Cloud-based (external provider)
   - Storage: Real-time transaction logs
   - Retention: Long-term transaction history
   - Security: Tokenization, encryption

4. **ERMS (Electronic Records Management)**
   - Function: Digital document storage for HR records
   - Deployment: 5 pilot entities
   - Storage: Scanned personnel files, HR documents

**Data Quality Issues:**

- Ghost worker data: Despite improvements, audits continue identifying
  fraudulent entries
- Manual reconciliation between systems indicates data quality gaps
- Limited data validation rules in some systems
- Timeliness issues in data updates

#### 4.1.4 Data Integration and Flow

**Current Data Flows:**

1. **IFMIS → CBG T24**: Electronic Fund Transfer data (EFT) - operational
2. **IFMIS → GamPay**: Payment requests - operational
3. **GamPay → IFMIS**: Transaction confirmations - operational
4. **CBMS → IFMIS**: Budget data - operational
5. **TMS ↔ IFMIS**: Cash management data - fully integrated
6. **HRMIS → IFMIS**: Payroll data - operational
7. **Biometric Devices → HRMIS**: Attendance data - partial integration
   (not complete)
8. **IFMIS → Power BI**: Analytics data - under development

**Data Exchange Challenges:**

1. **IFMIS ↔ GRA Systems**: Poor integration
   - Manual/email-based revenue reporting from GRA to MoFEA
   - No real-time revenue data flow
   - Manual reconciliation required
   - Data duplication and inconsistencies

2. **Multiple Data Entry Points**:
   - Same data entered in multiple systems
   - No single source of truth for some datasets
   - Data synchronisation issues

3. **Limited Real-Time Data Access**:
   - GamPay is only real-time integration across ministries
   - Other systems rely on batch processing or manual updates
   - Delayed financial reporting from some MDAs

#### 4.1.5 Data Analytics and Reporting

**Current Capabilities:**

1. **IFMIS Reporting**
   - Standard financial reports (budget execution, cash position, etc.)
   - Customizable report builder
   - Export to Excel for additional analysis
   - Audit trail reports

2. **HR/Payroll Reporting**
   - Payroll registers
   - Staff audit reports (ghost worker detection)
   - Establishment reports
   - Leave and attendance reports

3. **Power BI Analytics (Under Development)**
   - HR and payroll data warehouse
   - Dashboard monitoring for various reports
   - Advanced customized analytics
   - Real-time insights for decision-making

**Analytics Challenges:**

- Limited advanced analytics capabilities currently
- Data warehouse for cross-system analysis not operational
- Limited predictive analytics
- Insufficient data literacy among users
- Need for enhanced business intelligence tools

### 4.2 GRA Data Architecture

#### 4.2.1 Data Sources

**Primary Data Systems:**

1. **ITAS (Integrated Tax Administration System)**
   - Taxpayer registration data (TINs)
   - Tax return data (all domestic taxes)
   - Tax assessment records
   - Payment data (via GamPay integration)
   - Refund records
   - Compliance and audit data

2. **ASYCUDA World**
   - Import/export declarations
   - Customs duty calculations
   - Cargo tracking data
   - Clearance records
   - Payment data (via GamPay)
   - Trade statistics

3. **GamPay Transaction Data**
   - Real-time tax and customs payment transactions
   - Bank settlement confirmations
   - Reconciliation data

4. **Taxpayer Portal**
   - Online filing data (limited)
   - TIN verification requests
   - User access logs

#### 4.2.2 Data Ownership

**Data Ownership:**

- **GRA Domestic Tax Department**: Owns domestic tax data (ITAS)
- **GRA Customs Department**: Owns customs and trade data (ASYCUDA)
- **GRA ICT Department**: Manages data systems and integration
- **Central Bank/MoFEA**: Co-ownership of payment transaction data
  (GamPay)

**Data Governance Gaps:**

- Limited coordination between the Domestic Tax and Customs data
- No unified taxpayer view across systems
- Data sharing protocols with MoFEA are unclear
- Limited data governance policies

#### 4.2.3 Data Storage and Management

**Storage Systems:**

1. **ITAS Database**
   - Taxpayer records
   - Tax transaction history
   - Assessment and compliance data
   - Storage location: Not specified (likely GRA data center)

2. **ASYCUDA World Database**
   - Customs declarations
   - Trade statistics
   - Cargo and clearance records
   - Storage: GRA/Customs infrastructure

3. **GamPay Transaction Store**
   - Cloud-based storage (external)
   - Real-time transaction logs
   - Historical payment data

**Data Quality Issues:**

- Data silos between ITAS and ASYCUDA
- Limited data validation across systems
- Manual data entry errors
- Incomplete taxpayer master data
- Limited data cleansing processes

#### 4.2.4 Data Integration and Flow

**Current Data Flows:**

1. GamTax Net → GamPay: Tax payment requests (pilot only - NOT
   operational)
2. ASYCUDA World → GamPay: Customs payment requests (pilot only - NOT
   operational)
3. GamPay → GamTax Net: Payment confirmations (NOT operational)
4. GamPay → ASYCUDA: Payment confirmations (NOT operational)
5. GRA Systems → IFMIS: Manual/email reporting only (no system
   integration)

**Critical Data Flow Gaps:**

1. **GRA → MoFEA Revenue Reporting**:
   - Primarily manual/email-based
   - No real-time revenue data flow to IFMIS
   - Manual reconciliation required
   - Significant delays in revenue visibility

2. **ITAS ↔ ASYCUDA**:
   - Limited interoperability between tax and customs systems
   - No unified taxpayer view
   - Separate reporting streams

3. **GRA → Commercial Banks**:
   - Indirect integration via GamPay
   - Real-time for payments but limited for other data

#### 4.2.5 Data Analytics and Reporting

**Current Capabilities:**

- Basic tax revenue reports by type
- Customs trade statistics
- Payment transaction reports
- Compliance monitoring reports
- Manual Excel-based analysis

**Analytics Limitations:**

- Limited advanced analytics
- No revenue forecasting models
- Weak data-driven compliance targeting
- Limited GIS capabilities for property tax
- No integrated dashboard across tax and customs

**Primary Health Information Systems:**

1. **DHIS2 (District Health Information System 2)**
   - Facility-level service delivery data
   - Disease surveillance data (weekly IDSR reports)
   - HIV/AIDS patient data (UICs for ART patients)
   - Immunisation data (integrated with SPT)
   - Health facility performance metrics
   - Data quality indicators (timeliness, completeness)

2. **Smart Paper Technology (SPT) for Immunisation**
   - 374,693 children registered
   - Individual vaccination records
   - 125,344 fully vaccinated children
   - SMS follow-up data (245,316 children)
   - Over 99% data accuracy

3. **eCRVS (Electronic Civil Registration)**
   - 1,167,460 birth registrations
   - Birth certificate data (with NIN and QR code)
   - Vital statistics (births, deaths, marriages, divorces)
   - GIS-based location data

4. **e-NHIS (Electronic National Health Insurance)**
   - 15,734 beneficiary enrolment records
   - Claims data from 69 contracted facilities
   - Fee-for-service transactions
   - Performance-based financing metrics
   - Beneficiary satisfaction data (99.1% satisfaction)

5. **Electronic Medical Records (Limited)**
   - MRC Unit Gambia: Comprehensive EMR (full patient records)
   - Sharab Hospital: Private EMR
   - Public facilities: 60% unavailability of EHR systems
   - Mainly paper-based records (92% of facilities)

6. **Africa Laboratory Information System (A-LIS)**
   - Laboratory test requests
   - Laboratory results
   - Patient's lab history
   - Supplies management data
   - Limited national adoption

7. **Electronic Case-Based Surveillance**
   - Priority disease case data
   - Detection within 7 days (100% of target)
   - Weekly notifiable disease reports
   - Outbreak investigation data

8. **SMS for Health System**
   - Medication supply levels (50 clinics, 6 regional stores, 5
     hospitals)
   - Drug expiry monitoring
   - Disease incidence data
   - Real-time weekly analysis

---

### 4.3 MoH Data Architecture

#### 4.3.2 Data Ownership

**Data Ownership by System:**

- **HMIS Team (Directorate of Planning & Information)**: Custody of
  DHIS2, overall health data coordination
- **Ministry of Health (Civil Registration)**: Owns eCRVS birth
  registration data
- **National Health Insurance Authority (NHIA) [Department]**: Owns
  e-NHIS enrolment and claims data
- **Directorate of Public Health Services**: Owns surveillance data
  (IDSR, case-based)
- **Disease Control Programs**: Own program-specific data (HIV, TB,
  malaria, immunisation)
- **Health Facilities**: Own patient clinical records (paper-based
  primarily)
- **MRC Unit Gambia**: Owns research and clinical data (autonomous)

**Data Governance Challenges:**

- **No comprehensive health data governance framework**
- Multiple systems are managed by different teams with limited
  coordination
- Unclear data sharing policies across health systems
- No national health information exchange standards
- Data ownership conflicts between MoH and autonomous entities

#### 4.3.3 Data Storage and Management

**Storage Systems:**

1. **DHIS2 Database**
   - Central server maintained by HMIS team
   - Historical data from the 2010 implementation
   - Facility-level disaggregation
   - Integration with immunisation data from SPT

2. **eCRVS Database (WCC Group HERA)**
   - 1.17M+ birth registration records
   - GIS-based to prevent data manipulation
   - Birth certificates with NIN and QR code
   - Vital statistics database

3. **e-NHIS Platform**
   - Beneficiary enrolment database (15,734 records)
   - Claims database from 69 facilities
   - Fee-for-service transaction records
   - Hosting: Not specified (likely external cloud)

4. **SPT System (Shifo Foundation)**
   - Individual child immunisation records (374,693 children)
   - Vaccination history
   - SMS follow-up logs
   - Regional scanning station data

5. **Facility-Level Storage**
   - **92% paper-based clinical registers**
   - Limited digital patient record storage
   - Laboratory results (mostly paper or A-LIS where deployed)

6. **MRC Unit Gambia EMR Database**
   - Comprehensive patient records (clinical, pharmacy, lab, billing)
   - Integration with research databases (Electronic Data Capture
     systems)
   - Separate from national health systems

**Data Quality Issues:**

1. **DHIS2 Data Quality**:
   - Un-timely and incomplete facility reporting
   - Quarterly data verification reveals inconsistencies
   - Timeliness and completeness metrics variable by region
   - 2018 HIS Assessment: 48% adequacy of data sources
   - Manual entry from paper records introduces errors

2. **Parallel Reporting Systems**:
   - Multiple reporting channels create data fragmentation
   - Different programs collect same data differently
   - Duplication of effort and inconsistent data

3. **Data Silos**:
   - DHIS2, eCRVS, e-NHIS, A-LIS, SPT operate independently
   - Limited data exchange between systems
   - No unified patient identifier across systems
   - Patient records are fragmented across multiple systems

#### 4.3.4 Data Integration and Flow

**Current Data Flows:**

1. **Health Facilities → DHIS2**: Monthly aggregate reporting (manual
   entry from paper)
2. **SPT (Shifo) → DHIS2**: Immunization data integration (operational)
3. **Disease Surveillance → DHIS2**: Weekly IDSR reports (operational)
4. **A-LIS → DHIS2**: Laboratory data values for HMIS (limited)
5. **eCRVS → e-NHIS**: Planned integration (target: August 2025) - NOT
   YET OPERATIONAL
6. **e-NHIS → Health Facilities**: Claims processing (operational at 69
   facilities)

**Critical Data Integration Gaps:**

1. **eCRVS ↔ e-NHIS Interoperability**:
   - Target completion: August 2025
   - Currently separate systems
   - Birth registration does not automatically create NHIS eligibility
   - Manual processes for linking birth certificates to NHIS cards

2. **eCRVS ↔ National ID System**:
   - No integration between Health (birth certificates) and
     Immigration (NIN)
   - Different numbering schemes
   - Children under 18 have birth certificate numbers but no NIN
   - Planned unification announced but not yet implemented

3. **DHIS2 ↔ EMR Systems**:
   - No interoperability between DHIS2 and facility-level EMRs (where
     they exist)
   - Paper-based clinical records not digitally linked to DHIS2
   - Manual transcription from patient records to DHIS2

4. **Multiple Health Systems Not Connected**:
   - DHIS2, eCRVS, e-NHIS, A-LIS, SPT operate as silos
   - No health information exchange layer
   - No unified patient record
   - Limited longitudinal patient data

5. **Health → Other Government Systems**:
   - No integration with education systems (school health)
   - No integration with social services
   - Limited integration with civil registration beyond birth
     certificates

**Planned Interoperability Architecture:**

- Government Service Bus for health data integration (Digital Economy
  Master Plan)
- National health information exchange standards (not yet established)
- eCRVS-NHIS integration (August 2025 target)
- Electronic logistics management information system

#### 4.3.5 Data Analytics and Reporting

**Current Analytics Capabilities:**

1. **DHIS2 Analytics**:
   - Built-in data quality verification system
   - Timeliness and completeness monitoring by region
   - Quarterly HMIS data validation
   - Facility performance dashboards
   - Disease surveillance trend analysis

2. **SPT Analytics**:
   - Over 99% data accuracy for immunisation
   - Key performance indicators for vaccination programs
   - Automated HMIS report generation at facility, regional, and
     national levels
   - Coverage analysis by geographic area

3. **e-NHIS Analytics**:
   - Beneficiary enrolment tracking (15,734 vs 60,000 target = 26%)
   - Claims processing metrics by facility
   - Quality of care assessment scores (92.40% in pilot)
   - Beneficiary satisfaction (99.1%)

4. **Surveillance Analytics**:
   - Electronic case-based surveillance detecting diseases within 7
     days (100% target)
   - Weekly disease trend analysis
   - Outbreak early warning

**Analytics Limitations:**

- Limited advanced analytics and predictive modelling
- Inadequate data analysis capacity at the facility level
- Data use dimension is still developing (2018 assessment: 55% limited
  resources)
- No comprehensive health data warehouse
- Limited integration of data from multiple systems for holistic analysis
- The Gambia Health Observatory was planned but not yet implemented

---

### 4.4 MoCDE Data Architecture

#### 4.4.1 Data Sources

**Primary Data Systems:**

1. **National Digital Addressing System (NDAS)**
   - 133,000+ property addresses (Banjul, Kanifing, West Coast Region)
   - GPS/GIS coordinates for each property
   - Google Plus Codes
   - Property ownership data
   - Address verification records

2. **MyGov Portal (Development Phase)**
   - User registration data (not yet operational)
   - Service application data (5 initial services planned)
   - Transaction logs (planned)
   - Citizen feedback (planned)

3. **National ID Systems (Fragmented)**
   - Immigration: 11-digit NIN for citizens 18+ (GAMBIS database)
   - Health: Birth certificate numbers (eCRVS - 1.17M+ records)
   - Multiple separate numbering schemes across ministries

4. **Digital Infrastructure Monitoring**
   - Network connectivity data
   - Data center performance metrics
   - Government website analytics
   - Cybersecurity incident logs (gmCSIRT, SOC)

5. **ICT Sector Data**
   - Telecom operator data
   - Internet penetration statistics (57% population, 66.5% mobile)
   - Mobile connections (4.22M cellular connections)
   - Broadband subscribers (41,612 fixed broadband - Dec 2020)

#### 4.4.2 Data Ownership

**Data Ownership:**

- **GICTA**: Owns digital addressing data, e-government platform data
- **Department of Immigration**: Owns NIN database (GAMBIS)
- **Ministry of Health**: Owns birth registration data (eCRVS)
- **MoCDE**: Owns ICT sector regulatory data, digital infrastructure
  monitoring
- **NCSC/gmCSIRT**: Owns cybersecurity incident data
- **Telecom Operators**: Own network and subscriber data (shared with
  regulator)

**Data Governance Challenges:**

- Fragmented identity data across multiple systems
- No unified data governance for cross-cutting DPI initiatives
- Limited data sharing agreements between agencies
- Unclear data sovereignty policies for cloud-hosted systems
- No comprehensive data protection framework is operational

#### 4.4.3 Data Storage and Management

**Storage Systems:**

1. **Digital Addressing Database (NDAS)**
   - GPS/GIS property database
   - 133,000+ records and growing
   - Managed by GICTA

2. **National ID Databases (Multiple)**
   - GAMBIS (Immigration): Biometric ID database
   - eCRVS (Health): Birth registration database (1.17M+)
   - Separate databases not synchronized

3. **MyGov Backend (Planned)**
   - User identity database (integration with National ID pending)
   - Service transaction database
   - Application status tracking

4. **Government Cloud Storage (Planned)**
   - Tier 4 National Data Center (not yet established)
   - Current: Limited government data center capacity
   - Reliance on external cloud providers

5. **Cybersecurity Data**
   - Security incident logs (SOC, gmCSIRT)
   - Threat intelligence data
   - API security monitoring data

**Data Quality Issues:**

- Identity data fragmentation and inconsistencies
- Multiple numbering schemes for same individuals
- No master data management for citizen identity
- Limited data validation across fragmented systems

#### 4.4.4 Data Integration and Flow

**Current Data Flows:**

1. **Digital Addressing → Various Systems**: Planned integration with
   multiple government services (not yet operational)
2. **MyGov → Backend Systems**: Planned integration (not yet operational)
3. **eCRVS → National ID**: Planned unification (announced but not
   implemented)
4. **Cybersecurity Systems → Government Infrastructure**: Monitoring
   and alerting (operational)

**Critical Data Integration Gaps:**

1. **Unified National Identity**:
   - No integration between Immigration NIN and Health birth
     certificates
   - Children under 18 lack NIN
   - Multiple separate identity databases
   - MyGov depends on unified identity (not yet available)

2. **Digital Addressing Integration**:
   - Digital addresses not integrated with tax systems (GRA)
   - Not integrated with civil registration (eCRVS)
   - Not integrated with service delivery systems
   - Planned use for emergency services, e-commerce, urban planning

3. **Cross-Ministry Data Exchange**:
   - No operational Government Service Bus
   - Limited data sharing between ministries
   - GamPay is only successful cross-ministry real-time data
     integration
   - Mostly manual/email data exchange

**Planned Data Integration Architecture:**

- Government Service Bus (central integration layer)
- Open Data Platform (public data access)
- Unified National ID integration
- MyGov backend integration with all service delivery systems

#### 4.4.5 Data Analytics and Reporting

**Current Capabilities:**

- Digital infrastructure monitoring dashboards
- ICT sector statistics (penetration, access)
- Cybersecurity incident reporting (ITU Global Cybersecurity Index:
  107th globally, 32.12 score)
- Digital addressing analytics

**Planned Capabilities:**

- Open Data Platform for public access to government data
- MyGov analytics dashboard (service usage, citizen satisfaction)
- Integrated digital economy indicators
- Smart city analytics (digital addressing, IoT)

**Analytics Limitations:**

- Limited cross-government data analytics
- No integrated dashboard for digital transformation progress
- Weak data-driven policy making
- Limited digital maturity metrics

### 4.5 Cross-Cutting Data Architecture Issues

#### 4.5.1 Data Silos and Fragmentation

**Major Data Silos Identified:**

1. **Financial Data Silos**:
   - IFMIS vs GRA systems (poor integration)
   - GamPay transaction data vs IFMIS financial records
     (reconciliation required)
   - Budget data (CBMS) vs execution data (IFMIS) - integrated but
     limited analytics

2. **Identity Data Silos**:
   - Immigration NIN database (11-digit)
   - Birth certificate numbers (10-digit)
   - Health insurance numbers
   - Tax identification numbers (TIN)
   - No unified citizen identifier

3. **Health Data Silos**:
   - DHIS2 vs eCRVS vs e-NHIS vs A-LIS vs SPT
   - Paper-based clinical records vs digital systems
   - Each program collects similar data differently

4. **Cross-Ministry Silos**:
   - Each ministry maintains separate databases
   - Limited cross-ministry data sharing
   - Manual/email-based data exchange
   - No central data warehouse

#### 4.5.2 Data Standards and Interoperability

**Current Standards Status:**

**Weak or Absent Standards:**

- No national data standards across government
- No national health information exchange standards
- Limited data dictionary standardization
- No master data management practices
- Each system uses different data definitions

**Some Standards Adopted:**

- DHIS2: International standard for health data
- ASYCUDA World: International customs data standard
- GamPay: API-based integration (but APIs not versioned)

**Regional Frameworks:**

- African Union and ECOWAS initiatives provide some guidance
- Working toward adopting international standards (HL7, ICD-10, SNOMED
  for health)

**Standards Gaps:**

- No enterprise-wide data governance framework
- No data quality standards
- Limited metadata management
- No standardised API design guidelines
- Backward compatibility issues (GamPay APIs not versioned)

#### 4.5.3 Data Quality Management

**Data Quality Challenges:**

1. **Completeness**:
   - Health facility reporting is incomplete and untimely
   - Missing data in various government databases
   - Ghost workers in payroll (ongoing issue despite cleanups)

2. **Accuracy**:
   - Manual data entry errors
   - Data inconsistencies between systems
   - Limited validation rules
   - SPT immunisation: 99% accuracy (exception, not norm)

3. **Timeliness**:
   - Delayed reporting from facilities to DHIS2
   - Manual/email-based reporting causes delays (GRA to MoFEA)
   - Real-time data is limited to GamPay transactions only

4. **Consistency**:
   - The same person has different IDs in different systems
   - Data duplication across systems
   - Conflicting data from parallel reporting systems

**Data Quality Mechanisms:**

- DHIS2: Built-in data quality verification, quarterly validation
- IFMIS: Audit trails and controls
- Staff audits: Ghost worker detection (HRMIS/Payroll)
- Limited data quality monitoring in other systems

#### 4.5.4 Data Lifecycle Management

**Data Retention:**

- Financial records: Multi-year retention (IFMIS)
- Health records: Varies by system (paper records: indefinite;
  digital: not specified)
- Tax records: Long-term retention (ITAS, ASYCUDA)
- Transaction logs: GamPay maintains historical data

**Data Archival and Disposal:**

- Limited formal data archival policies
- No comprehensive data retention schedule across government
- Paper records storage challenges in many ministries
- Digital archival strategies not well-defined

**Data Backup and Recovery:**

- IFMIS: Regular backups (on-premises)
- GamPay: Cloud-based with provider backup
- Health systems: Backup practices vary by system
- No government-wide backup policy

#### 4.5.5 Master Data Management

**Current State:**

- **No enterprise-wide master data management**
- Each system maintains its own master data
- No authoritative source for:
  - Citizen identity (fragmented across systems)
  - Organization/entity data (ministries, facilities, etc.)
  - Location/address data (digital addressing emerging)
  - Service definitions

**Critical MDM Gaps:**

- No unique citizen identifier across government
- No central vendor/supplier master data (each ministry maintains own)
- No unified chart of accounts across agencies
- No master reference data for common entities (schools, health
  facilities, etc.)

---

## 5. INTEGRATION ARCHITECTURE

### 5.1 Integration Patterns and Standards

#### 5.1.1 Current Integration Patterns

**Pattern 1: API-Based Integration (GamPay Model)**

**Example**: GamPay Payment Gateway

Architecture:

- Hub-and-spoke model with GamPay as central hub
- REST APIs for system connections
- Real-time transaction processing
- Tokenization for API security
- SSL/TLS encryption

Connected Systems:

- IFMIS → GamPay
- CBG T24 ↔ GamPay
- GRA ITAS → GamPay
- GRA ASYCUDA World (GamPay integration pending)
- Commercial Banks ↔ GamPay

**Maturity**: API Level 4 (Mature) - Highest in government

**Strengths**:

- Real-time integration
- Proven model for payment processing
- Scalable architecture
- Proper domain ownership (Finance Ministry)

**Limitations**:

- APIs not versioned (backward compatibility issues)
- Highest failure rate among integration patterns
- No standardized SLA monitoring
- Limited documentation
- Some ministries having integration difficulties

**Pattern 2: Manual/Email-Based Exchange**

**Example**: GRA → MoFEA Revenue Reporting

Process:

- GRA prepares revenue reports manually
- Reports emailed to MoFEA
- MoFEA manually enters data into IFMIS (if needed)
- Manual reconciliation between systems

**Prevalence**: Common across government for cross-ministry data exchange

**Limitations**:

- Time-consuming and error-prone
- No real-time data
- Data duplication
- Inconsistencies and reconciliation challenges
- Delayed decision-making

**Pattern 3: Direct Database Integration**

**Example**: IFMIS ↔ CBMS, IFMIS ↔ TMS

Architecture:

- Direct database-to-database connections
- Batch or near-real-time data synchronization
- Tightly coupled systems

**Strengths**:

- Efficient for tightly integrated modules
- Good performance within same platform (Epicor)

**Limitations**:

- Tight coupling reduces flexibility
- Difficult to replace individual systems
- Limited to same platform/vendor
- Scalability challenges

GRA → IFMIS Revenue Data: While payment processing via GamPay is
operational, **revenue data reporting to IFMIS remains
manual/email-based**, preventing real-time revenue visibility for
Treasury.

**Pattern 4: File-Based Integration**

**Example**: Various systems exchanging CSV/Excel files

Process:

- System A exports data to file (CSV, Excel)
- File transferred manually or via shared folder
- System B imports file

**Prevalence**: Common for reporting and ad-hoc data exchange

**Limitations**:

- Manual process prone to errors
- Not real-time
- No data validation
- Version control issues
- Security concerns

**Pattern 5: Hybrid Paper-Digital**

**Example**: Smart Paper Technology (SPT) for Immunization

Architecture:

- Paper forms completed at point of care
- Regional scanning stations digitize forms
- Shifo software uploads to central system
- Integration with DHIS2

**Strengths**:

- Works in low-connectivity environments
- Maintains user familiarity with paper
- Over 99% data accuracy achieved

**Limitations**:

- Requires scanning infrastructure
- Not real-time (batch processing at regional level)
- Dependency on internet for uploads
- Physical form supply chain required

#### 5.1.2 Integration Standards

**Current Standards:**

**Adopted Standards:**

- REST APIs: Used by GamPay
- SSL/TLS: Encryption for GamPay APIs
- Tokenization: API authentication (GamPay)

**Absent/Weak Standards:**

- No government-wide API design guidelines
- No API versioning standards
- No standardized data exchange formats
- Limited use of international standards (HL7, FHIR for health)
- No service-oriented architecture (SOA) standards
- No integration testing standards

**Security Standards:**

- SOC monitors API security
- Some tokenisation and encryption implemented
- No comprehensive API security standards

#### 5.1.3 Integration Governance

**Current Governance:**

**GamPay Governance:**

- Domain ownership: Finance Ministry (CBG/MoFEA)
- Accountant General's Department manages operations
- Shared service model

**Other Integrations:**

- No central integration governance body
- Each ministry manages own integrations
- Limited coordination across government
- No integration architecture review board

**Governance Gaps:**

- No enterprise integration strategy
- No standard integration approval process
- Limited integration monitoring and SLA management
- No integration lifecycle management
- No integration performance metrics

---

### 5.2 Integration Inventory

#### 5.2.1 Financial Systems Integrations

| Source System | Target System | Integration Type | Protocol | Status | Data Flow | Frequency |
|--------------|--------------|-----------------|----------|--------|-----------|-----------|
| IFMIS | CBG T24 | EFT | Direct | Operational | Payment instructions | Real-time |
| IFMIS | GamPay | Payment Gateway | REST API | Operational | Payment requests | Real-time |
| GamPay | CBG T24 | Settlement | API | Operational | Transaction settlement | Real-time |
| GamPay | Commercial Banks | Payment Processing | API | Operational | Payments/confirmations | Real-time |
| CBMS | IFMIS | Budget Data | Direct DB | Operational | Budget allocations | Daily |
| TMS | IFMIS | Treasury | Direct DB | Operational | Cash management | Real-time |
| HRMIS | IFMIS | Payroll | Direct DB | Operational | Payroll transactions | Monthly |
| Biometric Devices | HRMIS | Attendance | Partial | In Progress | Clock-in/out data | Daily |
| IFMIS | Power BI | Analytics | Data Warehouse | Development | Financial/HR data | Planned |

#### 5.2.2 Revenue Systems Integrations

| Source System | Target System | Integration Type | Protocol | Status | Data Flow | Frequency |
|--------------|--------------|-----------------|----------|--------|-----------|-----------|
| GRA ITAS | GamPay | Tax Payment | REST API | Pilot only - NOT operational | Tax payment requests | Real-time |
| GRA ASYCUDA | GamPay | Customs Payment | REST API | Pilot only - NOT operational | Customs payment requests | Real-time |
| GamPay | ITAS | Payment Confirmation | API | Pilot only - NOT operational | Payment confirmations | Real-time |
| GamPay | ASYCUDA | Payment Confirmation | API | Pilot only - NOT operational | Payment confirmations | Real-time |
| ITAS | IFMIS | Revenue Reporting | Manual/Email | Poor | Revenue data | Monthly |
| ASYCUDA | IFMIS | Revenue Reporting | Manual/Email | Poor | Revenue data | Monthly |
| ITAS | ASYCUDA | Taxpayer Data | None | Not Integrated | - | - |

#### 5.2.3 Health Systems Integrations

| Source System | Target System | Integration Type | Protocol | Status | Data Flow | Frequency |
|--------------|--------------|-----------------|----------|--------|-----------|-----------|
| Health Facilities | DHIS2 | Reporting | Manual Entry | Operational | Aggregate health data | Monthly |
| SPT (Shifo) | DHIS2 | Immunization | Digital Upload | Operational | Individual immunization | Batch (regional) |
| Disease Surveillance | DHIS2 | IDSR | Manual/Digital | Operational | Weekly surveillance | Weekly |
| A-LIS | DHIS2 | Lab Data | Limited | Partial | Lab values | Varies |
| eCRVS | e-NHIS | Interoperability | Planned | Not Operational | Birth/insurance data | Target: Aug 2025 |
| e-NHIS | Health Facilities | Claims | Electronic | Operational | Claims/reimbursement | Daily (69 facilities) |
| eCRVS | National ID | Unification | Planned | Not Implemented | Birth/identity data | Announced |
| DHIS2 | EMR Systems | None | Not Integrated | Not Operational | - | - |

#### 5.2.4 Digital Public Infrastructure Integrations

| Source System | Target System | Integration Type | Protocol | Status | Data Flow | Frequency |
|--------------|--------------|-----------------|----------|--------|-----------|-----------|
| MyGov Portal | National ID | User Auth | Planned | Development | Identity verification | Planned real-time |
| MyGov Portal | eCRVS | Birth Certificates | Planned | Development | Certificate requests | Planned |
| MyGov Portal | Immigration | ID/Passport | Planned | Development | Application data | Planned |
| MyGov Portal | GamPay | Payment | Planned | Development | Service fees | Planned |
| Digital Addressing | Multiple Systems | Address Lookup | Planned | Limited | Address verification | Planned |
| eCRVS (Health) | NIN (Immigration) | Identity | Planned | Not Implemented | Birth/identity sync | Announced |

---

### 5.3 Integration Challenges

#### 5.3.1 Technical Challenges

**API Integration Issues:**

- APIs not versioned (GamPay): Causes backward compatibility problems
- The highest failure rate among integration patterns
- Limited error handling and retry mechanisms
- No standardised API documentation
- Inconsistent API design across systems

**System Heterogeneity:**

- Different technology platforms (Epicor, DHIS2, ASYCUDA, custom systems)
- Multiple vendors with proprietary formats
- Legacy systems are difficult to integrate
- Limited APIs are available on older systems

**Performance and Scalability:**

- Real-time integration is limited to GamPay
- Most systems rely on batch processing or manual exchange
- Network connectivity issues affect integration reliability
- Limited infrastructure for high-volume transactions

**Data Synchronisation:**

- No master data management
- Data inconsistencies across systems
- Timing issues (data updated in one system but not others)
- Manual reconciliation required

#### 5.3.2 Organisational Challenges

**Governance and Coordination:**

- No central integration authority
- Each ministry manages its own integrations independently
- Limited cross-ministry coordination
- No integration architecture review process

**Capacity and Skills:**

- Limited integration specialists across government
- Dependency on vendors for integration work
- Insufficient training on integration technologies
- Limited API development skills

**Domain Ownership:**

- Unclear ownership for shared data and services
- Resistance to sharing data across ministries
- Lack of domain-driven design principles
- GamPay's success is attributed to clear domain ownership (Finance)

#### 5.3.3 Process and Policy Challenges

**Integration Processes:**

- No standard integration request/approval process
- Ad-hoc integration development
- Limited integration testing
- Poor documentation of existing integrations

**Service Level Agreements:**

- No SLAs for integrations (GamPay noted)
- No performance monitoring
- No integration availability metrics
- Limited accountability for integration failures

**Change Management:**

- API changes break existing integrations (no versioning)
- Insufficient communication about system changes
- No impact analysis before system updates

---

### 5.4 Integration Best Practices (GamPay Case Study)

**Success Factors of GamPay Integration:**

1. **Clear Domain Ownership**: Finance Ministry, as domain expert owns
   payment infrastructure
2. **Shared Service Model**: Other ministries consume GamPay as a
   service (no duplication)
3. **Real-Time Architecture**: Immediate transaction processing and
   confirmation
4. **Hub-and-Spoke Model**: Central gateway reduces point-to-point
   complexity
5. **API-Based**: Modern, scalable integration approach
6. **Proper Security**: Tokenisation, encryption, SOC monitoring
7. **Strong Technical Implementation**: Robust API architecture

**Lessons Learned:**

**What Worked:**

- Domain-driven ownership principle
- Shared service approach prevents duplication
- Real-time integration meets user needs
- API architecture is scalable

**What Needs Improvement:**

- API versioning is critical for sustainability
- SLA monitoring is required for accountability
- Better documentation needed
- Integration support for ministries struggling to connect
- Expansion beyond customs to cover all tax and non-tax revenue

---

### 5.5 Planned Integration Architecture

**Government Service Bus (Planned)**

Vision:

- Central integration layer for all government systems
- Standardised APIs for common services
- Message-based asynchronous integration
- Service registry and discovery
- API gateway for security and monitoring

Status: Design phase (Digital Economy Master Plan)

**National Interoperability Framework (Needed)**

Components:

- Integration standards and guidelines
- Data exchange protocols
- Security and authentication standards
- API design principles
- Master data management
- Service-oriented architecture (SOA) principles

Status: Not yet developed

**Priority Integrations:**

1. **eCRVS ↔ e-NHIS** (Target: August 2025)
2. **eCRVS ↔ National ID Unification** (Announced, timeline unclear)
3. **IFMIS ↔ GRA Real-Time Revenue** (Critical gap)
4. **MyGov ↔ Backend Systems** (Multiple integrations required)
5. **Digital Addressing ↔ Tax/Service Systems** (Planned)

### 5.6 National Digital Addressing System

The National Digital Addressing System (NDAS) represents a critical
cross-cutting Digital Public Infrastructure initiative that provides
foundational addressing data for multiple government services, including
tax collection, emergency response, postal services, and urban planning.

**Implementation Scope**

As of 2025, the NDAS has successfully assigned unique digital addresses
to 135,500 properties nationwide through a phased implementation
approach:

- **Pilot Phase (Banjul):** 2,500 properties addressed as
  proof-of-concept
- **Phase 1 (Kanifing Municipality):** 33,000 properties addressed
- **Phase 2 (West Coast Region - Kombo North):** 100,000 properties
  addressed
- **Current Phase:** Nationwide rollout to remaining areas in progress

**Technology Platform**

NDAS utilizes the Google Plus Codes system integrated with GPS and GIS
mapping technology. Each property receives a unique alphanumeric code
that can be used for navigation, service delivery, and administrative
purposes. The system operates through both online and offline modes to
accommodate connectivity constraints.

**Governance Structure**

The National Digital Addressing Steering Committee (NDASC) was
established in October 2025 to provide oversight and coordination for
the NDAS initiative. GICTA serves as the technical implementation
agency, with support from the Google Africa Initiative.

**Core Data Elements**

The NDAS maintains the following core data elements for each addressed
property:

- **Digital Address Code:** Unique Google Plus Code identifier
- **GPS Coordinates:** Latitude and longitude
- **Administrative Location:** Region, district, ward, and settlement
- **Property Classification:** Residential, commercial, industrial,
  government, etc.
- **Physical Description:** Building type, approximate size, landmarks
- **Occupancy Information:** Owner/tenant name (where provided)

**Data Quality and Maintenance**

- Field verification conducted during addressing campaigns
- Updates managed through GICTA with quarterly validation cycles
- Integration with land administration systems planned for future phases
- Quality assurance through GPS verification and community validation

**Critical Integration Points**

NDAS serves as master data for location information across multiple
systems:

- **Gambia Revenue Authority (GRA):** Property tax assessment,
  business registration verification, tax compliance monitoring
- **Emergency Services:** Ambulance dispatch, fire services, police
  response coordination
- **Postal Services:** Mail delivery routing, courier services
  optimization
- **Urban Planning:** Development control, zoning enforcement,
  infrastructure planning
- **Utility Services:** NAWEC electricity connections, water services,
  billing systems
- **E-Commerce Platforms:** Delivery address standardization for
  online transactions
- **National ID System:** Address verification for ID card
  applications, planned integration

**Current Integration Status**

- **Limited Integration:** Currently operates as standalone system
  with minimal cross-system integration
- **Manual Data Sharing:** Digital address data shared through manual
  processes rather than API integration
- **No Real-Time Integration:** Systems like GRA and emergency
  services do not yet have real-time NDAS access
- **Pilot Integration Planned:** GRA property tax pilot identified as
  first integration use case

### 5.7 National Identity System

The Gambia's national identity infrastructure represents one of the
most critical integration challenges facing enterprise architecture
implementation. The current fragmentation is more severe than initially
assessed, with implications for virtually all digital government
services.

**Technical Structure of Current NIN**

The current National Identification Number operates through the Gambia
Biometric Identification System (GAMBIS), managed by the Department of
Immigration under the Ministry of Interior. The NIN employs an 11-digit
structure where:

- **First 6 digits:** Represent the cardholder's date of birth
  (DDMMYY format)
- **Remaining 5 digits:** Unique identifier assigned sequentially
- **Permanence:** NIN assigned since 2009 when biometric national ID
  cards were introduced
- **Coverage:** Required for all Gambian citizens aged 18 and above

**Current Applications**

The NIN is currently used across multiple identity documents:

- National ID cards (biometric chip cards)
- Driver's licenses
- Resident permits for foreign nationals
- Various government service applications

**Multiple Disconnected Numbering Systems**

The identity fragmentation challenge extends beyond previously
documented gaps:

- **Birth Certificate Numbers (Ministry of Health):** 10-digit
  certificate number system, completely separate from NIN
- **National ID Numbers (Ministry of Interior):** 11-digit NIN system
  for citizens 18+
- **Health Insurance Numbers (NHIA):** Separate numbering for health
  insurance enrollment
- **Passport Numbers:** Independent numbering system
- **Voter Registration Numbers:** Separate electoral commission system

**Critical Gap: No Cross-System Correlation**

The most severe architectural challenge is the complete absence of
correlation mechanisms:

- **Birth certificates for children under 18 do NOT include NIN:**
  Creates identity discontinuity when individuals turn 18
- **No database linkage:** Immigration Department's NIN database and
  Health Ministry's birth registration system operate independently
- **Manual matching required:** Any correlation between systems
  requires manual intervention and document verification
- **Data quality issues:** Inconsistent name spellings and demographic
  data across systems

**Current Procurement Issues**

A critical operational risk has emerged with the suspension of national
ID card issuance:

- **Semlex Contract Termination:** Government contract with Semlex for
  ID card production ended in 2024
- **Production Suspended:** ID card issuance has been suspended for
  several months as of 2025
- **New Contract Negotiations:** Government currently negotiating with
  potential vendors for card production
- **Service Delivery Impact:** Citizens unable to obtain new IDs or
  replace expired/lost cards, affecting access to services

**Implications for Digital Transformation**

The ID card production crisis creates immediate challenges for digital
service rollout:

- MyGov portal cannot launch National ID service without functioning
  card production
- Digital identity authentication depends on physical ID card
  availability
- New citizens turning 18 cannot obtain required identification
- Biometric chip capabilities remain unused even on existing cards

**Government's Unified Identification Vision**

In 2025, the government announced an ambitious initiative for a unified
National Identification System with the following characteristics:

- **Single NIN from Birth to Death:** One identifier assigned at birth
  and maintained throughout life
- **Universal Application:** Same NIN used on birth certificates, ID
  cards, driver's licenses, passports, health insurance, etc.
- **Cross-Ministry Integration:** NHIA, Ministry of Communications,
  GICTA, Immigration, Health coordinating implementation
- **Coverage Extension:** The System will cover both Gambian citizens
  and legal residents

**Architecture Requirements for Unified System**

Achieving the unified identity vision requires substantial architectural
development:

- **Master Identity Registry:** Centralized authoritative source for
  identity data with federated access model
- **Data Synchronization Layer:** Mechanisms to correlate existing
  11-digit NINs with 10-digit birth certificate numbers
- **Identity Federation Platform:** Enable authentication and
  authorization across multiple government systems
- **Birth-to-ID Integration:** Automated NIN assignment at birth
  registration with eCRVS system integration
- **Digital Identity Credentials:** Enable biometric chip utilization
  for digital authentication and e-signatures

**eCRVS Achievements**

Since August 2022, The Gambia has made significant progress with
electronic Civil Registration and Vital Statistics:

- **Scale Achievement:** 1.17 million people registered with digital
  birth certificates
- **Security Features:** QR codes and enhanced security features on
  new certificates
- **Unique Identification:** Each birth certificate contains unique
  identification number
- **Real-Time Generation:** System capable of generating unique
  numbers in real-time at registration

**Critical Integration Gap**

Despite eCRVS success, a critical integration gap remains:

- **Standalone Operation:** eCRVS operates separately from the
  national ID system
- **No Automatic NIN Assignment:** Birth registration does not trigger
  NIN creation or reservation
- **Future Integration Design:** System designed with future
  integration capability but not yet implemented
- **Manual Transition at Age 18:** No automated pathway from birth
  certificate number to NIN when citizens reach adulthood

---

## 6. TECHNOLOGY ARCHITECTURE

### 6.1 MoFEA Technology Infrastructure

#### 6.1.1 Computing Infrastructure

**IFMIS Infrastructure:**

Servers:

- Platform: Epicor 10 servers (on-premises)
- Location: Government data centre (Accountant General's Department)
- Configuration: Not specified (likely multiple servers for
  application, database, backup)
- Operating System: Not specified (likely Windows Server or Linux)

**Database:**

- Type: SQL Server 2016 (Epicor 10 integrated)
- Size: Not specified
- Backup: Regular backups performed
- High Availability: Not specified

**Client Devices:**

- Users: ~2,000+ users across 50 government MDAs
- Devices: Desktop computers/laptops
- Operating System: Not specified (likely Windows)

#### 6.1.2 Network Infrastructure

**Government Network:**

- Broadband Internet connectivity provided
- Network connectivity to 50 government agencies
- VPN or dedicated links: Not specified
- Network security: Firewall, basic security controls

**Connectivity Challenges:**

- Limited bandwidth in some locations
- Network reliability issues
- Connectivity gaps in remote offices

#### 6.1.3 HRMIS Infrastructure

**PMO Infrastructure:**

- HRMIS integrated with IFMIS (uses same infrastructure)
- 20 dedicated PMO staff workstations
- Biometric time attendance devices: 46 installed (target: 100)
  - Device type: Facial recognition/fingerprint scanners
  - Network connection: Ethernet/Wi-Fi to government network
  - Integration status: Partial (not yet fully integrated with HRMIS)

#### 6.1.4 Supporting Technology

**Electronic Records Management System (ERMS):**

- Deployment: 5 pilot entities
- Function: Digital document scanning and management
- Storage: Digital file server/document management system

**Microsoft Power BI:**

- Status: Under development for HR/payroll data warehouse
- Platform: Cloud-based Microsoft Power BI service
- Data Sources: HRMIS, Payroll, IFMIS

**Home-Grown System Development:**

- Development Environment: Not specified
- Team: 10 developers in training
- Target: Payroll and HR modules
- Infrastructure: New servers required

### 6.2 GRA Technology Infrastructure

#### 6.2.1 ITAS and ASYCUDA Infrastructure

**Tax Administration Infrastructure:**

- ITAS Platform: Server-based (likely on-premises at GRA)
- ASYCUDA Platform: Server-based customs system
- Database: Separate databases for ITAS and ASYCUDA
- Location: GRA data center or facilities

**Client Infrastructure:**

- GRA staff workstations (Domestic Tax and Customs departments)
- Taxpayer/trader access via web portals (limited)
- Clearing agents access to ASYCUDA

Infrastructure Maturity: GRA demonstrates the highest level of
infrastructure virtualisation across Tier 1 ministries, with 98% server
virtualisation achieved. This positions GRA as the government leader in
modern infrastructure practices and provides a model for other
ministries to follow.

Virtualization benefits realised:

- Improved resource utilisation and cost efficiency
- Enhanced disaster recovery capabilities
- Simplified server management and provisioning
- Foundation for future cloud migration

GRA Infrastructure Overview:

- Total Physical Servers: 2
- Total Virtual Servers: 21
- Virtualization Platform: ESXi
- Virtualization Rate: 98% (government leader)
- Data Center Location: Banjul HQ
- Backup Solution: Veeam Backup
- Disaster Recovery Site: Yes
- Network Monitoring Tools: PRTG, Zabbix, SOCRADAR

#### 6.2.2 GamPay Infrastructure

**Hosting:**

- Cloud-based platform (external provider, not in Gambia)
- Scalable cloud infrastructure
- High availability configuration

**Security:**

- Tokenization for API authentication
- SSL/TLS encryption for APIs
- Security Operations Center (SOC) monitoring
- Intrusion detection/prevention

**Integration Points:**

- REST API endpoints for connected systems
- API gateway for request routing
- Transaction processing engine
- Settlement processing with CBG and commercial banks

### 6.3 MoH Technology Infrastructure

#### 6.3.1 Health Information Systems Infrastructure

**DHIS2 Infrastructure:**

- Hosting: Central server managed by HMIS team
- Platform: Open-source DHIS2 software
- Database: PostgreSQL (standard for DHIS2)
- Location: Likely MoH/government data center
- Client Access: Web-based (browsers at health facilities)

**eCRVS Infrastructure (WCC Group HERA):**

- Solution Provider: WCC Group
- Hosting: Likely external hosting or government data center
- Platform: HERA Civil Registration and Vital Statistics solution
- GIS-based system with biometric integration (birth certificates)
- QR code generation for certificates

**e-NHIS Platform:**

- Hosting: Not specified (likely external cloud provider)
- Access: Web-based enrollment and claims system
- 69 contracted health facilities connected
- Electronic claims processing

**Smart Paper Technology (SPT):**

- Paper Forms: Physical smart paper supplied by Shifo Foundation
- Scanning Stations: Regional scanning infrastructure
- Shifo Software: Cloud-based digitization service
- Integration: API connection to DHIS2
- SMS Platform: Mobile network operator integration for follow-ups

**A-LIS (Africa Laboratory Information System):**

- Platform: Laboratory information system software
- Deployment: Limited (pilot facilities)
- Hosting: Local servers at lab facilities or central server

**MRC Unit Gambia EMR:**

- Custom-built electronic medical records system
- Hosting: MRC facilities (autonomous)
- Integration: Internal clinical systems (gate clinic, pharmacy, lab,
  billing)
- Research EDC integration planned

#### 6.3.2 Health Facility Infrastructure

**Facility-Level Technology:**

**Computing Devices:**

- Limited computers at health facilities (92% still use paper clinical
  registers)
- Desktop computers for DHIS2 data entry (where available)
- Mobile devices for SPT SMS follow-up

**Connectivity:**

- Internet: Variable (poor connectivity in rural areas)
- Mobile Networks: Coverage varies (SMS for Health uses mobile
  connectivity)
- Electricity: 62% national access rate (unreliable in many health
  facilities)

**Planned Infrastructure:**

- EU/European Investment Bank: Renewable energy for all public health
  facilities
- Enhanced connectivity as part of digital health expansion

#### 6.3.3 Near-Future Health Technology (Planned)

**National E-Health Network:**

- Dedicated e-health network infrastructure
- Telemedicine platform connectivity
- Remote healthcare training infrastructure

**Electronic Logistics Management:**

- System for drug supply chain management
- Integration with existing SMS for Health
- Facility-level stock management

**National EHR Scale-Up:**

- Expansion of electronic medical records beyond MRC and private
  facilities
- Standardized EHR platform selection
- Facility-level infrastructure upgrades required

### 6.4 MoCDE Technology Infrastructure

**Infrastructure Governance Transition:**

Under the government's digital transformation strategy, management of
national digital infrastructure assets is being progressively
transferred to GICTA. This includes:

- National Data Centre operations (when established)
- Government network backbone management
- Shared platform services
- Cloud infrastructure coordination

#### 6.4.1 National Digital Infrastructure

**Internet Connectivity:**

**Submarine Cable:**

- Primary: Africa-Coast-to-Europe (ACE) fiber optic cable (5.12
  Tbit/s)
- Status: Halfway through technical lifespan (4 years legal lifespan
  remaining)
- Issues: Frequent damages and disruptions
- Backup: Terrestrial network through Senegal

**Planned:**

- Second submarine cable ($30-35M World Bank allocation)
- Enhanced redundancy and digital sovereignty

**Internet Penetration:**

- Population: 57% (as per PURA 2024)
- Mobile Internet: 66.5% (2022)
- Fixed Broadband: 41,612 subscribers (December 2020)
- Mobile Connections: 4.22 million cellular (2022)

**Mobile Phone:**

- Ownership: 81% of population

#### 6.4.2 Data Centre Infrastructure

**Current Data Centres:**

1. **GAMTEL Private Cloud Data Centre**
   - Operator: GAMTEL (state telecom provider)
   - Services: Cloud hosting, colocation
   - Tier: Not specified (likely Tier 2-3)

2. **Government e-Government Mini Data Centre**
   - Location: Government facilities
   - Capacity: Limited
   - Services: IFMIS, some government systems

3. **West Africa Internet Exchange Point Data Centre**
   - Function: Internet peering, colocation
   - Regional connectivity hub

**Planned Infrastructure:**

**Tier 4 National Data Centre:**

- Status: Top priority, not yet established
- Tier: Tier 4 (highest reliability: 99.995% uptime)
- Purpose: Secure hosting for government and private sector
- Vision: Regional hub for transnational firms
- Government Cloud (G-Cloud) Platform operational by 2027

#### 6.4.3 Government Cloud Infrastructure

**G-Cloud Policy (2023-2027):**

Strategy:

- "Cloud First" policy for government technology procurement
- Centralised governance through the principal G-Cloud provider
- Tier 3/4 National Data Centre as a foundation

Current State:

- Limited government cloud infrastructure
- Reliance on external cloud providers (e.g., GamPay hosted externally)
- Some government systems on-premises (IFMIS)

**Cloud Services Planned:**

- Infrastructure as a Service (IaaS)
- Platform as a Service (PaaS)
- Software as a Service (SaaS)
- Disaster recovery and backup services
- Security services

#### 6.4.4 MyGov Infrastructure

**Development Infrastructure:**

- Development URL: citizen-dev.gm.orangebd.com
- Development Partner: OrangeBD (Bangladesh)
- Hosting: External (Bangladesh during development)
- Platform: Web and mobile (Android/iOS)

**Production Infrastructure (Planned):**

- Hosting: Government Cloud (G-Cloud) when available
- Integration: Government Service Bus for backend connections
- Authentication: Unified National ID system
- Payment: GamPay integration

#### 6.4.5 Digital Addressing Infrastructure

**NDAS Technology:**

- GPS/GIS mapping system
- Google Plus Codes technology
- Property database (133,000+ addresses)
- Web portal: digitaladdressing.gov.gm
- Mobile app for address lookup and verification

**Governance:**

- National Digital Addressing Steering Committee (NDASC)
- GICTA technical implementation

#### 6.4.6 Cybersecurity Infrastructure

**National Cybersecurity Coordination Centre (NCSC):**

- Status: Establishment underway (DTFA/WARDIP component)
- Function: National-level cybersecurity coordination
- Infrastructure: Security operations centre, incident response
  capabilities

**Computer Security Incident Response Team (gmCSIRT):**

- Status: Operational
- Function: Government cybersecurity incidents
- Monitoring: Government systems and networks

**Security Operations Centre (SOC):**

- Function: API security monitoring, threat detection
- Coverage: Government systems, including GamPay APIs
- Tools: Security information and event management (SIEM), intrusion
  detection

**Cybersecurity Tools:**

- Firewall and intrusion prevention systems (IPS)
- Antivirus and endpoint protection
- Security monitoring and logging
- Tokenisation and encryption (GamPay)

**Cybersecurity Performance:**

- ITU Global Cybersecurity Index: 107th position globally
- Score: 32.12
- Africa Ranking: 20th position

**Challenges:**

- Five-fold increase in cyberattacks in Africa (lack of frameworks)
- Need for strengthened cybersecurity standards for health systems
- Limited enforcement of data security protocols
- Capacity gaps in cybersecurity professionals

### 6.5 Cross-Cutting Technology Issues

#### 6.5.1 Technology Standardization Challenges

**Lack of Government-Wide Standards:**

- No standardized technology procurement guidelines
- Multiple vendors and platforms (Epicor, DHIS2, ASYCUDA, WCC, Shifo,
  OrangeBD, etc.)
- No enterprise architecture standards enforced
- Limited technology reuse across ministries

**Specific Technology Gaps:**

- No standard operating systems (Windows, Linux mix)
- No standard database platforms
- No standard development platforms
- No standard API frameworks
- Each system uses different technology stacks

#### 6.5.2 Infrastructure Limitations

**Connectivity:**

- Single submarine cable creates single point of failure
- Terrestrial backup through Senegal limited
- Rural connectivity gaps
- Inconsistent bandwidth across government facilities

**Power/Electricity:**

- 62% national electricity access
- An unreliable power supply affects system availability
- Limited backup power (UPS, generators) in many facilities
- Health facilities especially affected

**Data Centre Capacity:**

- No Tier 4 National Data Centre yet
- Existing data centre infrastructure:
  - GICTA Data Centre: Primary government facility (operational)
  - Gamtel Data Centre: Currently not functional
  - Note: The West African Exchange Point Data Centre referenced in
    some documents does not exist
- Limited government hosting capacity
- Reliance on external providers creates data sovereignty concerns
- Need for disaster recovery and business continuity infrastructure

#### 6.5.3 Technology Capacity

**IT Workforce:**

- 18 IT professionals at AGD for IFMIS (~2,000+ users across 50 MDAs)
- Limited ICT staff across other ministries and agencies
- Shortage of skilled ICT personnel (health sector noted)
- High dependency on foreign vendors and consultants
- Limited local software development capacity (10 developers in
  training for home-grown system)

**Digital Literacy:**

- Government workforce: Target 75% digital literacy by 2024 (via
  KGESDI)
- National workforce: Target 65% digital literacy by 2024
- Technology adoption challenges among older workers
- Insufficient training on new systems

#### 6.5.4 Technology Sustainability

**Vendor Dependency:**

- High reliance on foreign vendors (Epicor, WCC, Shifo, OrangeBD,
  Presight, etc.)
- Licensing costs for proprietary systems (IFMIS)
- Limited local capacity for system maintenance
- Vendor lock-in concerns

**Funding:**

- Project-based funding model (donor-dependent)
- High costs for system upgrades and maintenance
- Insufficient government budget for technology investments
- Sustainability concerns when donor funding ends

**Technology Refresh:**

- Aging infrastructure (ACE cable at half lifespan, IFMIS on older
  platform)
- Need for continuous technology upgrades
- Limited budget for technology refresh cycles
- Legacy systems difficult to replace

### 6.6 Technology Roadmap Priorities

**Short-Term (2025-2026):**

1. Second submarine cable deployment
2. Tier 3/4 National Data Centre establishment
3. Government Cloud (G-Cloud) foundation
4. MyGov infrastructure and backend integration
5. eCRVS-e-NHIS integration
6. IFMIS-GRA real-time integration
7. Expand biometric time attendance (54 additional devices)
8. National ID system unification infrastructure

**Medium-Term (2027-2028):**

1. G-Cloud platform fully operational
2. Government Service Bus implementation
3. National e-health network
4. Telemedicine platform infrastructure
5. Digital addressing integration with service systems
6. Open Data Platform
7. Enhanced cybersecurity infrastructure (NCSC fully operational)
8. Renewable energy for all public health facilities

**Long-Term (2029-2034):**

1. Advanced analytics and AI infrastructure
2. IoT platform for smart services
3. Blockchain platform integration (Gambia One)
4. Regional digital hub positioning
5. 5G network deployment
6. Advanced cybersecurity capabilities
7. Comprehensive digital government infrastructure

---

## 7. CROSS-CUTTING DPI INITIATIVES

### 7.1 GamPay - Government Payment Gateway

**Project Overview:**

**Purpose:** Central payment gateway for government revenue collection
and payment processing

**Owner:** Central Bank of Gambia (CBG) / Ministry of Finance & Economic
Affairs (MoFEA)

**Management:** Accountant General's Department (AGD) under MoFEA

**Status:** ✅ Fully Operational (Production) - Considered one of few
successful integrations in government

**Governance Model:** Domain ownership principle - Finance Ministry owns
and operates payment infrastructure; other ministries use it as shared
service

**Architecture:**

- Hub-and-spoke model with GamPay as central integration hub
- API-based architecture (REST APIs)
- Real-time transaction processing
- Cloud-based hosting (external provider)
- Security: Tokenization, SSL/TLS encryption, SOC monitoring
- API Maturity Level 4 (Mature) - Highest rating in government

**Current Integrations:**

1. IFMIS → GamPay → CBG T24 → Commercial Banks (complete chain
   operational)
2. GRA GamTax Net/ASYCUDA to GamPay integration (in development - pilot
   only, NOT operational)
3. Real-time payment processing for:
   - Tax revenue collection (customs integration in progress; domestic
     tax integration pending)
   - Non-tax revenue collection (integration incomplete)

**Success Factors:**

- Clear domain ownership (Finance Ministry as domain expert)
- Shared service model prevents duplication
- Real-time integration (only one across government)
- Robust API architecture
- Proper security implementation

**Challenges:**

- APIs not versioned (backward compatibility issues)
- Highest failure rate among integration patterns
- No SLA monitoring
- Limited documentation
- Some departments having "trouble" with integration
- Non-tax revenue integration incomplete
- No systematic citizen feedback collection

**Lessons for EA:**

- Domain-driven ownership critical for success
- Shared services more efficient than duplication
- Real-time integration meets user needs
- API versioning essential for sustainability

### 7.2 MyGov Citizen Portal

**Project Overview:**

**Purpose:** Comprehensive one-stop online portal for government
services

**Partnership:** South-South Cooperation Agreement between Bangladesh
(a2i program) and The Gambia

**Lead Ministries:** Ministry of Communications & Digital Economy
(MoCDE), Ministry of Public Service (MoPS)

**Technical Partner:** OrangeBD (Bangladesh) - implementing digital
government platform

**Status:** Active development and pilot phase (late 2025)

**Funding:** ECOWAS Commission grant, UNDP technical assistance

**Initial Services (5 Priority):**

1. Birth Certificate issuance
2. National Identity Card applications
3. Passport applications
4. Driver's License processing
5. Business Registration services

**Technical Architecture:**

- Platform: Web portal + mobile applications (Android/iOS)
- Languages: English, French, Portuguese
- Development URL: citizen-dev.gm.orangebd.com
- Integration: Government Service Bus (planned), backend systems,
  payment gateway (GamPay)
- Authentication: Unified National ID system (pending availability)

**Implementation Progress:**

**Completed:**

- Training of Trainers (TOT) on Service Process Simplification (Feb
  2025, 25 officials)
- Development portal operational
- Partnership agreement with Bangladesh

**In Progress:**

- Service process simplification for 5 initial services
- Backend system integration design
- Platform development and testing

**Pending:**

- National ID system unification (prerequisite)
- Production infrastructure setup (G-Cloud)
- Full public launch

**Challenges:**

- Dependency on fragmented National ID systems (not yet unified)
- Backend system integration complexity (multiple disconnected systems)
- Infrastructure dependencies (National Data Center, connectivity)
- Integration with legacy ministry systems

**Comparison with Bangladesh MyGov:**

- Bangladesh: 35 ministries, 178 offices, 1,852 services, 4.04M
  registered users
- Gambia: Starting with 5 services, phased expansion approach

**Timeline:**

- 2025: Pilot version launch, user testing, staff training
- 2025-2027: Gradual service expansion, backend integration
- Long-term: Comprehensive 24/7 one-stop-shop for government services

### 7.3 National Digital Identity System

**Current State: FRAGMENTED**

**System 1: National Identification Number (NIN) - Immigration
Department**

Technical Specifications:

- System: Gambia Biometric Identification System (GAMBIS)
- Format: 11-digit number (first 6 digits = date of birth DD/MM/YY)
- Operational: Since 2009 (biometric ID cards introduced)
- Coverage: All Gambian citizens aged 18 and above
- Uses: National ID cards, driver's licenses, resident permits
- Features: Biometric data capture, digital chip (not fully enabled)

**Current Issue:**

- ID card production suspended (Semlex contract ended 2024)
- Government negotiating new card production contracts

**System 2: Birth Certificate System - Ministry of Health**

Technical Specifications:

- System: Electronic Civil Registration and Vital Statistics (eCRVS) -
  WCC Group HERA
- Format: 10-digit certificate number (SEPARATE from NIN)
- Operational: Since August 2022
- Coverage: 1,167,460 people registered (mass registration Aug
  2022-Feb 2023)
- 53.64% of population registered as of March 2023
- Features: QR code, NIN included for adults, but children under 18 do
  NOT have NIN

**CRITICAL GAP:**

- No direct correlation between Immigration NIN and Health birth
  certificate system
- Different authorities issue different identification numbers
- No synchronization between databases
- Children under 18 have birth certificate numbers but no NIN

**Other Identity Systems:**

- Health insurance numbers (NHIS)
- Tax identification numbers (TIN - GRA)
- Various ministry-specific ID numbers

**Planned Unified System (2025 Government Announcement):**

Vision:

- Single National Identification Number (NIN) from birth to death
- Coverage: Both Gambians and legal residents
- Integration: NHIA, MoCDE, GICTA coordination
- Timeline: Unclear, depends on system integration and ID card
  production

**Digital Identity Strategy 2023-2028:**

- Framework: UN Economic Commission for Africa validation
- Implementation Partner: Presight (UAE) for digital ID and
  cybersecurity
- Objectives:
  - Unified digital ID system linking all government services
  - Maintain existing NIN structure while adding digital identifiers
  - Real-time authentication and verification
  - Support online and offline service delivery

**Impact on EA:**

- MyGov depends on unified National ID (not available)
- Service delivery integration blocked by identity fragmentation
- Data quality issues from multiple identity systems
- Master data management impossible without unified identity

### 7.4 National Digital Addressing System (NDAS)

**Project Overview:**

**Purpose:** Assign unique digital addresses to all properties nationwide

**Technology:** Google Plus Codes integrated with GPS/GIS mapping

**Implementation Partner:** GICTA

**Status:** Operational, nationwide rollout ongoing

**Governance:** National Digital Addressing Steering Committee (NDASC) -
established October 2025

**Progress:**

- Pilot: 2,500 properties in Banjul (complete)
- Phase 1: 33,000 properties in Kanifing Municipality (complete)
- Phase 2: 100,000 properties in West Coast Region/Kombo North
  (complete)
- **Total: 133,000+ properties addressed**
- Current Phase: Nationwide rollout to remaining areas

**Technical Architecture:**

- GPS/GIS mapping database
- Google Plus Codes for property identification
- Web portal: digitaladdressing.gov.gm
- Mobile app for address lookup and verification
- Property database managed by GICTA

**Impact Areas:**

- Emergency response optimization (ambulance, fire, police)
- E-commerce and postal services enhancement
- Urban planning and land administration
- Tax collection improvement (business visibility)
- Service delivery addressing

**Integration Status:**

- Currently standalone system
- Planned integration with:
  - Tax systems (GRA property tax assessment)
  - Civil registration (eCRVS)
  - Service delivery systems (MyGov, utilities)
  - Emergency services (health, police, fire)

**Challenges:**

- Limited integration with other government systems
- Address verification and validation processes
- Maintaining address database accuracy as properties change
- Rural area coverage gaps

### 7.5 Electronic Civil Registration and Vital Statistics (eCRVS)

**Project Overview:**

**Solution:** WCC Group HERA platform

**Funding:** World Bank - Gambia Essential Health Services Strengthening
Project (GEHSSP: $119.5M total)

**Launch:** August 1, 2022

**Mass Registration Campaign:** Aug 2022 - Feb 2023

**Status:** Operational

**Performance:**

- 1,167,460 people registered (all ages)
- 53.64% of population registered (as of March 2023)
- 43.47% of electronic birth certificates verified (March 2023)

**Technical Features:**

- Electronic registration of births, deaths, marriages, divorces
- Printed birth certificates with National Identification Number (NIN)
- QR code for verification and anti-fraud
- GIS-based system prevents data manipulation
- Simultaneous Health Insurance card issuance

**Integration:**

**Current:**

- Birth certificate issuance operational
- Simultaneous NHIS card generation (physical card, not system
  integration)

**Planned:**

- eCRVS ↔ e-NHIS interoperability: Target August 2025 (NOT YET
  OPERATIONAL)
- eCRVS ↔ National ID unification: Announced but not implemented
- eCRVS ↔ MyGov: Planned for birth certificate service

**Impact:**

- Legal identity foundation for all citizens
- Improved birth registration coverage (previously low)
- Health insurance enrollment enablement
- Vital statistics for planning and policy

**Challenges:**

- Currently operates separately from other government systems
- Integration with National ID system delayed
- Interoperability with NHIS not yet achieved (August 2025 target)
- No integration with Immigration Department NIN database

### 7.6 National Health Insurance Scheme (NHIS) - e-NHIS Platform

**Project Overview:**

**Legislation:** National Health Insurance Act (November 2021)

**Funding:** World Bank GEHSSP ($119.5M total project)

**Status:** Operational, expansion phase

**Implementation Timeline:**

- July 2023: Pilot Phase 1 at Bundung Maternal & Child Hospital
- Sept-Dec 2023: Pilot Phase 2
- April 1, 2024: National rollout commenced
- March 2025: Expansion to 54 additional facilities planned

**Coverage:**

- Beneficiaries: 15,734 (as of April 2025)
- Target: 60,000 (26% achieved)
- Contracted Facilities: 69 (expanded from 13)
- Services: 19 essential health interventions (maternal/newborn focus)

**Technical Platform:**

- Electronic enrollment system for females
- Electronic claims processing system
- Fee-for-service reimbursement model with performance-based financing
- Access via NHIS card or electronic birth certificate
- Standard Operating Procedures (SOPs) for e-NHIS use

**Performance Metrics:**

Pilot Results:

- 538 women enrolled (Phase 1)
- 399 women enrolled (Phase 2)
- 99.1% beneficiary satisfaction
- 92.40% quality of care assessment score

**Integration:**

- Current: 69 health facilities connected for claims processing
- Planned: Integration with eCRVS (birth registration) - Target August
  2025
- Future: Expansion beyond maternal/newborn to broader services

**Challenges:**

- Low enrollment (26% of target achieved)
- Urban-centric coverage (limited rural penetration)
- Need for nationwide expansion
- eCRVS integration delayed
- Dependency on electronic birth certificates for enrollment

### 7.7 Digital Transformation for Africa/WARDIP

**Project Scale:** $50 million (International Development Association
funding)

**Regional Scope:** Multi-country initiative - The Gambia, Guinea,
Guinea-Bissau, Mauritania

**Partners:** African Union, Smart Africa, ECOWAS

**Status:** Active implementation phase, project coordinator appointed

**Core Components:**

1. **Connectivity:**
   - Broadband access expansion
   - Second submarine cable deployment ($30-35M allocation)
   - National broadband network upgrade
   - Community-based fixed broadband and Wi-Fi for public facilities

2. **Digital Market Development:**
   - Cross-border data flows
   - Digital services integration
   - Regional digital economy initiatives

3. **Online Services:**
   - E-government platforms
   - Digital public services
   - MyGov and other citizen services

4. **Cybersecurity:**
   - National Cybersecurity Coordination Center (NCSC) establishment
   - Cybersecurity framework and capacity building
   - Regional cybersecurity cooperation

**Implementation Status:**

- Project coordinator appointed
- Multiple procurement processes underway
- NCSC establishment in progress
- Second submarine cable planning phase

**Impact on EA:**

- Critical infrastructure foundation for digital transformation
- Cybersecurity framework for government systems
- Regional interoperability requirements
- Connectivity improvements enabling digital services

---

## 8. SECURITY ARCHITECTURE

### 8.1 Cybersecurity Governance

**National Framework:**

**Policy Documents:**

- Cybersecurity Policy & Strategy 2020-2024
- National Cyber Security Strategy
- Cyber Crime Bill (in formulation)
- 2019 Malao Convention provisions
- Digital Economy Master Plan 2024-2034 (security provisions)

**Institutional Framework:**

1. **Directorate of Cyber Security (MoCDE)**
   - National-level cybersecurity policy and coordination
   - Cyber security strategy implementation
   - Sector coordination

2. **National Cybersecurity Coordination Center (NCSC)**
   - Status: Establishment underway (WARDIP component)
   - Function: National cybersecurity operations center
   - Coordination: Cross-sector incident response

3. **Computer Security Incident Response Team (gmCSIRT)**
   - Status: Operational
   - Function: Government cybersecurity incident response
   - Coverage: Government systems and networks

4. **Security Operations Center (SOC)**
   - Status: Operational
   - Function: Real-time security monitoring
   - Coverage: Government systems including GamPay APIs
   - Tools: SIEM, intrusion detection, threat intelligence

**Global Performance:**

- ITU Global Cybersecurity Index: 107th position globally (out of
  ~190 countries)
- Score: 32.12 (low score)
- Africa Ranking: 20th position
- Indicates significant room for improvement

### 8.2 Application Security

**Current Security Measures:**

**GamPay Payment Gateway:**

- Tokenization for API authentication
- SSL/TLS encryption for data in transit
- SOC monitoring of API traffic
- Security audit trails
- Transaction monitoring and fraud detection

**IFMIS:**

- Role-based access control (RBAC) for ~2,000+ users
- Audit trails for financial transactions
- User authentication and authorization
- Database security controls
- Regular backups

**Health Systems:**

- Limited security measures in many systems
- DHIS2: Standard authentication and access controls
- eCRVS: GIS-based anti-manipulation controls, QR codes for
  verification
- e-NHIS: Access controls for beneficiary and claims data
- Paper-based records: Physical security only

**General Application Security Issues:**

- Inconsistent security standards across systems
- Limited application penetration testing
- Weak password policies in some systems
- Limited multi-factor authentication (MFA)
- No government-wide application security standards

### 8.3 Network Security

**Current Measures:**

**Perimeter Security:**

- Firewalls protecting government network
- Intrusion Prevention Systems (IPS)
- Network segmentation (limited)
- VPN for remote access (some agencies)

**Network Monitoring:**

- SOC monitors network traffic
- Intrusion detection systems (IDS)
- Security information and event management (SIEM)
- Limited threat intelligence integration

**Challenges:**

- Single submarine cable creates vulnerability (DDoS, cable cuts)
- Limited network redundancy
- Inconsistent security controls across government facilities
- Weak network segmentation between ministries
- Limited bandwidth for security updates and patches

### 8.4 Data Security and Privacy

**Data Protection Framework:**

**Current State:**

- Data protection framework being developed (Digital Economy Master
  Plan)
- No comprehensive data protection legislation yet
- Limited enforcement of data security protocols
- No dedicated data protection authority

**Data Security Practices:**

**Financial Data:**

- IFMIS: Database encryption, access controls, audit logs
- GamPay: Cloud provider security (tokenization, encryption)
- Backup and recovery procedures

**Health Data:**

- Limited encryption for data at rest
- DHIS2: Standard security features
- eCRVS: GIS-based integrity controls
- 92% paper-based clinical records: Physical security only
- Need for health data privacy and security guidelines

**Identity Data:**

- GAMBIS (NIN): Biometric data security
- eCRVS: Birth certificate database security
- Fragmentation creates multiple points of vulnerability

**General Data Security Gaps:**

- No encryption standards for data at rest
- Limited data loss prevention (DLP) capabilities
- Weak data classification practices
- No data masking or anonymization standards
- Limited personal data protection

### 8.5 Physical Security

**Data Centers:**

**Current:**

- GAMTEL Private Cloud Data Center: Physical security (access controls,
  surveillance)
- Government Mini Data Center: Basic physical security
- Limited backup power (UPS, generators)
- Environmental controls (cooling, fire suppression) - varies by
  facility

**Planned:**

- Tier 4 National Data Center: Enhanced physical security (multi-layer
  access control, 24/7 monitoring, redundant power, cooling)

**Government Facilities:**

- Access control varies by facility
- Limited CCTV surveillance
- Paper records storage security inconsistent
- Biometric time attendance devices (46 installed) provide some access
  monitoring

**Challenges:**

- 62% national electricity access (unreliable power)
- Limited backup power infrastructure
- Physical security gaps in many government buildings
- Paper records vulnerable to fire, flood, theft

### 8.6 Identity and Access Management (IAM)

**Current State:**

**System-Specific IAM:**

- Each system manages its own user identities and access
- IFMIS: Role-based access control for ~2,000+ users
- DHIS2: User roles and permissions by facility/program
- GamPay: API tokenization for system access
- e-NHIS: User access for facility staff and administrators

**No Enterprise IAM:**

- No unified identity management across government
- No single sign-on (SSO) for government systems
- No centralized user provisioning/de-provisioning
- Each user has multiple usernames/passwords
- No federated identity management

**Authentication:**

- Mainly username/password authentication
- Limited multi-factor authentication (MFA)
- No biometric authentication for system access (except physical
  access via time attendance)
- Weak password policies in many systems

**Planned:**

- Unified National ID system could enable government-wide IAM
- MyGov will require centralized authentication
- Government Service Bus may include identity services

### 8.7 Security Challenges

**Technical Challenges:**

1. **Infrastructure Vulnerabilities:**
   - Single submarine cable (single point of failure)
   - Unreliable electricity (62% access rate)
   - Limited network redundancy
   - Aging infrastructure (ACE cable halfway through lifespan)

2. **System Security:**
   - Inconsistent security controls across systems
   - APIs not versioned (GamPay) - can introduce vulnerabilities
   - Limited security testing (penetration testing, vulnerability
     assessments)
   - Weak patch management across government

3. **Data Security:**
   - No data protection legislation enforced
   - Limited encryption practices
   - Data fragmentation increases attack surface
   - 92% paper-based health records vulnerable to physical threats

**Organizational Challenges:**

1. **Capacity:**
   - Limited cybersecurity professionals in government
   - Insufficient security training for IT staff and users
   - High dependency on vendors for security
   - Limited security awareness among government employees

2. **Governance:**
   - No enterprise security governance framework
   - Weak enforcement of security policies
   - Limited security incident response capabilities
   - No government-wide security architecture

3. **Threat Environment:**
   - Five-fold increase in cyberattacks in Africa
   - Limited threat intelligence sharing
   - Ransomware and malware threats increasing
   - Phishing and social engineering risks

**Policy and Compliance Challenges:**

1. **Regulatory Gaps:**
   - Cyber Security Bill still in formulation
   - No data protection law enforced
   - Limited compliance monitoring
   - No penalties for security breaches

2. **Standards:**
   - No government-wide security standards
   - Limited adoption of international standards (ISO 27001, NIST)
   - No security baseline for government systems

### 8.8 Security Roadmap Priorities

**Immediate (2025-2026):**

1. Finalise and enact Cyber Security Bill
2. Establish the National Cybersecurity Coordination Centre (NCSC)
   fully operational
3. Implement multi-factor authentication (MFA) for critical systems
4. Conduct security audits of major government systems
5. Deploy second submarine cable (redundancy)
6. Enhance SOC capabilities (threat intelligence, advanced monitoring)

**Short-Term (2026-2027):**

1. Data protection legislation and enforcement
2. Government-wide security architecture and standards
3. Enterprise identity and access management (IAM)
4. Security awareness training program for all government employees
5. Penetration testing and vulnerability assessment program
6. Incident response and disaster recovery plans

**Medium-Term (2027-2030):**

1. Tier 3/4 National Data Centre with enhanced physical and logical
   security
2. Government Cloud (G-Cloud) security services
3. Security operations centre (SOC) maturity enhancement
4. Cyber threat intelligence sharing platform
5. Advanced persistent threat (APT) detection capabilities
6. Compliance monitoring and enforcement framework

---

## 9. GAP ANALYSIS SUMMARY

### 9.1 Business Architecture Gaps

| Domain | Current State | Desired State | Gap | Priority |
|--------|-------------|--------------|-----|----------|
| Cross-Ministry Coordination | Limited coordination, each ministry operates independently | Coordinated digital transformation with shared goals | No enterprise-wide coordination mechanism | **CRITICAL** |
| Process Standardization | Processes vary significantly across ministries | Standardized processes based on best practices | Process fragmentation, duplication of effort | **HIGH** |
| Service Delivery | 90% in-person, limited digital services | 70% digital services by 2033 | Massive gap in digital service capability | **CRITICAL** |
| Governance | Sector-specific governance, limited enterprise view | Enterprise-wide EA governance with clear accountability | No EA governance framework operational | **CRITICAL** |
| Capacity | Limited EA skills, high vendor dependency | Strong local EA capacity, sustainable operations | Major capacity and skills gap | **HIGH** |

### 9.2 Application Architecture Gaps

| Domain | Current State | Desired State | Gap | Priority |
|--------|-------------|--------------|-----|----------|
| System Integration | Fragmented systems, mainly manual integration (except GamPay) | Seamless integration via Government Service Bus | Poor integration, data silos, manual processes | **CRITICAL** |
| Digital Services | Limited online services (MyGov in development) | Comprehensive one-stop portal (MyGov) with 500+ services | 495+ services gap, backend integration incomplete | **CRITICAL** |
| Identity Systems | Fragmented (multiple numbering schemes, no synchronization) | Unified National ID from birth to death | Identity fragmentation blocking service delivery | **CRITICAL** |
| Health Systems | Multiple silos (DHIS2, eCRVS, e-NHIS, A-LIS, SPT) | Integrated health information exchange | No interoperability, 60% EHR unavailability | **HIGH** |
| Financial Systems | IFMIS-GRA poor integration, manual revenue reporting | Real-time revenue integration | Revenue visibility gap, reconciliation burden | **HIGH** |
| Application Portfolio Management | No enterprise view of applications | Centralized application portfolio management | Unknown total applications, no rationalization | **MEDIUM** |

### 9.3 Data Architecture Gaps

| Domain | Current State | Desired State | Gap | Priority |
|--------|-------------|--------------|-----|----------|
| Master Data Management | No MDM, each system maintains own master data | Enterprise MDM for citizen, organization, location | No single source of truth for core entities | **CRITICAL** |
| Data Quality | Variable quality, ghost workers, incomplete reporting | High-quality data with validation and governance | Quality issues affecting decision-making | **HIGH** |
| Data Integration | Data silos, limited sharing, manual exchange | Integrated data flows via Government Service Bus | Data fragmentation, duplication, inconsistency | **CRITICAL** |
| Data Governance | Limited governance, unclear ownership | Comprehensive data governance framework with stewardship | No enterprise data governance | **HIGH** |
| Data Standards | Inconsistent, system-specific | Government-wide data standards and definitions | No interoperability, data mapping complexity | **HIGH** |
| Data Analytics | Basic reporting, limited advanced analytics | Enterprise data warehouse, AI-driven insights | Limited data-driven decision-making | **MEDIUM** |

### 9.4 Integration Architecture Gaps

| Domain | Current State | Desired State | Gap | Priority |
|--------|-------------|--------------|-----|----------|
| Integration Platform | Point-to-point, ad-hoc integration | Government Service Bus (enterprise integration layer) | No central integration platform | **CRITICAL** |
| Real-Time Integration | Only GamPay real-time; others batch/manual | Real-time integration for critical services | Real-time capability gap for most services | **HIGH** |
| API Management | Limited APIs, not versioned (GamPay), no standards | Enterprise API gateway with versioning, standards | API immaturity, sustainability issues | **HIGH** |
| Integration Standards | No standards, inconsistent approaches | Standardized integration patterns, protocols | Integration complexity, high failure rates | **HIGH** |
| Integration Governance | No governance, ad-hoc development | Integration architecture review and approval | Unmanaged integration landscape | **MEDIUM** |
| Interoperability | Critical systems not integrated (eCRVS-NHIS, eCRVS-NID, IFMIS-GRA) | Seamless interoperability across government | Major interoperability gaps blocking services | **CRITICAL** |

### 9.5 Technology Architecture Gaps

| Domain | Current State | Desired State | Gap | Priority |
|--------|-------------|--------------|-----|----------|
| Connectivity | Single submarine cable (ACE), frequent disruptions | Redundant submarine cables, reliable connectivity | Single point of failure, connectivity vulnerability | **CRITICAL** |
| Data Centre | Limited capacity, no Tier 3/4 centre | Tier 4 National Data Centre operational | No secure, reliable government hosting | **CRITICAL** |
| Cloud Infrastructure | External cloud, no G-Cloud | Government Cloud (G-Cloud) operational by 2027 | No government cloud platform | **HIGH** |
| Power/Electricity | 62% access, unreliable supply | Renewable energy for all public facilities | Unreliable power affecting system availability | **HIGH** |
| Technology Standards | No standards, multiple vendors/platforms | Standardized technology stack, reusable components | Technology fragmentation, vendor lock-in | **MEDIUM** |
| Cybersecurity | ITU Index 107th globally (32.12 score), NCSC not operational | Top 50 globally, comprehensive security framework | Major cybersecurity maturity gap | **CRITICAL** |
| IT Workforce | Limited ICT staff (18 at AGD for 350 users/50 MDAs) | Adequate IT staff with EA skills across government | Severe capacity shortage | **HIGH** |

**Note**: GRA's 98% server virtualisation represents a best practice
within government and demonstrates that mature infrastructure is
achievable with proper investment and technical capacity.

### 9.6 Cross-Cutting Gaps

| Domain | Current State | Desired State | Gap | Priority |
|--------|-------------|--------------|-----|----------|
| EA Maturity | Level 2.19 (Defined but not consistently applied) | Level 4+ (Managed and optimized) | 1.81 maturity level gap | **HIGH** |
| Digital Transformation | Project-based, donor-dependent | Sustainable, government-led transformation | Funding and ownership gap | **CRITICAL** |
| Vendor Dependency | High reliance on foreign vendors/consultants | Local capacity, sustainable support | Knowledge transfer and sustainability gap | **HIGH** |
| User Experience | Complex, in-person processes | Citizen-centric, seamless digital services | Service design and delivery gap | **HIGH** |

### 9.7 Priority Gap Summary

**CRITICAL GAPS (Must Address Immediately):**

1. System integration and interoperability (Government Service Bus)
2. National ID unification (prerequisite for many services)
3. Enterprise Architecture governance framework
4. Connectivity redundancy (second submarine cable)
5. Tier 4 National Data Center establishment
6. Master Data Management (citizen, organization, location)
7. Cybersecurity maturity enhancement
8. Service delivery digitalization (current: 10%, target: 70%)

**HIGH PRIORITY GAPS (Address in Short Term):**

1. Real-time integration capabilities beyond GamPay
2. Data quality and governance framework
3. API management and versioning standards
4. Cloud infrastructure (G-Cloud)
5. Health information exchange (eCRVS-NHIS-EHR)
6. IFMIS-GRA real-time integration
7. IT workforce capacity building
8. Access to DPI broadband connectivity
9. Technology standards and guidelines

**MEDIUM PRIORITY GAPS (Address in Medium Term):**

1. Enterprise data warehouse and advanced analytics
2. Application portfolio management
3. Integration governance framework
4. Technology standardization
5. Digital literacy and change management

---

## APPENDICES

### Appendix A: Assessment Data Sources

**Document Review:**

- EA Framework and Operating Model documents
- Digital Transformation Continuum
- EA Findings Summary (BDAT assessment)
- DPI Projects Status Report
- eHealth Status Report
- GamPay Project Overview
- MyGov Status Report
- National ID Status Report
- Payroll System Documentation
- ITU-Gambia Contract and Deliverables
- Digital Economy Master Plan 2024-2034
- E-Government Strategy 2021-2024
- Government Cloud Policy 2023-2027
- Cybersecurity Policy & Strategy 2020-2024
- Various ministry strategic plans and policies

**Stakeholder Engagement:**

- Ministry focal points from MoFEA, GRA, MoH, MoCDE
- Technical staff from IFMIS, HRMIS, GamPay, DHIS2, eCRVS, e-NHIS
- GICTA project managers
- World Bank project coordinators

**System Surveys:**

- Technical questionnaires from 4 Tier 1 ministries
- Application inventory (partial)
- Integration mapping
- Infrastructure assessment

**Public Sources:**

- World Bank project documents
- Government websites and portals
- News reports and press releases
- International organisation reports (WHO, ITU, UNECA)

---

### Appendix B: Acronyms and Abbreviations

| Acronym | Definition |
|---------|-----------|
| ACE | Africa-Coast-to-Europe (submarine cable) |
| AGD | Accountant General's Department |
| A-LIS | Africa Laboratory Information System |
| API | Application Programming Interface |
| ARM | Architectural Reference Model |
| ASYCUDA | Automated System for Customs Data |
| BDAT | Business, Data, Application, Technology |
| CBG | Central Bank of Gambia |
| CBMS | Central Budget Management System |
| gmCSIRT | Computer Security Incident Response Team |
| DHIS2 | District Health Information System 2 |
| DPI | Digital Public Infrastructure |
| DTFA | Digital Transformation for Africa |
| EA | Enterprise Architecture |
| eCRVS | Electronic Civil Registration and Vital Statistics |
| EFT | Electronic Fund Transfer |
| EHR | Electronic Health Records |
| EMR | Electronic Medical Records |
| ERMS | Electronic Records Management System |
| GAMBIS | Gambia Biometric Identification System |
| GEHSSP | Gambia Essential Health Services Strengthening Project |
| GICTA | Gambia ICT Agency |
| GIS | Geographic Information System |
| GPS | Global Positioning System |
| GRA | Gambia Revenue Authority |
| HERA | WCC Group eCRVS solution |
| HMIS | Health Management Information System |
| HRMIS | Human Resources Management Information System |
| IAM | Identity and Access Management |
| IDSR | Integrated Disease Surveillance and Response |
| IFMIS | Integrated Financial Management Information System |
| ITAS | Integrated Tax Administration System |
| ITU | International Telecommunication Union |
| MDM | Master Data Management |
| MoFEA | Ministry of Finance & Economic Affairs |
| MoH | Ministry of Health |
| MoCDE | Ministry of Communications & Digital Economy |
| MRC | Medical Research Council |
| NDASC | National Digital Addressing Steering Committee |
| NDAS | National Digital Addressing System |
| NHIA | National Health Insurance Authority |
| NHIS | National Health Insurance Scheme (e-NHIS: electronic platform) |
| NIN | National Identification Number |
| NCSC | National Cybersecurity Coordination Center |
| PAERA | Pan-African Enterprise Architecture Framework |
| PMO | Personnel Management Office |
| REST | Representational State Transfer (API protocol) |
| SOC | Security Operations Center |
| SPT | Smart Paper Technology (Shifo Foundation) |
| SSL/TLS | Secure Sockets Layer / Transport Layer Security |
| TIN | Tax Identification Number |
| TMS | Treasury Management System |
| TOGAF | The Open Group Architecture Framework |
| WARDIP | Western Africa Regional Digital Integration Project |
| WHO | World Health Organization |

---

### Appendix C: Key Performance Indicators (Current State)

**Digital Transformation Indicators:**

- EA Maturity Level: 2.19 (out of 5)
- Digital Service Delivery: ~10% (target: 70% by 2033)
- ITU Global Cybersecurity Index: 107th globally, 32.12 score
- Internet Penetration: 57% population, 66.5% mobile
- Mobile Phone Ownership: 81%
- Electricity Access: 62% nationally

**Financial Systems:**

- IFMIS Users: ~2,000+ across 50 government MDAs
- GamPay Transactions: Real-time for customs; domestic tax incomplete
- Ghost Workers Removed: 3,146 (2017), 2,611 (2019), 2,103 (2024)
- Civil Servants: 41,958
- Biometric Devices: 46 installed (target: 100)

**Health Systems:**

- DHIS2 Coverage: All health facilities (timeliness/completeness
  variable)
- eCRVS Registrations: 1,167,460 people (53.64% of population)
- e-NHIS Beneficiaries: 15,734 (target: 60,000 = 26% achieved)
- e-NHIS Facilities: 69 contracted (expanded from 13)
- SPT Immunisation: 374,693 children registered, 99% data accuracy
- EHR Availability: 60% unavailability in public facilities

**Digital Infrastructure:**

- Submarine Cables: 1 (ACE, 4 years legal lifespan remaining)
- National Data Centres: 1 functional (GICTA); Gamtel DC not
  operational; no Tier 4
- Fixed Broadband: 41,612 subscribers
- Mobile Connections: 4.22 million

**Identity Systems:**

- NIN Holders: Citizens 18+ (exact number not specified)
- Birth Certificates: 1.17M+ electronic
- ID Card Status: Production suspended (contract issue)

**Digital Addressing:**

- Properties Addressed: 133,000+ (pilot + Phase 1 + Phase 2)
- Coverage: Banjul, Kanifing, West Coast Region
- Remaining: Nationwide rollout ongoing
