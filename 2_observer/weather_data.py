from subject import Subject
from observer import Observer


class WeatherData(Subject):
    observers = []
    temperature = 0
    humidity = 0
    pressure = 0

    def register_observer(self, observer):
        if isinstance(observer, Observer):
            self.observers.append(observer)
        else:
            raise Exception('Param is not an instance of Observer')

    def remove_observer(self, observer):
        if isinstance(observer, Observer):
            self.observers.remove(observer)
        else:
            raise Exception('Param is not an instance of Observer')

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.temperature)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure
