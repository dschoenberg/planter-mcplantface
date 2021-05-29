from Sensors.BaseSensor import Sensor
from Sensors.MPL3115A2 import MPLSensor

class AirTempatureSensor(Sensor):
    def __init__(self):
        #print('new AirTempatureSensor')
        return

    def read_sensor(self):
        foo, bar, blah = MPLSensor.readSensor()
        print(foo, bar, blah)
        return blah
    
    @staticmethod
    def sensor_type():
        return 'air-temp'  
    
    @staticmethod
    def sensor_id():
        return 1

class WaterTempatureSensor(Sensor):
    def __init__(self):
        #print('new WaterTempatureSensor')
        return

    def read_sensor(self):
        return '4'
    
    @staticmethod
    def sensor_type():
        return 'water-temp'

    @staticmethod
    def sensor_id():
        return 2