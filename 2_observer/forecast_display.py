from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


class ForecastDisplay(Observer, DisplayElement):
    current_pressure = 29.92
    last_pressure = 0
    weather_data = None

    def __init__(self, weather_data):
        if isinstance(weather_data, WeatherData):
            self.weather_data = weather_data
            weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        self.display()

    def display(self):
        print('Forecast: ')
        if self.current_pressure > self.last_pressure:
            print('Improving weather on the way!')
        elif self.current_pressure == self.last_pressure:
            print('More of the same')
        elif self.current_pressure < self.last_pressure:
            print('Watch out for cooler, rainy weather')
