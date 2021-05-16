import requests 
import json
import time
from datetime import datetime
from datetime import date
import math

account_list = []
er = 0

def get_average_transaction(address="0x0000000000000000000000000000000000001004"):
    a = "https://api.bscscan.com/api?module=account&action=txlist&address="
    b = "&startblock=1&endblock=99999999&page=1&offset="
    c = "&sort=desc&apikey="
    record_number = "30"
    api_token = "EHK917H6T8GF36B3H62T5MSWDMS4YT6HUA"
    rq = a + address + b + record_number + c + api_token
    global er
    try:
        response = requests.get(rq)
    except requests.ConnectionError: 
        er = 1
        return 0
    if response.status_code != 200:
        er = 1
        return 0
    raw = response.json()
    i = 0
    total = 0
    for i in range(int(len(raw['result']))):
        if i>int(record_number) or not(str(raw['result'][i]['value']).isnumeric()) :
            break
        total+=int(raw['result'][i]['value'])
    if i==0:
        return 0
    if total==0:
        return 0
    return 10*math.log(total/i,10)

def get_time(address="0x0000000000000000000000000000000000001004"):
    a = "https://api.bscscan.com/api?module=account&action=txlist&address="
    b = "&startblock=1&endblock=99999999&page=1&offset="
    c = "&sort=asc&apikey="
    record_number = "1"
    api_token = "EHK917H6T8GF36B3H62T5MSWDMS4YT6HUA"
    rq = a + address + b + record_number + c + api_token
    global er
    try:
        response = requests.get(rq)
    except requests.ConnectionError:
        er = 1
        return 0
    if response.status_code != 200:
        er = 1
        return 0
    raw = response.json()
    if len(raw['result'])==0:
        er = 1
        return 0
    if not (str(raw['result'][0]['timeStamp']).isnumeric):
        er = 1
        return 0
    time_stamp = int(raw['result'][0]['timeStamp'])
    old_date = datetime.fromtimestamp(time_stamp)
    current_date = datetime.now()
    delta = current_date - old_date
    return delta.days

def get_balance(address="0x0000000000000000000000000000000000001004"):
    a = "https://api.bscscan.com/api?module=account&action=balance&address="
    b = "&tag=latest&sort=asc&apikey"
    api_token = "EHK917H6T8GF36B3H62T5MSWDMS4YT6HUA"
    rq = a + address + b + api_token
    global er
    try:
        response = requests.get(rq)
    except requests.ConnectionError:
        er = 1
        return 0
    if response.status_code != 200:
        er = 1
        return 0
    raw = response.json()
    if not (str(raw['result']).isnumeric()):
        er = 1
        return 0
    result = int(raw['result'])
    if result == 0:
        return 0
    return 10*math.log(result,10)

def get_fico(address="0x0000000000000000000000000000000000001004"):
    average_transaction = get_average_transaction(address)
    time.sleep(1)
    print (average_transaction)
    balance = get_balance(address)
    time.sleep(1)
    print (balance)
    history = get_time(address)
    time.sleep(1)
    print (history)
    fico =average_transaction*0.35 + balance*0.3 + 0.35*history
    global er
    info = {
        "address" : address,
        "average_transaction" : average_transaction,
        "balance" : balance,
        "history" : history,
        "fico" : int(fico),
        "error" : er
    }
    er = 0
    account_list.append(info)
    with open('fico.json', 'w') as outfile:
        json.dump(account_list, outfile,indent=4)
    return int(fico)

fo = open('acc.json','r')
acc = json.load(fo)
fo.close()
for i in acc:
    get_fico(acc[str(i)])
