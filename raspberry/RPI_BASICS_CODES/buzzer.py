import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)
print("buzzer on")



# import RPi.GPIO as GPIO
# from time import sleep
# #Disable warnings (optional)
# GPIO.setwarnings(False)
# #Select GPIO mode
# GPIO.setmode(GPIO.BCM)
# #Set buzzer - pin 23 as output
# buzzer=23
# GPIO.setup(buzzer,GPIO.OUT)
# #Run forever loop
# while True:
#  GPIO.output(buzzer,GPIO.HIGH)
#  print ("Beep")
#  sleep(0.5) # Delay in seconds
#  GPIO.output(buzzer,GPIO.LOW)
#  print ("No Beep")
#  sleep(0.5)