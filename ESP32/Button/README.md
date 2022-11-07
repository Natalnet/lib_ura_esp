# LED RGB SMD

Este código é para realizer um teste básico com um botão.

## Componentes

- NodeMCU ESP32
- Botão

<img src="https://cdn-learn.adafruit.com/assets/assets/000/035/367/original/microcontrollers_micropython_huzzah_button.png?1472798079" width="400">

Fonte da Imagem: https://learn.adafruit.com/assets/35367

## Ligações

A tabela abaixo ilustra o uso dos pinos do botão.

| Butão | ESP32   |
| ----- | ------- |
| 1     | GND     |
| 2     | GPIO 12 |

## Código Básico

Este código configura o pino 12 (GPIO12) como entrada e criar uma objeto com o nome _button_ para receber valores digitais desta entrada. No pino 12 foi conecatado um botão e configurado como PULL_UP para não precisar adicionar um resistor de proteção para o microcontrolador.

```python
import machine
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
cont = 0
while cont < 2000:
  if not button.value():
    print('Button pressed!')
  else:
    print('Not pressed!')
  cont = cont + 1
```

## Referências

- [Capa 3D para um botão](https://youtu.be/yc6e4zKoOgY)
- [Adafruit - Digital Inputs](https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs)
- [Entendendo os Resistores de Pull-Up e Pull-Down](https://blog.eletrogate.com/entendendo-os-resistores-de-pull-up-e-pull-down/)
