from auvsi_suas.client import client
from auvsi_suas.proto import interop_api_pb2
import urllib
import json
import time
import datetime
import csv
from google.protobuf.json_format import MessageToJson, MessageToDict

client = client.Client(url='http://10.10.130.10:80', username='jatayu', password='2604741296')
#client = client.Client(url='http://127.0.0.1:8000', username='testusr', password='testpass')
#client = client.Client(url='http://10.10.130.66:8000', username='testuser', password='testpass')

mission = client.get_mission(3)
#DictObj = MessageToDict(mission)
#print(DictObj)
#print(DictObj["offAxisOdlcPos"])
#print(DictObj["flyZones"][0]["boundaryPoints"])

#print (mission)
#print(type(mission))

try: 
    x = urllib.request.urlopen('http://10.10.130.104:56781/mavlink/') 
    #print(x.read())
  
# Catching the exception generated     
except Exception as e : 
    print(str(e))

from urllib.request import urlopen
#print(type(mav_json))
#print(mav_json["GPS_RAW_INT"]["msg"]["lat"]/1e7)
#print(mav_json["GPS_RAW_INT"]["msg"]["lon"]/1e7)
#print(mav_json["GPS_RAW_INT"]["msg"]["alt"]/1e3)
#print(mav_json["VFR_HUD"]["msg"]["heading"])
while(True):
    time.sleep(0.8)
    mav_json = json.load(urlopen("http://10.10.130.104:56781/mavlink/"))
    print("sent")
    #print(mav_json["GPS_RAW_INT"])
    telemetry= interop_api_pb2.Telemetry()
    telemetry.latitude = mav_json["GPS_RAW_INT"]["msg"]["lat"]/1e7
    telemetry.longitude = mav_json["GPS_RAW_INT"]["msg"]["lon"]/1e7
    telemetry.altitude = (mav_json["VFR_HUD"]["msg"]["alt"])*3.281
    telemetry.heading = mav_json["VFR_HUD"]["msg"]["heading"]
    client.post_telemetry(telemetry)
