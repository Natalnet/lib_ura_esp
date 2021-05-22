# Ponte H

Este código é para realizer testes básicos para a movimentação dos motores e o deslocamento do robô. Para mais detalhes ver o vídeo  ....

## Componentes 
* NodeMCU ESP32 
* 2 Motores DC TT 
* 1 Ponte H L9110 

Foto da Ponte H L9110:
![IMG_20210522_103527](https://user-images.githubusercontent.com/19957124/119228746-c844d580-baea-11eb-9ab5-8cec7d7fecf7.jpg)

Foto dos Motores DC TT: 
![IMG_20210522_103644](https://user-images.githubusercontent.com/19957124/119228753-d09d1080-baea-11eb-8d9c-b4694f747d84.jpg)

## Ligações 

Fotos das ligações: 
![IMG_20210522_103840](https://user-images.githubusercontent.com/19957124/119228758-d7c41e80-baea-11eb-9f44-955a3929f09f.jpg)

A tabela abaixo ilustra as conexões, por jumpers, entre os motores e o NodeMCU ESP32. 
O Motor esquerdo está ligado na entrada Motor A da ponte H e o Motor direito está ligado na entrada Motor B.  

| Ponte H L9110  | ESP32 |
| --------------- | --------------- | 
| B-1A | D5 |
| B-1B | D23 |
| G  | GND  | 
| VCC | Vin (5v) | 
| A-1A | D13 | 
| A-1B | D12 | 


## Código Básico 

### Motor Direito 

Este código configura o pino 13 para contrar a velocidade através de um sinal [PWM](https://www.embarcados.com.br/pwm-do-arduino/) e pino 12 como saída digital para controlar a direção do giro do motor. 

```python 
from machine import Pin,PWM

pinDVelocidade = 13
pinDDirecao = 12 

pwmD =  PWM(Pin(pinDVelocidade), freq=1000 ,duty = 0) 
direcaoD = Pin( pinDDirecao, Pin.OUT )
```

O ajuste da frequência no pino PWM pode ser realizado com o método _duty_ e a direção com os métodos _on_ e _off_. Para ajustar o motor direito para girar no sentido horário, considerando a montagem realizada na foto acima, basta usar os seguintes comandos: 
```python 
pwmD.duty(0)
direcaoD.on()
```
Nesta configuração valores mais próximo do zero são para a velocidade máxima. 

Para ajustar a movimentação no sentido horário: 
```python 
pwmD.duty(1000)
direcaoD.off()
```
Na movimentação no sentido horário valores mais elevados são para as maiores velocidades. Por exemplo `pwmD.duty(1000)`  é mais rápido que `pwmD.duty(700)`. 


### Motor Esquerdo 

Este código configura o pino 5 para controlar a velocidade através de um sinal [PWM](https://www.embarcados.com.br/pwm-do-arduino/) e pino 23 como saída digital para controlar a direção do giro do motor. 

```python 
pinEVelocidade = 5
pinEDirecao = 23 

pwmE =  PWM(Pin(pinEVelocidade), freq=1000 ,duty = 0) 
direcaoE = Pin( pinEDirecao, Pin.OUT )
```

Ajusta a velocidade no sentido horário 
```python 
pwmE.duty(0)
direcaoE.on()
```

No motor esquero girando no sentido horário, para diminuir a veolocidade de rotação basta aumentar o valor do _duty_  do PWM. No exemplo abaixo a volocidade de giro do eixo do motor diminui em relação ao valor _duty_ 0. 
```python 
pwmE.duty(200)
```

Ajusta a velocidade no sentido anti-horário:  
 ```python 
pwmE.duty(1000)
direcaoE.off()
```


## Referências 


* [Documentação básica do sensor de linha](https://github.com/Natalnet/lib_ura_esp/blob/master/ESP32/LineSensor/README.md)
* [Vídeo com uma demonstração do sensor de linha](https://youtu.be/9hUtZqEb3bc)
* [Usando as saídas PWM do Arduino](https://www.embarcados.com.br/pwm-do-arduino/)
