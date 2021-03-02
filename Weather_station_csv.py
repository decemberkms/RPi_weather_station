import smbus2
import bme280
import sys

import csv
#import sqlite3
import psutil as ps
from datetime import datetime
from time import sleep

class Logger():
    def __init__(self):
        self.data_dict = {}
        port = 1
        address =0x76
        bus = smbus2.SMBus(port)
        bme280.load_calibration_params(bus,address)
        self.bme280_data = bme280.sample(bus,address)
        
    def collect_data(self):
        ''' collect data and assign to class variable'''
        self.data_dict['Data'] = (datetime.now(), round(self.bme280_data.humidity, 2), round(self.bme280_data.pressure, 2), round(self.bme280_data.temperature, 2))
            
    def print_data(self):
        '''print select data '''
        print("-"*120)
        print("~~ {0:%Y-%m-%d, %H:%M:%S} ~~".format(*self.data_dict['Data']))
        #print("CPU TIME // User: {1:,.0f}, System: {3:,.0f}, Idle: {4:,.0f}".format(*self.data_dict['cpu']))
        #print("VIRT MEM // Totla: {1:,d}, Available: {2:,d}".format(*self.data_dict['vmemory']))
    
    def log_data(self):
        '''log the data into csv files'''
        for file, data in self.data_dict.items():
            with open('data/' + file + '.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
    
def main():
    while True:
        logger = Logger()
        logger.collect_data()
        logger.log_data()
        logger.print_data()
        sleep(0.1)
    

main()
