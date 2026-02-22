# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OpenEA is an enterprise-grade Enterprise Architecture (EA) tool based on an ontology engine. It provides a web-based platform for organizations to model, visualize, and analyze their enterprise architecture using knowledge-based ontologies.

## Build & Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create organization with users
python manage.py create_organisation <org_name> --users <username>

# Run development server
python manage.py runserver

# Run all tests
pytest

# Run a specific test file
pytest ontology/tests/o_concept/o_concept_create_test.py

# Run tests matching a pattern
pytest -k "test_concept"

# Export database
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 2 > db.json

# Import database
python manage.py loaddata db.json
```

## High-Level Architecture

### Core Modules

- **ontology/** - Heart of the application. Implements the EA ontology engine with models: Repository, OModel, OConcept, ORelation, OPredicate, OInstance, OSlot. Handles concept/relation management, import/export, graph visualization, gap analysis.

- **api/** - REST API (`/api/rest/`) and GraphQL (`/api/graphql`) endpoints. Uses Django REST Framework with JWT authentication.

- **authorization/** - RBAC implementation with AccessPermission, SecurityGroup models. ACLMiddleware enforces access control.

- **organisation/** - Multi-tenant support with Organisation, Profile, Task models. OrganisationManager provides user-scoped QuerySet filtering.

- **authentication/** - User registration, login, email verification.

- **enterprisearchitecture/** - EA-specific visualizations (capability view, product view, value stream, risk quadrant, cost analysis).

- **reporting/** - Custom HTML/JavaScript/XML report generation.

- **taxonomy/** - Tagging system with Tag and TagGroup models.

### Request Flow

```
Request → Gunicorn/uWSGI → Django Middleware Stack → URL Routing → Views → Controllers → Models → Database
```

Key middleware: Security, Auth, Logging (RequestMiddleware, ExecutionTimeMiddleware), ACL (ACLMiddleware).

### Data Model Patterns

All core models inherit from `GenericModel` with:
- UUID primary keys
- Audit fields: `created_at`, `created_by`, `modified_at`, `modified_by`
- Soft delete: `deleted_at`, `deleted_by`

Multi-tenancy is enforced via `OrganisationManager` which filters querysets by user's organization.

## Technology Stack

- **Backend**: Django 4.2, Django REST Framework, graphene-django (GraphQL)
- **Database**: SQLite (default), PostgreSQL supported
- **Frontend**: Bootstrap 5, jQuery 3.6, Vis.js (graph visualization), Select2
- **Testing**: pytest, pytest-django

## Key Configuration

- `openea/settings.py` - Django settings with environment-based config (dev/prod)
- `config.ini` - Application configuration (environment, database, email, MAX_GRAPH_NODES)
- `pytest.ini` - Test configuration

## API Endpoints

REST API at `/api/rest/`:
- `/users/`, `/organisations/`, `/repositories/`, `/models/`
- `/concepts/`, `/relations/`, `/predicates/`, `/instances/`, `/slots/`
- `/token/` (JWT), `/token/refresh`

GraphQL at `/api/graphql` with GraphiQL interface.

## Management Commands

Located in `organisation/management/commands/`:
- `create_organisation` - Create new organization
- `link_users` - Link users to organizations
- `remove_deleted` - Clean up soft-deleted records
- `app_init` - Initialize application
- `import_channels`, `normalize_applications` - Data import utilities

In `enterprisearchitecture/management/commands/`:
- `compute_criticality` - Calculate system criticality metrics
