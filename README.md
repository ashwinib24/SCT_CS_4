# 🎹 SkillCraft Task 4 – Keylogger with GUI Output

## 📝 Description

A basic keylogger program that captures and logs keystrokes to a file.  
The tool also includes a GUI display window showing the captured keystrokes in real-time.

## 📂 Files Included

- `keylogger.py`: Main script for logging and GUI
- `log.txt`: File where keystrokes are saved

## ⚙️ Features

- Captures every key pressed on the keyboard
- Stores the data in `log.txt`
- Real-time GUI window to monitor keys
- Stops logging on a specific keypress (e.g., Esc)

Requirements
Install dependencies using:

bash
Copy
Edit
pip install pynput tk
Libraries used:

pynput

tkinter (built-in with Python)

## ▶️ How to Run

```bash
python keylogger.py

The GUI window will launch.

Keystrokes will be recorded and shown.

log.txt will update automatically.