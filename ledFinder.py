import board
import neopixel

LED_COUNT               = 100                   # Number of LED pixels.
LED_PIN                 = board.D18             # GPIO pin connected to the pixels (18 is PCM).
LED_BRIGHTNESS          = 0.05                  # Float from 0.0 (min) to 1.0 (max)
LED_ORDER               = neopixel.GRB          # Strip type and colour ordering

COLOR_VFR               = (255,0,0)             # Green
COLOR_CLEAR             = (0,0,0)               # Clear

pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, pixel_order = LED_ORDER, auto_write = False)

print("Enter the identifier of the airport of the lit LED.  If no airport is lit enter NULL")
print("When all LEDs have been accounted for press enter on an empty line to exit.")
# used to figure out which LED goes where
for i  in range(LED_COUNT):
        pixels[i] = COLOR_CLEAR

pixels.show()

airportList = []
for i in range(LED_COUNT):
        pixels[i] = COLOR_VFR
        if i >= 1:
                pixels[i-1] = COLOR_CLEAR
        pixels.show()
        apt = input("Airport " + str(i) + ":")
        if apt == "":
                for j in airportList:
                        print(j.upper())
                exit()
        airportList.append(apt)

        
