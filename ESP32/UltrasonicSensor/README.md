# Sensor de Linha 

Este código é para realizer um teste básico de leitura de um sensor utrassônico para medir distância. 

## Componentes 

* NodeMCU ESP32 
* Sensor ultrassônico HCSR04 

## Ligações 
![IMG_20210620_215243](https://user-images.githubusercontent.com/19957124/122694540-0d584680-d214-11eb-9c18-9b82e1f20f72.jpg)

A tabela abaixo ilustra o uso dos jumpers para conectar o sensor à placa NodeMCU ESP32. A versão utilizada neste teste é compatível com 3.3 volts. 

| Sensor de distância | ESP32 |
| --------------- | --------------- | 
| GND | GND  | 
| Trig  | D19 | 
| Echo  | D18 |
| Vcc | 3.3v | 
 

## Código Básico 

Este código cria um objeto da classe HCSR04 para ter acesso ao sensor. No construtor do objeto `HCSR04(trigger_pin=19, echo_pin=18)` são configurados os pinos GPIO 19 para o pino trigger e GPIO 18 para o pino echo do sensor.  O objeto `sensor` é criado com as configurações definidas no construtor. O código faz a leitura da distância em centímetros com o método `distance_cm()`, guarda na variável `disctance` e mostra no terminal. 

```python 
from hcsr04 import HCSR04
sensor = HCSR04(trigger_pin=19, echo_pin=18)
distance = sensor.distance_cm()
print('Distance:', distance, 'cm')
```

## Referências 
* [Vídeo com uma demonstração do sensor de distância](https://youtu.be/wgBYIkIfLdg)
