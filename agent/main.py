import os
from fastapi import FastAPI
import yaml

app = FastAPI()


@app.post("/")
async def root() -> dict:
    return {}


def load_config() -> dict:
    """Load YAML configuration for the agent."""
    path = os.environ.get("CONFIG_PATH", "/app/configs/agent.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


if __name__ == "__main__":
    import uvicorn

    config = load_config()
    syslog(co)
    uvicorn.run(app, host="0.0.0.0", port=config.get("port", 8000))
