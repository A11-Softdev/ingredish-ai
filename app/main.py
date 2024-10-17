import uvicorn
from fastapi import FastAPI
from app.routers import menu_router

app = FastAPI()

# Include the menu router
app.include_router(menu_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
