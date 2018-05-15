from Sensors.BaseSensor import Sensor

class AirTempatureSensor(Sensor):
    def __init__(self):
        print('new AirTempatureSensor')

    def read_sensor(self):
        return 'Temp', 3

class WaterTempatureSensor(Sensor):
    def __init__(self):
        print('new WaterTempatureSensor')

    def read_sensor(self):
        return 'Temp', 4