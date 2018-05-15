from abc import ABC, abstractmethod
class Sensor(ABC):
    @abstractmethod
    def read_sensor(self):
        pass
    
    def P(self):
        print('p')

class TempSensor(Sensor):
    def __init__(self):
        print('new TempSensor')

    def read_sensor(self):
        self.P()
        return 'Temp', 3