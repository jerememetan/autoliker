from pynput.keyboard import Key, Controller

import time
keyboard = Controller()
time.sleep (3)
def like(): #like function
    keyboard.press('j')
    keyboard.release('j')

    keyboard.press ('l')
    keyboard.release('l')

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    print("Liked!")
    
count = int(input("Like how many posts? "))

while (count>0):
    like()
    
    count = count - 1

    time.sleep(3)


