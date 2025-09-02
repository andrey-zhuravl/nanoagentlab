FROM python:3.11-slim

WORKDIR /app

# Copy application code and default configs
COPY orchestrator /app/orchestrator
COPY configs /app/configs

# Install runtime dependencies
RUN pip install --no-cache-dir fastapi uvicorn httpx pyyaml

# Default configuration path
ENV CONFIG_PATH=/app/configs/router.yaml

EXPOSE 8101
