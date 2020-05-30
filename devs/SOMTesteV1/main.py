from som import SOM 
s = SOM() 

# teste do método distância euclidiana 
d = s.distancia([2,1,1],[4,2,3])
print(d,' = 3')

posM = s.melhorNeuronio([17, 13, 22]) 
print(posM) 
print(s.matrizNeuronios[posM[0]][posM[1]]) 

r = s.melhorReposta([17, 13, 22])
print('movimento: ',r) 