# Smart-Inventory-Management
# Inventory AI for Indian Manufacturing

## Features
- Demand forecasting (TensorFlow)
- Real-time inventory updates (IoT simulation)
- Quality control using computer vision (OpenCV)
- Automated supplier reordering
- Warehouse management, multi-location support

## Setup
1. Clone the repo.
2. `cd backend`
3. `pip install -r requirements.txt`
4. Setup PostgreSQL in settings.py
5. Run Django migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

## Usage
- Inventory APIs at `/inventory/<sku>/` and `/reorder/`
- Demand forecast via `demand_forecasting.py`
- Quality control using `quality_control.py`
- Simulate IoT sensor: `python scripts/iot_simulator.py`

## Documentation
See `/docs/presentation.pdf` for system architecture and project details.
