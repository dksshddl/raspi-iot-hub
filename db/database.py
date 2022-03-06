import motor.motor_asyncio
from bson import ObjectId
from conf import config

client = motor.motor_asyncio.AsyncIOMotorClient(config['mongo']['url'])

database = client["dksshddl"]

sensor_collection = database["sensor"]

async def add_sensor(sensor_info: dict) -> dict:
    admin = await sensor_collection.insert_one(sensor_info)
    new_admin = await sensor_collection.find_one({"_id": admin.inserted_id})
    return new_admin

async def retrieve_sensor_info():
    sensor_infos = []
    async for info in sensor_collection.find():
        sensor_infos.append(info)
    return sensor_infos

async def retrieve_sensor_info_by_time(start, end):
    # TODO retrieve_sensor_info_by_time
    pass
