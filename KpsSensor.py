import setting
import tap
import display

from threading import Thread

s = setting.main()
if s.cfg_ok:
    all_key = []
    for i in range(s.keynum):
        all_key += [tap.key(*s.key_setting[i], *s.tap_setting)]
    akey = tap.allKey(*s.tap_setting[1:])
    tap_main = tap.main(all_key, akey)
    dis_main = display.main(all_key, akey, *s.dis_setting)

    bg_cal = Thread(target = tap_main.start)

    bg_cal.start()
    dis_main.start()
