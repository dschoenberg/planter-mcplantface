#!/usr/bin/python
import time

from EventManager import EventManager 
from SensorManager import SensorManager 
from Sensors.Tempature import TempSensor 

s = SensorManager()
t = TempSensor()
e = EventManager()

def setup():
    s.register_sensor(t)
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