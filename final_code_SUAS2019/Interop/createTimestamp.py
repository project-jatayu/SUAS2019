from auvsi_suas.client import client
from auvsi_suas.proto import interop_api_pb2
import urllib
import json
import time
import datetime
import csv

try: 
    x = urllib.request.urlopen('http://10.10.130.72:56781/mavlink/') 
#    #print(x.read())
  
#
#  Catching the exception generated     
except Exception as e : 
    print(str(e))#

from urllib.request import urlopen

row = ["time", "lat", "lon", "heading"]
with open('time.csv', "w") as fp:
        writer = csv.writer(fp)
        writer.writerow(row)
while(True):
    time.sleep(1)
    mav_json = json.load(urlopen("http://10.10.130.72:56781/mavlink/"))
    print("sent")
    row = [datetime.datetime.now(),mav_json["GPS_RAW_INT"]["msg"]["lat"]/1e7,mav_json["GPS_RAW_INT"]["msg"]["lon"]/1e7, mav_json["VFR_HUD"]["msg"]["heading"]]
    #row = [datetime.datetime.now(),80,-76, 90]
    with open('time.csv', "a") as fp:
        writer = csv.writer(fp)
        writer.writerow(row)
        print("done")
    fp.close()
    #client.post_telemetry(telemetry)
    #json data for odlc