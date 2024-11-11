from fastapi import FastAPI
from controller.track_controller import router as last_fm_router
app = FastAPI()

app.include_router(last_fm_router)