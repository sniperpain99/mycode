
import tkinter as tk
import serial

# Placeholder for serial connection
arduino = None
blinking = False

def connect_arduino(port='COM3', baud_rate=9600):
    global arduino
    try:
        arduino = serial.Serial(port, baud_rate)
        print("Arduino connected successfully.")
        update_lamp("green")
    except Exception as e:
        print(f"Failed to connect to Arduino: {e}")
        update_lamp("red")

def send_command(command):
    if arduino:
        arduino.write(command.encode())
    else:
        print("Arduino not connected.")

def forward(event=None):
    print("Moving forward")
    send_command('F')
    start_blinking()

def backward(event=None):
    print("Moving backward")
    send_command('B')
    start_blinking()

def turn_left(event=None):
    print("Turning left")
    send_command('L')
    start_blinking()

def turn_right(event=None):
    print("Turning right")
    send_command('R')
    start_blinking()

def stop(event=None):
    print("Stopping")
    send_command('S')
    stop_blinking()

def quit_app():
    if arduino:
        arduino.close()
    root.destroy()

def update_lamp(color):
    canvas.itemconfig(lamp, fill=color)

def start_blinking():
    global blinking
    blinking = True
    blink()

def stop_blinking():
    global blinking
    blinking = False
    sending_label.config(text="")

def blink():
    if blinking:
        current_text = sending_label.cget("text")
        new_text = "" if current_text == "Sending!" else "Sending!"
        sending_label.config(text=new_text)
        root.after(200, blink)

# Create the main window
root = tk.Tk()
root.title("Terminator 2")

# Create label for status
status_label = tk.Label(root, text="Status")
status_label.grid(row=0, column=2, pady=5)

# Create canvas for lamp indicators
canvas = tk.Canvas(root, width=40, height=40)
canvas.grid(row=1, column=2, pady=5)

# Draw lamp indicator (initially red)
lamp = canvas.create_oval(10, 10, 30, 30, fill="red")

# Create buttons and arrange them using grid
btn_turn_left = tk.Button(root, text="Turn Left")
btn_turn_left.grid(row=2, column=0, padx=10, pady=10)
btn_turn_left.bind("<ButtonPress>", turn_left)
btn_turn_left.bind("<ButtonRelease>", stop)

btn_forward = tk.Button(root, text="Forward")
btn_forward.grid(row=2, column=2, padx=10, pady=10)
btn_forward.bind("<ButtonPress>", forward)
btn_forward.bind("<ButtonRelease>", stop)

btn_turn_right = tk.Button(root, text="Turn Right")
btn_turn_right.grid(row=2, column=4, padx=10, pady=10)
btn_turn_right.bind("<ButtonPress>", turn_right)
btn_turn_right.bind("<ButtonRelease>", stop)

btn_backward = tk.Button(root, text="Backward")
btn_backward.grid(row=3, column=2, padx=10, pady=10)
btn_backward.bind("<ButtonPress>", backward)
btn_backward.bind("<ButtonRelease>", stop)

btn_quit = tk.Button(root, text="Quit", command=quit_app)
btn_quit.grid(row=4, column=2, padx=10, pady=10)

# Label for "Sending!"
sending_label = tk.Label(root, text="")
sending_label.grid(row=5, column=2, pady=10)

# Connect to Arduino (Adjust the port and baud rate as needed)
connect_arduino(port='COM3', baud_rate=9600)

# Run the application
root.mainloop()

