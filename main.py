from turtle import title
from pynput.keyboard import Key, Listener
import time
from plyer import notification

keys = []

def on_press(key):
    global keys
    letter = "{0}".format(key)
    if letter[1].isalpha():
        # check if "q"
        if letter[1].capitalize() == 'Q':
            keys.append("Q")
        # break here to avoid errors
        elif keys == []:
            return
        # check if "qu"
        elif letter[1].capitalize() == 'U' and keys[-1] == "Q":
            keys.append("U")
        # check if "quo" ; we may be in trouble here
        elif letter[1].capitalize() == 'O' and keys[-1] == "U":
            keys.append("O")
        # this is serious, please be carefull omg he's doing it
        elif letter[1].capitalize() == 'I' and keys[-1] == "O":
            print("MAYDAY MAYDAY WE MAY GET FEURED THIS IS NOT AN EXERCISE")
            pop_up()
        # reset, we don't want our memory to blow up
        else :
            keys = []
            return
    
def on_release(key):
    if key == Key.esc:
        return False

# pop a windows notification 
def pop_up():  
    notification.notify(
        title = "ALERTE",
        message = "Vous êtes sur le point de vous faire FEURER",
        timeout = 10
        )
    

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()