import m3_rosebot

#


class ResponderToGUIMessages(object):
    def __init__(self,robot):
        """
        :type robot: rosebot.Rosebot
        """
        self.robot = robot
        self.stop_program=False
        self.mqtt_sender=None
    def forward(self,left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        right = int(right_wheel_speed)
        self.robot.drive_system.go(left, right)
    def stop(self):
        print('got stop')
        self.robot.drive_system.stop()
    def left(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed) * -1, int(rspeed))
        print('Got left')

    def backward(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed) * -1, int(rspeed) * -1)
        print('Got backward', "-",lspeed, "-",rspeed)

    def right(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed) * -1)
        print('Got right')
    def quit(self):
        self.stop_program=True

    def go_and_increase_frequency(self,speed,frequency_step):
        print("receive go and increase frequency")
        self.robot.drive_system.go_and_increase_frequency(speed,frequency_step)

    def go_forward_until(self,speed, rate):
        print("let this robot start to find object")
        self.robot.drive_system.go_and_increase_beep(int(speed),int(rate))

    def go_find(self, inches, speed):

        self.robot.drive_system.go_forward_until_distance_is_less_than(inches,speed,self.mqtt_sender)

        print("receive go&find")


    def go_back(self, inches, speed):
        print("receive go&back")
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)
    def dance(self):
        print('dance')
        self.robot.sound_system.speech_maker.speak('Hello everyone!')
        self.robot.drive_system.go_straight_for_inches_using_encoder(5,80)
        self.robot.drive_system.go_straight_for_inches_using_encoder(3,60)
        self.robot.drive_system.go_straight_for_inches_using_encoder(5, -80)
        self.robot.drive_system.go_straight_for_inches_using_encoder(3, -60)
        self.robot.drive_system.go_straight_for_seconds(3,-60)
        self.robot.drive_system.go_straight_for_seconds(6, 60)
        self.robot.drive_system.go_straight_for_seconds(3, -60)

        self.robot.arm_and_claw.calibrate_arm()

    def stretch_arm(self):
        print('stretch')
        self.robot.arm_and_claw.calibrate_arm()

    def pick_up(self):
        print("receive pick up")
        self.robot.arm_and_claw.raise_arm()

    def put_down(self):
        print("receive put down")
        self.robot.arm_and_claw.lower_arm()
