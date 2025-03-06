from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import collector

app = FastAPI()

# Allow CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(collector.router, prefix="/api", tags=["Collector"])

@app.get("/")
async def home():
    return {"message": "The API is running"}
