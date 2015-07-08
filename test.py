#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

if os.geteuid() != 0:
    print("not root")
    os.execvp("sudo", ["sudo"] + ["python"] + sys.argv)
    print("never reach here!")

import RPi.GPIO as GPIO
import time

print GPIO.VERSION
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led = 22

GPIO.setup(led, GPIO.OUT)
count = 0
speed = 1


def led_light():
    global count
    global speed
    GPIO.output(led, 1)
    time.sleep(speed)
    GPIO.output(led, 0)
    time.sleep(speed)
    speed -= 0.1
    count += 1
    return count


while count < 3:
    count = led_light()
    print(count)

print("end script")
