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
import spidev
import sys

# Temperature
TEMPPIN = 0

#
spi = spidev.SpiDev()
spi.open(0,0)

test = -10

# 7segLED address set
led_addr = [0x20, 0x21, 0x22, 0x23]
led = FaBo7Seg_TLC59208.TLC59208(led_addr)

def readadc(channel):
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

def arduino_map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

if __name__ == '__main__':
    try:
        while True:
            data = readadc(TEMPPIN)
            volt = arduino_map(data, 0, 1023, 0, 5000);
            temp = arduino_map(volt, 300, 1600, -30, 100);
            print "temp:", temp
            led.showNumberFullDigit(temp)

            test += 1
            if test > 10:
                test = -10

            time.sleep(0.5)

    except KeyboardInterrupt:
        spi.close()
        sys.exit(0)
