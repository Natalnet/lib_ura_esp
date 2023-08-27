# LED Simples

Este código é para realizar um teste básico com um LED.

## Componentes

- NodeMCU ESP32
- LED com resistor 
 
<img alt="IMG_20230825_180630" src="https://github.com/Natalnet/lib_ura_esp/assets/19957124/d369f28c-54b5-47ad-8325-417013535009" width="400"> 

## Ligações

<img alt="Circuit-Diagram-for-ESP32-LED" src="https://github.com/Natalnet/lib_ura_esp/assets/19957124/53ac9923-e7f3-41c4-a057-92e362cdd2b5"  width="400">

Fonte da Imagem: https://learn.adafruit.com/assets/35367

A tabela abaixo ilustra o uso dos pinos do botão.

| LED | ESP32   |
| ----- | ------- |
|   -   | GND     |
|   +   | GPIO 02 |

## Código Básico

Este código configura o pino 2 (GPIO 02) como saída e criar uma objeto com o nome _led_ para enviar valores digitais para porta 02. 

```python
import machine
led = machine.Pin(2, machine.Pin.OUT)
# Comando para liga o LED 
led.on()
# Comando para desliga o LED 
led.off() 
```

Imagem com o LED ligado: 

<img alt="IMG_20230825_180644" src="https://github.com/Natalnet/lib_ura_esp/assets/19957124/8e125a9c-9981-41b0-af8d-7b157244d093" width="400">


## Referências


- [“Hello World!” em MicroPython](https://www.youtube.com/watch?v=ylPkBzaZTZY) 

