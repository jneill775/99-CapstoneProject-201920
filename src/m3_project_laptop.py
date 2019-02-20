import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import m3_personal_gui as m3
import time



def main():
    delegate=Delegate_on_laptop()
    mqtt_sender=com.MqttClient(delegate)
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Dancer")
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    control_panel,canvas=get_shared_frames(main_frame,mqtt_sender,delegate)
    grid_frames(control_panel,canvas)
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender,delegate):
    control_panel = m3.control(main_frame, mqtt_sender)
    canvas,cv = m3.canvas(main_frame)   
    delegate.canvas=cv

    return control_panel, canvas

def grid_frames(control_panel, canvas):
    canvas.grid(row=1, column=0)
    control_panel.grid(row=2, column=0)

class Delegate_on_laptop(object):
    def __init__(self, canvas=None):
        self.canvas = canvas
    def show_black(self):
        print('black')
        self.canvas.create_rectangle(225,50,275,100,fill='black')
        self.canvas.create_text(200,120,text='show starts',fill='black')

main()