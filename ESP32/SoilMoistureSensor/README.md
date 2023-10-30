# LDR - Sensor de iluminação

Este código é para realizer um teste básico de leitura de um sensor de umidade do solo. Para mais detalhes ver o vídeo ???

## Componentes

- NodeMCU ESP32
- Sensor de Umidade do Solo

## Ligações

Circuito básico:

A tabela abaixo ilustra o uso dos jumpers para conectar o sensor à placa NodeMCU ESP32.

| Sensor de Umidade do Solo | ESP32 |
| ------------------------- | ----- |
| G                         | GND   |
| V+                        | 3.3v  |
| S                         | D35   |

## Código Básico

Este código configura o pino GPIO35 (D35) como entrada analógica (ADC) e realiza uma leitura.

```python
from machine import Pin, ADC

ldr = ADC(Pin(35))

ldr.atten(ADC.ATTN_11DB)

ldr_value = ldr.read()
print(ldr_value)
```

## Referências

- [Vídeo: Sensor de Luz, LDR, com Micropython e ESP32](https://youtu.be/Xb-_oG65H2I)
