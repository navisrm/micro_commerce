# Micro Commerce Platform

A complete e-commerce microservices platform with the following core services:

- **User Service**: Authentication, JWT tokens, user management
- **Product Service**: Catalog, search, MongoDB integration
- **Order Service**: Order processing, state management, business logic
- **API Gateway**: Request routing, authentication, rate limiting
- **Notification Service**: Event processing, background tasks

## Project Structure

```
micro_commerce/
├── user-service/         # Handles user authentication and management
├── product-service/      # Manages product catalog and search
├── order-service/        # Processes orders and business logic
├── api-gateway/          # Routes requests and handles authentication
└── notification-service/ # Manages event processing and notifications
```

Each service contains:
- `main.py` - Main FastAPI application
- `requirements.txt` - Service-specific dependencies

## Getting Started

Each service can be run independently using:

```bash
cd <service-directory>
pip install -r requirements.txt
uvicorn main:app --reload --port <port>
```
