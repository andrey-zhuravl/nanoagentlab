import os
from fastapi import FastAPI, HTTPException
import httpx
import yaml

app = FastAPI()

CASES_DIR = os.environ.get("CASES_DIR", os.path.join(os.path.dirname(__file__), "cases"))


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


def load_case(name: str) -> dict:
    path = os.path.join(CASES_DIR, f"{name}.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


@app.post("/run/{case}")
async def run_case(case: str) -> dict:
    data = load_case(case)
    results = []
    async with httpx.AsyncClient() as client:
        for step in data.get("steps", []):
            req = step.get("request", {})
            method = req.get("method", "GET")
            url = req.get("url")
            json_payload = req.get("json")
            response = await client.request(method, url, json=json_payload)
            expect = step.get("expect", {})
            if response.status_code != expect.get("status_code"):
                raise HTTPException(status_code=500, detail={"step": step.get("name"), "error": "status mismatch"})
            if "json" in expect and response.json() != expect["json"]:
                raise HTTPException(status_code=500, detail={"step": step.get("name"), "error": "json mismatch"})
            results.append({"step": step.get("name"), "status": "ok"})
    return {"case": case, "results": results}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8201)
