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
- Filter by knowledge set (ontology vs instances)
- Interactive node exploration
- Clickable nodes linking to detail pages

**How to Use:**

1. Navigate to the model detail page
2. Click the **Graph** tab
3. **For Ontology Graph** (shows concepts and relationships):
   - Check the **Relations** checkbox (selects all relationship types)
   - Check the **Predicates** checkbox (selects relationship rules)
   - Click **"Generate Ontology Graph"**
4. **For Instances Graph** (shows actual data):
   - Optionally select specific **Concepts** to filter
   - Check the **Instances** checkbox
   - Click **"Generate Instances Graph"**
5. Click **"Download Graph"** to save as SVG

**Note:** You must select at least some filters before generating. Empty selections produce no graph.

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

## 15. Configuration Examples

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

## 17. Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Redis connection error | Switch to LocMemCache in settings.py |
| User not found | Create user with `createsuperuser` first |
| SQLite constraint warnings | Safe to ignore for development |
| Graph generation 500 error | Install Graphviz: `brew install graphviz` (macOS) or `apt-get install graphviz` (Linux) |
| Graph button does nothing | Select filters first (Relations, Predicates, Instances) before clicking Generate |
| Slots causing errors | Ensure slots have predicates linked (run `populate_gambia_asis` after `populate_gambia_metamodel`) |
| Package build failures (Python 3.13) | Upgrade packages (pillow>=10.4, psycopg2-binary>=2.9.9, lxml>=5.0, Markdown>=3.5) |

---

## 18. Key Configuration Points

1. **Metamodel** - Use `populate_gambia_metamodel` or API for custom concepts
2. **Reports** - Create OReport objects with HTML/JS templates
3. **Import/Export** - Extend plugin system for custom formats
4. **Permissions** - Define SecurityGroups with AccessPermissions
5. **Visualizations** - Adjust MAX_GRAPH_NODES for complexity
6. **Multi-tenancy** - Create Organisations and assign Profiles
7. **API** - Use REST/GraphQL for programmatic access
8. **Languages** - Add locale files for additional languages
9. **Email** - Configure SMTP for notifications
10. **Database** - Switch to PostgreSQL for production
