import tkinter as tk
from tkinter import Radiobutton
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Function to turn on LEDs
def turn_on_led():
    led = selected_led.get()
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    if led == "Red":
        GPIO.output(17, GPIO.HIGH)
    elif led == "Green":
        GPIO.output(27, GPIO.HIGH)
    elif led == "Blue":
        GPIO.output(22, GPIO.HIGH)

# GUI setup
root = tk.Tk()
root.title("LED Control")

selected_led = tk.StringVar()
selected_led.set("Red")

radiobutton_red = Radiobutton(root, text="Red", variable=selected_led, value="Red")
radiobutton_red.pack(anchor=tk.W)

radiobutton_green = Radiobutton(root, text="Green", variable=selected_led, value="Green")
radiobutton_green.pack(anchor=tk.W)

radiobutton_blue = Radiobutton(root, text="Blue", variable=selected_led, value="Blue")
radiobutton_blue.pack(anchor=tk.W)

button = tk.Button(root, text="Turn On LED", command=turn_on_led)
button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()

# Clean up GPIO
GPIO.cleanup()
