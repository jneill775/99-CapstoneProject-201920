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
    # tones_9()
    # tones_9_cycle_faster()
    # cam_10()
    search()
    put_away()
    celebration()
    sleep()

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

def tones_9(initial_rate, rate_of_increase, robot):

    robot.drive_system.go(100, 100)
    robot.drive_system.left_motor.reset_position()
    start_distance = robot.drive_system.ir_proximity_sensor.get_distance_in_inches()
    start_time = time.time()
    rate = initial_rate
    delta = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()/ ((robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - 0.01) / rate_of_increase)

    while True:
        if robot.drive_system.left_motor.get_position() - start_distance >= delta:
            if time.time() - start_time >= rate:
                start_distance = robot.left_motor.get_position()
                start_time, rate = tones_9_cycle_faster(rate, rate_of_increase, robot)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches <= 1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break

def tones_9_cycle_faster(rate, rate_of_increase, robot):

    robot.led_system.left_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_on()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    return time.time(), rate - rate_of_increase

def cam_10(speed, direction, robot):

    if direction == "clockwise":
        robot.drive_system.spin_clockwise_until_sees_object(speed, 10)
        robot.drive_system.left_motor.turn_on(-50)
        robot.drive_system.right_motor.turn_on(50)
        time.sleep(.07)
    elif direction == "counterclockwise":
        robot.drive_system.spin_counterclockwise_until_sees_object(speed, 10)
        robot.drive_system.left_motor.turn_on(50)
        robot.drive_system.right_motor.turn_on(-50)
        time.sleep(.02)
    tones_9(.05, .005, robot)

def search():
    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.drive_system.spin_counterclockwise_until_sees_object()
    robot.drive_system.go()
    robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()

def put_away():
    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.drive_system.spin_clockwise_until_sees_object()
    robot.drive_system.go()
    robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()

def celebration():
    robot = rosebot.RoseBot()
    robot.sound_system.speech_maker()
    robot.arm_and_claw.move_arm_to_position()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()

def sleep():
    robot = rosebot.RoseBot()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_on()
    robot.sound_system.speech_maker()
    robot.drive_system.go_straight_for_inches_using_encoder()
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_off()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()