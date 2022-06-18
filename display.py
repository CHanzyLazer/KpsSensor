import error
from time import sleep
from tkinter import Tk, Canvas, PhotoImage
from tkinter.constants import *
from sys import exit
from numpy import square
from math import floor
from time import perf_counter
import PIL.ImageTk
import PIL.Image
import PIL.ImageDraw

class main:
    def __init__(self, all_key, akey, move, keynum=4,
                 arc_tap_path=('skin/arc_tap_2.png',), arc_tap_position=(0,0),    arc_tap_anchor='TL',  arc_tap_size=(256,256),  arc_tap_range=(150,240),  arc_tap_cmul=0.8,      arc_tap_ccolor=True,   arc_tap_basecolor=(0,0,255),
                 arc_move_path=('skin/arc_move.png',), arc_move_position=(0,0),   arc_move_anchor='TL', arc_move_size=(256,256), arc_move_range=(150,240), arc_move_cmul=0.75,    arc_move_ccolor=False,   arc_move_basecolor=(0,0,255),
                 akps_font_path='skin/font/thin',      akps_position=(163,130),   akps_anchor='BR',     akps_size=25,            akps_gap=2,               akps_ccolor=False,     akps_basecolor=(0,255,255),
                 tapnum_font_path='skin/font/thin',    tapnum_position=(128,240), tapnum_anchor='BC',   tapnum_size=10,          tapnum_gap=2,
                 mtext_font_path='skin/font/thin',     mtext_position=(168,135),  mtext_anchor='BL',    mtext_size=(55,20),      mtext_gap=2,

                 key_button_path=(('skin/key3_up.png','skin/key4_up.png','skin/key5_up.png','skin/key6_up.png'),
                                  ('skin/key3_down.png','skin/key4_down.png','skin/key5_down.png','skin/key6_down.png'),
                                  ('skin/key3_effect.png','skin/key4_effect.png','skin/key5_effect.png','skin/key6_effect.png')),
                 key_button_position=((70,130),(105,130),(151,130),(186,130)),
                 key_button_anchor=('TC','TC','TC','TC'),
                 key_button_size=((110,110),(110,110),(110,110),(110,110)),

                 show_key_tapnum=False,
                 key_tapnum_font_path=('skin/font/thin','skin/font/thin','skin/font/thin','skin/font/thin'),
                 key_tapnum_position=((70,202),(105,202),(151,202),(186,202)), 
                 key_tapnum_anchor=('BC','BC','BC','BC'),   
                 key_tapnum_size=(7,7,7,7),
                 key_tapnum_gap=(0,0,0,0),

                 show_key_kps=False,
                 key_kps_font_path=('skin/font/thin','skin/font/thin','skin/font/thin','skin/font/thin'),
                 key_kps_position=((70,210),(105,210),(151,210),(186,210)), 
                 key_kps_anchor=('BC','BC','BC','BC'),   
                 key_kps_size=(8,8,8,8),
                 key_kps_gap=(0,0,0,0),
                 key_kps_ccolor=True,   key_kps_basecolor=(0,0,255),

                 show_arc_tap=True,
                 show_arc_move=True,

                 sensor_basecolor=(0,0,0),
                 center_num = 4,
                 diff_font = True,       font_path='skin/font/thin',
                 idle_Kps=0.1,           idle_speed=0.5,
                 key_button_effect=True, effect_mul=0.8,
                 step_color = ((0,255,255),(0,200,200),(200,200,0),(255,0,0),(100,0,180)), color_step=(0.6,1.2,1.8),
                 window_size=(256,256), window_name='Kps_Sensor', show_lag=False):

        self.all_key, self.akey = all_key, akey
        self.move = move
        self.keynum = keynum
        self.sensor_basecolor = sensor_basecolor
        self.center = center_num
        self.sat = show_arc_tap
        self.sam = show_arc_move

        self.akps_center = self.center*self.keynum
        if show_arc_tap:
            self.at_path,  self.at_pos,  self.at_anc,   self.at_size,   self.at_range, self.at_center,  self.at_ccolor, self.at_bcolor = arc_tap_path,     arc_tap_position,    arc_tap_anchor,    arc_tap_size,  arc_tap_range,  self.center*arc_tap_cmul*self.keynum,  arc_tap_ccolor, arc_tap_basecolor
        if show_arc_move:
            self.am_path,  self.am_pos,  self.am_anc,   self.am_size,   self.am_range, self.am_center,  self.am_ccolor, self.am_bcolor = arc_move_path,    arc_move_position,   arc_move_anchor,   arc_move_size, arc_move_range, self.center*arc_move_cmul,             arc_move_ccolor, arc_move_basecolor
        self.ak_pos,   self.ak_anc,  self.ak_size,  self.ak_gap,    self.ak_ccolor, self.ak_bcolor                                 =                   akps_position,       akps_anchor,       akps_size,     akps_gap,                                              akps_ccolor,     akps_basecolor
        self.tn_pos,   self.tn_anc,  self.tn_size,  self.tn_gap                                                                    =                   tapnum_position,     tapnum_anchor,     tapnum_size,   tapnum_gap
        self.mt_pos,   self.mt_anc,  self.mt_size,  self.mt_gap                                                                    =                   mtext_position,      mtext_anchor,      mtext_size,    mtext_gap
        self.kb_path,  self.kb_pos,  self.kb_anc,   self.kb_size                                                                   = key_button_path,  key_button_position, key_button_anchor, key_button_size
        
        self.sktn = show_key_tapnum
        if show_key_tapnum:
            self.ktn_pos,  self.ktn_anc, self.ktn_size, self.ktn_gap                                                                   =                   key_tapnum_position, key_tapnum_anchor, key_tapnum_size,  key_tapnum_gap
        self.skk = show_key_kps
        if show_key_kps:
            self.kk_pos,   self.kk_anc,  self.kk_size,  self.kk_gap ,  self.kk_ccolor, self.kk_bcolor                                  =                   key_kps_position,    key_kps_anchor,    key_kps_size,  key_kps_gap,                                           key_kps_ccolor,  key_kps_basecolor

        if diff_font: self.ak_path, self.tn_path, self.mt_path, self.ktn_path, self.kk_path = akps_font_path, tapnum_font_path, mtext_font_path, key_tapnum_font_path, key_kps_font_path
        else: self.ak_path, self.tn_path, self.mt_path, self.kk_path = font_path, font_path, font_path, font_path, [font_path]*self.keynum, [font_path]*self.keynum


        def set_data():
            self.tapnum = int(datalines[0])
            self.key_tapnum = []
            for i in range(1,11):
                self.key_tapnum += [int(datalines[i])]
        try:
            data = open('disData.dat', 'r')
            datalines = data.readlines()
            set_data()
        except:
            data = open('disData.dat', 'w')
            data.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n')
            datalines = ['0']*11
            set_data()

        self.idk,        self.ids        = idle_Kps,          idle_speed
        self.kbte,       self.em         = key_button_effect, effect_mul
        self.step_color, self.color_step = step_color,        color_step
        self.wins = window_size
        self.show_lag = show_lag

        self.frames = 0
        self.time = perf_counter()
        self.ptime = self.time
        self.hun_time = 0.0

        mt_path = (self.mt_path+'/Loading.png',self.mt_path+'/Kps.png',self.mt_path+'/Max.png')
        if self.sat: self.arc_tap    = displayArc( *self.at_pos, *self.wins, self.at_path, self.at_size,  self.at_ccolor,     fill=self.at_bcolor,  anchor=self.at_anc, start=self.at_range[0], end=self.at_range[0])
        if self.sam: self.arc_move   = displayArc( *self.am_pos, *self.wins, self.am_path, self.am_size,  self.am_ccolor,     fill=self.am_bcolor,  anchor=self.am_anc, start=self.am_range[0], end=self.am_range[0])
        self.akps_num   = displayNum( *self.ak_pos, *self.wins, self.ak_path, self.ak_size,  self.ak_ccolor,     fill=self.ak_bcolor,  anchor=self.ak_anc, value=0,                gap=self.ak_gap,     xf=1)
        self.tapnum_num = displayNum( *self.tn_pos, *self.wins, self.tn_path, self.tn_size,                                            anchor=self.tn_anc, value=self.tapnum,      gap=self.tn_gap,     xf=0)
        self.mtext      = displayVImg(self.wins[0]>>1, self.wins[1]>>1, *self.wins, mt_path, self.mt_size, anchor='CENTER', gap=self.mt_gap)
        self.key_button = []
        self.key_button_effect = []
        self.key_tapnum_num = []
        self.key_kps_num = []
        for i in range(self.keynum):
            self.key_button        += [displayVImg(*self.kb_pos[i],  *self.wins, (self.kb_path[0][i],self.kb_path[1][i]), self.kb_size[i],  anchor=self.kb_anc[i])]
            self.key_button_effect += [displayVImg(*self.kb_pos[i],  *self.wins, (self.kb_path[2][i],),                   self.kb_size[i],  anchor=self.kb_anc[i])]
            if self.sktn: self.key_tapnum_num    += [displayNum( *self.ktn_pos[i], *self.wins, self.ktn_path[i],                        self.ktn_size[i], anchor=self.ktn_anc[i], value=self.key_tapnum[i], gap=self.ktn_gap[i], xf=0)]
            if self.skk:  self.key_kps_num       += [displayNum( *self.kk_pos[i],  *self.wins, self.kk_path[i],      self.kk_size[i],  self.kk_ccolor, fill=self.kk_bcolor, anchor=self.kk_anc[i],  gap=self.kk_gap[i],       xf=1)]
        #self.baseimg = PIL.Image.open('lol.png').resize(self.wins, PIL.Image.ANTIALIAS)
        self.baseimg = PIL.Image.new('RGBA', self.wins, (*self.sensor_basecolor,255))
        

        self.kbwin = Tk()
        try: self.kbwin.iconbitmap('skin/kps.ico') 
        except: error.img_error('skin/kps.ico')
        self.kbwin.title(window_name)
        self.kbwin.geometry('{}x{}'.format(*self.wins))
        self.kbwin.resizable(width=False, height=False)
        self.kbwin.protocol('WM_DELETE_WINDOW', self.close_window)
        self.cv = Canvas(self.kbwin, width=self.wins[0], height=self.wins[1])
        disimgTK = PIL.ImageTk.PhotoImage(PIL.Image.alpha_composite(self.baseimg, self.mtext.disimg))
        self.main_img = self.cv.create_image(0, 0, anchor='nw', image=disimgTK)
        self.disimgTK = disimgTK

        if self.show_lag:
            self.tap_lag = self.cv.create_text(self.wins[0]-5, self.wins[1]-2,  anchor='se', text='', justify=RIGHT, font=('Calibri', 8))
            self.mov_lag = self.cv.create_text(self.wins[0]-5, self.wins[1]-10, anchor='se', text='', justify=RIGHT, font=('Calibri', 8))
            self.dis_lag = self.cv.create_text(self.wins[0]-5, self.wins[1]-20, anchor='se', text='', justify=RIGHT, font=('Calibri', 8))
        self.cv.pack()

        self.max_Kps = 0.0
        self.max_speed = 0.0
        self.first = True
        self.idle_tap = False
        self.pidle_tap = 0
        self.idle_move = False
        self.pidle_move = 0

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
            if self.all_key[0].frames < 100:
                pass
            else:
                if self.first:
                    self.mtext.set_option(position=self.mt_pos, anchor=self.mt_anc, display=1)
                    self.first = False

                KPS = self.akey.dKPS
                speed = self.move.dspeed
                self.max_Kps = KPS if KPS>self.max_Kps else self.max_Kps
                self.max_speed = speed if speed>self.max_speed else self.max_speed
                if self.akey.clearKPS == True: # known bug: press reset when not self.idle_idle will refresh self.max_KPS in next frame
                    self.max_Kps = 0.0
                    self._change_num(self.akps_num, self.max_Kps, self.akps_center)
                    #self.mtext.set_option(display=1)
                    self._display()
                    self.akey.clearKPS = False
                kkps, kp, kdp, key_tapnum = [], [], [], []
                for i in range(self.keynum):
                    kkps += [self.all_key[i].dKPS]
                    kp += [self.all_key[i].position]
                    kdp += [self.all_key[i].dposition]
                    key_tapnum += [self.key_tapnum[i]+self.all_key[i].alltap]
                tapnum = self.tapnum + self.akey.alltap

                if KPS < self.idk and not (1 in kp) and not self.idle_tap:
                    self.pidle_tap += 1
                elif KPS >= self.idk: 
                    self.mtext.set_option(display=1)
                    self.pidle_tap = 0
                    self.idle_tap = False
                if speed < self.ids and not self.idle_move:
                    self.pidle_move += 1
                elif speed >= self.ids: 
                    self.pidle_move = 0
                    self.idle_move = False

                if self.pidle_tap >= 25 and not self.idle_tap:
                    self.mtext.set_option(display=2)
                    self._change_num(self.akps_num, self.max_Kps, self.akps_center)
                    if self.sat: self._change_arc_tap(self.arc_tap, 0.0, self.at_center, self.akps_center)
                    self._save_data(tapnum,*tuple(key_tapnum))
                    self._display()
                    self.idle_tap = True
                if self.pidle_move >= 25 and not self.idle_move:
                    if self.sam: self._change_arc_move(self.arc_move, 0.0, self.center, self.akps_center)
                    self._display()
                    self.idle_move = True

                if not self.idle_tap:
                    self._change_num(self.akps_num, KPS, self.akps_center)
                    if self.sat: self._change_arc_tap(self.arc_tap, KPS, self.at_center, self.akps_center)
                    self._change_num(self.tapnum_num, tapnum)
                    self._change_button(self.key_button, kp, kdp)
                    for i in range(self.keynum):
                        if self.sktn: self._change_num(self.key_tapnum_num[i], key_tapnum[i])
                        if self.skk:  self._change_num(self.key_kps_num[i], kkps[i], self.center)
                if not self.idle_move:
                    if self.sam: self._change_arc_move(self.arc_move, speed, self.am_center, self.akps_center)
                if not (self.idle_tap and self.idle_move):
                    self._display()

            if self.show_lag:
                self._Show_lag()
            self.kbwin.after(30, pframe)

        self.kbwin.after(0, pframe)
        self.kbwin.mainloop()

    def _display(self):
        disimg = self.baseimg
        if self.sam: disimg = PIL.Image.alpha_composite(disimg, self.arc_move.disimg)
        if self.sat: disimg = PIL.Image.alpha_composite(disimg, self.arc_tap.disimg)
        disimg = PIL.Image.alpha_composite(disimg, self.akps_num.numimg)
        disimg = PIL.Image.alpha_composite(disimg, self.mtext.disimg)
        disimg = PIL.Image.alpha_composite(disimg, self.tapnum_num.numimg)
        for kb in self.key_button:
            disimg = PIL.Image.alpha_composite(disimg, kb.disimg)
        if self.sktn: 
            for ktnn in self.key_tapnum_num:
                disimg = PIL.Image.alpha_composite(disimg, ktnn.numimg)
        if self.skk: 
            for kkn in self.key_kps_num:
                disimg = PIL.Image.alpha_composite(disimg, kkn.numimg)

        disimgTK = PIL.ImageTk.PhotoImage(disimg)
        self.cv.itemconfigure(self.main_img, image=disimgTK)
        self.disimgTK = disimgTK

    def _change_num(self, num, value, center=None):
        if num.get_option('change_color'):
            color = self._cal_color(value, center)
            num.set_option(value=value, fill=color)
        else:
            num.set_option(value=value)


    def _change_arc_tap(self, arc, value, center, c_center):
        endangle = self.at_range[0]+self.at_range[1]*self._cal_angle(value, center)
        if arc.get_option('change_color'):
            color = self._cal_color(value, c_center)
            arc.set_option(end=endangle, fill=color)
        else:
            arc.set_option(end=endangle)

    def _change_arc_move(self, arc, value, center, c_center):
        endangle = self.am_range[0]+self.am_range[1]*self._cal_angle(value, center)
        if arc.get_option('change_color'):
            color = self._cal_color(value, c_center)
            arc.set_option(end=endangle, fill=color)
        else:
            arc.set_option(end=endangle)

    def _change_button(self, key_button, keyp_args, keydp_args):
        for i in range(self.keynum):
            key_button[i].set_option(display=1 if keyp_args[i] else 0)
            if self.kbte:
                key_button[i].disimg = PIL.Image.blend(key_button[i].disimg, self.key_button_effect[i].disimg, keydp_args[i]*self.em)

    def _cal_angle(self, value, center):
        if value <= center:
            angle = (value/center)*0.5
        else:
            angle = 1 - (0.5*square(center/value))
        return angle

    def _cal_color(self, value, center):
        RGB = [0,0,0]
        steps = (center*self.color_step[0],center*self.color_step[1],center*self.color_step[2])
        # self.step_color = ((0,255,255),(0,200,200),(200,200,0),(255,0,0),(100,0,180))
        if value <= steps[0]:
            for i in range(3):
                RGB[i] = floor(self.step_color[0][i] + (self.step_color[1][i]-self.step_color[0][i])*square(value/steps[0]))
        elif value <= steps[1]:
            for i in range(3):
                RGB[i] = floor(self.step_color[1][i] + (self.step_color[2][i]-self.step_color[1][i])*square((value-steps[0])/(steps[1]-steps[0])))
        elif value <= steps[2]:
            for i in range(3):
                RGB[i] = floor(self.step_color[2][i] + (self.step_color[3][i]-self.step_color[2][i])*square((value-steps[1])/(steps[2]-steps[1])))
        else:
            for i in range(3):
                RGB[i] = floor(self.step_color[3][i] + (self.step_color[4][i]-self.step_color[3][i])*(1-square((steps[2]-steps[1])/(value-steps[1]))))
        return tuple(RGB)

    def _Show_lag(self):
        tap_lag = 0.0
        mov_lag = 0.0
        dis_lag = 0.0

        if self.all_key[0].frames <= 100:
            pass
        else:
            allkey_lag = 0.0
            for i in range(self.keynum):
                perkey_lag = (self.all_key[i].hun_time/100)-0.01
                allkey_lag += perkey_lag
            tap_lag = (allkey_lag/self.keynum)*1000

        if self.move.frames <= 100:
            pass
        else:
            mov_lag = ((self.move.hun_time/100)-0.01)*1000

        if self.frames <= 100:
            pass
        else:
            dis_lag = ((self.hun_time/100)-0.03)*1000

        self.cv.itemconfigure(self.tap_lag, text='tap: {:.2f} ms'.format(tap_lag))
        self.cv.itemconfigure(self.mov_lag, text='mov: {:.2f} ms'.format(mov_lag))
        self.cv.itemconfigure(self.dis_lag, text='dis: {:.2f} ms'.format(dis_lag))

    def _save_data(self, *args):
        data = open('disData.dat', 'w')
        datastr = ''
        for i in range(11):
            try:
                datastr += '{}\n'.format(args[i])
            except:
                datastr += '0\n'
        data.write(datastr)

