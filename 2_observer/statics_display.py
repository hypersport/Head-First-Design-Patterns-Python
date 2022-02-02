from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


class StaticsDisplay(Observer, DisplayElement):
    max_temp = -99
    min_temp = 200
    current_temp = 0
    nums = 0
    weather_data = None

    def __init__(self, weather_data):
        if isinstance(weather_data, WeatherData):
            self.weather_data = weather_data
            weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.nums += 1
        self.current_temp += temperature
        self.max_temp = max(self.max_temp, temperature)
        self.min_temp = min(self.min_temp, temperature)
        self.display()

    def display(self):
        print(f'Average temperature is {self.current_temp / self.nums}\n'
              f'Max temperature is {self.max_temp}\n'
              f'Min temperature is {self.min_temp}')
