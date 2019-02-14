"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jake Lauteri.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # run_test_arm()
    # calibrate_arm()s
    # real_thing()
def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def calibrate_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def move_arm_to_position():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position()

def lower_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()

def real_thing():
    robot = rosebot.RoseBot()
    receiver = rec.receiver(robot)
    mqtt_reciver = com.MqttClient(receiver)
    mqtt_reciver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if receiver.is_time_to_stop:
            break

def tones_9(self, freq, iteration):
    self.robot.drive_system.go(100, 100)
    self.robot.drive_system.left_motor.reset_position()
    start = self.robot.drive_system.left_motor.get_position()

    while True:
        if self.robot.drive_system.left_motor.get_position() - start >= 90:
            self.robot.sound_system.tone_maker.play_tone(freq, 500)
            freq = int(freq) + int(iteration)
            start = self.robot.drive_system.left_motor.get_position()
            break

def cam_10(self, speed, direction):
    if direction == "clockwise":
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, 10)
        self.robot.drive_system.left_motor.turn_on(-50)
        self.robot.drive_system.right_motor.turn_on(50)
        time.sleep(.05)
    elif direction == "counterclockwise":
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, 10)
        self.robot.drive_system.left_motor.turn_on(50)
        self.robot.drive_system.right_motor.turn_on(-50)
        time.sleep(.05)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()