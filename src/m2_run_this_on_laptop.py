"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jake Lauteri.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


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

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, my_tones = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, my_tones)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
    tones_frame = get_my_tones(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, tones_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, my_tones):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    drive_system_frame.grid(row=2, column=0)
    sound_system_frame.grid(row=3, column=0)
    control_frame.grid(row=4, column=0)
    my_tones.grid(row=0, column=1)

def my_tones(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    freq_label = ttk.Label(frame, text="Frequency:")
    freq_rate_label = ttk.Label(frame, text="Frequency Rate:")
    freq_entry = ttk.Entry(frame, width=8)
    freq_button = ttk.Button(frame, text="Frequency Beep")
    freq_rate_entry = ttk.Entry(frame, width=8)

    freq_label.grid(row=0, column=0)
    freq_rate_label.grid(row=0, column=1)
    freq_entry.grid(row=1, column=0)
    freq_button.grid(row=1, column=1)
    freq_rate_entry.grid(row=2, column=0)

    freq_button["command"] = lambda: handle_freq_button(freq_entry, freq_rate_entry, mqtt_sender)

    return frame

def handle_freq_button(freq_entry, freq_rate_entry, mqtt_sender):
    print('Frequency beeping')
    mqtt_sender.send_message('frequency', [freq_entry.get(), freq_rate_entry.get()])

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()