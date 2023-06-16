from fastapi import FastAPI

from routers.sushiRouter import router as sushiRouter
from routers.authRouter import router as authRouter
from models.baseModel import init

app = FastAPI()

app.include_router(sushiRouter)
app.include_router(authRouter)

init()