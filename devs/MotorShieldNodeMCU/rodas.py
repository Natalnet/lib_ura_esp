from machine import Pin,PWM
class Rodas:
  def __init__ (self):
    ## Frequencia de trabalho do motor
    # O valor maximo e 1024 
    self.freqA = 900
    self.freqB = 900 
    ## Os pinos para o Shield ESP s茫o fixos 
    # Para o motor A, esquerdo, os pinos sao:
    # 5 para velocidade e 0 para dire莽茫o 
    self.PwmA = PWM(Pin(5), freq=1000 ,duty = 0)
    self.DirA = Pin(0, Pin.OUT)   
    # Para o motor A, esquerdo, os pinos sao:
    # 5 para velocidade e 0 para dire鑾絘o
    self.PwmB = PWM(Pin(4), freq=1000 ,duty = 0)
    self.DirB = Pin(2, Pin.OUT)
    # Os pinos a seguir foram ocupados 
    # para controlar a ponte H 
    # D1 = GPIO 5
    # D2 = GPIO 4
    # D3 = GPIO 0
    # D4 = GPIO 2
     
    
  def frente(self):
    print("frente") 
    self.PwmA.duty(900)
    self.PwmB.duty(900) 
    self.DirA.off() 
    self.DirB.off() 
    
  def re(self):
    print("re") 
    self.PwmA.duty(900)
    self.PwmB.duty(900) 
    self.DirA.on() 
    self.DirB.on() 
 
  def esquerda(self):
    print("esquerda") 
    self.PwmA.duty(900)
    self.PwmB.duty(900) 
    self.DirA.on() 
    self.DirB.off() 
    
  def direita(self):
    print("direita") 
    self.PwmA.duty(900)
    self.PwmB.duty(900) 
    self.DirA.off() 
    self.DirB.on()  
    
  def parar(self):
    print("parar") 
    self.PwmA.duty(0)
    self.PwmB.duty(0) 
    self.DirA.off() 
    self.DirB.off()  
