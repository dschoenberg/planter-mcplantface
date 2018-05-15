#!/usr/bin/python
import time

from Events.EventManager import EventManager 
from Sensors.SensorManager import SensorManager 
from Sensors.Tempature import AirTempatureSensor 
from Sensors.Tempature import WaterTempatureSensor 

s = SensorManager()
e = EventManager()

def setup():
    s.register_sensor(WaterTempatureSensor())
    s.register_sensor(AirTempatureSensor())
def main():
    try:
        while True:
            s.read_all()
            e.send_event(None)
            time.sleep(5)
    except KeyboardInterrupt:
        pass  
  
if __name__== "__main__":
    setup()
    main()

exit(0)