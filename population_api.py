import requests
import json

api_url = "http://api.population.io/1.0/"

class population_api:
    '''
    api.population.io python api
    Author: Lo Ben (loben@illimited.cf)
    '''
    def __init__(self, country):
        self.country = country
        available_countries = self.all_countries() #find out which country have population result
        if (country not in available_countries):
            #print("Not available country!!!")
            pass
    
    def all_countries(self):
        '''
        list available countries.
        '''
        json_data = json.loads(requests.get(api_url+"/countries").text)
        result = json_data["countries"]
        result.remove("Australia/New Zealand")
        return result
    
    def wp_rank(self, dob = None, sex = None, country = None, require = None, date = None):
        '''
        determine world population rank.
        argv:
            dob (date string): the given date of birth, example: "1952-03-11"
            sex (string): the given sex, example: "male"
            country (string): the given country, example: "United Kingdom"
        return:
            rank (int): the calculated rank, example: 27228942
        '''

        if require == "today":
            payload = "{0}/wp-rank/{1}/{2}/{3}/{4}/".format(api_url, dob, sex, self.country, require)
            json_result = json.loads(requests.get(payload).text)
            return json_result['rank']
        
    def population_of_year(self, year = None):
        '''
        return all population of year in specific country.
        argv:
            year (int): the give year, example: 1980
            country(String): the given country, example:"United Kingdom"
        '''

        payload = "{0}/population/{1}/{2}".format(api_url, int(year), self.country) #construct url
        json_result = json.loads(requests.get(payload).text)
        
        sum_of_population = 0

        for n in json_result:
            #for debug
            print("Country: ", self.country, "\t n: ", n)
            sum_of_population += int(n['males']) + int(n['females'])
            #print(sum_of_population)

        return sum_of_population
    
    def population_of_year_interval(self, begin_year, end_year):
        result = {}
        for n in range(end_year - begin_year + 1):
            result[begin_year + n] = self.population_of_year(begin_year + n)
        return result
        

if __name__ == "__main__":
    '''
    a = population_api("Japan") #create class
    temp = a.wp_rank(dob = "2018-1-1", sex = "female", require = "today") #test wp_rank class
    #print("test wp_rank function:" + str(temp))
    print(a.population_of_year(1955))
    '''
    a = population_api("World") #create class
    a.all_countries()
    #print(a.population_of_year(1955))