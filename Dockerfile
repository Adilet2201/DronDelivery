# Dockerfile
FROM python:3.11-slim

# 1) Install system deps for psycopg2 and pg_isready
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      postgresql-client \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2) Copy & install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copy the rest of your code in
COPY . .

# 4) Make our entrypoint script executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# 5) Expose (not strictly necessary on Railway, but good practice)
EXPOSE 8000

# 6) Run our entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
