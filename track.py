import numpy as np
import pandas as pd
from average_angle import *
from formulas import *

class Track:
    def __init__(self) -> None:
        # Initialize empty arrays for md, i and az
        self._md_ = np.array([0])
        self._inc_ = np.array([0])
        self._az_ = np.array([0])
        # Initialize empty arrays for east, north and tvd
        self._east_ = np.array([0])
        self._north_ = np.array([0])
        self._tvd_ = np.array([0])
        self._hd_ = np.array([0])

    def kickoff(self, l):
        # Initialize start points
        self.md_ = 0
        self.inc_ = 0
        self.az_ = 0
        # Initialize end points
        self._md = self.md_ + l
        self._inc = self.inc_
        self._az = self.az_
        # Initialize md, i and az arrays
        self._md_ = np.append(self._md_[:-1], np.linspace(self.md_, self._md, 1000)) 
        self._inc_ = np.append(self._inc_[:-1], np.linspace(self.inc_, self._inc, 1000))
        self._az_ = np.append(self._az_[:-1], np.linspace(self.az_, self._az, 1000))
        # Calculate average angle on each array
        for m1, m2, i1, i2, a1, a2 in zip(self._md_[-1000:-1], np.roll(self._md_, -1)[-1000:-1], 
                                          self._inc_[-1000:-1], np.roll(self._inc_, -1)[-1000:-1],
                                          self._az_[-1000:-1], np.roll(self._az_, -1)[-1000:-1]):
            self._east_ = np.append(self._east_, delta_east(m1, m2, i1, i2, a1, a2))
            self._north_ = np.append(self._north_, delta_north(m1, m2, i1, i2, a1, a2))
            self._tvd_ = np.append(self._tvd_, delta_tvd(m1, m2, i1, i2))
            self._hd_ = np.append(self._hd_, delta_hd(m1, m2, i1, i2))

    def hold(self, l):
        # Initialize start points
        self.md_ = self._md
        self.inc_ = self._inc
        self.az_ = self._az
        # Initialize end points
        self._md = self._md + l
        self._inc = self._inc
        self._az = self._az
        # Initialize md, i and az arrays
        self._md_ = np.append(self._md_[:-1], np.linspace(self.md_, self._md, 1000)) 
        self._inc_ = np.append(self._inc_[:-1], np.linspace(self.inc_, self._inc, 1000))
        self._az_ = np.append(self._az_[:-1], np.linspace(self.az_, self._az, 1000))
        # Calculate average angle on each array
        for m1, m2, i1, i2, a1, a2 in zip(self._md_[-1000:-1], np.roll(self._md_, -1)[-1000:-1], 
                                          self._inc_[-1000:-1], np.roll(self._inc_, -1)[-1000:-1],
                                          self._az_[-1000:-1], np.roll(self._az_, -1)[-1000:-1]):
            self._east_ = np.append(self._east_, delta_east(m1, m2, i1, i2, a1, a2))
            self._north_ = np.append(self._north_, delta_north(m1, m2, i1, i2, a1, a2))
            self._tvd_ = np.append(self._tvd_, delta_tvd(m1, m2, i1, i2))
            self._hd_ = np.append(self._hd_, delta_hd(m1, m2, i1, i2))

    def build(self, q, inc, az):
        # Initialize start points
        self.md_ = self._md
        self.inc_ = self._inc
        self.az_ = self._az
        # Initialize end points
        self._md = self._md + arc(q, inc-self.inc_)
        self._inc = inc
        self._az = az
        # Initialize md, i and az arrays
        self._md_ = np.append(self._md_[:-1], np.linspace(self.md_, self._md, 1000)) 
        self._inc_ = np.append(self._inc_[:-1], np.linspace(self.inc_, self._inc, 1000))
        self._az_ = np.append(self._az_[:-1], np.linspace(self.az_, self._az, 1000))
        # Calculate average angle on each array
        for m1, m2, i1, i2, a1, a2 in zip(self._md_[-1000:-1], np.roll(self._md_, -1)[-1000:-1], 
                                          self._inc_[-1000:-1], np.roll(self._inc_, -1)[-1000:-1],
                                          self._az_[-1000:-1], np.roll(self._az_, -1)[-1000:-1]):
            self._east_ = np.append(self._east_, delta_east(m1, m2, i1, i2, a1, a2))
            self._north_ = np.append(self._north_, delta_north(m1, m2, i1, i2, a1, a2))
            self._tvd_ = np.append(self._tvd_, delta_tvd(m1, m2, i1, i2))
            self._hd_ = np.append(self._hd_, delta_hd(m1, m2, i1, i2))

    def drop(self, q, inc, az):
        # Initialize start points
        self.md_ = self._md
        self.inc_ = self._inc
        self.az_ = self._az
        # Initialize end points
        self._md = self._md + arc(q, self.inc_-inc)
        self._inc = inc
        self._az = az
        # Initialize md, i and az arrays
        self._md_ = np.append(self._md_[:-1], np.linspace(self.md_, self._md, 1000)) 
        self._inc_ = np.append(self._inc_[:-1], np.linspace(self.inc_, self._inc, 1000))
        self._az_ = np.append(self._az_[:-1], np.linspace(self.az_, self._az, 1000))
        # Calculate average angle on each array
        for m1, m2, i1, i2, a1, a2 in zip(self._md_[-1000:-1], np.roll(self._md_, -1)[-1000:-1], 
                                          self._inc_[-1000:-1], np.roll(self._inc_, -1)[-1000:-1],
                                          self._az_[-1000:-1], np.roll(self._az_, -1)[-1000:-1]):
            self._east_ = np.append(self._east_, delta_east(m1, m2, i1, i2, a1, a2))
            self._north_ = np.append(self._north_, delta_north(m1, m2, i1, i2, a1, a2))
            self._tvd_ = np.append(self._tvd_, delta_tvd(m1, m2, i1, i2))
            self._hd_ = np.append(self._hd_, delta_hd(m1, m2, i1, i2))

    def finish(self):
        self._east_ = np.cumsum(self._east_)
        self._north_ = np.cumsum(self._north_)
        self._tvd_ = np.cumsum(self._tvd_)
        self._hd_ = np.cumsum(self._hd_)
        self._x_ = self._east_
        self._y_ = self._north_
        self._z_ = np.negative(self._tvd_)
        return pd.DataFrame(np.c_[self._east_, self._north_, self._tvd_, 
                                  self._hd_, self._md_, self._inc_, 
                                  self._az_, self._x_, self._y_, self._z_],
                            columns=['east', 'north', 'tvd', 'hd', 'md', 
                                     'inc', 'az', 'x', 'y', 'z'])
    
    def set_step(self, step):
        df = self.finish()
        endpoint = self._md_[-1]
        md = np.arange(0, endpoint+step, step)
        stepdf = pd.DataFrame()
        for c in df.columns:
            stepdf[c] = np.interp(md, df['md'].values, df[c].values)
        return stepdf


    