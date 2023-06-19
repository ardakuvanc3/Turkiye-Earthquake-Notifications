import requests
import json
import time

url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"

payload = {}
headers = {}

response = requests.request("GET", url)

result = json.loads(response.text)

while True:
    count = 0
    print("{:<24} {:<39}  {:<12} {:<12}".format("Tarih","Bölge","Büyüklük","Derinlik"))

    for i in result["result"]:
        if(count>50):
            break
        if(i["mag"]>3):
            print("{:<24} {:<39}  {:<12} {:<12}".format(i["date"],i["title"],i["mag"],i["depth"]))
            count +=1


    time.sleep(15)
                
