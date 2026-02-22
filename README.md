# GICTA Enterprise Architecture Repository

Enterprise Architecture tool for the Gambia Information and Communications Technology Agency (GICTA), based on the OpenEA ontology engine.

![Default Home View](webapp/static/img/openea.svg?raw=true "Diagram view")

## Overview

This repository contains the Enterprise Architecture (EA) tool customized for GICTA, implementing the Gambia National EA Metamodel. The tool enables modeling, visualization, and analysis of enterprise architecture across government organizations.

## Main Features

* Web-based enterprise architecture modeling and visualization
* Gambia National EA Metamodel with 40 predefined concepts across 7 domains
* Dynamic graph visualization and impact analysis
* Custom HTML/JavaScript reports on the knowledge base
* Model import/export (JSON, Excel, XML)
* REST API and GraphQL endpoints for integration
* Multi-tenant architecture with role-based access control

## Gambia EA Metamodel

The metamodel covers 7 architectural domains:

| Domain | Concepts |
|--------|----------|
| **Strategy** | Vision, Goal, Objective, Initiative |
| **Service** | BusinessService, SupportService |
| **Business** | Customer, BusinessProcess, Workflow, Capability, OrganisationUnit, Role, Actor |
| **Application** | Application, ApplicationComponent, ApplicationFunction, ApplicationService |
| **Data** | DataEntity, DataObject, InformationFlow, DataDomain |
| **Technology** | TechnologyComponent, Server, Network, Location, Deployment, Vendor, ITCapability |
| **Investment** | Project, Demand, Budget |

See [docs/Gambia_EA_Metamodel_Reference_v1_0.md](docs/Gambia_EA_Metamodel_Reference_v1_0.md) for full documentation.

## Screenshots

### Graph View
![Graph View](webapp/static/img/OpenEA_graph.png?raw=true "Graph view")

### Impact Analysis View
![Impact Analysis View](webapp/static/img/OpenEA_impact_analysis.png?raw=true "Impact Analysis view")

### Matrix View
![Matrix View](webapp/static/img/OpenEA_matrix.png?raw=true "Matrix view")

### Custom HTML/Javascript Reports
![Custom Report](webapp/static/img/OpenEA_map.png?raw=true "Custom Reporting")

## Getting Started

### Prerequisites

* Python 3.10+ (tested with Python 3.13)
* pip

### Installation

Clone the repository:

```bash
git clone https://github.com/aarelaponin/gicta-ea-repo.git
cd gicta-ea-repo
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Create your organization and link your user:

```bash
python manage.py create_organisation gicta --users <your_username>
```

Populate the Gambia EA Metamodel:

```bash
python manage.py populate_gambia_metamodel --org gicta
```

Run the development server:

```bash
python manage.py runserver
```

Access the application at http://localhost:8000/

## Configuration

Key configuration files:

* `config.ini` - Application settings (database, email, graph limits)
* `openea/settings.py` - Django settings

See [docs/OpenEA_Configuration_Guide.md](docs/OpenEA_Configuration_Guide.md) for comprehensive configuration documentation.

## Usage

### Creating a Repository

1. Log in and click on your username at the top right
2. Select "Repositories"
3. Click "New Repository" and fill in the details

### Working with the Metamodel

After populating the Gambia EA Metamodel:

1. Create a new Model within your Repository
2. The predefined concepts (Application, Server, etc.) are available
3. Create instances of these concepts (e.g., a specific application)
4. Define relationships between instances using slots

### Visualizing Architecture

* **Graph View** - Visual network of relationships between instances
* **Impact Analysis** - Trace dependencies from any instance
* **Gap Analysis** - Compare models to identify differences

## API Access

### REST API

Base URL: `/api/rest/`

```bash
# Get JWT token
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"yourpassword"}'

# List models
curl -H "Authorization: Bearer <token>" http://localhost:8000/api/rest/models/
```

### GraphQL

Endpoint: `/api/graphql`

GraphiQL interface available for interactive queries.

## Documentation

* [Configuration Guide](docs/OpenEA_Configuration_Guide.md) - Comprehensive configuration reference
* [Gambia EA Metamodel](docs/Gambia_EA_Metamodel_Reference_v1_0.md) - Metamodel specification

## License

Based on [OpenEA](https://github.com/AGLA-Information-Systems/openea) by AGLA Information Systems.
