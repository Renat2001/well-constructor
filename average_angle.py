import numpy as np

def delta_north(md1, md2, i1, i2, az1, az2):
    '''
    Takes measured depth, inclination and azimuth angles of two points
    and calculate delta north
    '''
    md = md2 - md1
    i = (i1 + i2)/2
    az = (az1 + az2)/2
    return md * np.sin(np.radians(i)) * np.cos(np.radians(az))

def delta_east(md1, md2, i1, i2, az1, az2):
    '''
    Takes measured depth, inclination and azimuth angles of two points
    and calculate delta east
    '''
    md = md2 - md1
    i = (i1 + i2)/2
    az = (az1 + az2)/2
    return md * np.sin(np.radians(i)) * np.sin(np.radians(az))

def delta_tvd(md1, md2, i1, i2):
    '''
    Takes measured depth, inclination and azimuth angles of two points
    and calculate delta true vertical depth
    '''
    md = md2 - md1
    i = (i1 + i2)/2
    return md * np.cos(np.radians(i))

def delta_hd(md1, md2, i1, i2):
    '''
    Takes measured depth, inclination and azimuth angles of two points
    and calculate delta horizontal displacement
    '''
    md = md2 - md1
    i = (i1 + i2)/2
    return md * np.sin(np.radians(i))