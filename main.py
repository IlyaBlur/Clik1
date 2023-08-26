import keyboard
import mouse
import time

IsClicking = False


def start_Clicking():
    global IsClicking
    IsClicking = not IsClicking


keyboard.add_hotkey('Alt + X', start_Clicking)

while True:
    if IsClicking:
        mouse.click(button='left')
        time.sleep(0.01)
