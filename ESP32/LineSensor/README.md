# Sensor de Linha 

Este código é para realizer um teste básico de leitura de um sensor de linha. Para mais detalhes ver o vídeo https://youtu.be/9hUtZqEb3bc 

## Componentes 
* NodeMCU ESP32 
* Sensor Linha TCRT5000 com ajuste de sensibilidade 

## Ligações 
![sensor_de_lina_esp32](https://user-images.githubusercontent.com/19957124/117882360-a3e23100-b280-11eb-8494-7a96f8354e2c.jpg)

A tabela abaixo ilustra o uso dos jumpers para conectar o sensor à placa NodeMCU ESP32. 

| Sensor de Linha | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v | 
| S  | D4 | 

## Código Básico 

Este código configura o pino GPIO 04 (D4) como entrada, ativa o resistor de _pull up_ e realiza uma leitura.  

```python 
import machine
pinNum = 4 #D4 
sensor = machine.Pin(pinNum, machine.Pin.IN,  machine.Pin.PULL_UP)

print( sensor.value() )
```
Mais informações sobre resistor de _pull up_ ou _pull down_, [veja este link](https://www.filipeflop.com/blog/entendendo-o-pull-up-e-pull-down-no-arduino/)

## Referências 
* [Entendendo o pull-up e pull-down no Arduino](https://www.filipeflop.com/blog/entendendo-o-pull-up-e-pull-down-no-arduino/)
* [Vídeo com uma demonstração do sensor de linha](https://youtu.be/9hUtZqEb3bc)
