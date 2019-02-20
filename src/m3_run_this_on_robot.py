"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Yifei Xiao.
  Winter term, 2018-2019.
"""

import m3_rosebot
import mqtt_remote_method_calls as com
import time
import m3_personal_gui_delegate_ as rec

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()

def real_thing():
    robot=m3_rosebot.RoseBot()
    delegate=rec.ResponderToGUIMessages(robot)
    mqtt_receiver=com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()
    delegate.mqtt_sender=mqtt_receiver

    while True:
        time.sleep(0.01)
        if delegate.stop_program:
            break



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()