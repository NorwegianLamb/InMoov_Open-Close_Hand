import RPi.GPIO as GPIO
import time

#-----------------------------------------------------

GPIO.setmode(GPIO.BOARD)
pin=[7,11,12,13,15]
n_pin=int(len(pin))
pwm=[]
for i in range(len(pin)):
	GPIO.setup(pin[i], GPIO.OUT)
	pwm.append(GPIO.PWM(pin[i], 50))
	pwm[i].start(0)

scelta=int(input("2 to open, 12 to close, 7 to reset:"))

#------------------------------------------------------

for i in range(n_pin):
	pwm[i].ChangeDutyCycle(scelta)
	time.sleep(0.1)
time.sleep(2)

print("First cycle completed")

for i in range(n_pin):
	pwm[i].ChangeDutyCycle(scelta)
	time.sleep(0.1)
time.sleep(2)

print("Second cycle completed")

#------------------------------------------------------

for i in range(len(pin)):
	pwm[i].stop()
GPIO.cleanup()
