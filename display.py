import error
from tkinter import Tk, Canvas, PhotoImage
from tkinter.constants import *
from sys import exit
#from sys import exit
#from numpy import square
from math import floor, pow
from time import perf_counter
import PIL.ImageTk
import PIL.Image

class main:

    def __init__(self, all_key, akey,                   keynum=2, 
                       show_plate=True,                 plate_change_color=True, plate_base_color='#00ffff',
                       show_akey_kps=True,              akey_change_color=False, akey_base_color=('black','black'),    akey_text_size=(120,25),
                       show_key_kps=True,               key_change_color=True,   
                       show_key_button=True,            key_button_effect=True,
                       color_stepmul=(0.6, 1.5, 1.8),   arc_center_mul=4,        effct_mul=0.6, 
                       kn_base_color=('black','black'), kn_text_size=(40,40),    kn_position=((200, 340), (300, 340)), kn_size=((75, 75),(75,75)),
                       ####################################################################################
                       show_lag=False, window_name='Kps_Sensor'):

        self.all_key, self.akey = all_key, akey
        self.keynum = keynum
        self.sp,   self.pcc,  self.pbc            = show_plate,      plate_change_color, plate_base_color
        self.sak,  self.acc,  self.abc, self.ats  = show_akey_kps,   akey_change_color,  akey_base_color,  akey_text_size
        self.skk,  self.kcc,                      = show_key_kps,    key_change_color
        self.skbt, self.kbte                      = show_key_button, key_button_effect
        self.knbc, self.knts, self.knp, self.kns  = kn_base_color,  kn_text_size, kn_position, kn_size
        ########################################################################################
        self.csm = color_stepmul
        self.acm = arc_center_mul
        self.em = effct_mul
        self.show_lag = show_lag

        self.frames = 0
        self.time = perf_counter()
        self.ptime = self.time
        self.hun_time = 0.0

        self.kbwin = Tk()
        try: self.kbwin.iconbitmap('pht/kps.ico')
        except: error.img_error('kps.ico')
        self.kbwin.title(window_name)
        self.kbwin.geometry('500x500')
        self.kbwin.resizable(width=False, height=False)
        self.kbwin.protocol('WM_DELETE_WINDOW', self.close_window)
        self.cv = Canvas(self.kbwin, width=500, height=500)

        self.arc = self.cv.create_arc(0, 0, 500, 500, width=0, fill=self.pbc, outline=self.pbc, start=240, extent=-0,)
        # open all the image
        self.key_image = []
        self.keyup_image = []
        self.keydown_image = []
        self.keyeffect_image = []
        self.dkey_image_file = ['']*10
        try: self.plate_image = PIL.Image.open('pht/bg.png').resize((500,500), PIL.Image.ANTIALIAS)
        except: error.img_error('bg.png')
        self.main_image_file = PIL.ImageTk.PhotoImage(self.plate_image)
        self.main_image = self.cv.create_image(250, 250, anchor='center', image=self.main_image_file)
        if self.skbt:
            for i in range(self.keynum):
                self.key_image += [self.cv.create_image(*self.knp[i], anchor='center',image='')]
                try: self.keyup_image += [PIL.Image.open('pht/key{}_up.png'.format(i+1)).resize(self.kns[i], PIL.Image.ANTIALIAS)]
                except: error.img_error('key{}_up.png'.format(i+1))
                try: self.keydown_image += [PIL.Image.open('pht/key{}_down.png'.format(i+1)).resize(self.kns[i], PIL.Image.ANTIALIAS)]
                except: error.img_error('key{}_down.png'.format(i+1))
                try: self.keyeffect_image += [PIL.Image.open('pht/key{}_effect.png'.format(i+1)).resize(self.kns[i], PIL.Image.ANTIALIAS)]
                except: error.img_error('key{}_effect.png'.format(i+1))

        if self.sak:
            self.KPS_text = self.cv.create_text(350, 250, anchor='e', text='', fill=self.abc[0], justify = CENTER, font=('Visitor TT2 (BRK)', self.ats[0], 'bold'))
            self.KPS_text1 = self.cv.create_text(370, 275, text='Loading',fill=self.abc[1],justify = CENTER, font=('Visitor TT2 (BRK)', self.ats[1]))
        if self.show_lag:
            self.cal_lag = self.cv.create_text(495, 495, anchor='se', text='', justify=RIGHT, font=('Calibri', 10))
            self.dis_lag = self.cv.create_text(495, 480, anchor='se', text='', justify=RIGHT, font=('Calibri', 10))
        if self.skk:
            self.key_text = []
            for i in range(self.keynum):
                self.key_text += [self.cv.create_text(*self.knp[i], text='', anchor='center',fill=self.knbc[i],justify=CENTER, font=('Visitor TT2 (BRK)', self.knts[i], 'bold'))]
        self.cv.pack()

        self.first = True

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
        
    def start(self):
        def pframe():
            self._cal_time()
            if self.all_key[1].frames < 100:
                pass
            else:
                if self.first:
                    self.cv.itemconfigure(self.KPS_text1, text='Kps')
                    self.first = False
                KPS, kkps, kp, kdp=self.akey.dKPS, [], [], []
                for i in range(self.keynum):
                    kkps += [self.all_key[i].dKPS]
                    kp += [self.all_key[i].position]
                    kdp += [self.all_key[i].dposition]
                
                self.change_text(KPS, kkps)
                if self.sp:
                    self.change_arc(KPS)
                if self.skbt:
                    self.change_key(kp, kdp)

            if self.show_lag:
                self.Show_lag()
            self.kbwin.after(20, pframe)

        self.kbwin.after(0, pframe)
        self.kbwin.mainloop()

    def change_text(self, KPS, kkps):
        if self.sak:
            kps_str = '{:.1f}'.format(KPS)
            self.cv.itemconfigure(self.KPS_text, text=kps_str)
            if self.acc:
                self.cv.itemconfigure(self.KPS_text, fill=self.cal_color(KPS, self.keynum))
        if self.skk:
            for i in range(self.keynum):
                kps_str = '{:.1f}'.format(kkps[i])
                self.cv.itemconfigure(self.key_text[i], text=kps_str)
            if self.kcc:
                for i in range(self.keynum):
                    self.cv.itemconfigure(self.key_text[i], fill=self.cal_color(kkps[i]))

    def change_arc(self, KPS):
        self.cv.itemconfigure(self.arc, extent=-self.cal_angle(KPS))
        if self.pcc:
            color = self.cal_color(KPS,self.keynum)
            self.cv.itemconfigure(self.arc, fill=color, outline=color)

    def cal_angle(self, KPS):
        center = self.acm * self.keynum
        if KPS <= center:
            angle = (KPS/center)*150
        else:
            angle = 300 - (150*pow(center/KPS, 2))
        return angle

    def cal_color(self, KPS, keynum=1):
        R, G, B = 0, 255, 255
        step1 = self.acm * keynum * self.csm[0]
        step2 = self.acm * keynum * self.csm[1]
        step3 = self.acm * keynum * self.csm[2]
        if KPS <= step1:
            B = floor(255 - pow(KPS/step1, 2)*255)
        elif KPS <= step2:
            B = 0
            R = floor(pow((KPS-step1)/(step2-step1), 2)*255)
            G = floor(255 - pow((KPS-step1)/(step2-step1), 2)*55)
        elif KPS <= step3:
            B = 0
            R = 255
            G = floor(200 - pow((KPS-step2)/(step3-step2), 2)*200)
        else:
            B = floor(255 - pow(step3/KPS, 2)*255)
            R = floor(155 + pow(step3/KPS, 2)*100)
            G = 0
        return self.RGB2hex(R, G, B)

    def change_key(self, keyp_args, keydp_args):
        for i in range(self.keynum):
            if self.kbte:
                if keyp_args[i]:
                    dkey_image = PIL.Image.blend(self.keydown_image[i], self.keyeffect_image[i], keydp_args[i]*self.em)
                else:
                    dkey_image = PIL.Image.blend(self.keyup_image[i], self.keyeffect_image[i], keydp_args[i]*self.em)
            else:
                dkey_image = self.keydown_image[i] if keyp_args[i] else self.keyup_image[i]

            self.dkey_image_file[i] = PIL.ImageTk.PhotoImage(dkey_image)
            self.cv.itemconfigure(self.key_image[i],image=self.dkey_image_file[i])

    def Show_lag(self):
        cal_lag = 0.0
        dis_lag = 0.0

        if self.all_key[0].frames <= 100:
            pass
        else:
            allkey_lag = 0.0
            for i in range(self.keynum):
                perkey_lag = (self.all_key[i].hun_time/100)-0.01
                allkey_lag += perkey_lag
            cal_lag = (allkey_lag/self.keynum)*1000

        if self.frames <= 100:
            pass
        else:
            dis_lag = ((self.hun_time/100)-0.02)*1000

        self.cv.itemconfigure(self.cal_lag, text='cal: {:.2f} ms'.format(cal_lag))
        self.cv.itemconfigure(self.dis_lag, text='dis: {:.2f} ms'.format(dis_lag))

################################################
    def close_window(self):
        self.akey.is_openning = False
        exit()

    @staticmethod
    def RGB2hex(R=int, G=int, B=int):
        def check(colornum):
            if colornum > 255:
                return 255
            elif colornum < 0:
                return 0
            else:
                return colornum

        RGBhex = '#'
        Rstr = ('%x'%check(R)).zfill(2)
        Gstr = ('%x'%check(G)).zfill(2)
        Bstr = ('%x'%check(B)).zfill(2)
        RGBhex += (Rstr+Gstr+Bstr)
        return RGBhex

