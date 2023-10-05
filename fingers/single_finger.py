import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = int(input("Insert the pin: "))
GPIO.setup(pin, GPIO.OUT)

pwm=GPIO.PWM(pin, 50)
pwm.start(0)

pwm.ChangeDutyCycle(int(input("2 to close, 12 to open: ")))
time.sleep(1.5)

pwm.stop()
GPIO.cleanup()
