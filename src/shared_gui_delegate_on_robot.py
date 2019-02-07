"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
  Winter term, 2018-2019.
"""

class Reciever(object):
    def __init__(self, robot):
        """ :type robot:    rosebot.RoseBot"""
        self.robot = robot

    def forward(self, lspeed, rspeed):
        print('Got forward', lspeed, rspeed)
        self.robot.drive_system.go(int(lspeed), int(rspeed))
