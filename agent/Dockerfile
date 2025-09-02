FROM python:3.11-slim

WORKDIR /app

# Copy application code and default configs
COPY agent /app/agent
COPY configs /app/configs

# Install runtime dependencies
RUN pip install --no-cache-dir fastapi uvicorn pyyaml

# Default configuration path
ENV CONFIG_PATH=/app/configs/agent.yaml

EXPOSE 8000
