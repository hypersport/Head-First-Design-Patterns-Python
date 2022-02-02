from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


class CurrentConditionDisplay(Observer, DisplayElement):
    temperature = 0
    humidity = 0
    pressure = 0
    weather_data = None

    def __init__(self, weather_data):
        if isinstance(weather_data, WeatherData):
            self.weather_data = weather_data
            weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(f'Temperature is {self.temperature}\n'
              f'Humidity is {self.humidity}\n'
              f'Pressure is {self.pressure}')
