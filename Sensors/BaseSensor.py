from abc import ABC, abstractmethod, abstractproperty


class Sensor(ABC):
    @staticmethod
    @abstractmethod
    def sensor_type():
        pass
        
    @staticmethod
    @abstractmethod
    def sensor_id():
        pass

    @abstractmethod
    def read_sensor(self):
        pass
