import os
from fastapi import FastAPI
import httpx
import yaml


def load_config() -> dict:
    path = os.environ.get("CONFIG_PATH", "/app/configs/router.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


config = load_config()
app = FastAPI()


@app.post("/")
async def run_agent(payload: dict | None = None) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(config.get("agent_url", "http://agent:8000/"), json=payload or {})
        return response.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=config.get("port", 8001))
