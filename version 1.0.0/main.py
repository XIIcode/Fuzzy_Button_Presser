from pynput.keyboard import Key,Listener,Controller

def onPress(key):
    print("Pressed Key : ",key," : ",end='')
    if key == Key.esc:
        try:
            Listener._stop_platform()
        except Exception as e:
            print("\nEXITED")
            exit()

def onRelease(key):
    print("Released Key : ",key)


print("Welcome!! to fuzzy button presser to test your keyboard?\n")
print("press any key to test and escape key to exit\n")

#Setup a Keyboard listener to listen on Keyboard events 
with Listener(on_press=onPress,on_release=onRelease) as listener:
    listener.join()
    





