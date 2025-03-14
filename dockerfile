FROM python:3.12.7-slim

WORKDIR /Inventory_Management

RUN useradd --create-home appuser
RUN chown -R appuser:appuser /Inventory_Management

ENV PYTHONPATH="${PYTHONPATH}:/Inventory_Management"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
    
COPY requirements/dev.txt ./requirements/dev.txt
COPY requirements/prod.txt ./requirements/prod.txt

RUN pip install --no-cache-dir -r ./requirements/dev.txt
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN apt-get install -y git && \
    apt-get clean
COPY . .

USER root

EXPOSE 8000


