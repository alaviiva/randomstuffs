# Copypaste stuff to terminal
import time
keyboard.send_keys("<ctrl>+c")
#text = clipboard.get_selection()
#clipboard.fill_clipboard(text)
#window.activate("Firefox")
#if window.wait_for_focus(".*Firefox.*"):

window.activate("Terminal")
keyboard.send_keys("\"<ctrl>+<shift>+v")
time.sleep(0.2)
keyboard.send_keys("\" ")

#keyboard.send_keys("\""+text+"\" ")
