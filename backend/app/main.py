from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import generate  # Import your router

app = FastAPI()

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the generated router
app.include_router(generate.router, prefix="/api")