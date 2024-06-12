from fastapi import FastAPI
from endpoint import router as endpoint_router
import uvicorn
app = FastAPI()
app.include_router(endpoint_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)