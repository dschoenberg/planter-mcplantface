from Sensors.BaseSensor import Sensor

class AirTempatureSensor(Sensor):
    def __init__(self):
        print('new AirTempatureSensor')

    def read_sensor(self):
        return 3
    
    @staticmethod
    def sensor_type():
        return 'air-temp'  
    
    @staticmethod
    def sensor_id():
        return 1

class WaterTempatureSensor(Sensor):
    def __init__(self):
        print('new WaterTempatureSensor')

    def read_sensor(self):
        return '4'
    
    @staticmethod
    def sensor_type():
        return 'water-temp'

    @staticmethod
    def sensor_id():
        return 2
        
    def __del__(self):
        print('cleaning WaterTempatureSensor')