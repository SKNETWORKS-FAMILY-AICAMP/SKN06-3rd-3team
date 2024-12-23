import requests
import json
import os

url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'
params ={
    'serviceKey' : 'RZS0KuZzvLxLF0KgPrHlRXzbAZ4vE/mYaHJAA/D5LIm/FhJkvqYazMJw9Yw5EeU6ZX22Ah1utXz3xU8uJ6A7MA==', 
    'pageNo' : '49', 
    'numOfRows' : '81', 
    'entpName' : '', 
    'itemName' : '', 
    'itemSeq' : '', 
    'efcyQesitm' : '', 
    'useMethodQesitm' : '', 
    'atpnWarnQesitm' : '', 
    'atpnQesitm' : '', 
    'intrcQesitm' : '', 
    'seQesitm' : '', 
    'depositMethodQesitm' : '', 
    'openDe' : '', 
    'updateDe' : '', 
    'type' : 'json'
}

response = requests.get(url, params=params)

if response.status_code == 200 :
    res = json.loads(response.content)
    os.makedirs("data", exist_ok=True)  # 폴더 생성
    with open('data/medicine.txt', 'a', encoding='utf-8') as fw :
        for item in res['body']['items'] :
            
            entpName = item['entpName'].replace('\n', '') if item['entpName'] is not None else ''
            efcyQesitm = item['efcyQesitm'].replace('\n', '') if item['efcyQesitm'] is not None else ''
            useMethodQesitm = item['useMethodQesitm'].replace('\n', '') if item['useMethodQesitm'] is not None else ''
            atpnQesitm = item['atpnQesitm'].replace('\n', '') if item['atpnQesitm'] is not None else ''
            depositMethodQesitm = item['depositMethodQesitm'].replace('\n', '') if item['depositMethodQesitm'] is not None else ''
            intrcQesitm = item['intrcQesitm'].replace('\n', '') if item['intrcQesitm'] is not None else ''
            seQesitm = item['seQesitm'].replace('\n', '') if item['seQesitm'] is not None else ''
                        
            fw.write(item['itemName']+' '+entpName+' '+efcyQesitm+' '+useMethodQesitm+' '+atpnQesitm+' '+depositMethodQesitm+'\n\n')

