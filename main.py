#!/usr/bin/python
import time
import configparser
import sys
import requests

from Events.EventManager import EventManager
from Sensors.SensorManager import SensorManager
from Sensors.Tempature import AirTempatureSensor
from Sensors.Tempature import WaterTempatureSensor

s = SensorManager()
e = EventManager()
config = configparser.ConfigParser()

def default_configs():
    print('creating/resetting configuration')

    config['DEFAULT'] = {
        'PollInterval': '30',
        'DeviceId': "1"
    }
    config['Server'] = {}
    config['Server']['Url'] = 'https://planter-mcplantface.herokuapp.com/'
    config['Server']['Port'] = '443'
    with open('configuration.ini', 'w') as configfile:
        config.write(configfile)

def setup():
    config_read = config.read('configuration.ini')
    if len(config_read) == 0:  
        print('Config not found, please run python main.py --default-configs')
        sys.exit(1)

    s.register_sensor(WaterTempatureSensor())
    s.register_sensor(AirTempatureSensor())

def main():
    try:
        while True:
            sensor_data = s.read_all()
            print(sensor_data)

            logging_url = config['Server']['Url'] + 'log'

            r = requests.post(logging_url, json=sensor_data)
            print(logging_url, r.status_code, r.json())

            #todo
            #sys.exit(1)

            time.sleep(int(config['DEFAULT']['PollInterval']))
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '--default-configs':
            default_configs()
    setup()
    main()

exit(0)
