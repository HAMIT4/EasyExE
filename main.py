import time
import serial
import tkinter
from tkinter import ttk
from tkinter import messagebox

button_set = int
# enter the joint limits
base_default_min = 30
base_default_max = 270
joint2_default_min = 30
joint2_default_max = 270
joint3_default_min = 30
joint3_default_max = 270
# this class controls the robot arm by reading values from the gui
# this information is sent to the controller using serial communication
class RobotAxis:
    def __init__(self):
        # values will have to be redefined to meet the limits
        self.Base_position = 0
        self.Link1_position = 0
        self.Link2_position = 0
        self.Gripper_nature = 0

# default display values
class defaultDisplay:
    def __init__(self):
        base_default = 90
        joint2_default = 90
        joint3_default = 90
        base_joint_display.insert('1.0', base_default)
        base_joint_slider.set(base_default)
        joint_display_j2.insert('1.0', joint2_default)
        joint_slider_j2.set(joint2_default)
        joint_display_j3.insert('1.0', joint3_default)
        joint_slider_j3.set(joint3_default)


# functions for the gui communication
# class to init default values for buttons and text widgets
class defaultPosition:

    def __init__(self):
        self.default_basePosition = int(base_joint_display.get('1.0', "end-1c"))
        self.default_joint2Position = int(joint_display_j2.get('1.0', "end-1c"))
        self.default_joint3Position = int(joint_display_j3.get('1.0', "end-1c"))

    def decrement(self, button_set, min_value, max_value):

        if button_set == 0:
            if min_value < self.default_basePosition <= max_value:
                base_joint_display.delete('1.0', 'end')
                self.default_basePosition -= 1
                return self.default_basePosition
            else:
                messagebox.showinfo("Information", "YOU HAVE REACHED THE MINIMUM LIMIT!!")
        elif button_set == 1:
            if min_value < self.default_joint2Position <= max_value:
                joint_display_j2.delete('1.0', 'end')
                self.default_joint2Position -= 1
                return self.default_joint2Position
            else:
                messagebox.showinfo("Information", "YOU HAVE REACHED THE MINIMUM LIMIT!!")
        elif button_set == 2:
            if min_value < self.default_joint3Position <= max_value:
                joint_display_j3.delete('1.0', 'end')
                self.default_joint3Position -= 1
                return self.default_joint3Position
            else:
                messagebox.showinfo("Information", "YOU HAVE REACHED THE MINIMUM LIMIT!!")


    def increment(self, button_set, min_value, max_value):
        if button_set == 0:
            if min_value < self.default_basePosition <= max_value:
                base_joint_display.delete('1.0', 'end')
                self.default_basePosition += 1
                return self.default_basePosition
            else:
                messagebox.showinfo("Information", "YOU HAVE REACHED THE MAXIMUM LIMIT!!")
        elif button_set == 1:
            if min_value < self.default_joint2Position <= max_value:
                joint_display_j2.delete('1.0', 'end')
                self.default_joint2Position += 1
                return self.default_joint2Position
            else:
                messagebox.showinfo("Information", "YOU HAVE REACHED THE MAXIMUM LIMIT!!")
        elif button_set == 2:
            if min_value < self.default_joint3Position <= max_value:
                joint_display_j3.delete('1.0', 'end')
                self.default_joint3Position += 1
                return self.default_joint3Position
            else:
                messagebox.showinfo("Information", "YOU HAVE REACHED THE MAXIMUM LIMIT!!")






def comScan_data():
    try:
        serialObj = serial.Serial('COM6')
        com_data_display.delete('1.0', 'end')
        com_data_display.insert('1.0', serialObj)

    except serial.SerialException:
        com_data_display.delete('1.0', 'end')
        # com_data_display.insert('1.0', 'Serial NOT CONNECTED!')
        set_text_color(com_data_display, 'Serial NOT CONNECTED!', 'red')



def connect_to_com():
    selected_serial = com_combobox.get()
    try:
        serialObj = serial.Serial(selected_serial)
        time.sleep(3)
        com_connected_display.delete('1.0', 'end')
        # com_connected_display.insert('1.0', "CONNECTED")
        set_text_color(com_connected_display, 'CONNECTED', 'green')
    except serial.SerialException:
        # com_connected_display.insert('1.0', "Please select the CORRECT COM PORT")
        set_text_color(com_connected_display, "Please select the CORRECT COM PORT", 'red')


