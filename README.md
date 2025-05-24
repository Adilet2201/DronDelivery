# DronProjectDjango

A Django-based food ordering and delivery system, containerized with Docker Compose.  
Originally ported from a Flask prototype, now featuring:

- Custom `User` model  
- Restaurant, MenuItem, CartItem, Order, OrderItem, Product models  
- SQLite for quick local dev (switchable to PostgreSQL)  
- Django REST Framework with throttling  
- Swagger (drf-yasg) API docs  
- Silk profiling  
- CORS support  
- Celery + Redis (background tasks)  
- MinIO S3-compatible media storage  
- Nginx serving static & media  

---

## 📋 Prerequisites

- Docker & Docker Compose  
- Python 3.11+ (for local manage.py commands)  

---

## 🚀 Quickstart (SQLite & Docker)

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Adilet2201/DronDelivery
   cd DronProjectDjango
