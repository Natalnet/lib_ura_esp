# DS18B20 - Sensor de temperatura para água  

Este código é para realizer um teste básico de leitura de um sensor de temperatura para água, DS18B20. Para mais detalhes ver o vídeo  

## Componentes 
* NodeMCU ESP32 
* Sensor, DS18B20, de temperatura  
* 1 resistor de 4k7  


## Ligações 

Circuito básico: 


![ds18b20_montagem](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/06/ds18b20_esp32_single_normal.png)


A tabela abaixo ilustra o uso dos jumpers para conectar o sensor à placa NodeMCU ESP32. 

| Sensor DS18B20 | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v e ligado no resistor| 
| S  | D4 e ligado na outra extremidade do resistor  | 

## Código Básico 

Este código configura o pino GPIO04 (D4) como entrada serial endereçável (OneWire), apresenta o dispositivo através de seu endereço e realiza uma leitura. É possível ter mais de um sensor conenctado no mesmo pino (D4). 

```python 
import machine, onewire, ds18x20

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

ds_sensor.convert_temp()
for rom in roms:
    print(rom)
    print(ds_sensor.read_temp(rom))
```
 
## Referências 
* [Sensor DS18B20 Random Nerd Tutorial](https://randomnerdtutorials.com/micropython-ds18b20-esp32-esp8266/)
* https://RandomNerdTutorials.com 
* [Vídeo testando o sensor de temperatura de água, DS18B20, com Micropython e ESP32](https://youtu.be/B-SaZFqwZ-8) 
