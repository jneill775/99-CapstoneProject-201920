"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
  Winter term, 2018-2019.
"""
import time

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
        self.robot.sound_system.tone_maker.play_tone(int(f), int(s)).wait()
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
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity)
        print('Going straight until intensity is less than ', intensity)
    def straightuntilgreater(self, intensity):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity)
        print('Going straight until intensity is greater than ', intensity)
    def straightuntilcoloris(self, color):
        self.robot.drive_system.go_straight_until_color_is(color)
        print('Going straight until color is ', color)
    def straightuntilcolorisnot(self, color):
        self.robot.drive_system.go_straight_until_color_is_not(color)
        print('Going straight until color is not ', color)
    def straightdistless(self, distance):
        self.robot.drive_system.go_forward_until_distance_is_less_than(distance)
        print('Going forward until distance is less than ', distance)
    def straightdistmore(self, distance):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(distance)
        print('Going backward until distance is greater than ', distance)
    def distwithinrange(self, delta, inches):
        self.robot.drive_system.go_until_distance_is_within(delta, inches)
        print('Going forward until distance is +- ', delta, 'inches from ',inches)
    def clockwise(self, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(100, area)
        print('Spinning clockwise')
    def counterclockwise(self, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(100, area)
        print('Spinning counterclockwise')
    def display(self):
        self.robot.drive_system.display_camera_data()
        print('Displaying Camera Feed')
    def beepfreq(self, f, m):
        initialdist = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        self.robot.drive_system.go(100, 100)
        while True:
            percentdist = (self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() / initialdist)
            pausetime = 3 * (percentdist) / ((int(m)) + ((int(f)) * (1-percentdist)))
            self.robot.sound_system.beeper.beep().wait()
            print(pausetime)
            time.sleep(abs(pausetime))

            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 3:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break

    def LEDfrequency(self,frequency):
        self.robot.drive_system.go_and_increase_LEDfrequency(int(frequency))
        print('Going with the higher frequency ')
    def feature10_john(self, speed, clock):
        if int(clock) == 0:
            self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), 50)
            self.beepfreq(50, 50)
        elif int(clock) == 1:
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 50)
            self.beepfreq(50, 50)
        else:
            pass



