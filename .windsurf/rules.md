# Windsurf Rules - Microservices Bootcamp Implementation

## Project Overview
You are implementing a **complete e-commerce microservices platform** with these core services:
- **User Service**: Authentication, JWT tokens, user management
- **Product Service**: Catalog, search, MongoDB integration
- **Order Service**: Order processing, state management, business logic
- **API Gateway**: Request routing, authentication, rate limiting
- **Notification Service**: Event processing, background tasks

## Core Principle
**Implementation-focused coding assistant. No explanations unless specifically asked.**

---

## Day-by-Day Implementation Guide

### Day 1: Architecture & Project Setup
**Tasks you'll receive:**
1. Create project structure with all service directories
2. Set up Docker Compose with PostgreSQL, MongoDB, Redis
3. Create FastAPI templates for each service
4. Implement basic health check endpoints
5. Configure service networking

**Expected Structure:**
```
microservices-bootcamp/
├── user-service/
│   ├── main.py
│   ├── requirements.txt
│   ├── models.py
│   └── Dockerfile
├── product-service/
├── order-service/
├── api-gateway/
├── notification-service/
├── shared/
│   └── auth.py
├── docker-compose.yml
└── README.md
```

### Day 2: User Management Service
**Tasks you'll receive:**
- SQLAlchemy models for users
- JWT authentication implementation
- Pydantic schemas for validation
- Registration and login endpoints
- Password hashing with bcrypt
- Protected route decorators

**Key Files:**
- `user-service/models.py` - User database model
- `user-service/auth.py` - JWT token handling
- `user-service/schemas.py` - Pydantic models
- `user-service/main.py` - FastAPI endpoints

### Day 3: Product Catalog Service
**Tasks you'll receive:**
- MongoDB integration with Motor
- Product document models
- Full-text search implementation
- Category-based filtering
- File upload for product images
- Aggregation pipelines

**Key Files:**
- `product-service/database.py` - MongoDB connection
- `product-service/models.py` - Product schemas
- `product-service/search.py` - Search functionality
- `product-service/main.py` - CRUD endpoints

### Day 4: Order Processing Service
**Tasks you'll receive:**
- Order state machine implementation
- SQLAlchemy relationships (User-Order-Product)
- Business logic validation
- Service-to-service HTTP calls
- Order lifecycle endpoints
- Error handling patterns

**Key Files:**
- `order-service/models.py` - Order, OrderItem models
- `order-service/state_machine.py` - Order states
- `order-service/business_logic.py` - Validation rules
- `order-service/external_api.py` - Inter-service calls

### Day 5: API Gateway & Resilience
**Tasks you'll receive:**
- FastAPI gateway with request routing
- Circuit breaker implementation
- Retry logic with exponential backoff
- CORS and rate limiting middleware
- Service discovery configuration
- Request/response logging

**Key Files:**
- `api-gateway/main.py` - Main routing
- `api-gateway/middleware.py` - Cross-cutting concerns
- `api-gateway/circuit_breaker.py` - Resilience patterns
- `api-gateway/config.py` - Service endpoints

### Day 6: Event-Driven Architecture
**Tasks you'll receive:**
- Redis pub/sub setup
- Event publishing and subscription
- Celery task configuration
- Background notification processing
- Dead letter queue handling
- Event correlation IDs

**Key Files:**
- `shared/events.py` - Event definitions
- `notification-service/tasks.py` - Celery tasks
- `notification-service/subscribers.py` - Event handlers
- `shared/message_broker.py` - Redis pub/sub

### Day 7: Deployment & Monitoring
**Tasks you'll receive:**
- Production Dockerfile optimization
- Health check endpoints for all services
- Prometheus metrics integration
- Request tracing implementation
- Structured logging setup
- Docker Compose production config

**Key Files:**
- `*/health.py` - Health checks per service
- `*/metrics.py` - Prometheus metrics
- `shared/logging.py` - Structured logging
- `docker-compose.prod.yml` - Production setup

---

## Advanced Week (Days 8-10)

### Day 8: CQRS & Saga Patterns
**Tasks you'll receive:**
1. CQRS implementation for orders
2. Event sourcing setup
3. Saga orchestration for order processing
4. Materialized views
5. Compensation logic

### Day 9: Security & Testing
**Tasks you'll receive:**
1. OAuth 2.0 integration
2. Service-to-service auth
3. Unit tests for each service
4. Integration test suites
5. Contract testing setup

### Day 10: Performance & Scaling
**Tasks you'll receive:**
- Redis caching implementation
- Database connection pooling
- Load balancing configuration
- Query optimization
- Performance monitoring

---

## Technical Implementation Standards

### Database Patterns:
1. **PostgreSQL**: Users, Orders (relational data)
2. **MongoDB**: Products, Catalog (document data)
3. **Redis**: Cache, Sessions, Message broker

### API Standards:
1. REST endpoints with proper HTTP methods
2. OpenAPI/Swagger documentation
3. Consistent error response format
4. Request/response validation with Pydantic

### Service Communication:
1. HTTP for synchronous calls
2. Redis pub/sub for events
3. JWT for authentication
4. Correlation IDs for tracing

### Code Quality:
1. Type hints throughout
2. Async/await patterns
3. Environment variable configuration
4. Proper exception handling

---

## Response Format for Tasks

### Standard Implementation Response:
```markdown
I'll implement [specific feature].

Files to create/modify:
- service-name/file.py
- service-name/other-file.py

[Complete code for each file]

Setup commands:
pip install -r requirements.txt
docker-compose up -d

Test with:
curl http://localhost:8000/endpoint

Expected: [specific result]
```

### For Integration Tasks:
```markdown
I'll connect [Service A] with [Service B].

Modified files:
- service-a/external_api.py
- service-b/endpoints.py
- shared/schemas.py

[Complete code]

Test integration:
[specific curl commands or test steps]

Expected workflow: [end-to-end scenario]
```

---

## Debugging Protocol

### Service Won't Start:
1. Check Docker containers status
2. Verify database connections
3. Check environment variables
4. Provide corrected configuration

### API Calls Failing:
1. Verify service endpoints
2. Check request/response formats
3. Validate authentication tokens
4. Fix integration issues

### Database Issues:
1. Check connection strings
2. Verify table/collection schemas
3. Test queries individually
4. Provide working migrations

---

## Progress Validation

### After Each Implementation:
- Service starts successfully
- Health check returns 200
- Core endpoints respond correctly
- Integration tests pass

### Before Next Day:
- All services running in Docker
- Inter-service communication working
- Data persisting correctly
- No error logs in containers

---

## Emergency Responses

### If Requirements Unclear:
"I need clarification: Should I implement [Option A] or [Option B] for [specific feature]?"

### If Multiple Services Affected:
"This change requires updates to [Service List]. Should I modify all services or focus on [Primary Service]?"

### If Integration Breaks:
"Integration issue detected between [Service A] and [Service B]. Checking [specific component]..."

**Ready to implement the complete microservices e-commerce platform following this curriculum structure!**