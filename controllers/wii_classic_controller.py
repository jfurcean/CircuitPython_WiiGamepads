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

    # mapped buttons so they work appropriately with https://gamepad-tester.com/

    buttons_mapped=[0]*16

    buttons_mapped[0] = buttons.B
    buttons_mapped[1] = buttons.A
    buttons_mapped[2] = buttons.Y
    buttons_mapped[3] = buttons.X
    buttons_mapped[4] = buttons.L
    buttons_mapped[5] = buttons.R
    buttons_mapped[6] = buttons.ZL
    buttons_mapped[7] = buttons.ZR
    buttons_mapped[8] = buttons.select
    buttons_mapped[9] = buttons.start
    buttons_mapped[10] = buttons.home
    # button 12 (index 11) not used
    buttons_mapped[12] = dpad.up
    buttons_mapped[13] = dpad.down
    buttons_mapped[14] = dpad.left
    buttons_mapped[15] = dpad.right


    return buttons_mapped



gp = Gamepad(usb_hid.devices)
controller = ClassicController(board.STEMMA_I2C())


while True:

    joysticks, buttons, dpad, triggers = controller.values

    buttons_mapped = map_buttons(buttons,dpad)

    for i, button in enumerate(buttons_mapped):
        gamepad_button_num = i+1
        if button:
            gp.press_buttons(gamepad_button_num)
            # print(" press", gamepad_button_num, end="")
        else:
            gp.release_buttons(gamepad_button_num)
            # print(" release", gamepad_button_num, end="")

    gp.move_joystick(index = 0,
        x=int(map_range(joysticks.lx, 0, 63, -127, 127)),
        y=int(map_range(joysticks.ly, 0, 63, -127, 127)),
    )

    gp.move_joystick(index =1,
        x=int(map_range(joysticks.rx, 0, 31, -127, 127)),
        y=int(map_range(joysticks.ry, 0, 31, -127, 127)),
    )

    gp.move_analog(
        index = 0,
        value=int(map_range(triggers.left, 0, 31, 0, 127))
    )
    gp.move_analog(
        index=1, 
        value=int(map_range(triggers.right, 0, 31, 0, 127))
    )

    #print(f"lx:{joysticks.lx} ly:{joysticks.ly} rx:{joysticks.rx} ry:{joysticks.ry}")
    #print(f"trigger.left:{trigger.left} trigger.right:{trigger.right}")