import requests
import time
import json

server_token = ""

url = 'https://api.uber.com/v1/estimates/price?server_token='+server_token+'&start_latitude=17.4452462&start_longitude=78.3746176&end_latitude=17.4035689&end_longitude=78.4601055'

dataset = []
minutes = 0

starttime = time.time()
while minutes != 1440:
    response = requests.get(url)
    data = response.json()
    item = {}
    item['minutes'] = minutes
    item['prices'] = data['prices']
    print item
    dataset.append(item)
    time.sleep(300.0 - ((time.time() - starttime) % 300.0))
    minutes += 5
    if(minutes%60 == 0):
	f = open('dataset_'+str(minutes)+'.json', 'w')
	f.write(json.dumps(dataset, indent=4))
	f.close()


f = open('dataset.json', 'w')
f.write(json.dumps(dataset, indent=4))
f.close()

