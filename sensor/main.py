import time
import Adafruit_DHT

from pymongo import MongoClient

SENSOR = Adafruit_DHT.DHT11
PIN = 4

if __name__ == '__main__':
    client = MongoClient("mongodb+srv://mongo:<password>@cluster0.56m12.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    while True :
        h, t = Adafruit_DHT.read_retry(SENSOR, PIN)
        if h is not None and t is not None :
            print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        else :
            print('Read error')
        time.sleep(1)
