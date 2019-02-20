import rosebot
import time


# This program will run a cleaning bot.


def search():

    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.drive_system.spin_counterclockwise_until_sees_object((25, 100), 100)
    robot.drive_system.go(50, 50)
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d < 2:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


def put_away():

    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.drive_system.spin_clockwise_until_sees_object(100, 25)
    robot.drive_system.go(50,50)
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d < 3:
            robot.drive_system.stop()
            robot.arm_and_claw.lower_arm()
            robot.led_system.left_led.turn_off()
            robot.led_system.right_led.turn_off()
            break

def celebration():

    robot = rosebot.RoseBot()
    robot.sound_system.speech_maker.speak('Cleaned Up')
    robot.arm_and_claw.move_arm_to_position(2000)
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    time.sleep(.1)
    robot.arm_and_claw.move_arm_to_position(1000)
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    time.sleep(.1)
    robot.arm_and_claw.move_arm_to_position(2000)
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    time.sleep(.1)
    robot.arm_and_claw.move_arm_to_position(1000)
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    time.sleep(.1)
    robot.arm_and_claw.move_arm_to_position(2000)
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    time.sleep(.1)
    robot.arm_and_claw.move_arm_to_position(0)
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()



def sleep():

    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.sound_system.speech_maker.speak('Sleepy Time')
    robot.drive_system.go_straight_for_inches_using_encoder(25,(50,50))
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()

