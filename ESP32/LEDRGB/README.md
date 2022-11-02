# LED RGB SMD

Este código é para realizer um teste básico para ligar uma "array" de LEDs RGB SMD.  

## Componentes 
* NodeMCU ESP32 
* LED RGB SMD WS2812b 

![LED RBG em Capa 3D](https://user-images.githubusercontent.com/19957124/199511407-44272aba-0163-4ffd-b9f7-639ee960c1fa.jpeg)

<img src="https://user-images.githubusercontent.com/19957124/199511407-44272aba-0163-4ffd-b9f7-639ee960c1fa.jpeg" width="300">


## Ligações 

Desenho detalhado do LED RGB WS2812b: 

![093017_0609_GettoKnowWS1](https://user-images.githubusercontent.com/19957124/199502971-574e33a6-bc33-44f6-bb2f-d268cd71f303.png)

 
A tabela abaixo ilustra o uso dos pinos do LED SMD WS2812b. 

| LED RGB | ESP32 |
| --------------- | --------------- | 
| VSS  | GND  | 
| VDD | 3.3v | 
| DIN  | GPIO 23 | 

## Código Básico 

Este código cria um vetor de pixel com base na classe "NeoPixel" e configura o pino 23 (GPIO23) como um canal para o ajuste das cores dos leds. O exemplo abaixo está configurado para apenas um LED, mas basta ajustar o valor da variável n para aumentar o número de leds.   

```python 
import machine, neopixel
import time

n = 1
p = 23
np = neopixel.NeoPixel(machine.Pin(p), n)

np[0] = (255, 0, 0)
np.write()
time.sleep(1)

np[0] = (0, 255, 0)
np.write()
time.sleep(1)

np[0] = (0, 0, 255)
np.write()
time.sleep(1)

np[0] = (255, 0, 0)
np.write()
```
 
## Referências 
* [Capa 3D para LED RGB SMD](https://youtu.be/36GOA4zXLVs)
* [Neopixel with Micropython](https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html) 
* [Tutorials para ESP32 - https://randomnerdtutorials.com/](https://randomnerdtutorials.com/) 
