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
    tones_9()
    tones_9_cycle_faster()
    # cam_10()

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

def tones_9(self, initial_rate, rate_of_increase):

    self.robot.drive_system.go(100, 100)
    self.robot.drive_system.left_motor.reset_position()
    start_distance = self.robot.drive_system.ir_proximity_sensor.get_distance_in_inches()
    start_time = time.time()
    rate = initial_rate
    delta = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()/ ((self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - 0.01) / rate_of_increase)

    while True:
        if self.robot.drive_system.left_motor.get_position() - start_distance >= delta:
            if time.time() - start_time >= rate:
                start_distance = self.robot.left_motor.get_position()
                start_time, rate = tones_9_cycle_faster(self, rate, rate_of_increase)
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches <= 1:
            self.robot.drive_system.stop()
            self.robot.arm_and_claw.raise_arm()
            break

def tones_9_cycle_faster(self, rate, rate_of_increase):

    self.robot.led_system.left_led.turn_on()
    self.robot.led_system.left_led.turn_off()
    self.robot.led_system.right_led.turn_on()
    self.robot.led_system.right_led.turn_off()
    self.robot.led_system.left_led.turn_on()
    self.robot.led_system.right_led.turn_on()
    self.robot.led_system.left_led.turn_off()
    self.robot.led_system.right_led.turn_off()
    return time.time(), rate - rate_of_increase

def cam_10(self, speed, direction):

    if direction == "clockwise":
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, 10)
        self.robot.drive_system.left_motor.turn_on(-50)
        self.robot.drive_system.right_motor.turn_on(50)
        time.sleep(.07)
    elif direction == "counterclockwise":
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, 10)
        self.robot.drive_system.left_motor.turn_on(50)
        self.robot.drive_system.right_motor.turn_on(-50)
        time.sleep(.02)
    tones_9(self, .05, .005)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()