################################################
    def close_window(self):
        self.akey.is_openning = False
        self.move.is_openning = False
        sleep(0.1)
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

    #@staticmethod
    #def get_allpath(path='str'):

class displayCom:
    def get_option(self, key=None):
        return self._option if key==None else self._option[key]

    def _change_color(self, imgL, size, rgb):
        colorimg = PIL.Image.new('RGBA', size , (*rgb,255))
        return PIL.Image.composite(colorimg, self.noneimg, imgL)

    @staticmethod
    def get_pos(position, size, anchor):
        if anchor == 'BR':
            x = position[0] - size[0]
            y = position[1] - size[1]
        elif anchor == 'BL':
            x = position[0]
            y = position[1] - size[1]
        elif anchor == 'BC':
            x = position[0] - (size[0]>>1)
            y = position[1] - size[1]
        elif anchor == 'TR':
            x = position[0] - size[0]
            y = position[1]
        elif anchor == 'TL':
            x = position[0]
            y = position[1]
        elif anchor == 'TC':
            x = position[0] - (size[0]>>1)
            y = position[1]
        elif anchor == 'CENTER':
            x = position[0] - (size[0]>>1)
            y = position[1] - (size[1]>>1)
        else: error.inside_error('(display_003) BR BL BC or TR TL TC or CENTER')
        return x,y

