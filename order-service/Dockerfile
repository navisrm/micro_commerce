FROM python:3.11-slim

WORKDIR /app

COPY order-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY order-service/ .
COPY shared/ /app/shared

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
