from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import pdf, knowledge
from tortoise.contrib.fastapi import register_tortoise
import os

app = FastAPI()

# Include routers
app.include_router(pdf.router, prefix="/pdf", tags=["PDF"])
app.include_router(knowledge.router, prefix="/knowledge", tags=["Knowledge Base"])

# Serve static files for the frontend
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")
print(static_dir)

@app.get("/")
def read_root():
    return {"message": "Welcome to PDF Knowledge AI Filler"}

# Database configuration for Tortoise ORM
register_tortoise(
    app,
    db_url="sqlite://./knowledge.db",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080, reload=True)
