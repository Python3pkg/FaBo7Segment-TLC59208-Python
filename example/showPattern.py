# coding: utf-8
## @package FaBo7seg_TLC59208
#  This is a library for the FaBo 7seg I2C Brick.
#
#  http://fabo.io/211.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBo7Seg_TLC59208
import time

tlc59208 = FaBo7Seg_TLC59208.TLC59208()

try:
    while True:
        tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PIN_A | FaBo7Seg_TLC59208.LED_PIN_G | FaBo7Seg_TLC59208.LED_PIN_D);
        time.sleep(1)
        for i in xrange(10):
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM4)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM2)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM1)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM0)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM6)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM4)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM2)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM1)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM0)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM6)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
            time.sleep(0.05)

            tlc59208.showNumber(i)
            time.sleep(1)
            tlc59208.showDot()
            time.sleep(1)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
            time.sleep(1)
except KeyboardInterrupt:
    tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
