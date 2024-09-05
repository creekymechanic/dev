from gpiozero import LED
from signal import pause
import time

# Choose a GPIO pin (e.g., GPIO 18)
output_pin = 18

# Create an LED object (which we'll use to control our output)
led = LED(output_pin)

# Duration of the high signal in seconds
signal_duration = 0.1

def send_high_signal():
    led.on()
    time.sleep(signal_duration)
    led.off()
    print("Sent a high signal")

print("Press Enter to send a high signal. Press Ctrl+C to quit.")

try:
    while True:
        input("Press Enter to send signal...")
        send_high_signal()

except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    # The gpiozero library automatically cleans up on exit
    pass