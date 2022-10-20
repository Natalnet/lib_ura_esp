# LED RGB SMD

Este código é para realizer um teste básico para ligar uma "array" de LEDs RGB SMD.  

## Componentes 
* NodeMCU ESP32 
* LED RGB SMD WS2812b 

## Ligações 

Circuito básico: ???

 
A tabela abaixo ilustra o uso dos pinos do LED SMD WS2812b. 

| Sensor de LDR | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v | 
| S  | GPIO5 | 

## Código Básico 

Este código cria um vetor de pixel com base na classe "NeoPixel" e configura o pino 5 (GPIO5) como um canal para o ajuste das cores dos leds. O exemplo abaixo está configurado para apenas um LED, mas basta ajustar o valor da variável n para aumentar o número de leds.   

```python 
import machine, neopixel
n = 1
p = 5
np = neopixel.NeoPixel(machine.Pin(p), n)
np[0] = (0, 0, 255)
np.write()
```
 
## Referências 
* [Capa 3D para LED RGB SMD](https://youtu.be/36GOA4zXLVs)
