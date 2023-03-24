import numpy as np

def arc(q, i):
    '''
    Calculates arc length by given intensity rate and inclination angle
    '''
    return np.degrees(30/q) * np.radians(i) 