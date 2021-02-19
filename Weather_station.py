import smbus2
import bme280
from time import sleep

import datetime
import numpy as np
import pandas as pd

port = 1
address =0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

dict_origin = {"Time": [], "Humidity": [], "Pressure": [],"Temperature": []}

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = round(bme280_data.humidity, 2)
    pressure  = round(bme280_data.pressure ,2)
    ambient_temperature = round(bme280_data.temperature, 2)
    dict_origin["Humidity"].append(humidity)
    dict_origin["Pressure"].append(pressure)
    dict_origin["Temperature"].append(ambient_temperature)
    dict_origin["Time"].append(datetime.datetime.now())
    #print(dict_origin)
    df = pd.DataFrame.from_dict(dict_origin)
    print(df)
    #print(humidity, pressure, ambient_temperature)
    sleep(1)
