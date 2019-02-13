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
        self.is_time_to_stop = False

    def quit(self):
        print('Quitting')
        self.is_time_to_stop = True

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
        print('Beeping')
        for k in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()
    def freq(self, f, s):
        print('Playing frequency')
        self.robot.sound_system.tone_maker.play_tone(f, s).wait()
    def speak(self, s):
        print('Speaking')
        self.robot.sound_system.speech_maker.speak(s)
    def calibrate(self):
        self.robot.arm_and_claw.calibrate_arm()
        print('Calibrating')
    def movetopos(self, pos):
        self.robot.arm_and_claw.move_arm_to_position(pos)
        print('Moving')
    def straightuntilless(self, intensity):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(float(intensity))
        print('Going straight until intensity is less than ', intensity)
    def straightuntilgreater(self, intensity):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(float(intensity))
        print('Going straight until intensity is less than ', intensity)
    def straightuntilcoloris(self, color):
        self.robot.drive_system.go_straight_until_color_is(color, 100)
        print('Going straight until color is ', color)
    def straightuntilcolorisnot(self, color):
        self.robot.drive_system.go_straight_until_color_is_not(color, 100)
        print('Going straight until color is not ', color)