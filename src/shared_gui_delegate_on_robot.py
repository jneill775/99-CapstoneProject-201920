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
        self.robot.drive_system.go(int(lspeed), int(rspeed))
        print('Got forward', lspeed, rspeed)

    def stop(self):
        self.robot.drive_system.stop()
        print('Got stop')

    def backward(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed) * -1, int(rspeed) * -1)
        print('Got backward', "-",lspeed, "-",rspeed)

    def left(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed) * -1, int(rspeed))
        print('Got left')

    def right(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed) * -1)
        print('Got right')
    def hoist(self):
        self.robot.arm_and_claw.raise_arm()
        print('Hoist your dongers')
    def lower(self):
        self.robot.arm_and_claw.lower_arm()
        print('Lowering arm')
    def straightforseconds(self, s):
        self.robot.drive_system.go_straight_for_seconds(s, 100)
        print('Going straight for seconds')
    def straightusingtime(self, i):
        self.robot.drive_system.go_straight_for_inches_using_time(i, 100)
        print('Going straight for inches using time')
    def straightusingencoder(self, i):
        self.robot.drive_system.go_straight_for_inches_using_encoder(i, 100)
        print('Going straight for inches using encoder')
    def beep(self, n):
        self.robot.sound_system.beep(n)
        print('Beeping')
    def freq(self, f, s):
        self.robot.sound_system.play_freq(f, s)
        print('Playing frequency')
    def speak(self, s):
        self.robot.sound_system.speak(s)
        print('Speaking')