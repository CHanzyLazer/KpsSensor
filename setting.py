import defultConfig
import error
from allCompile import *
from re import search, findall
import yaml
from shutil import copyfile

class main:
    def __init__(self):
        self.cfg_ok = False
        self.key_setting_list = ['']*10
        self.keynum = 0
        try: 
            file = open('config.yaml', 'r', encoding="utf-8")
            file_data = file.read()
            file.close()
            data = yaml.load(file_data, Loader=yaml.FullLoader)
        except:
            self._set2defult()
            error.cfg_open_error()

        key_setting = data['key_setting']
        tap_setting = data['tap_setting']
        dispaly_setting = data['dispaly_setting']
        key_dispaly_setting = data['key_dispaly_setting']

        for i in range(10):
            is_mouse = False
            ks_key = 'key{}'.format(i+1)
            valuestr = key_setting[ks_key]
            if valuestr == 'mleft' or valuestr == 'mright':
                is_mouse = True
                valuestr = valuestr[1:]
            if valuestr != None:
                self.key_setting_list[i] = [i+1,valuestr,is_mouse]
                self.keynum += 1
        self.key_setting = tuple(self.key_setting_list)

        self.tap_setting = tap_setting

        ds_key = 'keynum{}_setting'.format(self.keynum)
        self.dis_setting = dispaly_setting
        self.dis_setting.update(key_dispaly_setting[ds_key])

        self.cfg_ok = True

    @staticmethod
    def _set2defult():
        copyfile('config.yaml', 'config.yaml.bak')
        cfg = open('config.yaml', 'w')
        cfg.write(defultConfig.configfile)

    @staticmethod
    def remove_blank(s):
        out = s
        out = out.replace(' ','')
        out = out.replace('\n','')
        out = out.replace('\r','')
        out = out.replace('\t','')
        return out