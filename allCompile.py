from re import compile, RegexFlag

key_setting_compile_name = compile(r"(?<=%)\w+?(?=:)")
key_setting_name = ('key1','key2','key3','key4','key5','key6','key7','key8','key9','key10')
key_setting_compile_value=\
{'key1': (0, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key2': (1, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key3': (2, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key4': (3, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key5': (4, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key6': (5, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key7': (6, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key8': (7, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
 'key9': (8, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I)),
'key10': (9, compile(r"(?<=:)(([a-z0-9,\.;'\[\]\+\-\*/=`]|up|down|left|right|mleft|mright|space|none)$)", RegexFlag.I))}


tap_setting_compile_name = compile(r"(?<=@)\w+?(?=:)")
tap_setting_name = ('dposition_decrease','tapframes','need_standframes','basemul','decrease_lv','zero_decrease_lv')
tap_setting_compile_value=\
{'dposition_decrease': (0, compile(r"(?<=:)([0-9]+(\.[0-9]+)?$)"), 'float', (0,0.50)),
 'tapframes'         : (1, compile(r"(?<=:)([0-9]+$)"),            'int',   (1,1000)),
 'need_standframes'  : (2, compile(r"(?<=:)([0-9]+$)"),            'int',   (1,1000)),
 'basemul'           : (3, compile(r"(?<=:)([0-9]+(\.[0-9]+)?$)"), 'int',   (1,1000)),
 'decrease_lv'       : (4, compile(r"(?<=:)([0-9]+$)"),            'int',   (0,8)),
 'zero_decrease_lv'  : (5, compile(r"(?<=:)([0-9]+$)"),            'int',   (0,8))}

dis_setting0_compile_name = compile(r"(?<=&0)\w+?(?=:)")
dis_setting0_name = ('show_plate', 'plate_change_color', 'plate_base_color', 'show_akey_kps', 'akey_change_color', 'akey_base_color', 'akey_text_size', 'show_key_kps', 'key_change_color', 'show_key_button', 'key_button_effect', 'color_stepmul', 'arc_center_mul', 'effct_mul', 'show_lag','window_name')
dis_setting0_compile_value=\
{'show_plate'          : (0, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                      'bool'),
 'plate_change_color'  : (1, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                      'bool'),
 'plate_base_color'    : (2, compile(r"(?<=:)(black$|white$|#[0-9a-f]{6}$)", RegexFlag.I),       'str' ),
 'show_akey_kps'       : (3, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                      'bool'), 
 'akey_change_color'   : (4, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                      'bool'),
 'akey_base_color'     : (5, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I),  'tuplestr',        (2,)),
 'akey_text_size'      : (6, compile(r"(?<=:)(([0-9]+,?)+$)"),                                   'tupleint',        (2, (1,500))), 
 'show_key_kps'        : (7, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                      'bool'), 
 'key_change_color'    : (8, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                      'bool'),
 'show_key_button'     : (9, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                      'bool'),
 'key_button_effect'   : (10, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                     'bool'), 
 'color_stepmul'       : (11, compile(r"(?<=:)(([0-9]+(\.[0-9]+)?,?)+$)"),                       'color_stepmul',   (0.01, 10)),
 'arc_center_mul'      : (12, compile(r"(?<=:)([0-9]+(\.[0-9]+)?$)"),                            'float',           (0.1, 50)), 
 'effct_mul'           : (13, compile(r"(?<=:)([0-9]+(\.[0-9]+)?$)"),                            'float',           (0.0, 1)), 
 'show_lag'            : (18, compile(r"(?<=:)(true$|false$)", RegexFlag.I),                     'bool'),
 'window_name'         : (19, compile(r"(?<=:)(\w+?$)", RegexFlag.I),                            'fullstr' )}

dis_setting1_compile_name = compile(r"(?<=&1)\w+?(?=:)")
dis_setting1_name = ('kn1_base_color', 'kn1_text_size', 'kn1_position', 'kn1_size', 'kn2_base_color', 'kn2_text_size', 'kn2_position', 'kn2_size', 'kn3_base_color', 'kn3_text_size', 'kn3_position', 'kn3_size', 'kn4_base_color', 'kn4_text_size', 'kn4_position', 'kn4_size', 'kn5_base_color', 'kn5_text_size', 'kn5_position', 'kn5_size', 'kn6_base_color', 'kn6_text_size', 'kn6_position', 'kn6_size', 'kn7_base_color', 'kn7_text_size', 'kn7_position', 'kn7_size', 'kn8_base_color', 'kn8_text_size', 'kn8_position', 'kn8_size', 'kn9_base_color', 'kn9_text_size', 'kn9_position', 'kn9_size', 'kn10_base_color', 'kn10_text_size', 'kn10_position', 'kn10_size')
dis_setting1_compile_value=\
{'kn1_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (1,)),
 'kn1_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (1, (1,500))),
 'kn1_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (1, (0,500))),
 'kn1_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (1, (0,500))),
 'kn2_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (2,)),
 'kn2_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (2, (1,500))),
 'kn2_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (2, (0,500))),
 'kn2_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (2, (0,500))),
 'kn3_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (3,)),
 'kn3_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (3, (1,500))),
 'kn3_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (3, (0,500))),
 'kn3_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (3, (0,500))),
 'kn4_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (4,)),
 'kn4_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (4, (1,500))),
 'kn4_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (4, (0,500))),
 'kn4_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (4, (0,500))),
 'kn5_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (5,)),
 'kn5_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (5, (1,500))),
 'kn5_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (5, (0,500))),
 'kn5_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (5, (0,500))),
 'kn6_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (6,)),
 'kn6_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (6, (1,500))),
 'kn6_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (6, (0,500))),
 'kn6_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (6, (0,500))),
 'kn7_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (7,)),
 'kn7_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (7, (1,500))),
 'kn7_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (7, (0,500))),
 'kn7_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (7, (0,500))),
 'kn8_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (8,)),
 'kn8_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (8, (1,500))),
 'kn8_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (8, (0,500))),
 'kn8_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (8, (0,500))),
 'kn9_base_color'      : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (9,)),
 'kn9_text_size'       : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (9, (1,500))),
 'kn9_position'        : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (9, (0,500))),
 'kn9_size'            : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (9, (0,500))),
 'kn10_base_color'     : (14, compile(r"(?<=:)(((black|white|#[0-9a-f]{6}),?)+$)", RegexFlag.I), 'tuplestr',        (10,)),
 'kn10_text_size'      : (15, compile(r"(?<=:)(([0-9]+,?)+$)"),                                  'tupleint',        (10, (1,500))),
 'kn10_position'       : (16, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tupleposition',   (10, (0,500))),
 'kn10_size'           : (17, compile(r"(?<=:)(((\([0-9]+,[0-9]+\)),?)+$)"),                     'tuplesize',       (10, (0,500)))}

position_compile = compile(r"(?<=\()([0-9]+,[0-9]+)(?=\))")