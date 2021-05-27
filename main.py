#!/usr/bin/python
import time
import configparser
import requests

from Events.EventManager import EventManager
from Sensors.SensorManager import SensorManager
from Sensors.Tempature import AirTempatureSensor
from Sensors.Tempature import WaterTempatureSensor

s = SensorManager()
e = EventManager()
config = configparser.ConfigParser()

def read_configs():
    config.read('configuration.ini')
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
    read_configs()
    s.register_sensor(WaterTempatureSensor())
    s.register_sensor(AirTempatureSensor())


def main():
    try:
        while True:
            s.read_all()
            e.send_event(None)
            water_url = config['Server']['Url'] + 'water-temp'
            #formdata waterTemp
            r = requests.post(water_url, {"waterTemp": "88"})
            print(water_url, r.status_code, r.json())

            time.sleep(int(config['DEFAULT']['PollInterval']))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    setup()
    main()

exit(0)
