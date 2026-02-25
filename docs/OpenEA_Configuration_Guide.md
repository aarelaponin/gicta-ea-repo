# OpenEA Configuration Guide

This guide provides comprehensive documentation of all configurable features and capabilities in the OpenEA Enterprise Architecture tool.

---

## 1. System Configuration

### 1.1 config.ini - Core Settings

**Location:** `config.ini` (project root)

#### DEFAULT Section
| Setting | Description | Example |
|---------|-------------|---------|
| `ENVIRONMENT` | Deployment environment | `dev` or `prod` |
| `SECRET_KEY` | Django secret key for cryptography | `secret_key_of_love` |
| `DEBUG` | Debug mode | `1` (on) or `0` (off) |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `CONTACT_EMAIL` | System contact email | `email@email.com` |
| `DOMAIN_URL` | Application base URL | `http://localhost:8000/` |
| `DEFAULT_CURRENCY` | Default currency code | `CAD` |

#### Database Section
| Setting | Description | Example |
|---------|-------------|---------|
| `SQL_ENGINE` | Database backend | `django.db.backends.sqlite3` or `django.db.backends.postgresql` |
| `SQL_DATABASE` | Database name/path | `db.sqlite3` |
| `SQL_USER` | Database username | `user` |
| `SQL_PASSWORD` | Database password | `password` |
| `SQL_HOST` | Database host | `localhost` |
| `SQL_PORT` | Database port | `5432` |

#### Graph Section
| Setting | Description | Default |
|---------|-------------|---------|
| `MAX_GRAPH_NODES` | Maximum nodes in visualization | `50` |
| `MAX_LENGTH_GRAPH_NODE_TEXT` | Character limit for node labels | `30` |

#### Email Section
| Setting | Description | Default |
|---------|-------------|---------|
| `EMAIL_BACKEND` | Email backend class | `django.core.mail.backends.smtp.EmailBackend` |
| `EMAIL_HOST` | SMTP server address | `localhost` |
| `EMAIL_PORT` | SMTP port | `25` |
| `EMAIL_HOST_USER` | SMTP username | |
| `EMAIL_HOST_PASSWORD` | SMTP password | |
| `EMAIL_USE_TLS` | Use TLS | `1` or `0` |
| `EMAIL_USE_SSL` | Use SSL | `1` or `0` |

### 1.2 Django Settings

**Location:** `openea/settings.py`

Key configurable items:
- **Internationalization:** 9 languages supported (EN, FR, ES, DE, JA, PT, RU, SW, ZH)
- **REST Framework:** 100 items per page, JWT token lifetime 1 hour
- **Caching:** Local memory cache (can be switched to Redis)

---

## 2. Core Ontology System

### 2.1 Data Model Hierarchy

```
Organisation
  └── Repository
        └── OModel (versioned)
              ├── OConcept (entity types)
              ├── ORelation (relationship types)
              ├── OPredicate (concept-relation-concept rules)
              ├── OInstance (actual data)
              │     └── OSlot (property values)
              └── OReport (custom reports)
```

### 2.2 Model Descriptions

| Model | Purpose | Key Fields |
|-------|---------|------------|
| **Repository** | Container for models | name, description, organisation |
| **OModel** | Versioned metamodel | name, version, description, repository |
| **OConcept** | Entity type definition | name, description, quality_status |
| **ORelation** | Relationship type | name, description, type (Property/Inheritance) |
| **OPredicate** | Rule connecting concepts | subject, relation, object, cardinality_min/max |
| **OInstance** | Actual data record | name, code, description, concept |
| **OSlot** | Property value | subject, object, predicate, value |
| **OReport** | Custom report | name, description, path, content |

### 2.3 Quality Status

All ontology objects support quality tracking:
- `Proposed` - Draft state
- `Approved` - Validated state

### 2.4 Audit Fields

All models include automatic audit tracking:
- `created_at`, `created_by`
- `modified_at`, `modified_by`
- `deleted_at`, `deleted_by` (soft delete)

---

## 3. Gambia EA Metamodel

### 3.1 Concept Domains (40 concepts)

