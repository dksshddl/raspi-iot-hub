from fastapi.logger import logger
import datetime

import Adafruit_DHT

from db.database import add_sensor

async def read_sensor_info():
    SENSOR = Adafruit_DHT.DHT11
    PIN = 4
    h, t = Adafruit_DHT.read_retry(SENSOR, PIN)
    if h is not None and t is not None :
        entity = {}
        entity['data'] = {"temperature" : f"{t:0.1f}", "humidity": f"{h:0.1f}"}
        entity['type'] = 'DHT11'
        entity['createdAt'] = datetime.datetime.now()
        logger.info("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        await add_sensor(entity)