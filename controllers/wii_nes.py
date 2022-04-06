# SPDX-FileCopyrightText: 2022 John Furcean
# SPDX-License-Identifier: MIT

# In order to use this you must have wii_classic_controller_usb.py
# and the associated boot.py file on your CIRCUITPY drive

import board
import usb_hid
from adafruit_simplemath import map_range
from hid_gamepad import Gamepad
from wiichuck.classic_controller import ClassicController


def map_buttons(buttons, dpad):

    # mapped they so they worked appropriately with https://gamepad-tester.com/

    buttons_mapped=[0]*16

    buttons_mapped[0] = buttons.B
    buttons_mapped[1] = buttons.A
    buttons_mapped[2] = buttons.select
    buttons_mapped[3] = buttons.start

    # buttons 5 - 12 not used
    
    buttons_mapped[12] = dpad.up
    buttons_mapped[13] = dpad.down
    buttons_mapped[14] = dpad.left
    buttons_mapped[15] = dpad.right

    return buttons_mapped



gp = Gamepad(usb_hid.devices)
controller = ClassicController(board.STEMMA_I2C())


while True:

    _, buttons, dpad, _ = controller.values

    buttons_mapped = map_buttons(buttons,dpad)

    for i, button in enumerate(buttons_mapped):
        gamepad_button_num = i+1
        if button:
            gp.press_buttons(gamepad_button_num)
            # print(" press", gamepad_button_num, end="")
        else:
            gp.release_buttons(gamepad_button_num)
            # print(" release", gamepad_button_num, end="")