import tkinter as tk
import serial

# Placeholder for serial connection
arduino = None

def connect_arduino(port='COM3', baud_rate=9600):
    global arduino
    try:
        arduino = serial.Serial(port, baud_rate)
        print("Arduino connected successfully.")
    except Exception as e:
        print(f"Failed to connect to Arduino: {e}")

def send_command(command):
    if arduino:
        arduino.write(command.encode())
    else:
        print("Arduino not connected.")

def forward():
    print("Moving forward")
    send_command('F')

def backward():
    print("Moving backward")
    send_command('B')

def face_left():
    print("Facing left")
    send_command('L')

def face_right():
    print("Facing right")
    send_command('R')

def quit_app():
    if arduino:
        arduino.close()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Arduino Control GUI")

# Create buttons
btn_forward = tk.Button(root, text="Forward", command=forward)
btn_forward.pack(pady=10)

btn_backward = tk.Button(root, text="Backward", command=backward)
btn_backward.pack(pady=10)

btn_face_left = tk.Button(root, text="Face Left", command=face_left)
btn_face_left.pack(pady=10)

btn_face_right = tk.Button(root, text="Face Right", command=face_right)
btn_face_right.pack(pady=10)

btn_quit = tk.Button(root, text="Quit", command=quit_app)
btn_quit.pack(pady=10)

# Connect to Arduino (Adjust the port and baud rate as needed)
connect_arduino(port='COM3', baud_rate=9600)

# Run the application
root.mainloop()

