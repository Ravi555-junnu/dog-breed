import requests
import json


#endpoints
URL="http://127.0.0.1:8000/"

def get_data():
    data={
        'id': 1,
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

get_data()
