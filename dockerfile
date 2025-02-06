# Base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy code
WORKDIR /app
COPY requirements.txt .
COPY latency_optimizer.py .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for AWS (replace with your credentials)
ENV AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY>
ENV AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_KEY>
ENV AWS_DEFAULT_REGION=us-east-1

CMD ["python", "latency_optimizer.py"]
