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

    #feature10_john()
    #beepfreq()

    real_thing()


def real_thing():
    robot = rosebot.RoseBot()
    reciever = rec.Reciever(robot)
    mqtt_reciever = com.MqttClient(reciever)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(0.01)
        if reciever.is_time_to_stop:
            break

def feature10_john(speed, clock):
    robot = rosebot.RoseBot()
    if int(clock) == 0:
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 50)
        beepfreq(50, 50)
    elif int(clock) == 1:
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 50)
        beepfreq(50, 50)
    else:
        pass

def beepfreq(f, m):
    robot = rosebot.RoseBot()
    initialdist = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.go(100, 100)
    while True:
        percentdist = (robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() / initialdist)
        pausetime = 3 * (percentdist) / ((int(m)) + ((int(f)) * (1-percentdist)))
        robot.sound_system.beeper.beep().wait()
        print(pausetime)
        time.sleep(abs(pausetime))

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 3:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break

def sprint3(dist, sweeps):
    robot = rosebot.RoseBot()
    print("Beginning sweep")
    robot.drive_system.sweep_plot(int(dist), int(sweeps))
    robot.arm_and_claw.raise_arm()

def check_item():
    robot = rosebot.RoseBot()

    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 7:
        return True
    else:
        return False

def sweep_plot(self, dist, sweeps):
    robot = rosebot.RoseBot()
    robot.tracker = 0
    dist = int(dist)
    sweeps = int(sweeps)

    for k in range(sweeps):
        if k % 2 != 1:
            self.go_straight_for_inches_using_time(dist, 100)
            if robot.sensor_system.check_item() is True:
                break
            self.spin_clockwise_for_time(0.55, 100)
            if robot.sensor_system.check_item() is True:
                break
            self.go_straight_for_inches_using_time(9, 100)
            if robot.sensor_system.check_item() is True:
                break
            self.spin_clockwise_for_time(0.55, 100)
            if robot.sensor_system.check_item() is True:
                break
            robot.tracker += 1
            print(robot.tracker)
        if k % 2 == 1:
            self.go_straight_for_inches_using_time(dist, 100)
            if robot.sensor_system.check_item() is True:
                break
            self.spin_counterclockwise_for_time(0.55, 100)
            if robot.sensor_system.check_item() is True:
                break
            self.go_straight_for_inches_using_time(9, 100)
            if robot.sensor_system.check_item() is True:
                break
            self.spin_counterclockwise_for_time(0.55, 100)
            if robot.sensor_system.check_item() is True:
                break
            robot.tracker += 1
            print(robot.tracker)
        if robot.tracker == sweeps:
            robot.sound_system.speech_maker.speak("Nothing found, returning")


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

main()