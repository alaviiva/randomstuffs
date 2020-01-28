# Copypaste address of currently open tab to telegram
import time

#window.activate("Firefox")
#if window.wait_for_focus(".*Firefox.*", 0):
if window.get_active_class().endswith("Firefox"):
  keyboard.send_keys("<ctrl>+l")
  time.sleep(0.1)
  keyboard.send_keys("<ctrl>+c")

  window.activate("Telegram")
  keyboard.send_keys("<ctrl>+v")
  time.sleep(0.1)
  keyboard.send_keys(" ")
