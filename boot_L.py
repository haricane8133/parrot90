import microcontroller, board, digitalio, storage, usb_cdc, usb_midi

print("LHS: Starting boot.py")

# This might be required to handle the high memory requirements of Adafruit's OLED libraries 
# But this is deprecated in CircuitPython 9. We have to find an alternative.
# import supervisor
# supervisor.set_next_stack_limit(4096 + 4096)

# The following code is to read button presses as the keyboard is booting up,
# to put the keyboard in specific states - maintenance mode, Keyboard Mode (Mac Mode, Windows Mode),
# or to enable certain features
# (maintenance mode is where we enable the USB storage for transfering code)

# To put the keyboard in maintenance mode, the user has to...
#     press the encoder button (the one you have configured for mute)
# To set the keyboard with Mac's keyconfigs, the user has to...
#     press the left CMD button (the one marked as ALT), when the keyboard is first connected
# To make the keyboard work with Windows' keyconfigs, the user has to...
#     press the left Windows button (the one marked as WIN), when the keyboard is first connected
# To enable WS connect experimental function, the user has to...
#     press the left Fn button, when the keyboard is first connected

# * Rotary Encoder button is connected to Row 5, Col 2
# * Windows Button is connected to Row 6, Col 3
# * Mac Button is connected to Row 6, Col 4
# * Fn Button is connected to Row 6, Col 2

# We are able to acheive this by mimicing the Keyboard Matrix.
# Since we are in COL2ROW diode orientation, we provide a voltage in column and check if row is high

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

# This is the Left side
microcontroller.nvm[0] = 0


# Initialize pins
col2 = digitalio.DigitalInOut(board.GP21)
col2.direction = digitalio.Direction.OUTPUT

col3 = digitalio.DigitalInOut(board.GP20)
col3.direction = digitalio.Direction.OUTPUT

col4 = digitalio.DigitalInOut(board.GP19)
col4.direction = digitalio.Direction.OUTPUT

row5 = digitalio.DigitalInOut(board.GP14)
row5.direction = digitalio.Direction.INPUT
row5.pull = digitalio.Pull.DOWN

row6 = digitalio.DigitalInOut(board.GP15)
row6.direction = digitalio.Direction.INPUT
row6.pull = digitalio.Pull.DOWN



# 1. Check Rotary Button press - to put in maintenance mode
col2.value = True
if row5.value:
  # maintenance Mode
  microcontroller.nvm[1] = 1
else:
  # Keyboard Mode
  microcontroller.nvm[1] = 0
  storage.disable_usb_drive()
  usb_cdc.disable()
  # usb_midi.disable()
col2.value = False

# 2.a) Read Alt Button Press - To put the keyboard in Mac Mode
col4.value = True
MAC_PRESSED = False
if row6.value:
  MAC_PRESSED = True
  microcontroller.nvm[2] = 1
col4.value = False

# 2.b) Check Windows Button press - To put in Windows mode
col3.value = True
if row6.value and not MAC_PRESSED:
  microcontroller.nvm[2] = 0
col3.value = False


# 3) Check Fn Button press - To enable WS connect experimental mode
col2.value = True
if row6.value:
  microcontroller.nvm[3] = 1
else:
  microcontroller.nvm[3] = 0
col2.value = False


col2.deinit()
col3.deinit()
col4.deinit()
row5.deinit()
row6.deinit()


if(microcontroller.nvm[1] == 1):
  print('LHS: Keyboard put in Maintainance mode. USB Storage enabled.')

if(microcontroller.nvm[2] == 0):
  print('LHS: Keyboard working in Windows Mode')
else:
  print('LHS: Keyboard working in Mac Mode')

if(microcontroller.nvm[3] == 1):
  print('LHS: WS Connect Experimentational feature enabled')