# decrement for pressing left button
def left_decrease(button_set, min, max):
    value = defaultPosition().decrement(button_set, min, max)
    if button_set == 0:
        try:
            base_joint_display.insert('1.0', value)
            base_joint_slider.set(value)
        except tkinter.TclError:
            pass
    elif button_set == 1:
        try:
            joint_display_j2.insert('1.0', value)
            joint_slider_j2.set(value)
        except tkinter.TclError:
            pass
    elif button_set == 2:
        try:
            joint_display_j3.insert('1.0', value)
            joint_slider_j3.set(value)
        except tkinter.TclError:
            pass

def right_increment(button_set, min, max):
    value = defaultPosition().increment(button_set, min, max)
    if button_set == 0:
        try:
            base_joint_display.insert('1.0', value)
            base_joint_slider.set(value)
        except tkinter.TclError:
            pass
    elif button_set == 1:
        try:
            joint_display_j2.insert('1.0', value)
            joint_slider_j2.set(value)
        except tkinter.TclError:
            pass
    elif button_set == 2:
        try:
            joint_display_j3.insert('1.0', value)
            joint_slider_j3.set(value)
        except tkinter.TclError:
            pass



def slider(event, slide_no):
    if slide_no == 0:
        slider_value = int(base_joint_slider.get())
        base_joint_display.delete('1.0', 'end')
        base_joint_display.insert('1.0', slider_value)
    elif slide_no == 1:
        slider_value = int(joint_slider_j2.get())
        joint_display_j2.delete('1.0', 'end')
        joint_display_j2.insert('1.0', slider_value)
    elif slide_no == 2:
        slider_value = int(joint_slider_j3.get())
        joint_display_j3.delete('1.0', 'end')
        joint_display_j3.insert('1.0', slider_value)

# custom text color function
def set_text_color(widget, text, color):
    # Create a tag with the specified color
    widget.tag_configure("color_tag", foreground=color)
    # Insert the text with the tag
    widget.insert('1.0', text, "color_tag")

