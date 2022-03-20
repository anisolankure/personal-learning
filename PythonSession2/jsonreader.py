from json import load

f = open('iot.json')

data = load(f)

for i in data['iot_devices']:
    print(i)
 
# Closing file
f.close()