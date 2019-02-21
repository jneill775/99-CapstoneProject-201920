"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and John Neill.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import rosebot
import m1_searchbot


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Super Epic Capstone Project *dabs*")
    root.config(bg='red')


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    #teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, my_frame, sprint3 = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    #grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, my_frame, sprint3)
    finalframe = get_sprint3_frame(main_frame, mqtt_sender)
    finalframe.grid(row=2, column=3)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


#def get_shared_frames(main_frame, mqtt_sender):
    #teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    #arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    #control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    #drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    #sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
    #my_frame = get_my_frame(main_frame, mqtt_sender)
    #sprint3 = get_sprint3_frame(main_frame, mqtt_sender)


    #return teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, my_frame, sprint3


#def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, my_frame, sprint3):
    #teleop_frame.grid(row=0, column=0)
    #arm_frame.grid(row=1, column=0)
    #drive_system_frame.grid(row=2, column=0)
    #sound_system_frame.grid(row=3, column=0)
    #control_frame.grid(row=4, column=0)
    #my_frame.grid(row=0, column=1)
    #sprint3.grid(row=1, column=1)

#def get_my_frame(window, mqtt_sender):

    # Construct the frame to return:
    #frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    #frame.grid()

    # Construct the widgets on the frame:
    #beep_freq_label = ttk.Label(frame, text="Beep Increase Rate:")
    #beep_rate_label = ttk.Label(frame, text="Beep Rate:")
    #feature_10_label = ttk.Label(frame, text="Feature 10")
    #speed_label = ttk.Label(frame, text="Spin Speed:")
    #clock_label = ttk.Label(frame, text="Counter/Clock:")

    #feature_10_entry = ttk.Entry(frame, width=8)
    #beep_freq_entry = ttk.Entry(frame, width=8)
    #beep_freq_button = ttk.Button(frame, text="Beep")
    #beep_rate_entry = ttk.Entry(frame, width=8)
    #clock_entry = ttk.Entry(frame, width=8)

    #feature_10_button = ttk.Button(frame, text="Feature 10")


    # Grid the widgets:
    #beep_freq_label.grid(row=0, column=1)
    #speed_label.grid(row=3, column=0)
    #beep_rate_label.grid(row=0, column=2)
    #beep_freq_entry.grid(row=1, column=1)
    #beep_rate_entry.grid(row=1, column=2)
    #beep_freq_button.grid(row=1, column=0)
    #feature_10_entry.grid(row=3, column=1)
    #feature_10_label.grid(row=2, column=1)
    #clock_entry.grid(row=4, column=1)
    #feature_10_button.grid(row=6, column=0)
    #clock_label.grid(row=4, column=0)


    # Set the Button callbacks:

    #beep_freq_button["command"] = lambda: handle_freq_button(beep_freq_entry, beep_rate_entry, mqtt_sender)
    #feature_10_button["command"] = lambda: handle_feature_10(feature_10_entry, clock_entry, mqtt_sender)


    #return frame


def get_sprint3_frame(window, mqtt_sender):

    # Construct the frame to return:
    frame = tkinter.Frame(window, borderwidth=50, relief="ridge", bg='red')
    frame.grid()

    title = ttk.Label(frame, text='Glorious Commissar Boris', font='Arial 18 bold', foreground='yellow', background='red')
    dist_label = ttk.Label(frame, text="Distance: ")
    sweeps_label = ttk.Label(frame, text="# of sweeps: ")
    dist_entry = ttk.Entry(frame, width=8)
    sweeps_entry = ttk.Entry(frame, width=8)
    go_button = ttk.Button(frame, text="Take Capitalist Pig to Gulag")
    hail_button = ttk.Button(frame, text="Salute!")



    title.grid(row=0, column=1)
    dist_label.grid(row=1, column=0)
    sweeps_label.grid(row=2, column=0)
    dist_entry.grid(row=1, column=1)
    sweeps_entry.grid(row=2, column=1)
    go_button.grid(row=3, column=1)
    hail_button.grid(row=4, column=1)


    go_button["command"] = lambda: handle_sprint3(dist_entry, sweeps_entry, mqtt_sender)
    hail_button["command"] = lambda: handle_hail_button(mqtt_sender)

    return frame


def handle_freq_button(freq_entry, freq_rate_entry, mqtt_sender):
    print('Frequency beeping')
    mqtt_sender.send_message('frequency', [freq_entry.get(), freq_rate_entry.get()])

def handle_feature_10(speed, clock, mqtt_sender):
    print("Feature 10")
    mqtt_sender.send_message("feature10_john", [speed.get(), clock.get()])
def handle_sprint3(dist_entry, sweeps_entry, mqtt_sender):
    mqtt_sender.send_message("sprint3", [dist_entry.get(), sweeps_entry.get()])
    print("Sprint 3")
def handle_hail_button(mqtt_sender):
    print("Hail Stalin!")
    mqtt_sender.send_message("m1_hail")
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()