FROM python:3.11-slim AS base
WORKDIR /app
# Install runtime dependencies separately for better caching
COPY agent/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS runtime
# Copy application code and default configs
COPY agent /app/agent
COPY configs /app/configs

# Default configuration path
ENV CONFIG_PATH=/app/configs/agent.yaml

EXPOSE 8000
