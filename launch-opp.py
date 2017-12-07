from neopixel import *
from PIL import Image
import urllib2
import StringIO
import time


LED_COUNT = 32      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 15     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

screenwidth = 8
screenheight = 4

def batu(strip):
    pngid = "{0:0=6d}".format(int(urllib2.urlopen('https://openpixel.batu.one/id.txt').read()))
    file = urllib2.urlopen(
        'https://openpixel.batu.one/img/' + pngid + '.png').read()
    image = Image.open(StringIO.StringIO(file)).convert('RGB')
    pixeldata = list(image.getdata())
    for y in xrange(screenheight):
        for x in xrange(screenwidth):
            currentpx = (screenwidth * screenheight) - (x + (y * screenwidth)) - 1
            strip.setPixelColor(x + (y * screenwidth), Color(pixeldata[currentpx][0], pixeldata[currentpx][1], pixeldata[currentpx][2]))
    strip.show()
    print(time.ctime() + ' - ' + pngid + '.png')
    time.sleep(60)


if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                              LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    while True:
        batu(strip)
