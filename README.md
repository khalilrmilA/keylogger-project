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
- Python 3.7+
- `pip` for installing dependencies.
- GMX mail account credentials for email notifications.
- Docker (for cross-compiling the application to Windows).

### **Installation**

#### **Step 1: Clone the Repository**
```bash
git clone <repository-url>
cd keylogger-project
