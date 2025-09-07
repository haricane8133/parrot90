import sys, time, board, microcontroller # type: ignore

# if microcontroller.nvm[1] == 1:
#     sys.exit()

print("LHS: Starting code.py")

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation


# Setup
print("LHS: Configuring Keyboard")

keyboard = KMKKeyboard()
keyboard.debug_enabled = True
# if microcontroller.nvm[1] == 1:
#     keyboard.debug_enabled = True

from kmk.modules.split import Split, SplitType, SplitSide
split = Split(
    split_side=SplitSide.LEFT,
    split_target_left=True,
    split_flip=False,
    split_type=SplitType.UART,
    # use_pio=True,
    data_pin=board.GP1,
    data_pin2=board.GP0,
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
#                                                                                                        Dummy      Dummy      Dummy      Dummy       (details above)
keyboard.col_pins = (board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP4, board.GP5, board.GP6, board.GP7)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
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
        KC.TRNS,  KC.TRNS, KC.F1,   KC.F2,    KC.F3,   KC.F4,   KC.F5,     KC.NO, KC.NO, KC.NO, KC.NO,                       KC.F6,    KC.F7,   KC.F8,   KC.NO,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.F13,  KC.F14,  KC.F15,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,   KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
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
        KC.TRNS,  KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.NO, KC.NO, KC.NO, KC.NO,                       KC.MPRV,  KC.MPLY, KC.MNXT, KC.TRNS, KC.MUTE, KC.VOLD, KC.VOLU, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.NO, KC.NO, KC.NO, KC.NO,                       KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],
]

if(microcontroller.nvm[2] == 0):
    keyboard.keymap = winMatrix
else:
    keyboard.keymap = macMatrix


# Rotary Encoder (only the rotating part. The button is included in the above keyboard matrix)
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
encoder_handler.pins = [(board.GP9, board.GP8, None, False)]
encoder_handler.map = [[(KC.VOLD, KC.VOLU, KC.NO)]]
keyboard.modules.append(encoder_handler)





print("LHS: Starting Display")

from random import randint
import busio, displayio, terminalio, i2cdisplaybus
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306
from kmk.extensions.lock_status import LockStatus


NAME = "Parrot90"
message1 = ["Greeny", "Parrot", "Parakeet", "Canopy", "Parakeeb", "Leaves", "Forrest", "KeeBird"]

WIDTH = 128
HEIGHT = 64
ROTATION = 0
BORDER = 1


displayio.release_displays()

# --- Initialize I2C
i2c = busio.I2C(board.GP3, board.GP2)   # SCL=GP3, SDA=GP2

# --- Create the I2C display bus
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)


# i2c = busio.I2C(scl=board.GP3, sda=board.GP2)
# i2c_display = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)

display = SSD1306(display_bus, width=WIDTH, height=HEIGHT, rotation=ROTATION)

# Create the root group
mainGrp = displayio.Group()


display.root_group = mainGrp

# Outer white background
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
mainGrp.append(bg_sprite)

# Inner black rect (border)
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
mainGrp.append(inner_sprite)


# Banner
banner = label.Label(terminalio.FONT, text=NAME, color=0xFFFFFF, x=4, y=7, scale=2)
mainGrp.append(banner)

# Mode
mode_text = '"' + message1[randint(0, len(message1)-1)] + '"'
if microcontroller.nvm[1] == 1:
    mode_text = "<Service Mode>"
mode_label = label.Label(terminalio.FONT, text=mode_text, color=0xFFFFFF, x=3, y=25)
mainGrp.append(mode_label)

# Host
hostText = "<Mac>" if microcontroller.nvm[2] else "<Win>"
host_label = label.Label(terminalio.FONT, text=hostText, color=0xFFFFFF, x=93, y=24)
mainGrp.append(host_label)

# Caps Lock symbol
caps_label = label.Label(terminalio.FONT, text="^", color=0xFFFFFF, x=103, y=23, scale=4)

class _LockStatus(LockStatus):
    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)
        if self.get_caps_lock():
            if caps_label not in mainGrp:
                mainGrp.append(caps_label)
        else:
            if caps_label in mainGrp:
                mainGrp.remove(caps_label)

keyboard.extensions.append(_LockStatus())

# -------------------------------
# WPM tracking (reset after idle)
# -------------------------------
from kmk.keys import KC

keys_typed = 0
start_time = None
last_key_time = None
last_oled_time = None

UPDATE_INTERVAL = 0.5
COUNT_RESET_TIME = 5

wpm_label = label.Label(terminalio.FONT, text="WPM: 0", color=0xFFFFFF, x=3, y=45)
mainGrp.append(wpm_label)

def get_wpm():
    global keys_typed, start_time
    if not start_time or keys_typed == 0:
        return 0
    elapsed = time.monotonic() - start_time
    if elapsed <= 0:
        return 0
    return int((keys_typed / 5) * 60 / elapsed)

# Wrap KMK process_key
orig_process_key = keyboard.process_key

def counting_process_key(key, is_pressed, int_coord=None):
    global keys_typed, start_time, last_key_time

    now = time.monotonic()

    if is_pressed:
        if keys_typed == 0:
            start_time = now
        keys_typed += 1
        last_key_time = now

    return orig_process_key(key, is_pressed, int_coord)

keyboard.process_key = counting_process_key

# Continuous update (so WPM drops to 0 if reset or idle)
def update_wpm():
    global keys_typed, start_time, last_oled_time, last_key_time, UPDATE_INTERVAL, COUNT_RESET_TIME

    now = time.monotonic()

    if last_key_time and now - last_key_time >= COUNT_RESET_TIME:
        # Reset if idle for some times
        keys_typed = 0
        start_time = None

    if last_oled_time == None or ((now - last_oled_time) > UPDATE_INTERVAL):
        wpm_label.text = f"WPM: {get_wpm()}"
        last_oled_time = now

keyboard.before_matrix_scan = update_wpm


# -------------------------------


if __name__ == '__main__':
    print("LHS: Firing up Keyboard!")
    keyboard.go()
