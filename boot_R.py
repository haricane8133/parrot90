import microcontroller, digitalio, board, storage, usb_cdc, usb_midi

print("RHS: Running boot.py")

# This might be required to handle the high memory requirements of Adafruit's OLED libraries 
# But this is deprecated in CircuitPython 9. We have to find an alternative.
# import supervisor
# supervisor.set_next_stack_limit(4096 + 4096)

# The following code is to read button presses as the keyboard is booting up,
# to put the keyboard in specific states - maintenance mode, Keyboard Mode (Mac Mode, Windows Mode),
# or some features
# (maintenance mode is where we enable the USB storage for transfering code)

# To put the keyboard in maintenance mode, the user has to...
#     press the F12 button
# To set the keyboard with Mac's keyconfigs, the user has to...
#     press the right CMD button (the one marked as ALT), when the keyboard is first connected
# To make the keyboard work with Windows' keyconfigs, the user has to...
#     press the right Windows button (the one marked as WIN), when the keyboard is first connected

# * F12 button is connected to Row 1, Col 8
# * ALT button is connected to Row 6, Col 5
# * WIN button is connected to Row 6, Col 6

# These are the variables that we set to indicate the status. We read this in code.py to customize the state of the keyboard.
# microcontroller.nvm[0] = 0 indicates that THIS SPLIT is the LEFT split (even though there are better methods provided by QMK, let us have this variable)
# microcontroller.nvm[0] = 1 indicates that THIS SPLIT is the RIGHT split (even though there are better methods provided by QMK, let us have this variable)
# microcontroller.nvm[1] = 1 indicates that the keyboard is started along with the USB storage (maintenance Mode)
# microcontroller.nvm[1] = 0 indicates that the keyboard is started normally (Keyboard Mode)
# microcontroller.nvm[2] = 0 indicates that the keyboard is set for Windows
# microcontroller.nvm[2] = 1 indicates that the keyboard is set for Mac
# microcontroller.nvm[3] = 0 indicates that the keyboard is NOT enabled for WS connect experimental feature
# microcontroller.nvm[3] = 1 indicates that the keyboard is enabled for WS connect experimental feature

# Note that once KMK is started, we will have to set variables in the KMK Object so that these values are shared with the other half


# This is the right side
microcontroller.nvm[0] = 1

col5 = digitalio.DigitalInOut(board.GP8)
col5.direction = digitalio.Direction.OUTPUT

col6 = digitalio.DigitalInOut(board.GP7)
col6.direction = digitalio.Direction.OUTPUT

col8 = digitalio.DigitalInOut(board.GP5)
col8.direction = digitalio.Direction.OUTPUT

row1 = digitalio.DigitalInOut(board.GP13)
row1.direction = digitalio.Direction.INPUT
row1.pull = digitalio.Pull.DOWN

row6 = digitalio.DigitalInOut(board.GP18)
row6.direction = digitalio.Direction.INPUT
row6.pull = digitalio.Pull.DOWN


# 1. Check Rotary Button press - to put in maintenance mode
col8.value = True
if row1.value:
  # maintenance Mode
  microcontroller.nvm[1] = 1
else:
  # Keyboard Mode
  microcontroller.nvm[1] = 0
  storage.disable_usb_drive()
  usb_cdc.disable()
  # usb_midi.disable()
col8.value = False

# 2.a) Read Alt Button Press - To put the keyboard in Mac Mode
col5.value = True
MAC_PRESSED = False
if row6.value:
  MAC_PRESSED = True
  microcontroller.nvm[2] = 1
col5.value = False

# 2.b) Check Windows Button press - To put in Windows mode
col6.value = True
if row6.value and not MAC_PRESSED:
  microcontroller.nvm[2] = 0
col6.value = False


col5.deinit()
col6.deinit()
col8.deinit()
row1.deinit()
row6.deinit()

if(microcontroller.nvm[1] == 1):
  print('RHS: Keyboard put in Maintainance mode. USB Storage enabled.')

if(microcontroller.nvm[2] == 0):
  print('RHS: Keyboard working in Windows Mode')
else:
  print('RHS: Keyboard working in Mac Mode')