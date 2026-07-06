from fastapi import FastAPI

app = FastAPI(
    title="AI CallFlow API",
    description="Backend für die KI-Telefonzentrale",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Willkommen bei AI CallFlow 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "online"
    }
