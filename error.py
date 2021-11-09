from tkinter import Tk
from tkinter.messagebox import showwarning, showerror
from sys import exit


def cfg_open_error():
    Tk().withdraw()
    showwarning(title='Warning', message='Can\'t open config.yaml, created a new defult config and the old is copied into \"config.yaml.bak\", you need to restart by hand')
    exit()

def cfg_length_error(length):
    Tk().withdraw()
    showerror(title='Error', message='config is too short, it must be at least 5 lines!\nNow is: {}'.format(length))
    exit()

def cfg_reading_error(line, info):
    Tk().withdraw()
    showerror(title='Error', message='line:{} {}'.format(line+1, info))
    exit()

def cfg_key_error():
    Tk().withdraw()
    showerror(title='Error', message='key error, the max number of key must be equal to key number(the number you set the key)')
    exit()

def cfg_keynum_error():
    Tk().withdraw()
    showerror(title='Error', message='key number error, it seems like you did not set any key')
    exit()

def cfg_tap_error():
    Tk().withdraw()
    showerror(title='Error', message='tap error, there are missed some tap setting in config.yaml, fix it or delete the config')
    exit()

def cfg_dis_error():
    Tk().withdraw()
    showerror(title='Error', message='display error, there are missed some display setting in config.yaml, fix it or delete the config')
    exit()

def img_error(img):
    Tk().withdraw()
    showerror(title='Error', message='image error, there are missed image in \'{}\', find it or reinstall'.format(img))
    exit()

def inside_error(info):
    Tk().withdraw()
    showerror(title='Inside_Error', message='inside error, there is an inside error, please contact me if necessary.\nInfo: {}'.format(info))
    exit()