import setting
import tap
import move
import display

from threading import Thread

s = setting.main()
if s.cfg_ok:
    all_key = []
    for i in range(s.keynum):
        all_key += [tap.key(*s.key_setting[i], **s.tap_setting)]
    akey = tap.allKey(**s.tap_setting)
    tap_main = tap.main(all_key, akey)
    move_main = move.main(20)
    dis_main = display.main(all_key, akey, move_main, s.keynum, **s.dis_setting)

    bgtap_cal = Thread(target = tap_main.start)
    bgmove_cal = Thread(target = move_main.start)

    bgtap_cal.start()
    bgmove_cal.start()
    dis_main.start()

