# Gunakan image Python resmi
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Copy file requirements terlebih dahulu
COPY requirements.txt .

# Install dependency Python
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file Python ke dalam container
COPY . .

# Default command (bisa dioverride saat docker-compose run)
CMD ["python"]