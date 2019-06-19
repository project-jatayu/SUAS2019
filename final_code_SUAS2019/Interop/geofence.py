import requests
import json
from auvsi_suas.client import client
from google.protobuf.json_format import MessageToJson, MessageToDict

#client = client.Client(url='http://10.10.130.66:8000', username='testuser', password='testpass')
#ping client = client.Client(url='http://192.168.43.124:8000', username='testuser', password='testpass')
#client = client.Client(url='http://10.10.130.66:8000', username='testuser', password='testpass')
#client = client.Client(url='http://127.0.0.1:8000', username='testuser', password='testpass')

#client = client.Client(url='http://127.0.0.1:8000', username='testuser', password='testpass')
client = client.Client(url='http://10.10.130.10:80', username='jatayu', password='2604741296')

mission = client.get_mission(3)
#DictObj = MessageToDict(mission)
#print(DictObj)
#print(DictObj["offAxisOdlcPos"])
#print(DictObj["flyZones"][0]["boundaryPoints"])

DictObj = MessageToDict(mission)
print(DictObj)
print(type(DictObj))
r = DictObj["flyZones"][0]["boundaryPoints"]
jsonObj = json.dumps(r)

with open('boundary.json', 'w') as outfile:  
    json.dump(jsonObj, outfile)