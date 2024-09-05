import RPi.GPIO as GPIO
import time
import keyboard

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Choose a GPIO pin (e.g., GPIO 18)
output_pin = 18

# Set up the pin as an output
GPIO.setup(output_pin, GPIO.OUT)

# Duration of the high signal in seconds
signal_duration = 0.1

def send_high_signal():
    GPIO.output(output_pin, GPIO.HIGH)
    time.sleep(signal_duration)
    GPIO.output(output_pin, GPIO.LOW)
    print("Sent a high signal")

try:
    print("Press 'w' to send a high signal. Press 'q' to quit.")
    while True:
        if keyboard.is_pressed('w'):
            send_high_signal()
            # Wait a bit to avoid multiple signals from one press
            time.sleep(0.2)
        elif keyboard.is_pressed('q'):
            print("Quitting...")
            break

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    # Clean up the GPIO settings
    GPIO.cleanup()