| Domain | Concepts |
|--------|----------|
| **Strategy** (4) | Vision, Goal, Objective, Initiative |
| **Service** (2) | BusinessService, SupportService |
| **Business** (7) | Customer, BusinessProcess, Workflow, Capability, OrganisationUnit, Role, Actor |
| **Application** (4) | Application, ApplicationComponent, ApplicationFunction, ApplicationService |
| **Data** (4) | DataEntity, DataObject, InformationFlow, DataDomain |
| **Technology** (7) | TechnologyComponent, Server, Network, Location, Deployment, Vendor, ITCapability |
| **Investment** (3) | Project, Demand, Budget |

### 3.2 Building Block Types (2)
- **ABB** - Architecture Building Block
- **SBB** - Solution Building Block

### 3.3 Governance Value Types (6)
- LifecycleStatus
- HealthRating
- ComplianceStatus
- DeliveryStatus
- Environment
- DataClassification

### 3.4 Relationship Types (28)

**Core Relationships (9):**
| Relation | Description |
|----------|-------------|
| realizes | Implementation relationship |
| supports | Support/enablement |
| uses | Usage dependency |
| contains | Composition |
| assignedTo | Assignment |
| serves | Service provision |
| triggers | Event triggering |
| flowsTo | Data/process flow |
| hosts | Hosting relationship |

**Extended Relationships (16):**
isPartOf, delivers, implements, ownedBy, hostedOn, locatedAt, connectedTo, suppliedBy, funds, compliesWith, replaces, dependsOn, carries, manages, exposedBy, isA

**Property Relationships (3):**
hasLifecycleStatus, hasComplianceStatus, hasProperty

### 3.5 Populating the Metamodel

```bash
python manage.py populate_gambia_metamodel --org <organisation_name>
```

This creates all 40 concepts, 28 relationships, and 70 predicate rules.

---

## 4. Visualization & Analysis

### 4.1 Graph Visualization

**URL:** `/model/<model_id>/graph/`

**System Requirement:** Graphviz must be installed on the server.

```bash
# macOS
brew install graphviz

# Ubuntu/Debian
sudo apt-get install graphviz

# Verify installation
dot -V
```

**Configuration:**
- `MAX_GRAPH_NODES` - Controls complexity (default: 50)
- `MAX_LENGTH_GRAPH_NODE_TEXT` - Label truncation (default: 30)

**Features:**
- SVG output format
- Two viewing modes: Simplified and Advanced
- Role-based presets for different architect perspectives
- BDAT layer filtering (Business, Data, Application, Technology)
- Organizational scope filtering
- Interactive node exploration
- Clickable nodes linking to detail pages

#### Simplified Mode (Default)

The Simplified mode is designed for TOGAF-trained Enterprise Architects with an intuitive interface:

| Control | Description |
|---------|-------------|
| **Architect View** | Select your role: Enterprise, Business, Application, Data, or Technology Architect |
| **Architecture Layers** | Toggle BDAT layers: Business, Application, Data, Technology |
| **Organizational Scope** | Filter by organizational unit (e.g., Ministry of Finance) |
| **Include subordinate units** | Include child organizations in scope |
| **Display Mode** | Context View (shows connections) or Strict Layer Filter (layer items only) |

**How to Use Simplified Mode:**

1. Navigate to the model detail page and click **Graph** tab
2. Ensure **Simplified** mode is selected (default)
3. Select an **Architect View** (e.g., Application Architect)
   - This auto-selects the appropriate architecture layers
4. Optionally adjust **Architecture Layers** checkboxes
5. Optionally select an **Organizational Scope** to filter by ownership
6. Choose **Display Mode**:
   - **Context View**: Shows selected items plus their connections to other layers
   - **Strict Layer Filter**: Shows only items from selected layers
7. Click **"Generate Architecture Diagram"**

**Display Mode Behavior:**

| Mode | Selected Layer | Shows |
|------|----------------|-------|
| Context View | Application | Applications + connected Business Processes, Data Entities, etc. |
| Strict Layer Filter | Application | Only Applications (no cross-layer items) |
| Strict + Org Scope | Data | Data Entities connected to the org unit's Applications |

#### Advanced Mode

The Advanced mode provides full control with EA-friendly terminology:

| Panel | Label | Description |
|-------|-------|-------------|
| **1** | Element Types | Types of architecture building blocks (formerly "Concepts") |
| **2** | Relationship Types | How elements connect to each other (formerly "Relations") |
| **3** | Structures | Valid relationship patterns (formerly "Predicates") |
| **4** | Elements | Actual items in your architecture (formerly "Instances") |

