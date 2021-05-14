import machine
import time

pin = machine.Pin(16, machine.Pin.OUT) #Definicao do pino como saida 
#Exemplo de ligar e desligar o led
pin.on()    #Desliga o led
pin.off()   #Liga o led
pin.value(0)
#Criará uma função para alternar o pino
#Essa funcao ira negar o valor que estiver no pino. Ex, se o pio tiver 0 (desligado) a funcao ira
#nega-lo, fazendo ele ficar com o valor de 1 ( ligado)
def toggle(p): 
    p.value(not p.value())  #Negacao do valor do pino
#Blink
while True:
    toggle(pin) #Chamada da funcao
    time.sleep_ms(500) #Tempo de espera