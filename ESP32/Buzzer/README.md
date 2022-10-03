# Buzzer - atuador sonoro 

Este código é para realizer um teste básico em um buzzer. Para mais detalhes ver o vídeo neste [link](https://youtu.be/eNcm6n8meGM). 

## Componentes 
* NodeMCU ESP32 
* Buzzer, atuador, para gerar sons

## Ligações 

A tabela abaixo ilustra o uso dos jumpers para conectar o atuador à placa NodeMCU ESP32. 

| Buzzer | ESP32 |
| --------------- | --------------- | 
| GND | GND  | 
| Vcc | 3.3v | 
| I/O  | GPIO23 | 

## Código Básico 
Este código configura o pino GPIO23 como saida PWM para o Buzzer. Primeiro, Configura o pino 23 como saída PWM e zera o sinal de saída. Em seguida ajusta a frequência do pulso PWD para 1047, e intensidade do sinal sonoro para 256, ficando ativo por 1 segundo. Interrompe o sinal por 1 segundo. Inicializa a frequência com 69 e intensidade 8 e deixa tocar por 1 s. Zera novamente e libera a porta. Quando mais próximo de zero for o valor do 'duty', menos barulhento é o sinal. 

```python 
from machine import Pin
from machine import PWM
from time import sleep_ms

# Configura o pino 23 como saída PWM e zera o sinal de saída
buzzer = PWM(Pin(23, Pin.OUT))
buzzer.init(freq=0, duty=0)

# Ajusta a frequência
buzzer.freq(1047)

# Ajusta a intensidade do barulho
buzzer.duty(256)
sleep_ms(1000)

# Zera o barulho
buzzer.duty(0)
sleep_ms(1000)

# Inicializa o barulho com uma frequência
buzzer.init(freq=69, duty=8)
sleep_ms(1000)
buzzer.duty(0)

# Desativa o pwm e libera a porta
buzzer.deinit()
```
 
## Referências 
* [Vídeo com explicações básicas da montagem do Buzzer com ESP32](https://youtu.be/eNcm6n8meGM)  
* [Teste com ESP32 e MicroPython tocando um trecho da música do Mario](https://youtu.be/N2lBoXjElc0) 
* [Códigos para o Buzzer - TechToTinker.blogspot.com](https://techtotinker.blogspot.com/2021/06/038-micropython-technotes-buzzer.html)