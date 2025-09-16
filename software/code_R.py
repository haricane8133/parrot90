import sys, board, microcontroller # type: ignore

# if microcontroller.nvm[1] == 1:
#     sys.exit()

print("RHS: Starting code.py")

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation


# Setup
print("RHS: Configuring Keyboard")

keyboard = KMKKeyboard()
keyboard.debug_enabled = True
# if microcontroller.nvm[1] == 1:
#     keyboard.debug_enabled = True

from kmk.modules.split import Split, SplitType, SplitSide
split = Split(
    split_side=SplitSide.RIGHT,
    split_target_left=True,
    split_flip=False,
    split_type=SplitType.UART,
    # use_pio=True,
    data_pin=board.GP0,
    data_pin2=board.GP1,
    # uart_flip = False,
)
split.debug_enabled = True
keyboard.modules.append(split)

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

# KMK firmware has a limitation for split keyboards as mentioned here - https://github.com/KMKfw/kmk_firmware/blob/26e350b3539c92c0842f56479db1f49b08d9c006/docs/en/split_keyboards.md#split_side
#     both splits must have the same number of columns (they say col * row must be same).
#     In our keyboard, though both keyboards have 6 rows, the left split has 7 columns and the right split has 11 columns
#     So we have to work around by adding 4 dummy columns to the Left split to get the match with right split.

# Keyboard Config
keyboard.col_pins = (board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
keyboard.row_pins = (board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keyboard Matrices
#                                                                         Dummy  Dummy  Dummy  Dummy
macMatrix = [
    [
        KC.ESC,   KC.NO,    KC.NO,   KC.NO,    KC.NO,   KC.NO,   KC.NO,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.MRWD, KC.MPLY, KC.MFFD, KC.NO,   KC.MUTE,  KC.VOLD,  KC.VOLU,   KC.NO,    KC.NO,    KC.NO,   KC.NO,
        KC.GRAVE, KC.N1,    KC.N2,   KC.N3,    KC.N4,   KC.N5,   KC.N6,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINUS, KC.EQUAL, KC.NO,     KC.BSPC,  KC.MO(1), KC.HOME, KC.PGUP,
        KC.TAB,   KC.Q,     KC.W,    KC.E,     KC.R,    KC.NO,   KC.T,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,     KC.LBRC,  KC.RBRC,   KC.BSLS,  KC.DEL,   KC.END,  KC.PGDN,
        KC.CAPS,  KC.A,     KC.S,    KC.D,     KC.F,    KC.NO,   KC.G,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,  KC.QUOT,  KC.NO,     KC.ENT,   KC.MO,    KC.NO,   KC.NO,
        KC.LSFT,  KC.MUTE,  KC.Z,    KC.X,     KC.C,    KC.V,    KC.B,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.N,    KC.M,    KC.COMM, KC.NO,   KC.DOT,   KC.SLSH,  KC.RSHIFT, KC.NO,    KC.NO,    KC.UP,   KC.NO,
        KC.LCTL,  KC.MO(1), KC.LALT, KC.LGUI,  KC.NO,   KC.NO,   KC.SPC,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.RGUI,  KC.RALT,  KC.MO(1),  KC.RCTRL, KC.LEFT,  KC.DOWN, KC.RIGHT
    ],
    [
        KC.TRNS,  KC.TRNS, KC.F1,   KC.F2,    KC.F3,   KC.F4,   KC.F5,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.F6,    KC.F7,   KC.F8,   KC.NO,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.F13,  KC.F14,  KC.F15,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],
]
winMatrix = [
    [
        KC.ESC,   KC.NO,    KC.F1,   KC.F2,    KC.F3,   KC.F4,   KC.F5,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.F6,   KC.F7,   KC.F8,   KC.NO,   KC.F9,    KC.F10,   KC.F11,    KC.F12,    KC.PSCREEN,       KC.SLCK, KC.PAUSE,
        KC.GRAVE, KC.N1,    KC.N2,   KC.N3,    KC.N4,   KC.N5,   KC.N6,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINUS, KC.EQUAL, KC.NO,     KC.BSPC,   KC.LT(1, KC.INS), KC.HOME, KC.PGUP,
        KC.TAB,   KC.Q,     KC.W,    KC.E,     KC.R,    KC.NO,   KC.T,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,     KC.LBRC,  KC.RBRC,   KC.BSLS,   KC.DEL,           KC.END,  KC.PGDN,
        KC.CAPS,  KC.A,     KC.S,    KC.D,     KC.F,    KC.NO,   KC.G,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,  KC.QUOT,  KC.NO,     KC.ENT,    KC.NO,            KC.NO,   KC.NO,
        KC.LSFT,  KC.MUTE,  KC.Z,    KC.X,     KC.C,    KC.V,    KC.B,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.N,    KC.M,    KC.COMM, KC.NO,   KC.DOT,   KC.SLSH,  KC.RSHIFT, KC.NO,     KC.NO,            KC.UP,   KC.NO,
        KC.LCTL,  KC.MO(1), KC.LGUI, KC.LALT,  KC.NO,   KC.NO,   KC.SPC,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.RALT,  KC.RGUI,  KC.MO(1),  KC.RCTRL,  KC.LEFT,          KC.DOWN, KC.RIGHT
    ],
    [
        KC.TRNS,  KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.MPRV,  KC.MPLY, KC.MNXT, KC.TRNS, KC.MUTE, KC.VOLD, KC.VOLU, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],
]

if(microcontroller.nvm[2] == 0):
    keyboard.keymap = winMatrix
else:
    keyboard.keymap = macMatrix
# keyboard.keymap = []

# from analogio import AnalogIn
# import board
# from kmk.handlers.sequences import send_string


# # Initialize the analog pin (e.g., GP26)
# slider = AnalogIn(board.GP26)  # GP26 corresponds to A0 in CircuitPython
# slider_val = 0
# slider_read_count = 0
# slider_avg_count = 20

# def read_slider():
#     return slider.value / 65535

# @keyboard.pre_loop_hook
# def handle_slider():
#     pos = read_slider()
#     if pos > 0.95:
#         keyboard.send(KC.BRIU)
#     elif pos < 0.05:
#         keyboard.send(KC.BRID)


if __name__ == '__main__':
    print("RHS: Firing up Keyboard!")
    keyboard.go()

