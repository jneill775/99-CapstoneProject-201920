"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and John Neill.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec

def main():

    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_pc()

    real_thing()

def return_value(return_val, mqtt_client=com.MqttClient()):
    mqtt_client.connect_to_pc()
    mqtt_client.send_message('update_interface', [return_val])

def real_thing():
    robot = rosebot.RoseBot()
    reciever = rec.Reciever(robot)
    mqtt_reciever = com.MqttClient(reciever)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(0.01)
        if reciever.is_time_to_stop:
            break

def sprint3(dist, sweeps):
    robot = rosebot.RoseBot()
    robot.sound_system.beeper.beep()
    sweep_plot(dist, sweeps)

def check_item():
    robot = rosebot.RoseBot()
    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
        return True
    else:
        return False

def sweep_plot(dist, sweeps):
    robot = rosebot.RoseBot()
    robot.tracker = 0
    dist = int(dist)
    sweeps = int(sweeps)

    for k in range(sweeps):
        if k % 2 != 1:
            robot.drive_system.go_straight_for_inches_using_time(dist, 100)
            if check_item() is True:
                break
            robot.drive_system.go()
            robot.drive_system.spin_clockwise_for_time(2, 100)
            if check_item() is True:
                break
            robot.drive_system.go_straight_for_inches_using_time(9, 100)
            if check_item() is True:
                break
            robot.drive_system.spin_clockwise_for_time(2, 100)
            if check_item() is True:
                break
            robot.tracker += 1
            print(robot.tracker)
        if k % 2 == 1:
            robot.drive_system.go_straight_for_inches_using_time(dist, 100)
            if check_item() is True:
                break
            robot.drive_system.spin_clockwise_for_time(2, 100)
            if check_item() is True:
                break
            robot.drive_system.go_straight_for_inches_using_time(9, 100)
            if check_item() is True:
                break
            robot.drive_system.spin_clockwise_for_time(2, 100)
            if check_item() is True:
                break
            robot.tracker += 1
            print(robot.tracker)
        if robot.tracker == sweeps:
            return_value(-1)
        return



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

main()