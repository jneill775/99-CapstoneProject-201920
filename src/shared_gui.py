"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Yifei Xiao.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame

def get_drive_system_frame(window, mqtt_sender):

    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Drive System")
    label1 = ttk.Label(frame, text="Duration of Movement OR Desired Distance:")
    time_entry = ttk.Entry(frame, width=8)
    color_label = ttk.Label(frame, text="Color Sensor Movement")
    ir_label = ttk.Label(frame, text="IR Movement")
    delta_label = ttk.Label(frame, text="Delta")
    inches_label = ttk.Label(frame, text="Inches")
    camera_label = ttk.Label(frame, text="Camera Movement")
    less_than_entry = ttk.Entry(frame, width=8)
    greater_than_entry = ttk.Entry(frame, width=8)
    straight_until_color_is_entry = ttk.Entry(frame, width=8)
    straight_until_color_is_not_entry = ttk.Entry(frame, width=8)
    forward_until_less_than_entry = ttk.Entry(frame, width=8)
    backward_until_greater_than_entry = ttk.Entry(frame, width=8)
    distance_within_entry_delta = ttk.Entry(frame, width=8)
    distance_within_entry_inches = ttk.Entry(frame, width=8)
    clockwise_area_entry = ttk.Entry(frame, width=8)
    counterclockwise_area_entry = ttk.Entry(frame, width=8)


    straight_until_less_button =  ttk.Button(frame, text="Go straight until intensity is less than:")
    straight_until_greater_button =  ttk.Button(frame, text="Go straight until intensity is greater than:")
    straight_until_color_is_button = ttk.Button(frame, text="Go straight until color is:")
    straight_until_color_is_not_button = ttk.Button(frame, text="Go straight until color is not:")
    forward_until_less_than_button = ttk.Button(frame, text="Go forward until dist less than:")
    backward_until_greater_than_button = ttk.Button(frame, text="Go backward until dist greater than:")
    go_until_within_button = ttk.Button(frame, text="Go until distance is within:")
    go_for_seconds = ttk.Button(frame, text="Go straight for seconds")
    go_for_time = ttk.Button(frame, text="Go straight for inches using time")
    go_for_encoder = ttk.Button(frame, text="Go straight for inches using encoder")
    camera_display_button = ttk.Button(frame, text="Display Camera Data")
    clockwise_area_button = ttk.Button(frame, text="Spin Clockwise Area:")
    counterclockwise_area_button = ttk.Button(frame, text="Spin Counterclockwise Area:")

    blank_label = ttk.Label(frame, text="")


    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    camera_label.grid(row=5, column=7)
    label1.grid(row=1, column=0)
    time_entry.grid(row=1, column=1)
    color_label.grid(row=5, column=1)
    less_than_entry.grid(row=6, column=1)
    greater_than_entry.grid(row=7, column=1)
    straight_until_color_is_entry.grid(row=8, column=1)
    straight_until_color_is_not_entry.grid(row=9, column=1)
    ir_label.grid(row=5, column=3)
    forward_until_less_than_entry.grid(row=6, column=3)
    backward_until_greater_than_entry.grid(row=7, column=3)
    delta_label.grid(row=8, column=3)
    inches_label.grid(row=8, column=4)
    distance_within_entry_delta.grid(row=9, column=3)
    distance_within_entry_inches.grid(row=9, column=4)
    clockwise_area_entry.grid(row=7, column=7)
    counterclockwise_area_entry.grid(row=8, column=7)



    blank_label.grid(row=2, column=1)
    forward_until_less_than_button.grid(row=6, column=2)
    backward_until_greater_than_button.grid(row=7, column=2)
    straight_until_color_is_button.grid(row=8, column=0)
    straight_until_color_is_not_button.grid(row=9, column=0)
    straight_until_less_button.grid(row=6, column=0)
    straight_until_greater_button.grid(row=7, column=0)
    go_until_within_button.grid(row=9, column=2)
    blank_label.grid(row=4, column=1)
    go_for_seconds.grid(row=3, column=0)
    go_for_time.grid(row=3, column=1)
    go_for_encoder.grid(row=3, column=2)
    camera_display_button.grid(row=6, column=7)
    clockwise_area_button.grid(row=7, column=6)
    counterclockwise_area_button.grid(row=8, column=6)

    # Set the Button callbacks:
    go_for_seconds["command"] = lambda: handle_go_straight_for_seconds(time_entry, mqtt_sender)
    go_for_time["command"] = lambda: handle_go_straight_for_inches_using_time(time_entry, mqtt_sender)
    go_for_encoder["command"] = lambda: handle_go_straight_for_inches_using_encoder(time_entry, mqtt_sender)
    straight_until_less_button["command"] = lambda: handle_straight_until_less_than(less_than_entry, mqtt_sender)
    straight_until_greater_button["command"] = lambda : handle_straight_until_greater_than(greater_than_entry, mqtt_sender)
    straight_until_color_is_button["command"] = lambda: handle_straight_until_color_is(straight_until_color_is_entry, mqtt_sender)
    straight_until_color_is_not_button["command"] = lambda: handle_straight_until_color_is_not(straight_until_color_is_not_entry, mqtt_sender)
    forward_until_less_than_button["command"] = lambda: handle_forward_until_less(forward_until_less_than_entry, mqtt_sender)
    backward_until_greater_than_button["command"] = lambda: handle_backward_until_greater(backward_until_greater_than_entry, mqtt_sender)
    go_until_within_button["command"] = lambda: handle_go_until_within(distance_within_entry_delta, distance_within_entry_inches, mqtt_sender)
    clockwise_area_button["command"] = lambda: handle_go_clockwise(clockwise_area_entry, mqtt_sender)
    counterclockwise_area_button["command"] = lambda: handle_go_counterclockwise(counterclockwise_area_entry, mqtt_sender)
    camera_display_button["command"] = lambda: handle_camera_display(mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_sound_system_frame(window, mqtt_sender):

    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sound System")
    beep_label = ttk.Label(frame, text="Beep for a number of times:")
    freq_label = ttk.Label(frame, text="Play a frequency (box 1) for a period of time(box 2):")
    speak_label = ttk.Label(frame, text="Speak a phrase:")


    beep_entry = ttk.Entry(frame, width=8)
    beep_entry.insert(0, "")

    freq_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    freq_entry.insert(0, "")

    time_entry = ttk.Entry(frame, width=8)
    time_entry.insert(0, "")

    speak_entry = ttk.Entry(frame, width=8)
    speak_entry.insert(0, "")



    beep_button = ttk.Button(frame, text="Beep")

    freq_button = ttk.Button(frame, text="Play Frequency")
    speak_button = ttk.Button(frame, text="Speak")


    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    beep_label.grid(row=1, column=0)
    speak_label.grid(row=1, column=1)
    freq_label.grid(row=1, column=2)
    beep_entry.grid(row=2, column=0)
    freq_entry.grid(row=2, column=1)
    speak_entry.grid(row=2, column=2)
    time_entry.grid(row=2, column=3)

    beep_button.grid(row=3, column=0)
    freq_button.grid(row=3, column=2)
    speak_button.grid(row=3, column=1)


    # Set the button callbacks:
    beep_button["command"] = lambda: handle_beep(beep_entry, mqtt_sender)
    freq_button["command"] = lambda: handle_freq(freq_entry, time_entry, mqtt_sender)
    speak_button["command"] = lambda: handle_speak(speak_entry, mqtt_sender)


    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Forward', [left_entry_box.get(), right_entry_box.get()])
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Backward', [left_entry_box.get(), right_entry_box.get()])
    mqtt_sender.send_message("backward", [left_entry_box.get(), right_entry_box.get()])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Left')
    mqtt_sender.send_message("left", [left_entry_box.get(), right_entry_box.get()])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Right')
    mqtt_sender.send_message("right", [left_entry_box.get(), right_entry_box.get()])

def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Stop')
    mqtt_sender.send_message("stop")

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Raise arm')
    mqtt_sender.send_message("hoist")


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Lower arm')
    mqtt_sender.send_message("lower")

def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Calibrating arm')
    mqtt_sender.send_message("calibrate")


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('Moving arm to position')
    mqtt_sender.send_message("movetopos", [arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('Quit')
    mqtt_sender.send_message("quit")

def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('Exit')
    handle_quit(mqtt_sender)
    exit()
###############################################################################
# Handlers for Buttons in the Drive System frame.
###############################################################################

def handle_go_straight_for_seconds(time_entry, mqtt_sender):
    print('Going straight for seconds')
    mqtt_sender.send_message("straightforseconds", [time_entry.get()])

def handle_go_straight_for_inches_using_time(time_entry, mqtt_sender):
    print('Going straight for inches using time')
    mqtt_sender.send_message("straightusingtime", [time_entry.get()])

def handle_go_straight_for_inches_using_encoder(time_entry, mqtt_sender):
    print('Going straight for inches using encoder')
    mqtt_sender.send_message("straightusingencoder", [time_entry.get()])

def handle_straight_until_less_than(less_than_entry, mqtt_sender):
    print('Going straight until intensity is less than ', less_than_entry)
    mqtt_sender.send_message("straightuntilless", [less_than_entry.get()])

def handle_straight_until_greater_than(greater_than_entry, mqtt_sender):
    print('Going straight until intensity is greater than ', greater_than_entry)
    mqtt_sender.send_message("straightuntilgreater", [greater_than_entry.get()])

def handle_straight_until_color_is(straight_until_color_is_entry, mqtt_sender):
    print('Going straight until color is ', straight_until_color_is_entry)
    mqtt_sender.send_message("straightuntilcoloris", [straight_until_color_is_entry.get()])

def handle_straight_until_color_is_not(straight_until_color_is_not_entry, mqtt_sender):
    print('Going straight until color is not ', straight_until_color_is_not_entry)
    mqtt_sender.send_message("straightuntilcolorisnot", [straight_until_color_is_not_entry.get()])

def handle_forward_until_less(forward_until_less_than_entry, mqtt_sender):
    print('Going forward until distance is less than ', forward_until_less_than_entry)
    mqtt_sender.send_message("straightdistless", [forward_until_less_than_entry.get()])

def handle_backward_until_greater(backward_until_greater_than_entry, mqtt_sender):
    print('Going backward until distance is greater than ', backward_until_greater_than_entry)
    mqtt_sender.send_message("straightdistmore", [backward_until_greater_than_entry.get()])

def handle_go_until_within(distance_within_entry_delta, distance_within_entry_inches, mqtt_sender):
    print('Going forward until distance is +- ', distance_within_entry_delta, 'inches from ', distance_within_entry_inches)
    mqtt_sender.send_message("distwithinrange", [distance_within_entry_delta.get(), distance_within_entry_inches.get()])

def handle_go_clockwise(clockwise_area_entry, mqtt_sender):
    print('Going clockwise for area ', clockwise_area_entry)
    mqtt_sender.send_message("clockwise", [clockwise_area_entry.get()])

def handle_go_counterclockwise(counterclockwise_area_entry, mqtt_sender):
    print('Going counterclockwise for area ', counterclockwise_area_entry)
    mqtt_sender.send_message("counterclockwise", [counterclockwise_area_entry.get()])

def handle_camera_display(mqtt_sender):
    print('Displaying Camera Feed')
    mqtt_sender.send_message("display")

###############################################################################
# Handlers for Buttons in the Sound System frame.
###############################################################################

def handle_beep(beep_entry, mqtt_sender):
    print('Beeping')
    mqtt_sender.send_message("beep", [beep_entry.get()])

def handle_freq(freq_entry, time_entry, mqtt_sender):
    print('Playing frequency')
    mqtt_sender.send_message("freq", [freq_entry.get(), time_entry.get()])

def handle_speak(speak_entry, mqtt_sender):
    print('Speaking')
    mqtt_sender.send_message("speak", [speak_entry.get()])

