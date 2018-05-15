from time import sleep

class SensorManager:
    sensors = []
    def __init__(self):
        print('new Sensormanager')

    def __del__(self):
        print('unregistering sensors')
        sleep(1)

        while len(self.sensors) > 0:
            foo = self.sensors.pop()
            print('removing {0}'.format(foo))
            del foo
        
        print('done {0} sensors remaining'.format(len(self.sensors)))
    
    def register_sensor(self, sensor):
        invert_op = getattr(sensor, "read_sensor", None)
        if callable(invert_op):
            self.sensors.append(sensor)
            print('registering sensor {0} is {1}'.format(sensor, len(self.sensors)))
        else:
            print('sensor {0}has no read_sensor method'.format(sensor))
    
    def read_all(self):
        for s in self.sensors:
            sensor_value = s.read_sensor()
            print(sensor_value)


    
    
