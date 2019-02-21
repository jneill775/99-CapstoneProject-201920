import tkinter
from tkinter import ttk
from PIL import ImageTk as itk

#yifei Xiao
def control(window, mqtt_sender):
    """"
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
    title_label=ttk.Label(frame,text='Dancer')
    title_label.grid(row=0,column=1)

    go_button=ttk.Button(frame,text='go & find️')
    go_button.grid(row=1,column=1)
    go_button["command"]=lambda :mqtt_sender.send_message('go_find',[4,50])
    back_button=ttk.Button(frame,text='moveaway')
    back_button.grid(row=3, column=1)
    back_button["command"]=lambda :mqtt_sender.send_message('go_back',[10,50])
    left_button = ttk.Button(frame, text='pick up')
    left_button.grid(row=2, column=0)
    left_button["command"] = lambda: mqtt_sender.send_message('pick_up', [])
    right_button = ttk.Button(frame, text='put down')
    right_button.grid(row=2, column=2)
    right_button["command"] = lambda: mqtt_sender.send_message('put_down', [])
    exit_button = ttk.Button(frame, text='exit')
    exit_button.grid(row=4, column=2)
    exit_button["command"] = lambda: exit()
    stretch_arm_button=ttk.Button(frame,text='stretch arm')
    stretch_arm_button.grid(row=4,column=0)
    stretch_arm_button['command'] = lambda: mqtt_sender.send_message('stretch_arm', [])
    dance_button=ttk.Button(frame,text='Dance')
    dance_button.grid(row=4,column=1)
    dance_button['command']=lambda :mqtt_sender.send_message('dance', [])

    blank=ttk.Label(frame,text='')
    blank.grid(row=3,column=1)

    window.bind_all('<KeyRelease>',lambda event:mqtt_sender.send_message('stop', []))
    window.bind_all('<Key-w>',lambda event:mqtt_sender.send_message('forward',[50,50]))
    window.bind_all('<Key-s>', lambda event: mqtt_sender.send_message('backward', [50,50]))
    window.bind_all('<Key-a>', lambda event: mqtt_sender.send_message('left', [40,40]))
    window.bind_all('<Key-d>', lambda event: mqtt_sender.send_message('right', [40,40]))

    return frame

def canvas(window):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    cv = tkinter.Canvas(frame, bg='white', width=500, height=200)
    cv.grid(row=1,column=0)

    cv.create_text(240,20,text='Dance',fill='black')
    return frame,cv

