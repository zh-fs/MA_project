import requests
from common.random_number import *
url = "https://wx.vipmaillist.com/EditorTemp/formInfo/CRjdla"
data = {"userId":"2028",
         "activityInfoId":"2115",
         "fullName":f"{random_name()}",
         "mobile":f"86-{random_number()}",
         "isReplaceSubmit":'false',
         "reconfirm":'null',
         "isFullStaff":"",
         "fopenId":"",
         "customFieldList":[],
         "sysCustomFieldList":[],
         "activityType":"activity"}
head = {'Content-Type':'application/json'}
i = 0
# resp = requests.post(url=url, json=data )
# print(resp.text)
while True:
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)
    resp = requests.post(url=url, json=data )
    print(resp.text)
    resp = requests.post(url=url, json=data)
    print(resp.text)