**How to Use Advanced Mode:**

1. Click **Advanced** to switch modes
2. Select **Element Types** (what to show)
3. Select **Relationship Types** (how things connect)
4. **Structures** auto-populate based on selections
5. **Elements** auto-populate based on structures
6. Click **"Generate Ontology Graph"** or **"Generate Elements Graph"**

#### Organizational Scope Filtering

When an organizational scope is selected, the graph filters to show only architecture elements owned by that organization:

- **Direct Ownership**: Elements directly owned by the selected org unit
- **Subordinate Units**: When checked, includes elements owned by child organizations
- **Transitive Filtering**: For non-Application layers with Strict mode, finds elements connected to the org unit's Applications

**Example:**
- Select "Ministry of Finance" + "Data" layer + "Strict Layer Filter"
- Shows: Data Entities used by Ministry of Finance's Applications
- Does NOT show: Unrelated Data Entities or Applications themselves

**Note:** If no results appear, it may mean no elements of the selected type are connected to that organization's systems.

### 4.2 Impact Analysis

**URL:** `/model/<model_id>/impact-analysis/`

**Features:**
- Select root instance
- Filter by predicate types
- Multi-level traversal (configurable depth)
- Returns impact tree + SVG visualization

### 4.3 Gap Analysis

**URL:** `/model/<model_id>/gap-analysis/`

**Features:**
- Compare two models
- Identify missing concepts, relations, predicates, instances
- Difference highlighting

### 4.4 Path Finder

**URL:** `/model/<model_id>/path-finder/`

**Features:**
- Find all paths between two instances
- Relationship-based connection discovery
- Traceability chains
- Optional relation filter for targeted analysis
- Multi-target mode to find paths to all instances of a concept

**Usage:**

1. **Start**: Select a concept and instance as the starting point
2. **End**: Either select a specific instance, or check "Find all instances of this concept" to discover all connected instances
3. **Relations Filter** (optional): Select one or more relations to filter the search

**Relation Filter Behavior:**

The relation filter applies to the **first edge only** from the start instance. This matches common EA analysis patterns:

| Question | Filter | Behavior |
|----------|--------|----------|
| "What does IFMIS **depend on**?" | dependsOn | First edge must be "dependsOn", then traces full path |
| "What does this app **support**?" | supports | First edge must be "supports", then traces downstream |
| "What organizations use IFMIS?" | (none) | Finds all paths regardless of relation types |

**Example:**

- **Query**: IFMIS → OrganisationUnit with "dependsOn" filter
- **Path found**: IFMIS → *dependsOn* → GamPay → *realizes* → Service → *ownedBy* → Ministry
- The first edge (dependsOn) matches the filter; subsequent edges can use any relation

---

## 5. Import/Export Capabilities

### 5.1 Supported Formats

| Format | Import | Export | File Extension |
|--------|--------|--------|----------------|
| JSON | ✓ | ✓ | .json |
| Excel | ✓ | ✓ | .xlsx |
| XML | ✓ | ✓ | .xml |

### 5.2 Export Options

**URL:** `/model/<model_id>/export/`

- Knowledge set selection (ontology/instances)
- Selective export by concept/relation/predicate/instance IDs
- Scheduled vs immediate execution
- Task-based async processing

### 5.3 Import Options

**URL:** `/model/<model_id>/import/`

- File upload interface
- Format auto-detection
- Task-based processing

### 5.4 Plugin Architecture

**Location:** `ontology/plugins/`

Available plugins:
- `json.py` - JSON import/export
- `excel.py` - Excel (XLSX) import/export
- `xml.py` - XML import/export
- `essential.py` - Standard ontology bootstrap

**Plugin Interface:**
```python
class Plugin_v1:
    def capabilities():
        return {CAPABILITY_IMPORT, CAPABILITY_EXPORT}

    def get_format():
        return ('FORMAT_CODE', 'Display Name')

    def get_file_extension(knowledge_set):
        return 'ext'

    def import_ontology(model, path, filename, filters):
        pass

    def export_ontology(model, path, filename, filters):
        pass
```

---