def train():
    base = base_joint_display.get('1.0', "end-1c")
    rec_joint2 = joint_display_j2.get('1.0', "end-1c")
    rec_joint3 = joint_display_j3.get('1.0', "end-1c")
    base = base_joint_display.get('1.0', "end-1c")
    rec_movements.insert('1.0', f'Base Junction Axis : {base}\n')
    rec_movements.insert('1.0', f'Junction 2 Axis : {rec_joint2}\n')
    rec_movements.insert('1.0', f'Junction 3 Axis : {rec_joint3}\n')

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('Easy EXE')
    # create our main frame
    frame = tkinter.LabelFrame(window)
    frame.pack()
    # create com select frame
    com_frame = tkinter.LabelFrame(frame, text='COM select')
    com_frame.grid(row=0, column=0, columnspan=2, sticky='news', padx=10, pady=10)
    # just a btw
    gui_label = tkinter.Label(window, text="EASY EXE")
    gui_label.pack()
    # feed data to our com select plane
    com_scan = tkinter.Button(com_frame, text='Scan COM Data', command=comScan_data)
    com_scan.grid(row=0, column=0)
    com_data_display = tkinter.Text(com_frame, height=5, width=50)
    com_data_display.grid(row=0, column=1)
    com_label = tkinter.Label(com_frame, text='COM PORT')
    com_combobox = ttk.Combobox(com_frame, values=['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6'])
    com_connect = tkinter.Button(com_frame, text='Connect COM', command=connect_to_com)
    com_connected_display = tkinter.Text(com_frame, height=1, width=40)
    com_label.grid(row=1, column=0)
    com_combobox.grid(row=1, column=1)
    com_connect.grid(row=2, column=0)
    com_connected_display.grid(row=2, column=1)
    # auto padding
    for widget in com_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    # TRAIN FRAME ROW 1, COLUMN 0
    train_frame = tkinter.LabelFrame(frame, text='TRAIN')
    train_frame.grid(row=1, column=0, sticky='news', padx=10, pady=10)
    # gui under the train frame
    button_frame = tkinter.Frame(train_frame)
    button_frame.grid(row=0, column=0, padx=5, pady=5, sticky='news')
    # display frame
    display_frame = tkinter.Frame(train_frame)
    display_frame.grid(row=0, column=1, padx=20, pady=5)
    train_combos = tkinter.Label(button_frame, text='Select Train Positions')
    train_combobox = ttk.Combobox(button_frame, values=[1, 2, 3, 4, 5, 6])
    train_button = tkinter.Button(button_frame, text='TRAIN', command=train)  # records all the movements being made
    rec_movements = tkinter.Text(display_frame, height=10, width=50)  # displays all the recorded movements
    play_button = tkinter.Button(button_frame, text='Play')
    train_combos.grid(row=0, column=0)
    train_combobox.grid(row=1, column=0)
    train_button.grid(row=2, column=0)
    play_button.grid(row=3, column=0, sticky='news', pady=5)
    rec_movements.grid(row=0, column=0)

    for widget in button_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    # MOVEMENT FRAME ROW 1, COLUMN 1
    movement_frame = tkinter.LabelFrame(frame, text='MOVEMENT CONTROL')
    movement_frame.grid(row=1, column=1, sticky='news', padx=10, pady=10)
    # gui under control frame
    base_joint = tkinter.LabelFrame(movement_frame, text='Base Joint Axis')
    base_joint.grid(row=0, column=0)
    # under base joint axis
    left_button = tkinter.Button(base_joint, text='<-', command=lambda: left_decrease(0, base_default_min, base_default_max), default='active')
    right_button = tkinter.Button(base_joint, text='->', command=lambda: right_increment(0, base_default_min, base_default_max))
    base_joint_display = tkinter.Text(base_joint, height=0.5, width=10, )
    # create a custom style
    style = ttk.Style()
    style.configure("calm", troughcolor="light blue", slidercolor="blue")
    base_joint_slider = ttk.Scale(base_joint, from_=base_default_min, to=base_default_max, orient='horizontal',
                                  style='')  # add a command to generate values
    base_joint_slider.bind("<Button-1>", lambda event, arg=0: slider(event, arg))
    left_button.grid(row=0, column=0)
    base_joint_display.grid(row=0, column=1)
    right_button.grid(row=0, column=2)
    base_joint_slider.grid(row=0, column=3)
    # automate padding
    for widget in base_joint.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    # joint 2 link1
    joint2 = tkinter.LabelFrame(movement_frame, text='Joint 2 Link1')
    joint2.grid(row=1, column=0, sticky='news')
    # under base joint axis
    left_button_j2 = tkinter.Button(joint2, text='<-', command=lambda: left_decrease(1, joint2_default_min, joint2_default_max))
    right_button_j2 = tkinter.Button(joint2, text='->', command=lambda: right_increment(1, joint2_default_min, joint2_default_max))
    joint_display_j2 = tkinter.Text(joint2, height=0.5, width=10, )
    style = ttk.Style()
    style.configure("calm", troughcolor="light blue", slidercolor="blue")
    joint_slider_j2 = ttk.Scale(joint2, from_=joint2_default_min, to=joint2_default_max, orient='horizontal', style='')
    joint_slider_j2.bind("<Button-1>", lambda event, arg=1: slider(event, arg))
    # add a command to generate values
    left_button_j2.grid(row=0, column=0)
    joint_display_j2.grid(row=0, column=1)
    right_button_j2.grid(row=0, column=2)
    joint_slider_j2.grid(row=0, column=3)
    for widget in joint2.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    # joint 3 link1
    joint3 = tkinter.LabelFrame(movement_frame, text='Joint 3 Link1')
    joint3.grid(row=2, column=0, sticky='news')
    # under base joint axis
    left_button_j3 = tkinter.Button(joint3, text='<-', command=lambda: left_decrease(2, joint3_default_min, joint3_default_max))
    right_button_j3 = tkinter.Button(joint3, text='->', command=lambda: right_increment(2, joint3_default_min, joint3_default_max))
    joint_display_j3 = tkinter.Text(joint3, height=0.5, width=10, )
    style = ttk.Style()
    style.configure("calm", troughcolor="light blue", slidercolor="blue")
    joint_slider_j3 = ttk.Scale(joint3, from_=joint3_default_min, to=joint3_default_max, orient='horizontal', style='')
    joint_slider_j3.bind("<Button-1>", lambda event, arg=2: slider(event, arg))
    # add a command to generate values
    left_button_j3.grid(row=0, column=0)
    joint_display_j3.grid(row=0, column=1)
    right_button_j3.grid(row=0, column=2)
    joint_slider_j3.grid(row=0, column=3)
    for widget in joint3.winfo_children():
        widget.grid_configure(padx=5, pady=5)
    defaultDisplay()

    window.mainloop()