class displayArc(displayCom):
    def __init__(self, x, y, bx, by, allpath, size, change_color=False, **kw):
        self._option = {
            'position'    : (x,y),
            'base_size'   : (bx,by), # cannot change
            'allpath'     : allpath, # cannot change
            'size'        : size, # cannot change
            'anchor'      : 'TL', # 'BR' 'BL' 'BC' or 'TR' 'TL' 'TC' or 'CENTER'
            'start'       : 0,
            'end'         : 0,
            'display'     : 0,
            'change_color': change_color,
            'fill'        : (0,0,0),
            }
        self.baseimg = PIL.Image.new('RGBA', self._option['base_size'], (0,0,0,0))
        self.disimg = self.baseimg.copy()
        self.allarcimg = []
        self.allarcimgL = []
        for path in self._option['allpath']:
            try: eachimg = PIL.Image.open(path).resize(self._option['size'], PIL.Image.NEAREST)
            except: error.img_error(path)
            self.allarcimg += [eachimg]
            if self._option['change_color']:
                self.allarcimgL += [eachimg.split()[3]]
        self.noneimg = PIL.Image.new('RGBA', self._option['size'], (255,255,255,0))
        self.baseL = PIL.Image.new('L', self._option['size'], 0)
        self.set_option(**kw)

    def set_option(self, **kw):
        for key in kw.keys():
            self._option[key] = kw[key]
        if self._option['change_color']:
            self.allarcimg[self._option['display']] =\
               self._change_color(self.allarcimgL[self._option['display']], self._option['size'], self._option['fill'])
        arcL = self.baseL.copy()
        drawarc = PIL.ImageDraw.Draw(arcL)
        drawarc.pieslice((0,0,*self._option['size']), self._option['start'], self._option['end'], fill=255)
        arcimg = PIL.Image.composite(self.allarcimg[self._option['display']], self.noneimg, arcL)
        self.disimg = self.baseimg.copy()
        self.disimg.paste(arcimg, self.get_pos(self._option['position'], self._option['size'], self._option['anchor']))
        return self.disimg

