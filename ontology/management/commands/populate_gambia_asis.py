"""
Management command to populate the Gambia AS-IS Architecture in OpenEA.

Implements Step 4 from the OpenEA adoption plan:
  "Populate As-Is instances (ministries, apps, etc.)"

Based on:
  - D5 EA Findings Document (D5_ea-findings-BDAT-v3.md)
  - AS-IS Architecture for 4 Tier 1 Ministries

Usage:
  python manage.py populate_gambia_asis --org <organisation_name>

  If --org is not provided, defaults to 'GICTA'.

This command is idempotent - running it multiple times will not create
duplicates (uses get_or_create pattern).

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
# REPOSITORY AND MODEL NAMES
# =============================================================================
REPOSITORY_NAME = "Gambia National EA Repository"
MODEL_NAME = "Gambia National EA Metamodel"
MODEL_VERSION = "1.0"

# =============================================================================
# ORGANISATION UNITS (Tier 1 Ministries + Key Departments)
# Format: (name, code, description, parent_code or None)
# =============================================================================
ORGANISATION_UNITS = [
    # Tier 1 Ministries
    ("Ministry of Finance & Economic Affairs", "mofea",
     "Central government ministry responsible for budget, treasury, and "
     "financial management. Manages IFMIS, CBMS, TMS, HRMIS, and GamPay. "
     "Digital Maturity: High (Mature systems).",
     None),
    ("Gambia Revenue Authority", "gra",
     "Semi-autonomous revenue agency responsible for tax collection and "
     "customs. Manages GamTax Net and ASYCUDA World. "
     "Digital Maturity: High (Level 3.0 - API integration, 98% virtualised).",
     None),
    ("Ministry of Health", "moh",
     "Central government ministry responsible for health service delivery "
     "and public health. Manages DHIS2, eCRVS, e-NHIS, SPT, A-LIS. "
     "Digital Maturity: Medium (Active digital transformation).",
     None),
    ("Ministry of Communications & Digital Economy", "mocde",
     "Central government ministry responsible for ICT policy, digital "
     "infrastructure, and e-government. Leads MyGov, digital addressing, "
     "and cybersecurity initiatives. "
     "Digital Maturity: Medium (Leading transformation).",
     None),

    # MoFEA Departments
    ("Accountant General's Department", "agd",
     "Manages IFMIS, treasury operations, and government payments. "
     "18 IT professionals supporting ~2,000+ users across 50 MDAs.",
     "mofea"),
    ("Budget Directorate", "budget-dir",
     "Responsible for budget preparation, execution, and monitoring via CBMS.",
     "mofea"),
    ("Personnel Management Office", "pmo",
     "Manages 41,958 civil servants through HRMIS and Payroll modules. "
     "20 dedicated staff. Integrated with biometric attendance system.",
     "mofea"),

    # GRA Departments
    ("Domestic Tax Department", "gra-domestic",
     "Handles Income Tax (PIT, CIT), VAT, PAYE, Environment Tax, "
     "Fringe Benefits, and Rental Income Tax via GamTax Net.",
     "gra"),
    ("Customs Department", "gra-customs",
     "Handles import/export duties and customs compliance via ASYCUDA World. "
     "Operates at all border posts.",
     "gra"),
    ("GRA ICT Department", "gra-ict",
     "Manages ITAS, ASYCUDA World, and GamPay integration. "
     "Handles technical matters on API integration.",
     "gra"),

    # MoH Departments
    ("Directorate of Health Services", "dhs",
     "Clinical service delivery across 91 health facilities (public, private, "
     "not-for-profit).",
     "moh"),
    ("Directorate of Public Health Services", "dphs",
     "Disease surveillance, immunisation, health promotion. "
     "Coordinates IDSR and SPT programs.",
     "moh"),
    ("Directorate of Planning & Information", "dpi",
     "HMIS team manages DHIS2, data collection, and M&E.",
     "moh"),
    ("National Health Insurance Authority", "nhia",
     "Manages National Health Insurance Scheme (NHIS). "
     "15,734 beneficiaries as of April 2025 (target: 60,000). "
     "69 contracted facilities.",
     "moh"),

    # MoCDE Departments/Agencies
    ("Gambia ICT Agency", "gicta",
     "Technical implementation agency for digital addressing, e-government "
     "platforms, and EA governance. Holds government-wide EA mandate.",
     "mocde"),
    ("Directorate of E-Government", "e-gov-dir",
     "Manages MyGov portal development, digital services, and e-government "
     "policy.",
     "mocde"),
    ("Directorate of Cyber Security", "cyber-dir",
     "National cybersecurity coordination, NCSC, gmCSIRT operations.",
     "mocde"),

    # Other Key Agencies
    ("Central Bank of Gambia", "cbg",
     "Central bank. Co-owns GamPay payment gateway with MoFEA. "
     "Provides T24 core banking system for EFT processing.",
     None),
    ("Department of Immigration", "immigration",
     "Manages National Identification Number (NIN) through GAMBIS. "
     "Part of Ministry of Interior. Issues ID cards, driver's licenses, "
     "resident permits.",
     None),
]

# =============================================================================
# APPLICATIONS
# Format: (name, code, description, owner_code, vendor, status, tech_details)
# =============================================================================
APPLICATIONS = [
    # =========================================================================
    # MoFEA APPLICATIONS
    # =========================================================================
    ("IFMIS", "ifmis",
     "Integrated Financial Management Information System (Epicor 10). "
     "Core government financial system operational since 2014. "
     "~2,000+ users across 50 MDAs. Modules: General Ledger, AP/AR, "
     "Cash Management, Fixed Assets, Budget Execution. "
     "Integrated with CBG T24 (EFT), GamPay, CBMS, TMS.",
     "agd", "Epicor", "Operational",
     "Platform: Epicor 10, Hosting: On-premises, Integration: REST APIs"),

    ("CBMS", "cbms",
     "Central Budget Management System. Integrated with IFMIS for budget "
     "preparation, allocation, and monitoring. Supports annual budget "
     "workflows and quarterly execution monitoring.",
     "budget-dir", "Epicor", "Operational",
     "Platform: Integrated with IFMIS"),

    ("TMS", "tms",
     "Treasury Management System. Manages cash flow, Electronic Fund "
     "Transfers (EFT), and Treasury Single Account (TSA). Fully integrated "
     "with IFMIS and CBG T24.",
     "agd", "Epicor", "Operational",
     "Platform: Integrated with IFMIS, Integration: CBG T24"),

    ("HRMIS", "hrmis",
     "Human Resources Management Information System. Manages 41,958 civil "
     "servants. Modules: Employee master data, Payroll (13 pay grades), "
     "Leave management, Performance appraisal, Training records. "
     "Ghost worker detection: removed 3,146 (2017), 2,611 (2019), "
     "1,424+679 (2024).",
     "pmo", "Epicor", "Operational",
     "Platform: Recently integrated with IFMIS"),

    ("GamPay", "gampay",
     "Government Payment Gateway. Only real-time cross-ministry integration "
     "in government. Hub-and-spoke architecture. API Maturity Level 4 "
     "(highest in government). Tokenisation, SSL/TLS encryption, SOC "
     "monitoring. Cloud-hosted.",
     "agd", "Custom (CBG)", "Operational",
     "Architecture: Hub-and-spoke, Protocol: REST APIs, Hosting: Cloud"),

    ("ERMS", "erms",
     "Electronic Records Management System. Digital document storage for HR "
     "records. Deployed at 5 pilot entities (including PMO, MoFEA).",
     "pmo", "Unknown", "Pilot",
     "Function: Digital document management"),

    ("Power BI Analytics", "powerbi",
     "Microsoft Power BI analytics platform for HR and payroll data "
     "warehouse. Dashboard monitoring for various reports. Partnership "
     "between Ministry of Public Service and AGD.",
     "agd", "Microsoft", "InDevelopment",
     "Platform: Power BI, Data Sources: HRMIS, Payroll, IFMIS"),

    ("Biometric Time Attendance", "biometric-attendance",
     "Staff attendance monitoring system. 46 devices installed (target: 100). "
     "Automated salary suspension for >1 month absenteeism. Partial "
     "integration with HRMIS.",
     "pmo", "Unknown", "Operational",
     "Devices: 46 biometric scanners"),

    # =========================================================================
    # GRA APPLICATIONS
    # =========================================================================
    ("GamTax Net", "gamtax-net",
     "Integrated Tax Administration System (ITAS). Handles domestic taxes: "
     "Income Tax (PIT, CIT), VAT, PAYE, Environment Tax, Fringe Benefits, "
     "Rental Income Tax. Taxpayer registration, TIN management, tax return "
     "filing, assessment, compliance monitoring. GamPay integration "
     "(pilot only - NOT operational). No online taxpayer services.",
     "gra-domestic", "TechBiz", "Operational",
     "Database: SQL Server 2019, Platform: .NET VB.net, OS: Windows, "
     "Version: 4.0, Hosting: On-premise"),

    ("ASYCUDA World", "asycuda",
     "UNCTAD customs management system (Version 4.3.3). Import/export "
     "declaration processing at all border posts. Duty calculation, cargo "
     "tracking, risk management, trade statistics. TIN integration with "
     "GamTax Net. Connected to Gambia National Single Window (GNSW).",
     "gra-customs", "UNCTAD", "Operational",
     "Database: PostgreSQL, Platform: Java, OS: Redhat Linux 7.0, "
     "Hosting: On-premise"),

    # =========================================================================
    # MoH APPLICATIONS
    # =========================================================================
    ("DHIS2", "dhis2",
     "District Health Information System 2. Open-source health data "
     "platform deployed nationally at all health facilities. "
     "Core health data aggregation, facility-level data entry, HIV/AIDS "
     "patient management (UICs for ART), immunisation data integration "
     "with SPT, disease surveillance reporting (weekly for IDSR), "
     "data quality verification (quarterly).",
     "dpi", "HISP (Open Source)", "Operational",
     "Platform: DHIS2 Open Source, Hosting: Central HMIS team"),

    ("eCRVS", "ecrvs",
     "Electronic Civil Registration and Vital Statistics. WCC Group HERA "
     "platform. Launched August 2022. Mass registration (Aug 2022-Feb 2023): "
     "1,167,460 people registered (53.64% of population). "
     "Birth certificates with NIN and QR code. Simultaneous NHIS card "
     "issuance. eCRVS-NHIS interoperability target: August 2025.",
     "moh", "WCC Group", "Operational",
     "Platform: HERA, Features: QR code, GIS-based fraud prevention"),

    ("e-NHIS", "e-nhis",
     "National Health Insurance Scheme Digital Platform. Pilot Phase 1: "
     "July 2023 at Bundung Maternal & Child Hospital. National rollout: "
     "April 2024. 69 contracted facilities, 15,734 beneficiaries (26% of "
     "60,000 target). Electronic enrolment, claims processing "
     "(fee-for-service), 19 essential interventions (maternal/newborn focus). "
     "99.1% beneficiary satisfaction, 92.40% quality score.",
     "nhia", "Custom", "Operational",
     "Model: Fee-for-service, Facilities: 69 contracted"),

    ("SPT", "spt",
     "Smart Paper Technology for Immunisation. Shifo Foundation solution. "
     "Hybrid paper-digital: forms at point of care, regional scanning, "
     "Shifo software uploads to central system. Integration with DHIS2. "
     "374,693 children registered, 125,344 fully vaccinated, 245,316 "
     "followed up with SMS. 99% data accuracy, 60% admin time reduction.",
     "dphs", "Shifo Foundation", "Operational",
     "Technology: Hybrid paper-digital, Deployment: All 91 health facilities"),

    ("A-LIS", "alis",
     "Africa Laboratory Information System. Part of Health Laboratory "
     "Information Management System (HLIMS) Master Plan. Electronic lab "
     "test requests, result reports, patient history, supplies management.",
     "moh", "Custom", "Pilot",
     "Guidelines: Published January 2023, Target: National Public Health Labs"),

    ("EMRS", "emrs",
     "Electronic Medical Records System (MRC Unit Gambia). Custom-built for "
     "MRC Clinical Services Department. Implemented March 2015 (Phase 1 "
     "complete March 2017). Gate Clinic automation, pharmacy, inventory, "
     "in-patient, electronic patient cards, lab integration, billing.",
     "moh", "MRC Custom", "Operational",
     "Scope: MRC Clinical Services only"),

    ("IDSR", "idsr",
     "Integrated Disease Surveillance and Response - Electronic Case-Based "
     "Surveillance. Strategy adopted 2003, 3rd edition adapted 2022. "
     "Indicator-Based Surveillance at all facilities. Weekly reporting for "
     "notifiable diseases. 90% facilities have standard case definitions, "
     "88% have IDSR-trained focal person.",
     "dphs", "Custom", "Operational",
     "Type: Indicator-Based Surveillance (IBS)"),

    # =========================================================================
    # MoCDE APPLICATIONS
    # =========================================================================
    ("MyGov", "mygov",
     "Citizen Portal. Development partnership with Bangladesh a2i program. "
     "Technical implementation: OrangeBD. Active development/pilot phase "
     "(late 2025). Web and mobile (Android/iOS), multilingual (EN, FR, PT). "
     "Initial services: Birth certificate, National ID, Passport, Driver's "
     "license, Business registration. Integration with National ID, eCRVS, "
     "Immigration, GamPay planned.",
     "e-gov-dir", "OrangeBD (Bangladesh)", "InDevelopment",
     "URL: citizen-dev.gm.orangebd.com, Platform: Web + Mobile"),

    ("Government Portal", "gov-portal",
     "Gambia Government Website (gambia.gov.gm). Informational portal with "
     "ministry information, news, policy documents, links to services. "
     "Limited transactional capabilities.",
     "e-gov-dir", "GICTA", "Operational",
     "URL: gambia.gov.gm"),

    ("Digital Addressing Portal", "ndas",
     "National Digital Addressing System. Google Plus Codes with GPS/GIS. "
     "135,500 properties addressed: Pilot (2,500 Banjul), Phase 1 (33,000 "
     "Kanifing), Phase 2 (100,000 West Coast Region). Nationwide rollout "
     "ongoing. NDASC established October 2025.",
     "gicta", "Google Africa Initiative", "Operational",
     "URL: digitaladdressing.gov.gm, Technology: Google Plus Codes"),

    ("GAMBIS", "gambis",
     "Gambia Biometric Identification System. Managed by Department of "
     "Immigration. 11-digit NIN (first 6 = DOB DDMMYY). Operational since "
     "2009. Used on national ID cards, driver's licenses, resident permits. "
     "ID card production suspended (Semlex contract ended 2024).",
     "immigration", "Semlex (ended)", "Operational",
     "Format: 11-digit NIN, Coverage: Citizens 18+"),

    ("Open Data Platform", "open-data",
     "Government Open Data Strategy 2023-2026 implementation. Development "
     "partner: e-Governance Academy (eGA) via AU-EU Digital for Development "
     "Hub. Public data accessibility and transparency.",
     "gicta", "e-Governance Academy", "InDevelopment",
     "Framework: Government Open Data Strategy 2023-2026"),

    ("Gambia One", "gambia-one",
     "Blockchain-powered Digital Public Infrastructure platform. Partnership "
     "with Kalp Foundation (India). Secure data exchange, government service "
     "digitalisation, youth blockchain training, citizen data ownership.",
     "mocde", "Kalp Foundation (India)", "InDevelopment",
     "Technology: Blockchain"),

    ("NCSC", "ncsc",
     "National Cybersecurity Coordination Centre. Establishment underway as "
     "DTFA/WARDIP component. Part of $50M WARDIP program. National "
     "cybersecurity coordination and incident response.",
     "cyber-dir", "WARDIP", "InDevelopment",
     "Funding: WARDIP $50M program"),

    ("gmCSIRT", "gmcsirt",
     "Computer Security Incident Response Team. Government cybersecurity "
     "incident response. Operational under Directorate of Cyber Security.",
     "cyber-dir", "GICTA", "Operational",
     "Function: Incident response"),

    ("SOC", "soc",
     "Security Operations Centre. API security monitoring, threat detection. "
     "Coverage includes government systems and GamPay APIs.",
     "cyber-dir", "GICTA", "Operational",
     "Coverage: Government systems, GamPay APIs"),

    # =========================================================================
    # BANKING SYSTEMS
    # =========================================================================
    ("CBG T24", "cbg-t24",
     "Central Bank of Gambia Core Banking System. Temenos T24 platform. "
     "Handles Electronic Fund Transfer (EFT) from IFMIS. Integrated with "
     "GamPay for transaction settlement to commercial banks.",
     "cbg", "Temenos", "Operational",
     "Platform: Temenos T24, Function: Core banking, EFT"),
]

# =============================================================================
# TECHNOLOGY COMPONENTS
# Format: (name, code, description, type, owner_code, vendor)
# =============================================================================
TECHNOLOGY_COMPONENTS = [
    # Databases
    ("SQL Server 2019", "sqlserver-2019",
     "Microsoft SQL Server 2019 database for GamTax Net. On-premise hosting.",
     "Database", "gra", "Microsoft"),
    ("PostgreSQL Server", "postgres",
     "PostgreSQL database server for ASYCUDA World. On-premise hosting "
     "on Redhat Linux 7.0.",
     "Database", "gra", "PostgreSQL"),
    ("IFMIS Database", "ifmis-db",
     "Epicor 10 relational database for IFMIS. On-premises government "
     "data centre. Multi-year retention, role-based access (~2,000+ users).",
     "Database", "agd", "Epicor"),

    # Servers/Platforms
    ("IFMIS Server", "ifmis-server",
     "On-premises server infrastructure hosting IFMIS at government "
     "data centre.",
     "Server", "agd", "Unknown"),
    ("DHIS2 Server", "dhis2-server",
     "Server infrastructure hosting DHIS2 under central HMIS team custody.",
     "Server", "dpi", "Unknown"),
    ("GamTax Net Server", "gamtax-server",
     "On-premises Windows server hosting GamTax Net with .NET Framework.",
     "Server", "gra", "Unknown"),
    ("ASYCUDA Server", "asycuda-server",
     "On-premises Redhat Linux 7.0 server hosting ASYCUDA World Java "
     "application.",
     "Server", "gra", "Unknown"),

    # Networks
    ("ACE Submarine Cable", "ace-cable",
     "Africa-Coast-to-Europe submarine fibre optic cable. 5.12 Tbit/s "
     "capacity. At halfway point of technical lifespan (4 years legal "
     "lifespan remaining). Frequent damage and disruptions. Primary "
     "internet connectivity for The Gambia.",
     "Network", "mocde", "ACE Consortium"),
    ("Terrestrial Backup Link", "terrestrial-backup",
     "Terrestrial network backup through Senegal. Secondary connectivity "
     "option when ACE cable is disrupted.",
     "Network", "mocde", "GAMTEL"),
    ("GAMTEL Network", "gamtel-network",
     "National telecommunications network operated by GAMTEL (state "
     "telecom provider).",
     "Network", "mocde", "GAMTEL"),

    # Data Centres
    ("GAMTEL Data Centre", "gamtel-dc",
     "GAMTEL Private Cloud Data Centre. Operational. Current government "
     "hosting capacity.",
     "DataCentre", "mocde", "GAMTEL"),
    ("Government Mini Data Centre", "gov-mini-dc",
     "Government e-Government Mini Data Center. Operational. Limited "
     "capacity.",
     "DataCentre", "gicta", "GICTA"),
    ("WAIEP Data Centre", "waiep-dc",
     "West Africa Internet Exchange Point Data Center. Operational. "
     "Internet peering and data centre services.",
     "DataCentre", "mocde", "WAIEP"),
    ("Tier 4 National Data Centre", "tier4-ndc",
     "Planned Tier 4 National Data Centre. Top priority infrastructure. "
     "Target: G-Cloud platform operational by 2027. Secure hosting for "
     "public and private sector, regional hub positioning.",
     "DataCentre", "gicta", "Planned"),

    # Cloud Infrastructure
    ("GamPay Cloud", "gampay-cloud",
     "Cloud-based hosting for GamPay payment gateway. External provider. "
     "Real-time transaction logs, long-term history, tokenization, "
     "encryption.",
     "Cloud", "agd", "External Provider"),
]

# =============================================================================
# VENDORS
# Format: (name, code, description)
# =============================================================================
VENDORS = [
    ("Epicor", "epicor",
     "US-based ERP vendor. Provides IFMIS (Epicor 10) platform including "
     "financial management, budget, treasury, and HRMIS modules."),
    ("TechBiz", "techbiz",
     "Vendor for GamTax Net Integrated Tax Administration System. "
     ".NET VB.net platform."),
    ("UNCTAD", "unctad",
     "United Nations Conference on Trade and Development. Provides ASYCUDA "
     "World customs management system."),
    ("WCC Group", "wcc-group",
     "Vendor for HERA eCRVS solution for civil registration and vital "
     "statistics."),
    ("OrangeBD", "orangebd",
     "Bangladesh-based company implementing MyGov citizen portal. "
     "Partnership with Bangladesh a2i program."),
    ("Shifo Foundation", "shifo",
     "Provider of Smart Paper Technology (SPT) for immunisation tracking."),
    ("Presight", "presight",
     "UAE-based company. Partner for digital identity infrastructure and "
     "cybersecurity system development."),
    ("Google Africa Initiative", "google-africa",
     "Provides Google Plus Codes technology and support for National "
     "Digital Addressing System."),
    ("Kalp Foundation", "kalp",
     "India-based foundation. Partner for Gambia One blockchain platform "
     "development."),
    ("Microsoft", "microsoft",
     "Provider of SQL Server database and Power BI analytics platform."),
    ("Temenos", "temenos",
     "Provider of T24 core banking system used by Central Bank of Gambia."),
    ("HISP", "hisp",
     "Health Information Systems Programme. Provider of DHIS2 open-source "
     "health information system."),
    ("e-Governance Academy", "ega",
     "Estonian organization. Development partner for Open Data Platform "
     "via AU-EU Digital for Development Hub."),
    ("Semlex", "semlex",
     "Previous vendor for national ID card production (GAMBIS). Contract "
     "ended 2024."),
    ("ACE Consortium", "ace-consortium",
     "Consortium operating the Africa-Coast-to-Europe submarine cable."),
    ("GAMTEL", "gamtel",
     "State telecommunications provider. Operates national telecom "
     "infrastructure and data centre."),
]

# =============================================================================
# BUSINESS PROCESSES
# Format: (name, code, description, owner_code)
# =============================================================================
BUSINESS_PROCESSES = [
    # MoFEA Processes
    ("Budget Management", "budget-mgmt",
     "Annual budget preparation through CBMS. Quarterly budget execution "
     "monitoring. Performance-based budgeting initiatives. Budget approval "
     "workflow through National Assembly.",
     "mofea"),
    ("Financial Management", "financial-mgmt",
     "Payment processing via IFMIS. Electronic Fund Transfer (EFT) to "
     "commercial banks via CBG T24. Treasury Single Account (TSA) framework. "
     "Accounts payable/receivable management.",
     "agd"),
    ("Revenue Collection", "revenue-collection",
     "GamPay integration with GRA for tax revenue. Non-tax revenue "
     "collection (partial integration). Real-time transaction processing "
     "for government fees. Payment reconciliation and reporting.",
     "agd"),
    ("Payroll Management", "payroll-mgmt",
     "Personnel Management Office manages 41,958 civil servants. HRMIS and "
     "Payroll modules integrated with IFMIS. Biometric time attendance. "
     "Automated salary processing with ghost worker detection.",
     "pmo"),

    # GRA Processes
    ("Tax Administration", "tax-admin",
     "Taxpayer registration and TIN issuance. Tax return filing and "
     "assessment. Payment collection. Tax refund processing. Compliance "
     "monitoring and auditing.",
     "gra"),
    ("Customs Operations", "customs-ops",
     "Import/export declaration processing via ASYCUDA World at all border "
     "posts. Duty calculation and collection. Risk management and cargo "
     "inspection. Trade facilitation and single window initiatives.",
     "gra"),
    ("Revenue Management", "revenue-mgmt",
     "Daily revenue collection monitoring. Revenue forecasting and target "
     "setting. Debt management and collection. Revenue reporting to MoFEA "
     "(manual/email-based).",
     "gra"),

    # MoH Processes
    ("Health Service Delivery", "health-delivery",
     "Clinical care at 91 health facilities. Maternal and newborn health "
     "services. Disease management programs (HIV, TB, malaria, NCDs). "
     "Emergency health services. Laboratory and diagnostic services.",
     "dhs"),
    ("Public Health Programs", "public-health",
     "Immunization services (SPT for 374,693 children). Disease surveillance "
     "(IDSR weekly reporting). Health promotion and prevention. Community-"
     "based health programs (Village Health Workers).",
     "dphs"),
    ("Health Information Management", "health-info-mgmt",
     "Data collection via DHIS2 from all health facilities. Weekly disease "
     "surveillance reporting. Quarterly HMIS data verification. Monthly "
     "facility reporting.",
     "dpi"),
    ("Health Insurance Operations", "health-insurance",
     "NHIS enrolment (15,734 beneficiaries). Electronic claims processing "
     "via e-NHIS. Fee-for-service reimbursement to 69 contracted facilities. "
     "19 essential health interventions.",
     "nhia"),
    ("Birth Registration", "birth-reg",
     "Mass registration campaign (Aug 2022-Feb 2023): 1,167,460 people. "
     "Electronic birth certificates with NIN and QR code. Simultaneous "
     "health insurance card issuance. 53.64% population registered.",
     "moh"),

    # MoCDE Processes
    ("E-Government Development", "e-gov-dev",
     "MyGov citizen portal development (Bangladesh partnership). Digital "
     "service design and delivery. Government website management. Service "
     "Process Simplification. Training of 25 officials (Feb 2025).",
     "e-gov-dir"),
    ("Digital Infrastructure Management", "digital-infra",
     "National broadband network expansion. Second submarine cable project "
     "($30-35M). National Data Centre establishment (Tier 4 planned). "
     "Digital addressing system (133,000+ properties).",
     "gicta"),
    ("Digital Policy & Regulation", "digital-policy",
     "Digital Economy Master Plan 2024-2034 implementation. ICT sector "
     "regulation and licensing. Data protection framework development. "
     "Universal access and digital inclusion programs.",
     "mocde"),
    ("Cybersecurity Coordination", "cybersecurity",
     "NCSC establishment underway. gmCSIRT operations. Cyber Security Bill "
     "formulation. Government systems security monitoring via SOC.",
     "cyber-dir"),
    ("Digital Public Infrastructure Coordination", "dpi-coord",
     "DTFA/WARDIP program coordination ($50M). Digital identity strategy "
     "(Presight partnership). National addressing system rollout. "
     "Blockchain platform development (Kalp Foundation). Open Data Platform.",
     "gicta"),
]

# =============================================================================
# BUSINESS SERVICES
# Format: (name, code, description, owner_code)
# =============================================================================
BUSINESS_SERVICES = [
    ("Tax Filing Service", "tax-filing",
     "Taxpayer registration, TIN issuance, and tax return submission. "
     "Handled by GRA Domestic Tax Department via GamTax Net.",
     "gra"),
    ("Customs Declaration Service", "customs-declaration",
     "Electronic import/export declaration submission via ASYCUDA World. "
     "Available online for customs agents and importers/exporters.",
     "gra"),
    ("Government Payment Service", "gov-payment",
     "Real-time payment processing for government fees and taxes via "
     "GamPay. Multi-channel (online, mobile, POS).",
     "agd"),
    ("Birth Certificate Service", "birth-cert",
     "Electronic birth registration and certificate issuance via eCRVS. "
     "Includes NIN and QR code. Mass registration achieved 53.64% coverage.",
     "moh"),
    ("Health Insurance Enrollment", "nhis-enrollment",
     "Electronic enrollment in National Health Insurance Scheme. Access "
     "via NHIS card or electronic birth certificate. 19 essential "
     "interventions covered.",
     "nhia"),
    ("Immunization Service", "immunization",
     "Childhood immunization tracking via Smart Paper Technology. SMS "
     "follow-up for missed appointments. 374,693 children registered.",
     "dphs"),
    ("Digital Address Service", "digital-address",
     "Unique digital address assignment for properties using Google Plus "
     "Codes. 135,500 properties addressed nationwide.",
     "gicta"),
]

# =============================================================================
# CAPABILITIES
# Format: (name, code, description)
# =============================================================================
CAPABILITIES = [
    ("Financial Management", "cap-financial",
     "Ability to manage government finances including budgeting, treasury, "
     "payments, and financial reporting."),
    ("Revenue Collection", "cap-revenue",
     "Ability to collect tax and non-tax revenue through integrated "
     "payment channels."),
    ("Human Resource Management", "cap-hrm",
     "Ability to manage civil service workforce including payroll, "
     "attendance, and performance."),
    ("Customs Administration", "cap-customs",
     "Ability to process customs declarations, calculate duties, and "
     "facilitate trade."),
    ("Health Information Management", "cap-health-info",
     "Ability to collect, aggregate, and analyse health data from "
     "facilities nationwide."),
    ("Civil Registration", "cap-civil-reg",
     "Ability to register births, deaths, marriages, and issue official "
     "certificates."),
    ("Health Insurance Administration", "cap-health-insurance",
     "Ability to enroll beneficiaries and process health insurance claims."),
    ("Disease Surveillance", "cap-surveillance",
     "Ability to detect, monitor, and respond to disease outbreaks."),
    ("Digital Service Delivery", "cap-digital-service",
     "Ability to deliver government services through digital channels."),
    ("Digital Identity", "cap-digital-id",
     "Ability to issue and verify digital identities for citizens."),
    ("Cybersecurity", "cap-cybersecurity",
     "Ability to protect government systems and respond to cyber incidents."),
    ("Digital Infrastructure", "cap-digital-infra",
     "Ability to provide connectivity and hosting infrastructure."),
]

# =============================================================================
# DATA ENTITIES
# Format: (name, code, description, type, owner_code)
# type: Master, Reference, Transactional
# =============================================================================
DATA_ENTITIES = [
    ("Taxpayer Record", "de-taxpayer",
     "Taxpayer registration data including TIN, tax returns, assessments, "
     "payments, refunds, and compliance history.",
     "Master", "gra"),
    ("Financial Transaction", "de-fin-txn",
     "Government financial transactions including payments, receipts, "
     "budget allocations, commitments, and expenditures.",
     "Transactional", "agd"),
    ("Employee Record", "de-employee",
     "Civil servant master data including payroll, leave, performance, "
     "training, and attendance records. 41,958 records.",
     "Master", "pmo"),
    ("Health Record", "de-health",
     "Aggregate health data from facilities including disease surveillance, "
     "immunisation, and service delivery statistics.",
     "Transactional", "dpi"),
    ("Birth Registration Record", "de-birth-reg",
     "Civil registration data for births including NIN, certificate number, "
     "QR code. 1.17M+ records.",
     "Master", "moh"),
    ("NHIS Beneficiary Record", "de-nhis",
     "Health insurance enrollment and claims data. 15,734 beneficiaries.",
     "Master", "nhia"),
    ("Customs Declaration", "de-customs",
     "Import/export declaration data including tariffs, duties, cargo "
     "tracking, and clearance records.",
     "Transactional", "gra"),
    ("Payment Transaction", "de-payment",
     "GamPay payment transaction records including real-time logs, "
     "settlements, and reconciliation data.",
     "Transactional", "agd"),
    ("National ID Record", "de-nid",
     "Citizen identification data including 11-digit NIN, biometric data, "
     "ID card issuance records.",
     "Master", "immigration"),
    ("Digital Address", "de-digital-addr",
     "Property digital address data including Plus Code, GPS coordinates, "
     "administrative location, and property classification. 135,500 records.",
     "Master", "gicta"),
]

# =============================================================================
# PROJECTS
# Format: (name, code, description, owner_code, funding_source, status)
# =============================================================================
PROJECTS = [
    ("DTFA/WARDIP", "wardip",
     "Digital Transformation for Africa / Western Africa Regional Digital "
     "Integration Program. $50M World Bank IDA funding. Components: "
     "Connectivity, Digital Market Development, Online Services, "
     "Cybersecurity. GICTA operationalisation, NCSC procurement, digital "
     "addressing rollout, MyGov development.",
     "mocde", "World Bank IDA ($50M)", "InProgress"),
    ("GEHSSP", "gehssp",
     "Gambia Essential Health Services Strengthening Project. $119.5M "
     "World Bank funding for health sector. Supports NHIS expansion, "
     "health system strengthening.",
     "moh", "World Bank IDA ($119.5M)", "InProgress"),
    ("Second Submarine Cable", "submarine-cable-2",
     "Second submarine cable deployment to reduce single point of failure. "
     "$30-35M World Bank allocation. Enhanced digital sovereignty and "
     "redundancy for ACE cable.",
     "mocde", "World Bank ($30-35M)", "Planned"),
    ("MyGov Development", "mygov-project",
     "Citizen portal development with Bangladesh a2i partnership. Technical "
     "implementation by OrangeBD. Initial 5 priority services. Training of "
     "25 government officials completed February 2025.",
     "e-gov-dir", "UNDP/WARDIP", "InProgress"),
    ("National Digital Addressing", "ndas-project",
     "Nationwide digital addressing system rollout. 135,500 properties "
     "addressed. Partnership with Google Africa Initiative. NDASC "
     "established October 2025.",
     "gicta", "WARDIP", "InProgress"),
    ("Tier 4 Data Centre", "tier4-dc-project",
     "National Tier 4 Data Centre establishment. Top priority infrastructure "
     "project. Target: G-Cloud platform operational by 2027.",
     "gicta", "Government/WARDIP", "Planned"),
    ("eCRVS-NHIS Integration", "ecrvs-nhis-integration",
     "Interoperability between eCRVS birth registration and NHIS health "
     "insurance systems. Target completion: August 2025.",
     "moh", "GEHSSP", "InProgress"),
    ("National ID Unification", "nid-unification",
     "Unified National Identification System from birth to death. "
     "Integration between NHIA, MoCDE, and GICTA. Coverage of Gambians "
     "and legal residents.",
     "mocde", "Government", "Planned"),
    ("GRA-IFMIS Integration", "gra-ifmis-integration",
     "Real-time revenue data integration between GRA systems and IFMIS. "
     "Critical gap requiring resolution. Currently manual/email-based.",
     "gra", "Government", "Planned"),
    ("Power BI Analytics", "powerbi-project",
     "Development of HR and payroll data warehouse with Microsoft Power BI. "
     "Dashboard monitoring and advanced analytics. Partnership between "
     "Ministry of Public Service and AGD.",
     "pmo", "Government", "InProgress"),
]

# =============================================================================
# RELATIONSHIPS (SLOTS)
# Format: (subject_concept, relation, object_concept, subject_code, object_code)
# =============================================================================
SLOTS = [
    # Application supports BusinessProcess
    ("Application", "supports", "BusinessProcess", "ifmis", "financial-mgmt"),
    ("Application", "supports", "BusinessProcess", "ifmis", "budget-mgmt"),
    ("Application", "supports", "BusinessProcess", "cbms", "budget-mgmt"),
    ("Application", "supports", "BusinessProcess", "tms", "financial-mgmt"),
    ("Application", "supports", "BusinessProcess", "hrmis", "payroll-mgmt"),
    ("Application", "supports", "BusinessProcess", "gampay", "revenue-collection"),
    ("Application", "supports", "BusinessProcess", "gampay", "financial-mgmt"),
    ("Application", "supports", "BusinessProcess", "gamtax-net", "tax-admin"),
    ("Application", "supports", "BusinessProcess", "asycuda", "customs-ops"),
    ("Application", "supports", "BusinessProcess", "asycuda", "revenue-mgmt"),
    ("Application", "supports", "BusinessProcess", "dhis2", "health-info-mgmt"),
    ("Application", "supports", "BusinessProcess", "dhis2", "public-health"),
    ("Application", "supports", "BusinessProcess", "ecrvs", "birth-reg"),
    ("Application", "supports", "BusinessProcess", "e-nhis", "health-insurance"),
    ("Application", "supports", "BusinessProcess", "spt", "public-health"),
    ("Application", "supports", "BusinessProcess", "idsr", "public-health"),
    ("Application", "supports", "BusinessProcess", "mygov", "e-gov-dev"),
    ("Application", "supports", "BusinessProcess", "ndas", "digital-infra"),
    ("Application", "supports", "BusinessProcess", "gambis", "birth-reg"),
    ("Application", "supports", "BusinessProcess", "ncsc", "cybersecurity"),
    ("Application", "supports", "BusinessProcess", "gmcsirt", "cybersecurity"),
    ("Application", "supports", "BusinessProcess", "soc", "cybersecurity"),

    # Application ownedBy OrganisationUnit
    ("Application", "ownedBy", "OrganisationUnit", "ifmis", "agd"),
    ("Application", "ownedBy", "OrganisationUnit", "cbms", "budget-dir"),
    ("Application", "ownedBy", "OrganisationUnit", "tms", "agd"),
    ("Application", "ownedBy", "OrganisationUnit", "hrmis", "pmo"),
    ("Application", "ownedBy", "OrganisationUnit", "gampay", "agd"),
    ("Application", "ownedBy", "OrganisationUnit", "erms", "pmo"),
    ("Application", "ownedBy", "OrganisationUnit", "powerbi", "agd"),
    ("Application", "ownedBy", "OrganisationUnit", "biometric-attendance", "pmo"),
    ("Application", "ownedBy", "OrganisationUnit", "gamtax-net", "gra-domestic"),
    ("Application", "ownedBy", "OrganisationUnit", "asycuda", "gra-customs"),
    ("Application", "ownedBy", "OrganisationUnit", "dhis2", "dpi"),
    ("Application", "ownedBy", "OrganisationUnit", "ecrvs", "moh"),
    ("Application", "ownedBy", "OrganisationUnit", "e-nhis", "nhia"),
    ("Application", "ownedBy", "OrganisationUnit", "spt", "dphs"),
    ("Application", "ownedBy", "OrganisationUnit", "alis", "moh"),
    ("Application", "ownedBy", "OrganisationUnit", "emrs", "moh"),
    ("Application", "ownedBy", "OrganisationUnit", "idsr", "dphs"),
    ("Application", "ownedBy", "OrganisationUnit", "mygov", "e-gov-dir"),
    ("Application", "ownedBy", "OrganisationUnit", "gov-portal", "e-gov-dir"),
    ("Application", "ownedBy", "OrganisationUnit", "ndas", "gicta"),
    ("Application", "ownedBy", "OrganisationUnit", "gambis", "immigration"),
    ("Application", "ownedBy", "OrganisationUnit", "open-data", "gicta"),
    ("Application", "ownedBy", "OrganisationUnit", "gambia-one", "mocde"),
    ("Application", "ownedBy", "OrganisationUnit", "ncsc", "cyber-dir"),
    ("Application", "ownedBy", "OrganisationUnit", "gmcsirt", "cyber-dir"),
    ("Application", "ownedBy", "OrganisationUnit", "soc", "cyber-dir"),
    ("Application", "ownedBy", "OrganisationUnit", "cbg-t24", "cbg"),

    # Application manages DataEntity
    ("Application", "manages", "DataEntity", "ifmis", "de-fin-txn"),
    ("Application", "manages", "DataEntity", "hrmis", "de-employee"),
    ("Application", "manages", "DataEntity", "gampay", "de-payment"),
    ("Application", "manages", "DataEntity", "gamtax-net", "de-taxpayer"),
    ("Application", "manages", "DataEntity", "asycuda", "de-customs"),
    ("Application", "manages", "DataEntity", "dhis2", "de-health"),
    ("Application", "manages", "DataEntity", "ecrvs", "de-birth-reg"),
    ("Application", "manages", "DataEntity", "e-nhis", "de-nhis"),
    ("Application", "manages", "DataEntity", "gambis", "de-nid"),
    ("Application", "manages", "DataEntity", "ndas", "de-digital-addr"),

    # TechnologyComponent suppliedBy Vendor
    ("TechnologyComponent", "suppliedBy", "Vendor", "sqlserver-2019", "microsoft"),
    ("TechnologyComponent", "suppliedBy", "Vendor", "postgres", "unctad"),
    ("TechnologyComponent", "suppliedBy", "Vendor", "ifmis-db", "epicor"),
    ("TechnologyComponent", "suppliedBy", "Vendor", "ace-cable", "ace-consortium"),
    ("TechnologyComponent", "suppliedBy", "Vendor", "terrestrial-backup", "gamtel"),
    ("TechnologyComponent", "suppliedBy", "Vendor", "gamtel-network", "gamtel"),
    ("TechnologyComponent", "suppliedBy", "Vendor", "gamtel-dc", "gamtel"),

    # Application dependsOn Application
    ("Application", "dependsOn", "Application", "cbms", "ifmis"),
    ("Application", "dependsOn", "Application", "tms", "ifmis"),
    ("Application", "dependsOn", "Application", "hrmis", "ifmis"),
    ("Application", "dependsOn", "Application", "ifmis", "gampay"),
    ("Application", "dependsOn", "Application", "ifmis", "cbg-t24"),
    ("Application", "dependsOn", "Application", "gamtax-net", "gampay"),
    ("Application", "dependsOn", "Application", "asycuda", "gampay"),
    ("Application", "dependsOn", "Application", "spt", "dhis2"),
    ("Application", "dependsOn", "Application", "idsr", "dhis2"),
    ("Application", "dependsOn", "Application", "mygov", "gambis"),
    ("Application", "dependsOn", "Application", "mygov", "ecrvs"),
    ("Application", "dependsOn", "Application", "mygov", "gampay"),

    # BusinessProcess realizes Capability
    ("BusinessProcess", "realizes", "Capability", "financial-mgmt", "cap-financial"),
    ("BusinessProcess", "realizes", "Capability", "budget-mgmt", "cap-financial"),
    ("BusinessProcess", "realizes", "Capability", "revenue-collection", "cap-revenue"),
    ("BusinessProcess", "realizes", "Capability", "payroll-mgmt", "cap-hrm"),
    ("BusinessProcess", "realizes", "Capability", "tax-admin", "cap-revenue"),
    ("BusinessProcess", "realizes", "Capability", "customs-ops", "cap-customs"),
    ("BusinessProcess", "realizes", "Capability", "health-info-mgmt", "cap-health-info"),
    ("BusinessProcess", "realizes", "Capability", "birth-reg", "cap-civil-reg"),
    ("BusinessProcess", "realizes", "Capability", "health-insurance", "cap-health-insurance"),
    ("BusinessProcess", "realizes", "Capability", "public-health", "cap-surveillance"),
    ("BusinessProcess", "realizes", "Capability", "e-gov-dev", "cap-digital-service"),
    ("BusinessProcess", "realizes", "Capability", "digital-infra", "cap-digital-infra"),
    ("BusinessProcess", "realizes", "Capability", "cybersecurity", "cap-cybersecurity"),

    # OrganisationUnit contains OrganisationUnit (hierarchy)
    ("OrganisationUnit", "contains", "OrganisationUnit", "mofea", "agd"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "mofea", "budget-dir"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "mofea", "pmo"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "gra", "gra-domestic"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "gra", "gra-customs"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "gra", "gra-ict"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "moh", "dhs"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "moh", "dphs"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "moh", "dpi"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "moh", "nhia"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "mocde", "gicta"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "mocde", "e-gov-dir"),
    ("OrganisationUnit", "contains", "OrganisationUnit", "mocde", "cyber-dir"),

    # Project delivers Application
    ("Project", "delivers", "Application", "mygov-project", "mygov"),
    ("Project", "delivers", "Application", "ndas-project", "ndas"),
    ("Project", "delivers", "Application", "wardip", "ncsc"),
    ("Project", "delivers", "Application", "wardip", "open-data"),
    ("Project", "delivers", "Application", "powerbi-project", "powerbi"),

    # Project implements Initiative (projects implement WARDIP)
    ("Project", "implements", "Project", "mygov-project", "wardip"),
    ("Project", "implements", "Project", "ndas-project", "wardip"),
    ("Project", "implements", "Project", "tier4-dc-project", "wardip"),
    ("Project", "implements", "Project", "submarine-cable-2", "wardip"),
    ("Project", "implements", "Project", "ecrvs-nhis-integration", "gehssp"),

    # DataEntity ownedBy OrganisationUnit
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-taxpayer", "gra"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-fin-txn", "agd"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-employee", "pmo"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-health", "dpi"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-birth-reg", "moh"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-nhis", "nhia"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-customs", "gra"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-payment", "agd"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-nid", "immigration"),
    ("DataEntity", "ownedBy", "OrganisationUnit", "de-digital-addr", "gicta"),

    # Capability ownedBy OrganisationUnit
    ("Capability", "ownedBy", "OrganisationUnit", "cap-financial", "mofea"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-revenue", "gra"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-hrm", "pmo"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-customs", "gra"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-health-info", "moh"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-civil-reg", "moh"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-health-insurance", "nhia"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-surveillance", "moh"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-digital-service", "mocde"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-digital-id", "mocde"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-cybersecurity", "mocde"),
    ("Capability", "ownedBy", "OrganisationUnit", "cap-digital-infra", "mocde"),

    # BusinessService serves Customer (implied)
    ("BusinessService", "realizes", "BusinessProcess", "tax-filing", "tax-admin"),
    ("BusinessService", "realizes", "BusinessProcess", "customs-declaration", "customs-ops"),
    ("BusinessService", "realizes", "BusinessProcess", "gov-payment", "revenue-collection"),
    ("BusinessService", "realizes", "BusinessProcess", "birth-cert", "birth-reg"),
    ("BusinessService", "realizes", "BusinessProcess", "nhis-enrollment", "health-insurance"),
    ("BusinessService", "realizes", "BusinessProcess", "immunization", "public-health"),
    ("BusinessService", "realizes", "BusinessProcess", "digital-address", "digital-infra"),
]


class Command(BaseCommand):
    help = (
        "Populate the Gambia AS-IS Architecture in OpenEA. "
        "Creates instances for: OrganisationUnits (20+), Applications (30+), "
        "TechnologyComponents (15+), Vendors (15+), BusinessProcesses (15+), "
        "BusinessServices (7), Capabilities (12), DataEntities (10), "
        "Projects (10), and their relationships. "
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
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Print detailed output for each item created.',
        )

    def handle(self, *args, **options):
        org_name = options['org']
        dry_run = options['dry_run']
        verbose = options['verbose']

        # Resolve organisation
        try:
            organisation = Organisation.objects.get(name=org_name)
        except Organisation.DoesNotExist:
            raise CommandError(
                f"Organisation '{org_name}' not found. "
                f"Create it first with: python manage.py create_organisation "
                f"{org_name} --users <username>"
            )

        # Find repository and model
        try:
            repository = Repository.objects.get(
                name=REPOSITORY_NAME,
                organisation=organisation
            )
        except Repository.DoesNotExist:
            raise CommandError(
                f"Repository '{REPOSITORY_NAME}' not found. "
                f"Run 'python manage.py populate_gambia_metamodel --org {org_name}' "
                f"first to create the metamodel."
            )

        try:
            model = OModel.objects.get(
                name=MODEL_NAME,
                version=MODEL_VERSION,
                repository=repository
            )
        except OModel.DoesNotExist:
            raise CommandError(
                f"Model '{MODEL_NAME}' v{MODEL_VERSION} not found. "
                f"Run 'python manage.py populate_gambia_metamodel --org {org_name}' "
                f"first to create the metamodel."
            )

        if dry_run:
            self._print_plan()
            return

        with transaction.atomic():
            # Load concept map
            concept_map = {}
            for concept in OConcept.objects.filter(model=model):
                concept_map[concept.name] = concept

            # Verify required concepts exist
            required_concepts = [
                'OrganisationUnit', 'Application', 'TechnologyComponent',
                'Vendor', 'BusinessProcess', 'BusinessService', 'Capability',
                'DataEntity', 'Project'
            ]
            missing = [c for c in required_concepts if c not in concept_map]
            if missing:
                raise CommandError(
                    f"Missing concepts in metamodel: {missing}. "
                    f"Run 'python manage.py populate_gambia_metamodel' first."
                )

            # Create instances
            instance_map = {}
            counts = {
                'OrganisationUnit': 0, 'Application': 0,
                'TechnologyComponent': 0, 'Vendor': 0,
                'BusinessProcess': 0, 'BusinessService': 0,
                'Capability': 0, 'DataEntity': 0, 'Project': 0
            }

            # 1. Create Organisation Units
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 1: Organisation Units ==="
            ))
            for name, code, desc, parent_code in ORGANISATION_UNITS:
                instance, created = self._create_instance(
                    model, organisation, concept_map['OrganisationUnit'],
                    name, code, desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['OrganisationUnit'] += 1

            # 2. Create Vendors
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 2: Vendors ==="
            ))
            for name, code, desc in VENDORS:
                instance, created = self._create_instance(
                    model, organisation, concept_map['Vendor'],
                    name, code, desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['Vendor'] += 1

            # 3. Create Technology Components
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 3: Technology Components ==="
            ))
            for name, code, desc, tc_type, owner, vendor in TECHNOLOGY_COMPONENTS:
                full_desc = f"{desc}\nType: {tc_type}"
                instance, created = self._create_instance(
                    model, organisation, concept_map['TechnologyComponent'],
                    name, code, full_desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['TechnologyComponent'] += 1

            # 4. Create Applications
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 4: Applications ==="
            ))
            for name, code, desc, owner, vendor, status, tech in APPLICATIONS:
                full_desc = f"{desc}\n\nVendor: {vendor}\nStatus: {status}\n{tech}"
                instance, created = self._create_instance(
                    model, organisation, concept_map['Application'],
                    name, code, full_desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['Application'] += 1

            # 5. Create Business Processes
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 5: Business Processes ==="
            ))
            for name, code, desc, owner in BUSINESS_PROCESSES:
                instance, created = self._create_instance(
                    model, organisation, concept_map['BusinessProcess'],
                    name, code, desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['BusinessProcess'] += 1

            # 6. Create Business Services
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 6: Business Services ==="
            ))
            for name, code, desc, owner in BUSINESS_SERVICES:
                instance, created = self._create_instance(
                    model, organisation, concept_map['BusinessService'],
                    name, code, desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['BusinessService'] += 1

            # 7. Create Capabilities
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 7: Capabilities ==="
            ))
            for name, code, desc in CAPABILITIES:
                instance, created = self._create_instance(
                    model, organisation, concept_map['Capability'],
                    name, code, desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['Capability'] += 1

            # 8. Create Data Entities
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 8: Data Entities ==="
            ))
            for name, code, desc, de_type, owner in DATA_ENTITIES:
                full_desc = f"{desc}\nType: {de_type}"
                instance, created = self._create_instance(
                    model, organisation, concept_map['DataEntity'],
                    name, code, full_desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['DataEntity'] += 1

            # 9. Create Projects
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 9: Projects ==="
            ))
            for name, code, desc, owner, funding, status in PROJECTS:
                full_desc = f"{desc}\n\nFunding: {funding}\nStatus: {status}"
                instance, created = self._create_instance(
                    model, organisation, concept_map['Project'],
                    name, code, full_desc, verbose
                )
                instance_map[code] = instance
                if created:
                    counts['Project'] += 1

            # 10. Create Relationships (Slots)
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n=== Step 10: Relationships (Slots) ==="
            ))
            slot_count = 0
            slot_created = 0
            slot_skipped = 0

            # Build predicate lookup map: (subject_concept, relation_name, object_concept) -> predicate
            predicate_map = {}
            for predicate in OPredicate.objects.filter(model=model):
                key = (predicate.subject.name, predicate.relation.name, predicate.object.name)
                predicate_map[key] = predicate

            for subj_concept, rel_name, obj_concept, subj_code, obj_code in SLOTS:
                subject = instance_map.get(subj_code)
                obj = instance_map.get(obj_code)

                if not subject:
                    if verbose:
                        self.stderr.write(
                            f"  WARNING: Subject '{subj_code}' not found, skipping."
                        )
                    slot_skipped += 1
                    continue
                if not obj:
                    if verbose:
                        self.stderr.write(
                            f"  WARNING: Object '{obj_code}' not found, skipping."
                        )
                    slot_skipped += 1
                    continue

                # Look up the predicate
                predicate_key = (subj_concept, rel_name, obj_concept)
                predicate = predicate_map.get(predicate_key)
                if not predicate:
                    if verbose:
                        self.stderr.write(
                            f"  WARNING: Predicate '{subj_concept} {rel_name} {obj_concept}' "
                            f"not found, skipping slot."
                        )
                    slot_skipped += 1
                    continue

                slot, created = OSlot.objects.get_or_create(
                    subject=subject,
                    predicate=predicate,
                    object=obj,
                    model=model,
                    organisation=organisation,
                    defaults={
                        'name': rel_name,
                        'description': f"{subject.name} {rel_name} {obj.name}"
                    }
                )
                slot_count += 1
                if created:
                    slot_created += 1
                    if verbose:
                        self.stdout.write(self.style.SUCCESS(
                            f"  + {subject.name} → {rel_name} → {obj.name}"
                        ))

            # Summary
            self.stdout.write(self.style.MIGRATE_HEADING(
                "\n" + "=" * 60
            ))
            self.stdout.write(self.style.MIGRATE_HEADING(
                "  SUMMARY: AS-IS Architecture Population"
            ))
            self.stdout.write(self.style.MIGRATE_HEADING(
                "=" * 60
            ))
            self.stdout.write(f"  Repository     : {REPOSITORY_NAME}")
            self.stdout.write(f"  Model          : {MODEL_NAME} v{MODEL_VERSION}")
            self.stdout.write("")
            self.stdout.write("  Instances Created:")
            total_instances = sum(counts.values())
            for concept_name, count in counts.items():
                self.stdout.write(f"    {concept_name:20s}: {count}")
            self.stdout.write(f"    {'TOTAL':20s}: {total_instances}")
            self.stdout.write("")
            self.stdout.write(f"  Relationships  : {slot_count} processed "
                            f"({slot_created} new, {slot_skipped} skipped)")
            self.stdout.write("")

            self.stdout.write(self.style.SUCCESS(
                "\nGambia AS-IS Architecture populated successfully!\n"
            ))
            self.stdout.write(
                "Next steps:\n"
                "  1. Open OpenEA and navigate to the repository.\n"
                "  2. View the instance lists for each concept type.\n"
                "  3. Explore the graph visualization to see relationships.\n"
                "  4. Run impact analysis on key applications (IFMIS, GamPay, DHIS2).\n"
            )

    def _create_instance(self, model, organisation, concept, name, code,
                        description, verbose):
        """Create or update an instance."""
        instance, created = OInstance.objects.get_or_create(
            name=name,
            concept=concept,
            model=model,
            organisation=organisation,
            defaults={'description': description}
        )
        if not created:
            instance.description = description
            instance.save()
        if verbose:
            status = "+" if created else "·"
            self.stdout.write(f"  {status} [{concept.name}] {name}")
        return instance, created

    def _print_plan(self):
        """Print what would be created in dry-run mode."""
        self.stdout.write(self.style.MIGRATE_HEADING(
            "\n=== DRY RUN: Gambia AS-IS Architecture ===\n"
        ))

        self.stdout.write(f"Repository: {REPOSITORY_NAME}")
        self.stdout.write(f"Model: {MODEL_NAME} v{MODEL_VERSION}\n")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"Organisation Units ({len(ORGANISATION_UNITS)}):"
        ))
        for name, code, desc, parent in ORGANISATION_UNITS:
            parent_str = f" (→ {parent})" if parent else ""
            self.stdout.write(f"  - {name}{parent_str}")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nApplications ({len(APPLICATIONS)}):"
        ))
        for name, code, desc, owner, vendor, status, tech in APPLICATIONS:
            self.stdout.write(f"  - {name} [{status}] ({vendor})")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nTechnology Components ({len(TECHNOLOGY_COMPONENTS)}):"
        ))
        for name, code, desc, tc_type, owner, vendor in TECHNOLOGY_COMPONENTS:
            self.stdout.write(f"  - {name} [{tc_type}]")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nVendors ({len(VENDORS)}):"
        ))
        for name, code, desc in VENDORS:
            self.stdout.write(f"  - {name}")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nBusiness Processes ({len(BUSINESS_PROCESSES)}):"
        ))
        for name, code, desc, owner in BUSINESS_PROCESSES:
            self.stdout.write(f"  - {name}")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nBusiness Services ({len(BUSINESS_SERVICES)}):"
        ))
        for name, code, desc, owner in BUSINESS_SERVICES:
            self.stdout.write(f"  - {name}")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nCapabilities ({len(CAPABILITIES)}):"
        ))
        for name, code, desc in CAPABILITIES:
            self.stdout.write(f"  - {name}")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nData Entities ({len(DATA_ENTITIES)}):"
        ))
        for name, code, desc, de_type, owner in DATA_ENTITIES:
            self.stdout.write(f"  - {name} [{de_type}]")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nProjects ({len(PROJECTS)}):"
        ))
        for name, code, desc, owner, funding, status in PROJECTS:
            self.stdout.write(f"  - {name} [{status}]")

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\nRelationships ({len(SLOTS)}):"
        ))
        rel_counts = {}
        for subj_concept, rel, obj_concept, subj, obj in SLOTS:
            key = f"{subj_concept} → {rel} → {obj_concept}"
            rel_counts[key] = rel_counts.get(key, 0) + 1
        for key, count in sorted(rel_counts.items()):
            self.stdout.write(f"  - {key}: {count}")

        total = (len(ORGANISATION_UNITS) + len(APPLICATIONS) +
                len(TECHNOLOGY_COMPONENTS) + len(VENDORS) +
                len(BUSINESS_PROCESSES) + len(BUSINESS_SERVICES) +
                len(CAPABILITIES) + len(DATA_ENTITIES) + len(PROJECTS))

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"\n  TOTALS: {total} instances, {len(SLOTS)} relationships\n"
        ))
