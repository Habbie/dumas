#!/usr/bin/env python3

"""
led    switch
24     23
17     27
"""

from gpiozero import Button, LED
from signal import pause
import functools

# de eerste knop (knop 0) is de resetknop
# na de resetknop tonen/spelen we het pauzescherm
# bij opstarten doen we hetzelfde

# de andere knoppen zijn om talen te kiezen
# als een taal is gekozen en de video in die taal draait, wordt die niet onderbroken, *behalve* door de resetknop

# tijdens het pauzescherm branden (of pulseren?) alle LEDs
# tijdens afspelen van een taalvideo zijn de LEDs uit

# mode is een index in de verschillende arrays. 0 is de pauzestand. 1 en verder zijn talen.

mode = 0

button_ids = [ 23, 27 ]
led_ids    = [ 24, 17 ]

def playvid(v):
  print("starting vid", v)

def pushed(b):
  global mode
  print("user pushed", b)
  if b == mode:
    print("doing nothing")
    return

  if b == 0:
    print("resetting to pause screen")
    for led in leds[1:]:
      led.on()
    playvid(b)
    mode = 0
    return
  else:
    # visitor wants to play a video, is this allowed?
    if mode == 0:
      # it is allowed!
      print("playing video", b)

      # we turn all LEDs off while a video is playing
      # if you want the LEDs to show which video is playing, write something else for the two lines below
      for led in leds[1:]:
        led.off()
      playvid(b)
      mode = b
      return
    else:
      print("user tried to switch videos while one was playing, denying")
      return
   

    

def video1():
  leds[0].on()
  leds[1].off()
  print("we spelen nu video 1")

def video2():
  leds[1].on()
  leds[0].off()
  print("we spelen nu video 2")


buttons = [ Button(i) for i in button_ids ]
leds = [ LED(i) for i in led_ids ]

for i in range(len(buttons)):
	buttons[i].when_pressed = functools.partial(pushed, i)

print("ready")
pause()
