import os, sys, io
import M5
from M5 import *
import machine
import time

timehere = None

def update_time(timer):
    global timehere
    current_time = time.localtime()
    time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    timehere.setText(time_str)

def setup():
  global timehere
  M5.begin()
  clock_timer = machine.Timer(0)
  clock_timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=update_time)
  Widgets.fillScreen(0xdb8fef)
  timehere = Widgets.Label("timehere", 34, 89, 1.0, 0x06ff42, 0xdb8fef, Widgets.FONTS.DejaVu56)

def loop():
  M5.update()

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
