#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,0)

aux=True
while True:

	humidity, temperature=Adafruit_DHT.read_retry(11,2)
	print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
	
	if temperature>=25 and aux==True:
		print "se prendieron los ventiladores"
		aux=False
		GPIO.output(3,1)
	elif temperature<25:
		print "se apagaron los ventiladores"
		aux=True
		GPIO.output(3,0)
