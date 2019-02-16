"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Yifei Xiao.
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
    mqtt_sender=com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root=tkinter.Tk()
    root.title("Capstone Project W19")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame=ttk.Frame(root,padding=10,borderwidth=5,relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame,are_frame,control_frame,drive_system_frame,sound_system_frame,my_frame=get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,are_frame,control_frame,drive_system_frame, sound_system_frame,my_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame=shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame=shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame=shared_gui.get_control_frame(main_frame,mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
    my_LED_frame = get_my_own_frame(main_frame, mqtt_sender)

    return teleop_frame,arm_frame,control_frame,drive_system_frame,sound_system_frame,my_LED_frame


def grid_frames(teleop_frame, arm_frame, control_frame,drive_system_frame, sound_system_frame,my_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    drive_system_frame.grid(row=2,column=0)
    sound_system_frame.grid(row=3, column=0)
    control_frame.grid(row=4, column=0)
    my_frame.grid(row=0, column=1)


def get_my_own_frame(window,mqtt_sender):


    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    LED_freq_label = ttk.Label(frame, text="LED Frequency step:")
    LED_freq_label.grid(row=0, column=1)
    LED_freq_entry = ttk.Entry(frame, width=8)
    LED_freq_label = ttk.Label(frame, text="LED Frequency:")
    LED_freq_label.grid(row=0, column=3)
    LED_freq_entry2 = ttk.Entry(frame, width=8)
    LED_freq_entry2.grid(row=0,column=4)


    LED_freq_button = ttk.Button(frame, text="LED")
    go_and_get_label = ttk.Label(frame, text="GO and pick:")
    go_and_get_clock_entry = ttk.Entry(frame, width=8)
    go_and_get_clock_label=ttk.Label(frame,text='clock cw=0, ccw=1')
    go_and_get_speed_entry = ttk.Entry(frame, width=8)
    go_and_get_frequency_step_entry = ttk.Entry(frame, width=8)
    go_and_get_frequency_entry=ttk.Entry(frame,width=8)
    go_and_get_frequency_entry.grid(row=3,column=5)

    go_and_get_button = ttk.Button(frame, text="GO")


    LED_freq_entry.grid(row=0, column=2)
    LED_freq_button.grid(row=0, column=0)
    # go_and_get_label.grid(row=0, column=1)
    go_and_get_clock_label.grid(row=2,column=2)
    go_and_get_clock_entry.grid(row=3, column=2)
    go_and_get_speed_entry.grid(row=3, column=3)
    go_and_get_frequency_step_entry.grid(row=3, column=4)
    go_and_get_button.grid(row=3, column=0)

    LED_freq_button["command"] = lambda: handle_LED_freq_button(LED_freq_entry, LED_freq_entry2,mqtt_sender)
    go_and_get_button['command']=lambda :mqtt_sender.send_message("feature10_yifei",[int(go_and_get_clock_entry.get()),int(go_and_get_speed_entry.get()),int(go_and_get_frequency_step_entry.get()),
                                                                                int(go_and_get_frequency_entry.get())])
    return frame

def handle_LED_freq_button(LED_freq_entry,LED_freq2,mqtt_sender):
    print('LED shifting')
    freq_step=int(LED_freq_entry.get())
    freq=int(LED_freq2.get())
    mqtt_sender.send_message("LEDfrequency", [freq_step,freq])



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()