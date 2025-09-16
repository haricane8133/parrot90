# Parrot90 Software
1. Flash CircuitPython 9.2.8 on the two Raspberry PI Picos. Instructions [here](https://circuitpython.org/)
2. Install latest KMK (copy KMK) to the two picos. Instructions [here](https://github.com/KMKfw/kmk_firmware)
3. Install all library dependencies as mentioned in the following section.
4. Transfer the code from this folder to the two picos
5. Make sure to the underscore from `code.py` and `boot.py` for respective Picos.

### Dependencies
* https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306/releases/download/3.0.3/adafruit-circuitpython-displayio-ssd1306-py-3.0.3.zip
* https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/releases/download/3.3.3/adafruit-circuitpython-display-text-py-3.3.3.zip
* https://github.com/adafruit/Adafruit_CircuitPython_ImageLoad/releases/download/1.24.4/adafruit-circuitpython-imageload-9.x-mpy-1.24.4.zip
Note: After downloading all libraries, just rename their parent folders to the actual library and flatten out the lib folder in the parent so that code can import properly. For Adafruit_CircuitPython_DisplayIO_SSD1306, rename the py file to __init__.py also.

### Debug
If you need to debug through serial port, use the following -
`python -m serial.tools.miniterm COMX 115200`