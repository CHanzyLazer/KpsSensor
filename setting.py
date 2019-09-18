import defultConfig
import error
from allCompile import *
from re import search, findall


class main:
    def __init__(self):
        self.cfg_ok = False
        self.key_setting_list = ['']*10
        self.tap_setting_list = ['', '', '', '', '', '']
        self.dis_setting_list = ['', 
                                   '', '', '',
                                   '', '', '', '',
                                   '', '',
                                   '', '',
                                   '', '', '', 
                                   '', '', '','',
                                   '', '']
        self.keynum = 0
        try:
            cfg = open('config.cfg', 'r')
            cfglines = cfg.readlines()
        except:
            self._set2defult()
            error.cfg_open_error()

        lineslen = len(cfglines)
        if lineslen < 4:
            error.cfg_length_error(lineslen)

        self.cfgnblines = []
        for line in cfglines:
            self.cfgnblines += [self.remove_blank(line)]

        for i in range(lineslen):
            line = self.cfgnblines[i]
            if line != '':
                if line[0] == '%':
                    self._get_key_setting(line, i)
                    #print(self.key_setting_list)
                if line[0] == '@':
                    self._get_tap_setting(line, i)
                    #print(self.tap_setting_list)
        self._check_key()
        if self.keynum == 0:
            error.cfg_keynum_error()
        self.dis_setting_list[0] = self.keynum
        self._check_tap()

        for i in range(lineslen):
            line = self.cfgnblines[i]
            if line != '':
                if line[0] == '&':
                    try:
                        marknum = line[1]
                    except:
                        error.cfg_reading_error(i, 'wrong name(200)')
                    if marknum == '0':
                        self._get_dis_setting0(line, i)
                        #print(self.dis_setting_list)
                    elif marknum == '1':
                        self._get_dis_setting1(line, i)
                        #print(self.dis_setting_list)
                    else:
                        error.cfg_reading_error(i, 'wrong mark(200), do not change the number behind \'&\'')

        self._check_dis()
        self.key_setting = tuple(self.key_setting_list)
        self.tap_setting = tuple(self.tap_setting_list)
        self.dis_setting = tuple(self.dis_setting_list)
        self.cfg_ok = True


    def _get_key_setting(self, line, linenum):
        name = search(key_setting_compile_name, line)
        if name == None:
            error.cfg_reading_error(linenum, 'wrong name(00)')
        namestr = name.group(0)
        if namestr not in key_setting_name:
            error.cfg_reading_error(linenum, 'wrong name(01)')
        nameans = key_setting_compile_value[namestr]
        value = search(nameans[1], line)
        if value == None:
            error.cfg_reading_error(linenum, 'wrong value(00), it must be \'a-z0-9,.\';[]+-*/`=\' or up/down/left/right/mlef/mright/space or none, case insensitive')
        valuestr = value.group(0).lower()
        if valuestr == 'none':
            pass
        else:
            is_mouse = False
            if valuestr == 'mleft' or valuestr == 'mright':
                is_mouse = True
                valuestr = valuestr[1:]
            if self.key_setting_list[nameans[0]] != '':
                error.cfg_reading_error(linenum, 'same name(00)')

            self.key_setting_list[nameans[0]] = (nameans[0]+1, valuestr, is_mouse)
            self.keynum += 1
           
    def _get_tap_setting(self, line, linenum):
        name = search(tap_setting_compile_name, line)
        if name == None:
            error.cfg_reading_error(linenum, 'wrong name(10)')
        namestr = name.group(0)
        if namestr not in tap_setting_name:
            error.cfg_reading_error(linenum, 'wrong name(11)')
        nameans = tap_setting_compile_value[namestr]
        value = search(nameans[1], line)
        if value == None:
            if nameans[2] == 'int':
                error.cfg_reading_error(linenum, 'wrong value(10), it must be integer')
            elif nameans[2] == 'float':
                error.cfg_reading_error(linenum, 'wrong value(11), it must be integer or float')
        valuestr = value.group(0).lower()
        ###########################
        if nameans[2] == 'int':
            try:
                valueout = int(valuestr)
            except:
                error.cfg_reading_error(linenum, 'wrong value(12), it must be integer')
            if valueout >= nameans[3][0] and valueout <= nameans[3][1]: pass
            else:
                error.cfg_reading_error(linenum, 'wrong value(14), it must be in {}'.format(nameans[3]))
        ###########################
        elif nameans[2] == 'float':
            try:
                valueout = float(valuestr)
            except:
                error.cfg_reading_error(linenum, 'wrong value(13), it must be integer or float')
            if valueout >= nameans[3][0] and valueout <= nameans[3][1]: pass
            else:
                error.cfg_reading_error(linenum, 'wrong value(14), it must be in {}'.format(nameans[3]))
        ###########################
        self.tap_setting_list[nameans[0]] = valueout


    def _get_dis_setting0(self, line, linenum):
        name = search(dis_setting0_compile_name, line)
        if name == None:
            error.cfg_reading_error(linenum, 'wrong name(210)')
        namestr = name.group(0)
        if namestr not in dis_setting0_name:
            error.cfg_reading_error(linenum, 'wrong name(211)')
        nameans = dis_setting0_compile_value[namestr]
        value = search(nameans[1], line)
        if value == None:
            if nameans[2] == 'float':
                error.cfg_reading_error(linenum, 'wrong value(200), it must be integer or float')
            elif nameans[2] == 'bool':
                error.cfg_reading_error(linenum, 'wrong value(201), it must be true or false, case insensitive')
            elif nameans[2] == 'tuplestr':
                error.cfg_reading_error(linenum, 'wrong value(202), it must be like this: \'white, #012345\', case insensitive')
            elif nameans[2] == 'tupleint':
                error.cfg_reading_error(linenum, 'wrong value(203), it must be like this: \'40, 30\'')
            elif nameans[2] == 'color_stepmul':
                error.cfg_reading_error(linenum, 'wrong value(204), it must be like this: \'0.9, 1.0, 1.7\'')
            elif nameans[2] == 'fullstr':
                error.cfg_reading_error(linenum, 'wrong value(205), it must be 0-9a-z or _')
        ###########################
        if nameans[2] == 'fullstr':
            valueout = value.group(0)
        else: valuestr = value.group(0).lower()
        ###########################
        if nameans[2] == 'float':
            try:
                valueout = float(valuestr)
            except:
                error.cfg_reading_error(linenum, 'wrong value(210), it must be integer or float')
            if valueout >= nameans[3][0] and valueout <= nameans[3][1]: pass
            else:
                error.cfg_reading_error(linenum, 'wrong value(211), it must be in {}'.format(nameans[3]))
        ###########################
        elif nameans[2] == 'bool':
            valueout = True if valuestr=='true' else False
        ###########################
        elif nameans[2] == 'str':
            valueout = valuestr
        ###########################
        elif nameans[2] == 'tuplestr':
            valuelist = valuestr.split(',')
            if len(valuelist) != nameans[3][0]:
                error.cfg_reading_error(linenum, 'wrong value(212), number of setting do not match, it need be {}, but here is {}'.format(nameans[3][0], len(valuelist)))
            valueout = tuple(valuelist)
        ###########################
        if nameans[2] == 'tupleint':
            valuelist = valuestr.split(',')
            if len(valuelist) != nameans[3][0]:
                error.cfg_reading_error(linenum, 'wrong value(213), number of setting do not match, it need be {}, but here is {}'.format(nameans[3][0], len(valuelist)))
            valueoutlist = []
            for valueliststr in valuelist:
                try:
                    valuelistint = int(valueliststr)
                except:
                    error.cfg_reading_error(linenum, 'wrong value(214), it must be integer')
                if valuelistint >= nameans[3][1][0] and valuelistint <= nameans[3][1][1]: pass
                else:
                    error.cfg_reading_error(linenum, 'wrong value(215), it must be in {}'.format(nameans[3][1]))
                valueoutlist += [valuelistint]
            valueout = tuple(valueoutlist)
        ###########################
        elif nameans[2] == 'color_stepmul':
            valuelist = valuestr.split(',')
            if len(valuelist) != 3:
                error.cfg_reading_error(linenum, 'wrong value(216), number of setting do not match, it need be {}, but here is {}'.format(3, len(valuelist)))
            valueoutlist = []
            for valueliststr in valuelist:
                try:
                    valuelistf = float(valueliststr)
                except:
                    error.cfg_reading_error(linenum, 'wrong value(217), it must be integer or float')
                if valuelistf >= nameans[3][0] and valuelistf <= nameans[3][1]: pass
                else:
                    error.cfg_reading_error(linenum, 'wrong value(218), it must be in {}'.format(nameans[3]))
                valueoutlist += [valuelistf]
            if valueoutlist[0] < valueoutlist[1] and valueoutlist[1] < valueoutlist[2]:
                valueout = tuple(valueoutlist)
            else:
                error.cfg_reading_error(linenum, 'wrong value(219), these three value must be increasing')
        ###########################
        self.dis_setting_list[nameans[0]+1] = valueout

    def _get_dis_setting1(self, line, linenum):
        name = search(dis_setting1_compile_name, line)
        if name == None:
            error.cfg_reading_error(linenum, 'wrong name(220)')
        namestr = name.group(0)
        if namestr not in dis_setting1_name:
            error.cfg_reading_error(linenum, 'wrong name(221)')
        nameans = dis_setting1_compile_value[namestr]
        if nameans[3][0] != self.keynum:
            pass
        else:
            value = search(nameans[1], line)
            if value == None:
                if nameans[2] == 'tuplestr':
                    error.cfg_reading_error(linenum, 'wrong value(220), it must be like this: \'white, #012345, ...\', number equals to the key number')
                elif nameans[2] == 'tupleint':
                    error.cfg_reading_error(linenum, 'wrong value(221), it must be like this: \'40, 30, ...\', number equals to the key number')
                elif nameans[2] == 'tupleposition':
                    error.cfg_reading_error(linenum, 'wrong value(222), it must be like this: \'(100, 200), (300, 400), ...\', number equals to the key number')
                elif nameans[2] == 'tuplesize':
                    error.cfg_reading_error(linenum, 'wrong value(223), it must be like this: \'(10, 20), (30, 40), ...\', number equals to the key number')
            valuestr = value.group(0).lower()
            ###########################
            if nameans[2] == 'tuplestr':
                valuelist = valuestr.split(',')
                if len(valuelist) != nameans[3][0]:
                    error.cfg_reading_error(linenum, 'wrong value(230), number of setting do not match, it need be {}, but here is {}'.format(nameans[3][0], len(valuelist)))
                valueout = tuple(valuelist)
            ###########################
            if nameans[2] == 'tupleint':
                valuelist = valuestr.split(',')
                if len(valuelist) != nameans[3][0]:
                    error.cfg_reading_error(linenum, 'wrong value(231), number of setting do not match, it need be {}, but here is {}'.format(nameans[3][0], len(valuelist)))
                valueoutlist = []
                for valueliststr in valuelist:
                    try:
                        valuelistint = int(valueliststr)
                    except:
                        error.cfg_reading_error(linenum, 'wrong value(232), it must be integer')
                    if valuelistint >= nameans[3][1][0] and valuelistint <= nameans[3][1][1]: pass
                    else:
                        error.cfg_reading_error(linenum, 'wrong value(233), it must be in {}'.format(nameans[3][1]))
                    valueoutlist += [valuelistint]
                valueout = tuple(valueoutlist)
            ###########################
            if nameans[2] == 'tupleposition' or nameans[2] == 'tuplesize':
                valuelist = findall(position_compile, valuestr)
                if valuelist == []:
                    error.cfg_reading_error(linenum, 'wrong value(234), it must be like this: \'(100, 200), (300, 400), ...\', number equals to the key number')
                if len(valuelist) != nameans[3][0]:
                    error.cfg_reading_error(linenum, 'wrong value(235), number of setting do not match, it need be {}, but here is {}'.format(nameans[3][0], len(valuelist)))
                valueoutlist = []
                for valueliststr in valuelist:
                    valueliststrlist = valueliststr.split(',')
                    if len(valueliststrlist) != 2:
                        error.cfg_reading_error(linenum, 'wrong value(236), number of position/size value do not equal to 2, here is {}'.format(len(valueliststrlist)))
                    try:
                        valuelslint0 = int(valueliststrlist[0])
                        valuelslint1 = int(valueliststrlist[1])
                    except:
                        error.cfg_reading_error(linenum, 'wrong value(237), position/size value must be integer')
                    if valuelslint0 >= nameans[3][1][0] and valuelslint0 <= nameans[3][1][1] and \
                       valuelslint1 >= nameans[3][1][0] and valuelslint1 <= nameans[3][1][1] : pass
                    else:
                        error.cfg_reading_error(linenum, 'wrong value(238), position/size value must be in {}'.format(nameans[3][1]))
                    valueoutlist += [(valuelslint0, valuelslint1)]
                valueout = tuple(valueoutlist)
            ###########################
            self.dis_setting_list[nameans[0]+1] = valueout

    def _check_key(self):
        pi = 'defult'
        for i in self.key_setting_list:
            if (i != '') and (pi == ''):
                error.cfg_key_error()
            pi = i

    def _check_tap(self):
        for i in self.tap_setting_list:
            if i == '':
                error.cfg_tap_error()

    def _check_dis(self):
        for i in self.dis_setting_list:
            if i == '':
                error.cfg_dis_error()

    @staticmethod
    def _set2defult():
        cfg = open('config.cfg', 'w')
        cfg.write(defultConfig.config)

    @staticmethod
    def remove_blank(s):
        out = s
        out = out.replace(' ','')
        out = out.replace('\n','')
        out = out.replace('\r','')
        out = out.replace('\t','')
        return out