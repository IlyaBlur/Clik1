import keyboard
import mouse
import time
from plyer import notification


def show_notification(title, message):
    notification.notify(title=title,
                        message=message,
                        app_icon="icon.ico",
                        timeout=1)


IsClicking = False


def start_Clicking():
    global IsClicking
    IsClicking = not IsClicking
    if IsClicking:
        show_notification("Кликер", "Кликер включен")
    else:
        show_notification("Кликер", "Кликер выключен")


keyboard.add_hotkey('Alt + X', start_Clicking)

while True:
    if IsClicking:
        mouse.click(button='left')
        time.sleep(0.01)