## 6. Custom Reports

### 6.1 Report Configuration

**URL:** `/model/<model_id>/reports/`

| Field | Description |
|-------|-------------|
| name | Report identifier |
| description | Report description |
| path | File path to template |
| content | Inline HTML/JS code |

### 6.2 Report Types

- **HTML/JavaScript** - Custom interactive reports
- **XML** - XSLT transformation
- **JSON** - Data serialization

### 6.3 Knowledge Base Integration

Reports can query:
- Concept hierarchies
- Relationship traversals
- Instance filtering and aggregation

---

## 7. Authorization & Security

### 7.1 Permission Model

| Action | Description |
|--------|-------------|
| LIST | View list of objects |
| CREATE | Create new objects |
| VIEW | View object details |
| UPDATE | Modify objects |
| DELETE | Delete objects |
| EXECUTE | Run reports/operations |

### 7.2 Components

| Component | Purpose |
|-----------|---------|
| **SecurityGroup** | Role definition (Admin, Editor, Viewer) |
| **AccessPermission** | Permission assignment to groups |
| **Profile** | User membership with group assignment |

### 7.3 ACL Middleware

- Enforces permissions on every request
- Integrated with user profiles
- Organisation-scoped filtering

### 7.4 Authentication Methods

- Session authentication (web UI)
- JWT Bearer tokens (API)
- Basic authentication (API)

**Token Endpoints:**
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh token

---

## 8. Multi-Tenancy & Organizations

### 8.1 Organization Model

| Field | Description |
|-------|-------------|
| name | Organization name |
| location | Physical location |
| description | Description |
| is_active | Active status |

### 8.2 Profile Model

| Field | Description |
|-------|-------------|
| user | Django User reference |
| organisation | Organization membership |
| role | Role description |
| phone, address | Contact info |
| is_active | Active status |

### 8.3 Data Isolation

- `OrganisationManager` automatically filters queries
- Users only see data from their organization
- Superuser can access all organizations

### 8.4 Task Management

| Status | Description |
|--------|-------------|
| PENDING | Waiting to start |
| STARTED | In progress |
| SUCCESS | Completed successfully |
| WARNING | Completed with warnings |
| FAILURE | Failed |
| CANCELLED | Cancelled by user |

---

## 9. REST API

### 9.1 Endpoints

**Base URL:** `/api/rest/`

| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/users/` | GET, POST | User management |
| `/organisations/` | GET, POST, PUT, DELETE | Organization CRUD |
| `/repositories/` | GET, POST, PUT, DELETE | Repository CRUD |
| `/models/` | GET, POST, PUT, DELETE | Model CRUD |
| `/concepts/` | GET, POST, PUT, DELETE | Concept CRUD |
| `/relations/` | GET, POST, PUT, DELETE | Relation CRUD |
| `/predicates/` | GET, POST, PUT, DELETE | Predicate CRUD |
| `/instances/` | GET, POST, PUT, DELETE | Instance CRUD |
| `/slots/` | GET, POST, PUT, DELETE | Slot CRUD |
| `/token/` | POST | JWT token generation |
| `/token/refresh/` | POST | Token refresh |

### 9.2 Model-Scoped Queries

| Endpoint | Description |
|----------|-------------|
| `/model/<id>/concepts/` | Concepts in model |
| `/model/<id>/relations/` | Relations in model |
| `/model/<id>/predicates/` | Predicates in model |
| `/model/<id>/instances/` | Instances in model |
| `/model/<id>/slots/` | Slots in model |

### 9.3 Authentication

```bash
# Get token
curl -X POST /api/token/ -d '{"username":"admin","password":"pass"}'

# Use token
curl -H "Authorization: Bearer <token>" /api/rest/models/
```

### 9.4 Pagination

- Default: 100 items per page
- Use `?page=N` for pagination

---

## 10. GraphQL API

### 10.1 Endpoint

**URL:** `/api/graphql`

GraphiQL UI enabled for interactive queries.

### 10.2 Available Queries

```graphql
query {
  o_organisation_list { id name }
  o_repository_list { id name }
  o_model_list { id name version }
  o_model_detail_by_name(name: "Model", version: "1.0") { id }
  o_relation_list { id name }
  o_concept_list { id name }
  o_predicate_list { id subject { name } relation { name } object { name } }
  o_instance_list { id name concept { name } }
}
```

---

## 11. Management Commands

### 11.1 Organization Commands

```bash
# Create organization with users
python manage.py create_organisation <name> --users <username> [--superadmin]

