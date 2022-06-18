from keyboard import is_pressed
from mouse import is_pressed as m_is_pressed
from time import perf_counter, sleep
from math import fabs
#from multiprocessing import Process

class main:
    def __init__(self, all_key, akey):
        self.all_key = all_key
        self.akey = akey

    def start(self):
        while self.akey.is_openning:
            KPS = 0
            allkeytap = 0
            for keyn in self.all_key:
                keyn._cal_time()
                keyn._trigger()
                keyn._cal_dposition()
                KPS += keyn._cal_KPS()
                keyn._cal_dKPS()
                allkeytap += keyn.alltap
            self.akey._cal_KPS(KPS)
            self.akey._cal_dKPS()
            self.akey.check_reset_maxKPS()
            self.akey.alltap = allkeytap
            sleep(0.01)

class allKey:
    def __init__(self, dposition_decrease= 0.05, tapframes = 100, need_standframes = 100, basemul = 10, decrease_lv = 2, zero_decrease_lv = 1):
        # staticmethod
        self.tapframes = tapframes
        self.minkps = (100/self.tapframes)
        self.nsf = need_standframes
        self.nsf2 = self.nsf<<2
        self.m = basemul
        self.dl = decrease_lv
        self.zdl = zero_decrease_lv
        # trigger
        self.keypev = False
        self.__tapmun = 0
        self.__tapint = 0
        # kps
        self.alltap = 0
        self.KPS = 0
        self.dKPS = 0
        self.clearKPS = False
        self.standframes = 0
        self.stand_all_KPS = 0
        # exit
        self.is_openning = True

    def _cal_KPS(self, KPS):
        self.KPS = KPS

    def __change_dKPS(self):
        self.dKPS += ((self.KPS - self.dKPS)/self.m)

    def __change_dKPS_dl(self):
        self.dKPS += ((self.KPS - self.dKPS)/(self.m<<self.dl))

    def __change_dKPS_stand(self):
        self.dKPS = self.stand_all_KPS/self.standframes

    def __change_dKPS_stand2(self):
        self.dKPS = self.stand_all_KPS/self.nsf2

    def __change_dKPS_w2(self):
        a = (self.KPS + 0.3)/(self.m<<self.zdl)
        if self.dKPS > (self.KPS + a):
            self.dKPS -= a
        elif self.dKPS < self.KPS:
            self.dKPS += a
        elif self.dKPS != 0:
            self.dKPS = 0

    def _cal_dKPS(self):
        if fabs(self.KPS - self.dKPS) <= (self.minkps) and (self.KPS != 0):  # KPS is going to stand, and KPS is not zero
            if self.standframes < self.nsf:
                self.standframes += 1
                self.stand_all_KPS += self.KPS
                self.__change_dKPS_dl()
            elif self.standframes < self.nsf2:                               # KPS is standed
                self.standframes += 1
                self.stand_all_KPS += self.KPS
                self.__change_dKPS_stand()
            else:
                self.stand_all_KPS += self.KPS
                self.stand_all_KPS -= self.dKPS
                self.__change_dKPS_stand2()
        else:                                                                # KPS is not standed
            self.stand_all_KPS = 0
            self.standframes = 0
            if fabs(self.KPS - self.dKPS) <= (self.minkps) and (self.KPS == 0):  # KPS is close to zero
                self.__change_dKPS_w2()
            else:
                self.__change_dKPS()                                         # KPS is not stand

        return self.dKPS
    
    def check_reset_maxKPS(self):
        if is_pressed("ctrl+r"):
            self.clearKPS = True

class key(allKey):
    def __init__(self, keynum, keystr, is_mouse = False, dposition_decrease= 0.05, tapframes = 100, need_standframes = 100, basemul = 10, decrease_lv = 2, zero_decrease_lv = 1):
        # staticmethod
        self.keynum = keynum
        self.keystr = keystr
        self.tapframes = tapframes
        self.minkps = (100/self.tapframes)
        self.nsf = need_standframes
        self.nsf2 = self.nsf<<2
        self.m = basemul
        self.dl = decrease_lv
        self.zdl = zero_decrease_lv
        self.dpd = dposition_decrease
        self.is_mouse = is_mouse
        # trigger
        self.keypev = 0
        self.__tapmun = 0
        self.__tapint = 0
        # kps
        self.alltap = 0
        self.KPS = 0
        self.frames = 0
        self.time = 0
        self.ptime = 0
        self.hun_time = 0
        self.dKPS = 0.0
        self.standframes = 0
        self.stand_all_KPS = 0
        # key position
        self.position = 0
        self.dposition = 0.0
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

    def _keytap(self):
        self.alltap += 1
        #print("key{}:{}".format(self.keynum, self.alltap))

    def _tapint1(self):
        self.__tapint = self.__tapint<<1
        self.__tapint = self.__tapint^((self.__tapint>>self.tapframes)<<self.tapframes)
        self.__tapint = self.__tapint^1

    def _tapint0(self):
        self.__tapint = self.__tapint<<1
        self.__tapint = self.__tapint^((self.__tapint>>self.tapframes)<<self.tapframes)
        
    def _trigger_keyposition(self):
        if is_pressed(self.keystr):
            self.position = 1
        else:
            self.position = 0

    def _trigger_mouseposition(self):
        if m_is_pressed(self.keystr):
            self.position = 1
        else:
            self.position = 0

    def _trigger_tap(self):
        if self.position and not self.keypev:
            self._tapint1()
            self._keytap()
            #print(Key.KPS)
        else:
            self._tapint0()
        self.keypev = self.position

    def _trigger(self):
        if self.is_mouse:
            self._trigger_mouseposition()
        else:
            self._trigger_keyposition()
        self._trigger_tap()

    def _cal_KPS(self):
        if self.frames > 100:
            self.__tapmun = 0
            a = self.__tapint
            while a != 0:
                a = a&(a - 1)
                self.__tapmun += 1
            self.KPS = self.__tapmun/((self.tapframes/100)*self.hun_time)
        return self.KPS

    def _cal_dposition(self):
        if self.frames > 100:
            if self.position:
                self.dposition = 1.0
            elif self.dposition > self.dpd :
                self.dposition -= self.dpd*(self.hun_time/1.0)
            else:
                self.dposition = 0
        return self.dposition


def _test():
    from threading import Thread
    # (self, keynum, keystr, tapframes = 100, need_standframes = 100, basemul = 10, decrease_lv = 2, zero_decrease_lv = 2, dposition_decrease= 0.05, is_mouse = False)
    # (self, tapframes = 100, need_standframes = 100, basemul = 10, decrease_lv = 2, zero_decrease_lv = 2)
    setting = (30, 50, 15, 2, 0)

    key1 = key(1, 'a', *setting)
    key2 = key(2, 's', *setting)
    key3 = key(3, 'z', *setting)
    key4 = key(4, 'x', *setting)
    key5 = key(5, '2', *setting)
    key6 = key(6, '3', *setting)
    all_key = (key1, key2, key3, key4, key5, key6)
    akey = allKey(*setting)
    m = main(all_key, akey)

    bg_cal = Thread(target = m.start)
    bg_cal.start()

    while True:
        print(m.akey.dKPS)
        sleep(0.2)

if __name__ == "__main__":
    _test()







