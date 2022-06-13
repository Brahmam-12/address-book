from fastapi import FastAPI
from routes.user_routes import user_api_router
app=FastAPI()

app.include_router(user_api_router)