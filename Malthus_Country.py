from Malthus import *
from population_api import *

class Malthus_Country:
    def __init__(self, country, default_begin_year = 1980, interval = 10):
        self.country = country
        self.default_begin_year = default_begin_year
        self.interval = interval

        self.get_essential_info() #get population to build up Malthus Module
        self.math_obj() #build up Malthus Module
    
    def get_essential_info(self):
        self.p0 = population_api(self.country).population_of_year(self.default_begin_year)
        self.p1 = population_api(self.country).population_of_year(self.default_begin_year + self.interval)

    def math_obj(self):
        self.Malthus_obj = Malthus(self.default_begin_year, self.p0, self.default_begin_year + self.interval, self.p1)

    def get_population_of_year(self, year):
        return int(self.Malthus_obj.calculate_population(year))

    def get_interval_population(self, begin_year, end_year):
        result = {}
        for n in range(end_year - begin_year + 1):
            result[begin_year + n] = self.get_population_of_year(begin_year + n)
        return result

def main():
    a = Malthus_Country("World")
    print(a.get_interval_population(1990, 2012))

if __name__ == "__main__":
    main()