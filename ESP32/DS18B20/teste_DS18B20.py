#Fonte: https://randomnerdtutorials.com/micropython-ds18b20-esp32-esp8266/ 
## Complete project details at https://RandomNerdTutorials.com 

import machine, onewire, ds18x20, time

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

for i in range(2):
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  print(i)
  for rom in roms:
    print(rom)
    print(ds_sensor.read_temp(rom))
  time.sleep(5)      


