FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

RUN apt-get update && \
    apt-get -y install gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8090

CMD ["gunicorn", "--bind", "0.0.0.0:8090", "--workers", "2", "API.wsgi:application"]

