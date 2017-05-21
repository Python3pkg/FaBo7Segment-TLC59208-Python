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
        for i in range(10):
            tlc59208.showNumber(i)
            time.sleep(0.5)

except KeyboardInterrupt:
    tlc59208.showNumber(10)
