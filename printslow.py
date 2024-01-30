"""
Animation for text
"""
from time import sleep
from sys import stdout
from random import random

typing_speed = 500 #wpm
def slow_type(t):
  """
  Creates a typing animation effect.
  """
  for l in t:
      stdout.write(l)
      stdout.flush()
      sleep(random()*10.0/typing_speed)
  print('')