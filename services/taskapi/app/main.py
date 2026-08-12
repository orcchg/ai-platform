from fastapi import FastAPI
from app.config import Settings

def create_app() -> FastAPI:
    app = FastAPI()
    # settings = Settings()

    @app.get("/healthz")
    async def health():
        return {"status":"ok"}

    return app

app = create_app()
