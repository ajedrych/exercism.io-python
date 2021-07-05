earth_year = 31557600

planet_years = {'earth': 1, 'mercury': 0.2408467, 'venus': 0.61519726, 'mars': 1.8808158, 'jupiter': 11.862615,
    'saturn': 29.447498, 'uranus': 84.016846, 'neptune': 164.79132}

class SpaceAge(object):

    def __init__(self, seconds):
        self.seconds = seconds
        for planet in planet_years:
            self.__method_(planet)

    def _on_planet(self, planet):
        self.planet = planet
        return round(self.seconds / earth_year / planet_years[planet], 2)

    def __method_(self, planet):
        func = lambda: self._on_planet(planet)
        func.__name__ = "on_" + planet
        self.__setattr__(func.__name__, func)

    pass