class displayNum(displayCom):
    def __init__(self, x, y, bx, by, path, size, change_color=False, **kw):
        self._option = {
            'position'    : (x,y),
            'base_size'   : (bx,by), # cannot change
            'path'        : path, # cannot change
            'point_size'  : (0,0), # cannot change
            'font_size'   : (0,0), # cannot change
            'value'       : 0,
            'xf'          : 0,
            'anchor'      : 'BR', # 'BR' 'BL' 'BC' or 'TR' 'TL' 'TC' or 'CENTER'
            'gap'         : 2,
            'change_color': change_color, # cannot change
            'fill'        : (0,0,0),
            }

        self.baseimg = PIL.Image.new('RGBA', self._option['base_size'], (0,0,0,0))
        self.numimg = self.baseimg.copy()
        try: self.point = PIL.Image.open(path+'/point.png')
        except: error.img_error(path+'/point.png')
        self._option['point_size'] = (floor((size/self.point.size[1])*self.point.size[0]), size)
        self.point = self.point.resize(self._option['point_size'], PIL.Image.NEAREST)
        if self._option['change_color']:
            self.pointL = self.point.split()[3]
        self.available_char = '0123456789.'
        self.noneimg_p = PIL.Image.new('RGBA', self._option['point_size'], (0,0,0,0))
        self.allnum = []
        self.allnumL = []
        try: origin_font_size = PIL.Image.open(path+'/1.png').size
        except: error.img_error(path+'/1.png')
        self._option['font_size'] = (floor((size/origin_font_size[1])*origin_font_size[0]), size)
        self.noneimg = PIL.Image.new('RGBA', self._option['font_size'], (0,0,0,0))
        for i in range(10):
            try: eachimg = PIL.Image.open(path+'/{}.png'.format(i)).resize(self._option['font_size'], PIL.Image.NEAREST)
            except: error.img_error(path+'/{}.png'.format(i))
            self.allnum += [eachimg]
            if self._option['change_color']:
                self.allnumL += [eachimg.split()[3]]
        self.set_option(**kw)

    def _change_color_p(self, imgL, size, rgb):
        colorimg = PIL.Image.new('RGBA', size , (*rgb,255))
        return PIL.Image.composite(colorimg, self.noneimg_p, imgL)

    def set_option(self, **kw):
        for key in kw.keys():
            self._option[key] = kw[key]
        self.numimg = self.baseimg.copy()

        text = '%*.*f'%(0,self._option['xf'],self._option['value'])
        textlen = len(text)
        x, y = self.get_pos(self._option['position'], (self._option['font_size'][0]*textlen+self._option['gap']*(textlen-1),self._option['font_size'][1]), self._option['anchor'])

        for char in text:
            if char in self.available_char:
                if char == '.':
                    if self._option['change_color']:
                        self.point =\
                           self._change_color_p(self.pointL, self._option['point_size'], self._option['fill'])
                    self.numimg.paste(self.point, (x,y))
                    x += self._option['point_size'][0]+self._option['gap']
                else:
                    num = int(char)
                    if self._option['change_color']:
                        self.allnum[num] =\
                           self._change_color(self.allnumL[num], self._option['font_size'], self._option['fill'])
                    self.numimg.paste(self.allnum[num], (x,y))
                    x += self._option['font_size'][0]+self._option['gap']
            else: error.inside_error('(display_002) 0123456789.')
        return  self.numimg