# Link users to organization
python manage.py link_users --org <name> --users <user1> <user2>

# Remove soft-deleted records
python manage.py remove_deleted
```

### 11.2 Ontology Commands

```bash
# Populate Gambia metamodel (40 concepts, 28 relations, 70+ predicates)
python manage.py populate_gambia_metamodel --org <org_name>

# Populate AS-IS architecture data (133 instances, 143 relationships)
python manage.py populate_gambia_asis --org <org_name>

# Dry-run mode (preview what would be created)
python manage.py populate_gambia_asis --org <org_name> --dry-run

# Verbose output (detailed logging)
python manage.py populate_gambia_asis --org <org_name> --verbose

# Initialize application
python manage.py app_init
```

**AS-IS Architecture Data (populate_gambia_asis):**

| Category | Count | Examples |
|----------|-------|----------|
| OrganisationUnit | 19 | MoFEA, GRA, MoH, MoCDE + departments |
| Application | 27 | IFMIS, GamPay, DHIS2, GamTax Net, ASYCUDA, eCRVS, MyGov |
| TechnologyComponent | 15 | SQL Server, PostgreSQL, ACE Cable, Data Centres |
| Vendor | 16 | Epicor, TechBiz, UNCTAD, WCC Group, OrangeBD |
| BusinessProcess | 17 | Budget Management, Tax Administration, Health Delivery |
| BusinessService | 7 | Tax Filing, Government Payment, Birth Certificate |
| Capability | 12 | Financial Management, Revenue Collection, Digital Identity |
| DataEntity | 10 | Taxpayer Records, Health Records, Civil Registration |
| Project | 10 | WARDIP, GEHSSP, MyGov Development, NDAS |

### 11.3 Enterprise Architecture Commands

```bash
# Compute criticality scores
python manage.py compute_criticality
```

### 11.4 Data Commands

```bash
# Export database
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 2 > db.json

