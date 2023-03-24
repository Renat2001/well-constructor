from functools import singledispatchmethod
from formulas import *

class Segment:
    def __init__(self, length, inclination, azimuth) -> None:
        self.length = length
        self.inclination = inclination
        self.azimuth = azimuth

    def start(self):
        '''
        Returns end values for measured depth, inclination and azimuth respectively
        '''
        pass
    
    def end(self):
        '''
        Returns end values for measured depth, inclination and azimuth respectively
        '''
        pass

class KickOff(Segment):
    def __init__(self, length) -> None:
        super().__init__(length, 0, 0)

    def start(self):
        return 0, 0, 0
    
    def end(self):
        return self.length, 0, 0

class Build(Segment):
    def __init__(self, rate, inclination, azimuth) -> None:
        super().__init__(arc(rate, inclination), inclination, azimuth)
        self.rate = rate
        


