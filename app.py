from typing import Optional
import queue

from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from services.scheduler.sensor import read_sensor_info

app = FastAPI()

app.queue_system = queue.Queue()
app.queue_limit = 5

app.scheduler = AsyncIOScheduler()
app.scheduler.add_job(read_sensor_info, 'cron', hour="*/1")
app.scheduler.start()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}