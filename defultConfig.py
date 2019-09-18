config = '''you can change the setting here
if there are too any errors to fix, delet this file and restart, I will change it to defult
things behind the '%, @, &' will be read

Version: 0.7.2
Date: 2019-09-18
By: CHanzy
*********************
key setting 
if it is mouse, set it 'mleft' or 'mright'
if you don't use this key, set it 'none' or just delete
use 'space' to identify space
use 'up'/'down'/'left'/'right' to identify direction key

% key1: z
defult: z
% key2: x
defult: x
% key3: none
defult: none
% key4: none
defult: none
% key5: none
defult: none
% key6: none
defult: none
% key7: none
defult: none
% key8: none
defult: none
% key9: none
defult: none
% key10: none
defult: none

********************
* ADVANCED SETTING *
********************
tap setting

@ dposition_decrease: 0.05
defult: 0.05
0-0.50, speed to decrease the key effect, HIGHER IS FASTER

@ tapframes: 50
defult: 50
1-1000, MUST be integer,length of frames to detect your tap, higher will make the results more refined,lower will make the results react faster

@ need_standframes: 100
defult: 100 
1-1000, MUST be integer, length of frames you need to stand, higher will make the results more refined,lower will make the results react faster

@ basemul: 10
defult: 10 
1-1000, MUST be integer, base speed to change display kps, HIGHER IS SLOWER

@ decrease_lv: 2
defult: 2 
0-8, MUST be integer, decrease the speed when close to real kps, HIGHER IS SLOWER

@ zero_decrease_lv: 1
defult: 1 
0-8, MUST be integer, decrease the speed when close to zero, HIGHER IS SLOWER
********************
display setting

&0 show_plate: True
&0 plate_change_color: True
&0 plate_base_color: #00ffff
defult: True, True, #00ffff
set the plate
color now can only be '#RGB' or 'black' or 'white'

&0 show_akey_kps: True
&0 akey_change_color: False
&0 akey_base_color: black, black
&0 akey_text_size: 120, 25
defult: True; False; black,black; 120,25
set the center, all kps and the kps behind display
color now can only be '#RGB' or 'black' or 'white'

&0 show_key_kps: True
&0 key_change_color: True
defult: True, True
set single key's kps display

&0 show_key_button: True
&0 key_button_effect: True
defult: True, True
set key button display

&0 color_stepmul: 0.6, 1.5, 1.8
defult: 0.6,1.5,1.8
set 3 color change steps
0.01-10, MUST be increasing
each color setting is coming soon

&0 arc_center_mul: 4
defult: 4
set the base kps in center of the plate
0.1-50, defult is recommanded
the real kps will be 'arc_center_mul*keynum'
this will also effect the color change, change color_stepmul to set back if you don't want the effect

&0 effct_mul: 0.6
defult: 0.6
set the max effect diaphaneity
0.0-1, if you want to turn off effect, setting 'key_button_effect' to False is recommanded
********************
color now can only be '#RGB' or 'black' or 'white'

&1 kn1_base_color: black
&1 kn1_text_size:  40
&1 kn1_position:   (250,340)
&1 kn1_size:       (100,100)
defult: 
black
40
(250,340)
(100,100)
set single key button's display when keynum is 1

&1 kn2_base_color: black,     black
&1 kn2_text_size:  40,        40
&1 kn2_position:   (200,340), (300,340)
&1 kn2_size:       (75,75),   (75,75)
defult:
black,     black
40,        40
(200,340), (300,340)
(75,75),   (75,75)
set single key button's display when keynum is 2

&1 kn3_base_color: black,     black,     black
&1 kn3_text_size:  40,        40,        40
&1 kn3_position:   (160,340), (250,340), (340,340)
&1 kn3_size:       (75,75),   (75,75),   (75,75)
defult:
black,     black,     black
40,        40,        40
(160,340), (250,340), (340,340)
(75,75),   (75,75),   (75,75)
set single key button's display when keynum is 3

&1 kn4_base_color: black,     black,     black,     black
&1 kn4_text_size:  30,        30,        30,        30
&1 kn4_position:   (145,340), (215,340), (285,340), (355,340)
&1 kn4_size:       (60,60),   (60,60),   (60,60),   (60,60)
defult:
black,     black,     black,     black
30,        30,        30,        30
(145,340), (215,340), (285,340), (355,340)
(60,60),   (60,60),   (60,60),   (60,60)
set single key button's display when keynum is 4

&1 kn5_base_color: black,     black,     black,     black,     black
&1 kn5_text_size:  25,        25,        25,        25,        25
&1 kn5_position:   (118,340), (175,340), (250,400), (325,340), (382,340)
&1 kn5_size:       (50,50),   (50,50),   (200,50),  (50,50),   (50,50)
defult:
black,     black,     black,     black,     black
25,        25,        25,        25,        25
(118,340), (175,340), (250,400), (325,340), (382,340)
(50,50),   (50,50),   (200,50),  (50,50),   (50,50)
set single key button's display when keynum is 5

&1 kn6_base_color: black,     black,     black,     black,     black,     black
&1 kn6_text_size:  25,        25,        25,        25,        25,        25
&1 kn6_position:   (115,340), (169,340), (223,340), (277,340), (331,340), (385,340)
&1 kn6_size:       (50,50),   (50,50),   (50,50),   (50,50),   (50,50),   (50,50)
defult:
black,     black,     black,     black,     black,     black
25,        25,        25,        25,        25,        25
(115,340), (169,340), (223,340), (277,340), (331,340), (385,340)
(50,50),   (50,50),   (200,50),  (50,50),   (50,50),   (50,50)
set single key button's display when keynum is 6

&1 kn7_base_color: black,     black,     black,      black,     black,     black,     black
&1 kn7_text_size:  20,        20,        20,         20,        20,        20,        20
&1 kn7_position:   (110,340), (155,340), (200,340), (250,390), (300,340), (345,340), (390,340)
&1 kn7_size:       (40,40),   (40,40),   (40,40),   (200,40),   (40,40),   (40,40),   (40,40)
defult:
black,     black,     black,      black,    black,     black,     black
20,        20,        20,         20,       20,        20,        20
(100,340), (150,340), (200,340), (250,390), (300,340), (350,340), (400,340)
(40,40),   (40,40),   (40,40),   (200,40),  (40,40),   (40,40),   (40,40)
set single key button's display when keynum is 7

&1 kn8_base_color: black,    black,     black,     black,     black,     black,     black,     black
&1 kn8_text_size:  20,       20,        20,        20,        20,        20,        20,        20
&1 kn8_position:   (96,340), (140,340), (184,340), (228,340), (272,340), (316,340), (360,340), (404,340)
&1 kn8_size:       (40,40),  (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40)
defult:
black,    black,     black,     black,     black,     black,     black,     black
20,       20,        20,        20,        20,        20,        20,        20
(96,340), (140,340), (184,340), (228,340), (272,340), (316,340), (360,340), (404,340)
(40,40),  (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40)
set single key button's display when keynum is 8

&1 kn9_base_color: black,    black,     black,     black,     black,     black,     black,     black,     black
&1 kn9_text_size:  20,       20,        20,        20,        20,        20,        20,        20,        20
&1 kn9_position:   (94,340), (136,340), (178,340), (220,340), (250,390), (280,340), (322,340), (364,340), (406,340)
&1 kn9_size:       (40,40),  (40,40),   (40,40),   (40,40),   (200,40),  (40,40),   (40,40),   (40,40),   (40,40)
defult:
black,    black,     black,     black,     black,     black,     black,     black,     black
20,       20,        20,        20,        20,        20,        20,        20,        20
(94,340), (136,340), (178,340), (220,340), (250,390), (280,340), (322,340), (364,340), (406,340)
(40,40),  (40,40),   (40,40),   (40,40),   (200,40),  (40,40),   (40,40),   (40,40),   (40,40)
set single key button's display when keynum is 9

&1 kn10_base_color: black,     black,     black,     black,     black,     black,     black,     black,     black,     black
&1 kn10_text_size:  20,        20,        20,        20,        20,        20,        20,        20,        20,        20
&1 kn10_position:   (136,340), (158,382), (180,340), (202,382), (224,340), (276,340), (298,382), (320,340), (342,382), (364,340)
&1 kn10_size:       (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40)
defult:
black,     black,     black,     black,     black,     black,     black,     black,     black,     black
20,        20,        20,        20,        20,        20,        20,        20,        20,        20
(136,340), (158,382), (180,340), (202,382), (224,340), (276,340), (298,382), (320,340), (342,382), (364,340)
(40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40),   (40,40)
set single key button's display when keynum is 10
********************

&0 show_lag: False
defult: False
set whether show lags

&0 window_name: Kps_Sensor
defult: 'Kps_Sensor'
set window_name
this will be useful for obs'''