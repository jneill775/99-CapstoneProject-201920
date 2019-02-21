import rosebot
import time

robot = rosebot.RoseBot()

def sprint3(dist, sweeps):
    print("Beginning sweep")
    robot.sound_system.speech_maker.speak("Hunting kulaks")
    sweep_plot(int(dist), int(sweeps))
    robot.sound_system.speech_maker.speak("Taking to gulag")
    robot.arm_and_claw.raise_arm()
    return_to_start()
    robot.arm_and_claw.calibrate_arm()
    robot.sound_system.speech_maker.speak("Arrived at gulag")



def check_item():

    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
        return True
    else:
        return False

def sweep_plot(dist, sweeps):
    robot.tracker = 0
    dist = int(dist)
    sweeps = int(sweeps)

    for k in range(sweeps):
        if k % 2 != 1:
            robot.drive_system.go_straight_for_inches_using_time(dist, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.drive_system.spin_clockwise_for_time(0.63, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.drive_system.go_straight_for_inches_using_time(9, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.drive_system.spin_clockwise_for_time(0.63, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.tracker += 1
            print(robot.tracker)
        if k % 2 == 1:
            robot.drive_system.go_straight_for_inches_using_time(dist, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.drive_system.spin_counterclockwise_for_time(0.63, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.drive_system.go_straight_for_inches_using_time(9, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.drive_system.spin_counterclockwise_for_time(0.63, 100)
            if check_item() is True:
                robot.drive_system.go_straight_for_inches_using_time(2, -100)
                break
            robot.tracker += 1
            print(robot.tracker)
        if robot.tracker == sweeps:
            robot.sound_system.speech_maker.speak("Nothing found, returning")

def return_to_start():
    if robot.tracker == 0:
        robot.drive_system.spin_clockwise_for_time(1, 100)
        robot.drive_system.go_straight_until_color_is("White")
    elif robot.tracker % 2 == 0:
        robot.drive_system.spin_counterclockwise_for_time(0.65, 100)
        robot.drive_system.go_straight_for_inches_using_time(9 * robot.tracker, 100)
        robot.drive_system.spin_counterclockwise_for_time(0.65, 100)
        robot.drive_system.go_straight_until_color_is("White")
    elif robot.tracker % 2 != 0:
        robot.drive_system.spin_clockwise_for_time(0.65, 100)
        robot.drive_system.go_straight_for_inches_using_time(9 * robot.tracker, 100)
        robot.drive_system.spin_counterclockwise_for_time(0.65, 100)
        robot.drive_system.go_straight_until_color_is("White")
    else:
        pass