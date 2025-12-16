from pynput.keyboard import Controller, Key
import pyautogui


keyboard = Controller()

class KeyControl:
    def __init__(self):
        print()

    def type(self, text):
        pyautogui.write(text, interval=0.02)  # types text

    def press_enter(self):
        pyautogui.press('enter')  # presses Enter

    def copy(self):
        pyautogui.hotkey("command", "c")

    def paste_1(self):
        pyautogui.hotkey("command", "v")
        # V is pasted first time, macos issue

    def paste_2(self):
        pyautogui.keyDown("command")
        time.sleep(0.05)      # tiny delay is critical on macOS
        pyautogui.press("v")
        time.sleep(0.05)
        pyautogui.keyUp("command")


    def paste(self):
        with keyboard.pressed(Key.cmd):
            keyboard.press('v')
            keyboard.release('v')


# # usage
# time.sleep(3)  # time to focus the target window
# t = Typing("Hello, world!")
# t.type()
# t.press_enter()
