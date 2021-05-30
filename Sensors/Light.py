from Sensors.BaseSensor import Sensor
from Sensors.MPL3115A2 import MPL3115A2

class LightSensor(Sensor):
    def __init__(self):
        #print('new AirTempatureSensor')
        return

    def read_sensor(self):
        luminance = MPL3115A2().readSensor()
        return luminance
    
    @staticmethod
    def sensor_type():
        return 'luminance'  
    
    @staticmethod
    def sensor_id():
        return 2
