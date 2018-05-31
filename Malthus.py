from math import log
from math import exp
from math import pow

class Malthus:
    '''
    Use Malthus Model to calculate population.
    '''
    def __init__(self, t0 = None, p0 = None, t1=None, p1=None, _lambda=None):
        '''
        Args:
            t0: 任意時間點
            p0: 任意時間點的人口
            t1: 特定時間點
            p1: 特定時間點的人口
            _lambda: 可以代入已知constant
        '''
        self.t0 = t0
        self.p0 = p0
        self.t1 = t1
        self.p1 = p1
        self._lambda = _lambda

        if (_lambda == None and (t0 != None and p0 != None)) and t1 != None and p1 != None:
            self.calculate_lambda()
    
    
    def calculate_lambda(self, t1 = None, p1 = None):
        '''
        Calculate constant lambda
        '''
        try:
            _lambda = lambda _t1, _p1: log(_p1/self.p0)/(_t1-self.t0)
            if t1 != None and p1 != None:
                self._lambda = _lambda(t1, p1)
                return self._lambda
            else:
                self._lambda = _lambda(self.t1, self.p1)
                return self._lambda
        except:
            print("Error model!!!")
    

    def calculate_population(self, t1 = None):
        '''
        Calculate population
        args:
            t1: 特定時間
        '''
        try:
            _population = lambda _t1: self.p0 * pow(exp(1), self._lambda * (_t1 - self.t0))
            if t1 != None:
                self.population = _population(t1)
                return self.population
            else:
                self.population = _population(self.t1)
                return self.population
        except:
            print("Error model!!!")

if __name__ == "__main__":
    a = Malthus(1966, 1300e6, 1971.1, 1500e6)
    print("calculate lambda: ", a.calculate_lambda())
    print("calculate population: ", a.calculate_population(2000))