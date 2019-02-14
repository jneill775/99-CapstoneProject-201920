"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Yifei Xiao.
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
    real_thing()

def real_thing():
    robot=rosebot.RoseBot()
    delegate=rec.Reciever(robot)
    mqtt_receiver=com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break

def beeper(time):
    robot = rosebot.RoseBot()
    robot.sound_system.beeper.beep(time)

def tone_make(frequency, duration):
    robot = rosebot.RoseBot()
    robot.sound_system.tone_maker.play_tone(frequency,duration).wait()

def speak(str):
    robot = rosebot.RoseBot()
    robot.sound_system.speech_maker.speak(str)

def go_and_increase_LEDfrequency(speed,frequency):
    robot = rosebot.RoseBot()
    robot.drive_system.go_and_increase_LEDfrequency(speed,frequency)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()