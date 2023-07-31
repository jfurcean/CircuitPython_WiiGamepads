# CircuitPython WiiGamepads

CircuitPython lets you define custom [HID devices](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices#custom-hid-devices-3096614-9). This code defines a gamepad descriptor in `boot.py`, a gamepad library in `hid_gamepad.py`, and customer controller code for the different Wii accessory controllers. The USB descriptor is universal for all the controllers and presents 16 buttons, 2 Joysticks, and 2 analog controls, but only sends reports for the controls used.

## How to use WiiGamepads

1. Copy `boot.py`, `code.py`, `hid_gamepad.py`, and `controllers/` to the root of your `CIRCUITPY` drive.
2. Uncomment the controller you wish to use in `code.py`. Your `code.py` file would like the example below if you wanted to use the Wii Classic Controller
3. Unplug CircuitPython microcontroller and plug it back in for the new USB descriptor to be read by your computer.

### Code.py Example
```python
# Place this file in the root of your CIRCUITPY drive
# uncomment the controller you plan on using

from controllers import wii_classic_controller
# from controllers import wii_nunchuk
# from controllers import wii_nes
# from controllers import wii_guitar
# from controllers import wii_drums
```