class displayVImg(displayCom):
    def __init__(self, x, y, bx, by, allpath, size, change_color=False, **kw):
        self._option = {
            'position'    : (x,y),
            'base_size'   : (bx,by), # cannot change
            'allpath'     : allpath, # cannot change
            'size'        : size, # cannot change
            'anchor'      : 'TL', # 'BR' 'BL' 'BC' or 'TR' 'TL' 'TC' or 'CENTER'
            'display'     : 0,
            'change_color': change_color,
            'fill'        : (0,0,0),
            }
        self.baseimg = PIL.Image.new('RGBA', self._option['base_size'], (0,0,0,0))
        self.disimg = self.baseimg.copy()
        self.noneimg = PIL.Image.new('RGBA', self._option['size'], (255,255,255,0))
        self.allimg = []
        self.allimgL = []
        for path in self._option['allpath']:
            try: eachimg = PIL.Image.open(path).resize(self._option['size'], PIL.Image.NEAREST)
            except: error.img_error(path)
            self.allimg += [eachimg]
            if self._option['change_color']:
                self.allimgL += [eachimg.split()[3]]
        self.set_option(**kw)

    def set_option(self, **kw):
        for key in kw.keys():
            self._option[key] = kw[key]
        self.disimg = self.baseimg.copy()
        if self._option['change_color']:
            self.allimg[self._option['display']] =\
                self._change_color(self.allimgL[self._option['display']], self._option['size'], self._option['fill'])
        self.disimg.paste(self.allimg[self._option['display']], self.get_pos(self._option['position'], self._option['size'], self._option['anchor']))
        return self.disimg


def _test1():
    arc1 = displayArc(0,0,500,500,500,500,('skin/arc_tap.png',), start=120, end=420)
    arc1.arcimg.save('arc_tap_1.png')
    arc1.set_option(position=(0,0,500,500), start=120, end=250)
    arc1.arcimg.save('arc_tap_2.png')

    num1 = displayNum(250,250,500,500,'skin/font/thin', 20)
    num1.numimg.save('num_1.png')
    num1.set_option(position=(200,200), text='123.233', gap=10, anchor='TR')
    num1.numimg.save('num_2.png')
    num1.set_option(position=(200,200), text='233.123', gap=5, anchor='TL')
    num1.numimg.save('num_3.png')

    vimg = displayVImg(250,250,500,500,('skin/font/thin/Kps.png', 'skin/font/thin/Max.png', 'skin/font/thin/Loading.png'), (110,40))
    vimg.disimg.save('vimg_1.png')
    vimg.set_option(position=(200,200), display=1, anchor='TR')
    vimg.disimg.save('vimg_2.png')
    vimg.set_option(position=(200,200), display=2, anchor='TL')
    vimg.disimg.save('vimg_3.png')

