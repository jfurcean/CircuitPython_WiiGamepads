# SPDX-FileCopyrightText: 2022 John Furcean
# SPDX-License-Identifier: MIT

# In order to use this you must have wii_classic_controller_usb.py
# and the associated boot.py file on your CIRCUITPY drive

import board
import usb_hid
from adafruit_simplemath import map_range
from hid_gamepad import Gamepad
from wiichuck.guitar import Guitar

def map_buttons(buttons, strum):

    # mapped buttons so they work appropriately with https://gamepad-tester.com/

    buttons_mapped=[0]*16

    buttons_mapped[0] = buttons.green
    buttons_mapped[1] = buttons.red
    buttons_mapped[2] = buttons.yellow
    buttons_mapped[3] = buttons.blue
    buttons_mapped[4] = buttons.orange

    # buttons 6 - 8 not used

    buttons_mapped[8] = buttons.select
    buttons_mapped[9] = buttons.start

    # buttons 11 - 12 not used

    buttons_mapped[12] = strum.up
    buttons_mapped[13] = strum.down

    # buttons 15 - 16 not used

    return buttons_mapped


gp = Gamepad(usb_hid.devices)
controller = Guitar(board.STEMMA_I2C())


while True:

    joystick, buttons, strum, whammy, _ = controller.values


    buttons_mapped = map_buttons(buttons, strum)

    for i, button in enumerate(buttons_mapped):
        gamepad_button_num = i+1
        if button:
            gp.press_buttons(gamepad_button_num)
            # print(" press", gamepad_button_num, end="")
        else:
            gp.release_buttons(gamepad_button_num)
            # print(" release", gamepad_button_num, end="")



    gp.move_joystick(index=0,
        x=int(map_range(joystick.x, 0, 64, -127, 127)),
        y=int(map_range(joystick.y, 0, 64, -127, 127)),
    )

    gp.move_analog(index=0,
        value=int(map_range(whammy, 0, 31, 0, 127)),
    )