# Import database
python manage.py loaddata db.json
```

---

## 12. URL Structure

### 12.1 Main URLs

| URL Pattern | View |
|-------------|------|
| `/` | Homepage |
| `/admin/` | Django admin |
| `/rosetta/` | Translation UI |

### 12.2 Ontology URLs

| URL Pattern | View |
|-------------|------|
| `/repository/` | Repository list |
| `/repository/create/` | Create repository |
| `/repository/<id>/` | Repository detail |
| `/model/` | Model list |
| `/model/create/` | Create model |
| `/model/<id>/` | Model detail |
| `/model/<id>/graph/` | Graph visualization |
| `/model/<id>/impact-analysis/` | Impact analysis |
| `/model/<id>/gap-analysis/` | Gap analysis |
| `/model/<id>/export/` | Export model |
| `/model/<id>/import/` | Import data |

### 12.3 Configuration URLs

| URL Pattern | View |
|-------------|------|
| `/configuration/` | Configuration list |
| `/configuration/create/` | Create configuration |
| `/configuration/<id>/` | Configuration detail |
| `/configuration/<id>/rebuild/` | Rebuild from metamodel |
| `/configuration/graph_presets/<org_id>/` | Graph presets configuration |
| `/configuration/graph_presets/<org_id>/reset/` | Reset presets to defaults |

### 12.4 Graph Presets API URLs

| URL Pattern | Method | Description |
|-------------|--------|-------------|
| `/o_model/<model_id>/presets/` | GET | Get graph presets for model's organization |
| `/o_model/<model_id>/org_units/` | GET | Get organizational units from model |

---

## 13. Localization

### 13.1 Supported Languages

| Code | Language |
|------|----------|
| en-us | English (US) |
| fr | French |
| es | Spanish |
| de | German |
| ja | Japanese |
| pt | Portuguese |
| ru | Russian |
| sw | Swahili |
| zh-cn | Chinese (Simplified) |

### 13.2 Translation Management

**URL:** `/rosetta/`

Django Rosetta interface for managing translations.

**Locale files:** `locale/<lang>/LC_MESSAGES/`

---

## 14. Deployment

### 14.1 Development Server

```bash
python manage.py runserver [port]
```

### 14.2 Production - Gunicorn

**Config:** `gunicorn.conf.py`

```bash
gunicorn openea.wsgi --config gunicorn.conf.py
```

### 14.3 Production - uWSGI

**Config:** `uwsgi.ini`

```bash
uwsgi --ini uwsgi.ini
```

### 14.4 Static Files

```bash
python manage.py collectstatic
```

---

## 15. Graph Presets Administration

### 15.1 Overview

Graph Presets allow administrators to configure default selections for the Graph visualization based on architect roles and TOGAF/BDAT architecture layers.

**URL:** `/configuration/graph_presets/<organisation_id>/`

### 15.2 Architect Roles

Default architect role presets are provided:

| Role | Display Name | Default Element Types | Default Relations |
|------|--------------|----------------------|-------------------|
| `enterprise_architect` | Enterprise Architect | All types | All relations |
| `business_architect` | Business Architect | Business Process, Capability, Service, Business Function, Value Stream | realizes, supports, uses |
| `application_architect` | Application Architect | Application, Application Component, Interface, Application Service, System | dependsOn, uses, realizes, contains, supports, manages, replaces |
| `data_architect` | Data Architect | Data Entity, Data Object, Data Domain, Information Flow | uses, flowsTo, contains, manages |
| `technology_architect` | Technology Architect | Technology Component, Server, Network, Platform, Infrastructure, Hardware | hosts, connectedTo, dependsOn, contains, manages |

### 15.3 Architecture Layers (BDAT)

| Layer | Display Name | Element Types |
|-------|--------------|---------------|
| `business` | Business Layer | Business Process, Capability, Business Service, Business Function, Value Stream, Workflow |
| `application` | Application Layer | Application, Application Component, Application Service, Interface, System, Software |
| `data` | Data Layer | Data Entity, Data Object, Data Domain, Information Flow, Database |
| `technology` | Technology Layer | Technology Component, Server, Network, Platform, Infrastructure, Hardware, Location |

### 15.4 Customizing Presets

**Via Admin UI:**
1. Navigate to `/configuration/graph_presets/<org_id>/`
2. Expand role or layer accordions to view settings
3. Use **Raw JSON Editor** for advanced configuration
4. Click **Save Configuration**

**Auto-Map from Model:**
1. Select a model from the dropdown
2. Click **Auto-Map Concepts**
3. Concepts are automatically assigned to layers based on naming patterns

**Reset to Defaults:**
1. Click **Reset to Defaults** button
2. Confirm the action

### 15.5 Preset JSON Schema

```json
{
  "roles": {
    "role_id": {
      "display_name": "Role Display Name",
      "description": "Role description",
      "default_concepts": ["Concept Name 1", "Concept Name 2"],
      "default_relations": ["relation-name-1", "relation-name-2"]
    }
  },
  "layers": {
    "layer_id": {
      "display_name": "Layer Display Name",
      "concepts": ["Concept Name 1", "Concept Name 2"]
    }
  },
  "org_unit_config": {
    "concept_name": "Organisation Unit",
    "ownership_relation": "ownedBy"
  }
}
```

### 15.6 Organizational Unit Configuration

The `org_unit_config` section defines how organizational scope filtering works:

| Setting | Description | Default |
|---------|-------------|---------|
| `concept_name` | Concept name for org units | "Organisation Unit" |
| `ownership_relation` | Relation indicating ownership | "ownedBy" |

Elements are considered "owned by" an org unit when there's a slot: `Element ownedBy OrgUnit`

### 15.7 Adding Custom Roles

**Via API:**
```bash
curl -X POST /configuration/graph_presets/<org_id>/role/custom_role/ \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Custom Architect",
    "description": "Custom role description",
    "default_concepts": ["Concept1", "Concept2"],
    "default_relations": ["relation1", "relation2"]
  }'
