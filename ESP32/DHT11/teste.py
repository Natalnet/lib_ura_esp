# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))
cont = 0
while cont < 10:
  cont = cont + 1
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()

    print('Temperatura: %3.1f C' %temp)

  except OSError as e:
    print('Falha ao ler o sensor.')
