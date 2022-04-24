# DS18B20 - Sensor de temperatura para água  

Este código é para realizer um teste básico de leitura de um sensor de temperatura ambiente, DHT11. Para mais detalhes ver o vídeo neste [link](https://youtu.be/XGheCgyzBLo). 

## Componentes 
* NodeMCU ESP32 
* Sensor, DHT11, de temperatura  

## Ligações 
Circuito básico: 

A tabela abaixo ilustra o uso dos jumpers para conectar o sensor à placa NodeMCU ESP32. 

| Sensor DS18B20 | ESP32 |
| --------------- | --------------- | 
| -  | GND  | 
|  + | 3.3v | 
| S  | D14 | 

## Código Básico 
Este código configura o pino GPIO14 como entrada do sinal lido do sensor dht11. 

```python 
from machine import Pin
import dht

sensor = dht.DHT11(Pin(14))

sensor.measure()
temp = sensor.temperature()
print('Temperatura: %3.1f C' %temp)


```
 
## Referências 
* [MicroPython: ESP32/ESP8266 with DHT11/DHT22 Temperature and Humidity Sensor](https://randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor/)
* https://RandomNerdTutorials.com 
* [Vídeo testando o sensor de temperatura ambiente com Micropython e ESP32](https://youtu.be/XGheCgyzBLo) 
