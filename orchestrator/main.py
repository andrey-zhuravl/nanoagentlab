from fastapi import FastAPI
import httpx

app = FastAPI()


@app.post("/")
async def run_agent(payload: dict | None = None) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post("http://agent:8000/", json=payload or {})
        return response.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
