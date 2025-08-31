FROM python:3.11-slim

WORKDIR /app

# Copy application code and configs
COPY agent /app/agent
COPY configs /app/configs

# Install runtime dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Default configuration path
ENV CONFIG_PATH=/app/configs/echo.yaml

EXPOSE 8000

CMD ["python", "-m", "agent.main"]
