#Se declaran las librerias que se van a utilizar
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
import Adafruit_DHT
import urllib2

#Se declara el pin 4 como salida para el accionamiento del ventilador
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,0)

#Se guarda el URL de la pagina de THINGSPEAK para subir la informacion.
myAPI="Q64R95RS1CK4Z6MY"
baseURL='https://api.thingspeak.com/update?api_key=%s' % myAPI

#Se declara una variable auxiliar
aux=True

#Se declara un tiempo de espera entre subidas de informacion

delay=30 #en segundos


while True:
	
	humidity1, temperature1=Adafruit_DHT.read_retry(11,2)
	humidity2, temperature2=Adafruit_DHT.read_retry(11,3)
	print 'Al interior de la caja:\n Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature1, humidity1)
	print 'En el ambiente exterior:\n Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature2, humidity2)
	
	if temperature1>=25 and aux==True:
        	print "se prende el ventilador"
        	aux=False
        	GPIO.output(4,1)
        elif temperature1<25 and aux==False:
        	print "se apaga el ventilador"
        	aux=True
        	GPIO.output(4,0)

	try:
		f=urllib2.urlopen(baseURL + "&field1=%s&field2=%s&field3=%s&field4=%s" % (temperature1, temperature2, humidity1, humidity2))
		f.close()

		sleep(int(delay))

	except:
		print "failed uploading data"
