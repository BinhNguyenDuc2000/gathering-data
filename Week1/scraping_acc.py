from web3 import Web3
import requests
import certifi
from collections import defaultdict
import json
import time

test_add = "0x631Fc1EA2270e98fbD9D92658eCe0F5a269Aa161"
numbers_transactions = 10000
ankr_url = "https://apis.ankr.com/3d77a1b9a82046a09c03301c8b1e839a/95090ca72924ce5506d7e32008384fd2/binance/full/main"
web3 = Web3(Web3.HTTPProvider(ankr_url))
print("isConnected:", web3.isConnected())

txs_apt = "https://api.bscscan.com/api?module=account&action=txlist&address="+ test_add +"&startblock=1&endblock=99999999&page=1&offset="+ str(numbers_transactions) +"&sort=asc&apikey=YourApiKeyToken"
response1 = requests.get(txs_apt, verify = certifi.where())
address_content = response1.json()
result1 = address_content.get("result")

def get_key(val , dict):
    for key, value in dict.items():
        if val == value:
            return key
    return -1

users = {}
k = 0
for tran in result1:
    tx_from = tran.get("from")
    tx_to = tran.get('to')
    if tx_from.upper() != test_add.upper():
        if get_key(tx_from, users) == -1:
            users[k] = tx_from
            k = k + 1
    elif tx_to.upper() != test_add.upper() and get_key(tx_to, users) == -1:
            users[k] = tx_to
            k = k + 1

with open("acc.json", "w") as outfile:
    json.dump(users, outfile)

