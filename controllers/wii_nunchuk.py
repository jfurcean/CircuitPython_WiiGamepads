# SPDX-FileCopyrightText: 2022 John Furcean
# SPDX-License-Identifier: MIT

# In order to use this you must have wii_classic_controller_usb.py
# and the associated boot.py file on your CIRCUITPY drive

import board
import usb_hid
from adafruit_simplemath import map_range
from hid_gamepad import Gamepad
from wiichuck.nunchuk import Nunchuk

def map_buttons(buttons):

    # mapped buttons so they work appropriately with https://gamepad-tester.com/

    buttons_mapped=[0]*16

    buttons_mapped[0] = buttons.C
    buttons_mapped[1] = buttons.Z

    # buttons 3 - 16 not used

    return buttons_mapped


gp = Gamepad(usb_hid.devices)
controller = Nunchuk(board.STEMMA_I2C())


while True:

    joystick, buttons, _ = controller.values

    buttons_mapped = map_buttons(buttons)

    for i, button in enumerate(buttons_mapped):
        gamepad_button_num = i+1
        if button:
            gp.press_buttons(gamepad_button_num)
            # print(" press", gamepad_button_num, end="")
        else:
            gp.release_buttons(gamepad_button_num)
            # print(" release", gamepad_button_num, end="")



    gp.move_joystick(index=0,
        x=int(map_range(joystick.x, 0, 255, -127, 127)),
        y=int(map_range(joystick.y, 0, 255, -127, 127)),
    )

