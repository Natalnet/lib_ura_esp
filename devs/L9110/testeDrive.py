from L9110URA import L9110URA 
import time 

dr = L9110URA(13,12,5,23) 

# Re 
dr.configura(1,1000,1,1000)

time.sleep(1)
dr.frente()

time.sleep(1)
dr.re() 

time.sleep(1)
dr.parar() 

time.sleep(1)
dr.esquerda()  

time.sleep(1)
dr.direita()  

for i in range(10):
    dr.frente(1000 - i*100)
    time.sleep(1) 
dr.parar()

dr.passoDireita()
dr.passoEsquerda()
dr.passoFrente()
dr.passoRe() 