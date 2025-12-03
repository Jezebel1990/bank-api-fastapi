from fastapi import FastAPI

app = FastAPI(
    title="API Bancária",
    description="API assíncrona para depósitos, saques e extratos bancários.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "API Bancária está no ar 🚀"}
