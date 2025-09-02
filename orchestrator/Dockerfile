FROM python:3.11-slim AS base
WORKDIR /app
# Install runtime dependencies separately for better caching
COPY orchestrator/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS runtime
# Copy application code and default configs
COPY orchestrator /app/orchestrator
COPY configs /app/configs

# Default configuration path
ENV CONFIG_PATH=/app/configs/router.yaml

EXPOSE 8101
