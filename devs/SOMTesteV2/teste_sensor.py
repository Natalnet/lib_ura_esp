contI = 2
for a in angles:
    sf.setAngle(a)
    time.sleep_ms(500)
    d = sensorD.distance_cm() 
    if d > 70: 
        d = 70
    amostra[contI] = d 
    time.sleep_ms(10)
    contI -= 1 

distance = sensorD.distance_cm()
print('Amostra:', amostra)

acao = som.melhorReposta(amostra)
print(acao) 
sf.setAngle(10)