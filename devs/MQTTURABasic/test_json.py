import json 

c = open('conf.json') 
  
conf = json.load(c) 
  
print(conf["ssid"])  
  
 
c.close()