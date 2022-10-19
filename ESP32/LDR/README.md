# LDR - Sensor de iluminação 

Este código é para realizer um teste básico de leitura de um sensor de LDR. Para mais detalhes ver o vídeo  https://youtu.be/Xb-_oG65H2I

## Componentes 
* NodeMCU ESP32 
* Sensor LDR 
* 1 resistor de 10k 


## Ligações 

Circuito básico: 


![ldr_montagem](https://user-images.githubusercontent.com/19957124/144618767-7b6ceaba-a161-4883-bb33-e345597811f6.png)


A tabela abaixo ilustra o uso dos jumpers para conectar o sensor à placa NodeMCU ESP32. 

| Sensor de LDR | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v | 
| S  | D33 | 

## Código Básico 

Este código configura o pino GPIO33 (D33) como entrada analógica (ADC) e realiza uma leitura.  

```python 
from machine import Pin, ADC

ldr = ADC(Pin(33))

ldr.atten(ADC.ATTN_11DB)      

ldr_value = ldr.read()
print(ldr_value)
```
 
## Referências 
* [Vídeo: Sensor de Luz, LDR, com Micropython e ESP32](https://youtu.be/Xb-_oG65H2I)
* [Código com LDR](https://github.com/Natalnet/lib_ura_esp/edit/master/ESP32/LDR/)