```

**Via JSON Editor:**
Add a new entry under `roles` in the Raw JSON Editor.

---

## 16. Terminology Reference

The Graph UI uses EA-friendly terminology:

| Ontology Term | EA Term | Description |
|---------------|---------|-------------|
| Concept | Element Type | Types of architecture building blocks |
| Relation | Relationship Type | How elements connect to each other |
| Predicate | Structure | Valid relationship patterns (Subject-Relation-Object) |
| Instance | Element | Actual items in your architecture |

---

## 17. Configuration Examples

### 15.1 Development Configuration

```ini
[DEFAULT]
ENVIRONMENT = dev
DEBUG = 1
DJANGO_ALLOWED_HOSTS = localhost,127.0.0.1
DOMAIN_URL = http://localhost:8000/

[Database]
SQL_ENGINE = django.db.backends.sqlite3
SQL_DATABASE = db.sqlite3

[Graph]
MAX_GRAPH_NODES = 50
MAX_LENGTH_GRAPH_NODE_TEXT = 30
```

### 15.2 Production Configuration

```ini
[DEFAULT]
ENVIRONMENT = prod
DEBUG = 0
DJANGO_ALLOWED_HOSTS = yourdomain.com
DOMAIN_URL = https://yourdomain.com/
SECRET_KEY = <strong-random-key>

[Database]
SQL_ENGINE = django.db.backends.postgresql
SQL_DATABASE = openea_prod
SQL_USER = openea
SQL_PASSWORD = <secure-password>
SQL_HOST = db.server.com
SQL_PORT = 5432

[Email]
EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_USE_TLS = 1

[Graph]
MAX_GRAPH_NODES = 100
MAX_LENGTH_GRAPH_NODE_TEXT = 50
```

---

## 16. Typical Workflow

1. **Create Organization**
   ```bash
   python manage.py create_organisation myorg --users admin
   ```

2. **Populate Metamodel**
   ```bash
   python manage.py populate_gambia_metamodel --org myorg
   ```

3. **Populate AS-IS Architecture** (optional - for Gambia EA)
   ```bash
   python manage.py populate_gambia_asis --org myorg
   ```
   This creates 133 instances based on the D5 AS-IS Architecture document.

4. **Create Repository** → `/repository/create/`

5. **Create Model** → `/model/create/` (within repository)

6. **Define/Import Concepts** → Use populated metamodel or create custom

7. **Create Instances** → Add actual data records

8. **Add Slots** → Define property values

9. **Visualize** → Graph view, Impact Analysis

10. **Export** → JSON/Excel/XML for sharing

---

## 18. Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Redis connection error | Switch to LocMemCache in settings.py |
| User not found | Create user with `createsuperuser` first |
| SQLite constraint warnings | Safe to ignore for development |
| Graph generation 500 error | Install Graphviz: `brew install graphviz` (macOS) or `apt-get install graphviz` (Linux) |
| Graph button does nothing | Select filters first (Relations, Predicates, Instances) before clicking Generate |
| Empty graph with org scope | No elements of selected type connected to that org unit's systems. Try Context View or different layer. |
| Empty graph with strict filter | No relationships exist between items of selected layer. Try Context View to see cross-layer connections. |
| Presets not matching | Concept names in presets must match model concepts. Use Auto-Map or check exact names. |
| "add_segment: error" in console | Graphviz rendering issue - usually means graph data is empty or has orphan references |
| Slots causing errors | Ensure slots have predicates linked (run `populate_gambia_asis` after `populate_gambia_metamodel`) |
| Package build failures (Python 3.13) | Upgrade packages (pillow>=10.4, psycopg2-binary>=2.9.9, lxml>=5.0, Markdown>=3.5) |

---

## 19. Key Configuration Points

1. **Metamodel** - Use `populate_gambia_metamodel` or API for custom concepts
2. **Graph Presets** - Configure architect roles and BDAT layers at `/configuration/graph_presets/`
3. **Reports** - Create OReport objects with HTML/JS templates
4. **Import/Export** - Extend plugin system for custom formats
5. **Permissions** - Define SecurityGroups with AccessPermissions
6. **Visualizations** - Adjust MAX_GRAPH_NODES for complexity; use Simplified mode for TOGAF architects
7. **Multi-tenancy** - Create Organisations and assign Profiles
8. **Org Scope Filtering** - Define `ownedBy` relationships to enable organizational filtering in graphs
9. **API** - Use REST/GraphQL for programmatic access
10. **Languages** - Add locale files for additional languages
11. **Email** - Configure SMTP for notifications
12. **Database** - Switch to PostgreSQL for production
