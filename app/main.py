from fastapi import FastAPI

from routers.sushiRouter import router as sushiRouter
from routers.authRouter import router as authRouter
from routers.userRouter import router as userRouter
from routers.adminRouter import router as adminRouter
from models.baseModel import init

app = FastAPI()

app.include_router(sushiRouter)
app.include_router(authRouter)
app.include_router(userRouter)
app.include_router(adminRouter)

init()