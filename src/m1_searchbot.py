import rosebot
import time


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
