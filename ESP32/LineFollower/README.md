# Seguidor de linha

Este código é para realizer um teste básico para fazer o robô seguir linha. Para mais detalhes ver o vídeo [neste link.](https://www.youtube.com/watch?v=pcTP0I5jl6E) 

## Componentes 
* NodeMCU ESP32 
* 2 Sensores de Linha, TCRT5000, com ajuste de sensibilidade 
* 2 Motores DC TT 
* 1 Ponte H L9110 

## Ligações 
 
A tabela abaixo ilustra o uso dos jumpers para conectar o sensor de linha esquerdo ao NodeMCU ESP32. 

| Sensor de Linha Esquerdo | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v | 
| S  | D18 | 

A tabela abaixo ilustra as conexões do sensor de linha direito ao NodeMCU ESP32. 

| Sensor de Linha Direito | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v | 
| S  | D19 | 

A tabela abaixo ilustra as conexões entre os motores e o NodeMCU ESP32. 
O Motor esquerdo está ligado na entrada Motor A da ponte H e o Motor direito está ligado na entrada Motor B.  

| Ponte H L9110  | ESP32 |
| --------------- | --------------- | 
| B-1A | D5 |
| B-1B | D23 |
| G  | GND  | 
| VCC | Vin (5v) | 
| A-1A | D13 | 
| A-1B | D12 | 

Para mais informações sobre o uso da Ponte H L9110 [ver este link.]() 

## Código Básico 

### Sensores de linha 

Este código configura os pinos GPIO 18 (D18) e GPIO 19 (D19) como entradas para os sensores de linha da esquerda e da direita respectivamente. 

```python 
from machine import  Pin
# Pinos reservados para o sensor de linha 
pinEsq = 18 
pinDir = 19 
sensorLinhaEsq = machine.Pin(pinEsq, machine.Pin.IN,  machine.Pin.PULL_UP)
sensorLinhaDir = machine.Pin(pinDir, machine.Pin.IN, machine.Pin.PULL_UP)
```
Mais informações sobre o sensor de linha, [veja este link.](https://github.com/Natalnet/lib_ura_esp/blob/master/ESP32/LineSensor/README.md)


### Seguidor de linha 

De acordo com os testes realizados, o sensor vai responder verdadeiro (valor 1) quando estiver em cima da linha (preta), se tiver sobre uma região clara, detecta falso (valor 0). 

O código a seguir é um código muito simples de um algoritmo de seguir linha. A estratégia é a seguinte: 

Repetir até que a condição de parada aconteça:
1. Espera delta milisegundos 
2. Andar para frente caso o senosr de linha da esquerda (SLE) e o da direita (SLD) identifiquem a cor mais clara (região livre). 
3. Caso a situação 2 falhe, verifica se encontrou linha nos dois sensores e para. Logo a condição de parada é encontrar uma linha nos dois sensores. Neste caso o robô para seu movimento. 
4. Caso a situação 3 falhe, é por que foi testado a situação 2 e também falhou. Logo apenas um dos senores está detectando a linha preta. O teste realizado é verificar se o sensor de linha esquerdo detectou a linha e a ação é girar para esquerda. 
5. Significa que todas os testes anteriores falharam e para garantir, o teste de detecção de linha no sensor direito e realizado, caso verdadeiro a ação é girar para esquerda.  


```python 
parar =  False 
delta = 50 

while ( not parar ):
  time.sleep_ms(delta) 
  if ( not sensorLinhaDir.value() and not sensorLinhaEsq.value() ): 
    dr.frente()
  elif (  sensorLinhaDir.value() and  sensorLinhaEsq.value() ):
    dr.parar()
    parar = True
  elif ( sensorLinhaEsq.value() ):
    dr.esquerda()
  elif ( sensorLinhaDir.value() ):
    dr.direita() 
```

## Referências 


* [Documentação básica do sensor de linha](https://github.com/Natalnet/lib_ura_esp/blob/master/ESP32/LineSensor/README.md)
* [Vídeo com uma demonstração do sensor de linha](https://youtu.be/9hUtZqEb3bc)
* [Demonstração seguidor de linha do URA 6.0 ESP](https://www.youtube.com/watch?v=pcTP0I5jl6E) 
