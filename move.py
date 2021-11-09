from win32api import GetCursorPos,GetSystemMetrics
from time import perf_counter, sleep
from math import hypot

class main:
    def __init__(self, basemul=10):
        # staticmethod
        self.m = basemul
        self.systemMetrics = GetSystemMetrics(1)
        # time
        self.frames = 0
        self.time = perf_counter()
        self.ptime = self.time
        self.hun_time = 0.0
        # speed
        self.posx = 0
        self.posy = 0
        self.pposx = 0
        self.pposy = 0
        self.dposx = 0
        self.dposy = 0
        self.pixel_speed = 0.0
        self.dspeed = 0.0
        # exit
        self.is_openning = True
        

    def _cal_time(self):
        if self.frames == 0:
            self.time = perf_counter()
            self.frames += 1
        else:
            self.ptime = self.time
            self.time = perf_counter()
            dt = self.time - self.ptime
            self.hun_time += dt

        if self.frames <= 100:
            self.frames += 1
        else:
            self.hun_time -= (self.hun_time / 100)
        return self.hun_time

    def _cal_pixel_speed(self):
        if self.frames >= 99:
            self.pposx = self.posx
            self.pposy = self.posy
        self.posx = GetCursorPos()[0]
        self.posy = GetCursorPos()[1]
        if self.frames >= 100:
            self.pixel_speed = hypot(self.posx-self.pposx, self.posy-self.pposy)/(self.hun_time/100)
        return self.pixel_speed

    def _cal_dspeed(self):
        if self.frames >= 100:
            speed = self.pixel_speed/self.systemMetrics
            if self.dspeed > 1:
                self.dspeed += ((speed - self.dspeed)/(self.m))
            else:
                a = (speed + 1)/(self.m<<1)
                if self.dspeed > (speed + a):
                    self.dspeed -= a
                elif self.dspeed < speed:
                    self.dspeed += a
                elif self.dspeed != 0:
                    self.dspeed = 0

    def start(self):
        while self.is_openning:
            self._cal_time()
            try: self._cal_pixel_speed()
            except: pass
            self._cal_dspeed()
            sleep(0.01)

def _test():
    from threading import Thread
    m = main()
    bg_cal = Thread(target = m.start)
    bg_cal.start()

    while True:
        print('{:.1f},{:.1f}, ({:.1f}, {:.1f}), ({:.1f}, {:.1f})'.format(m.dspeed,m.pixel_speed,GetCursorPos()[0],GetCursorPos()[1],m.posx,m.posy))
        sleep(0.2)


if __name__ == "__main__":
    #print(GetSystemMetrics(0),GetSystemMetrics(1))
    #print(type(GetCursorPos()),GetCursorPos())
    _test()