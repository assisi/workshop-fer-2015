#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from time import sleep

"""
A simple demo of Casu interaction.
The Casu diagnostic LED lights red, when an object appears in front,
and it lights green, when an object appears behind it.

This demo is suitable for deployment on the Casu hardware (BeagleBone).
Just copy this .py file and the casu.rtc file to a folder on the 
BeagleBone and run it.
"""

from assisipy import casu

class CasuController:
    """ 
    A demo Casu controller.
    Implements a simple bee-detecting behavior.
    """

    def __init__(self, rtc_file):
        self.__casu = casu.Casu(rtc_file)

    def react_to_bees(self):
        """ 
            Changes Casu color to red, when a bee is detected in front of the Casu,
            and to Green, when a bee is detected behind a Casu.
        """
        while True:
            print(self.__casu.get_ir_raw_value(casu.ARRAY))
            self.__casu.diagnostic_led_standby()
            if self.__casu.get_ir_raw_value(casu.IR_F) > 10000:
                self.__casu.set_diagnostic_led_rgb(g=1)
            if self.__casu.get_ir_raw_value(casu.IR_B) > 10000:
                self.__casu.set_diagnostic_led_rgb(r=1)
            if (self.__casu.get_ir_raw_value(casu.IR_FR) > 10000 or
                self.__casu.get_ir_raw_value(casu.IR_BR) > 10000):
                self.__casu.set_diagnostic_led_rgb(b=1)
            if (self.__casu.get_ir_raw_value(casu.IR_FL) > 10000 or
                self.__casu.get_ir_raw_value(casu.IR_BL) > 10000):
                self.__casu.set_diagnostic_led_rgb(b=1)
            sleep(0.5)


if __name__ == '__main__':

    ctrl = CasuController(argv[1])

    # Run the Casu control program.
    ctrl.react_to_bees()


            

    
