# Week 3 — Day 18 API Testing

## Objective

Validate SentinelX Backend v1 APIs through Swagger/OpenAPI and automated tests.

## Testing Environment

- FastAPI
- PostgreSQL
- Swagger UI / OpenAPI
- JWT authentication
- Pytest
- Windows development environment

## API Testing Results

### Authentication

- POST `/api/auth/register` — PASS
- POST `/api/auth/login` — PASS
- GET `/api/auth/me` — PASS

### Users

- GET `/api/users` with authentication — PASS
- Admin user creation — PASS
- Analyst user creation attempt — correctly rejected with HTTP 403

### Events

- POST `/api/events` — PASS
- GET `/api/events` — PASS
- Day 18 test event successfully stored and retrieved

### Alerts

- POST `/api/alerts` — PASS
- GET `/api/alerts` — PASS
- Day 18 test alert successfully stored and retrieved

### Incidents

- POST `/api/incidents` — PASS
- GET `/api/incidents` — PASS
- Day 18 test incident successfully stored and retrieved

### Hosts

- POST `/api/hosts` — PASS
- GET `/api/hosts` — PASS
- Day 18 test host successfully stored and retrieved

## Authentication and Authorization

JWT authentication was verified through Swagger.

Role-based authorization was also verified:

- Admin → allowed to create users
- Analyst → denied user creation with HTTP 403

## Automated Test Results

Pytest authentication and existing backend tests:

21 passed

One non-blocking Starlette/httpx deprecation warning was observed.

## Conclusion

Day 18 API testing successfully verified the SentinelX Backend v1 API layer, authentication, authorization, database-backed CRUD endpoints, and Swagger/OpenAPI integration.

The backend is ready to proceed to Week 4 log ingestion.

