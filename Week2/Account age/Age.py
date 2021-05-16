from bscscan import BscScan     # install from source : pip install git+https://github.com/pcko1/bscscan-python.git
from etherscan import Etherscan # install from source : pip install git+https://github.com/pcko1/etherscan-python.git
from datetime import datetime
import time

# Make a ditionary for age rating
age_rating={}
age_rating.update(dict.fromkeys([0,1,2],10))
age_rating.update(dict.fromkeys([3,4,5],20))
age_rating.update(dict.fromkeys([6,7,8,9,10,11],25))
age_rating.update(dict.fromkeys([12,13,14,15,16,17],30))
age_rating.update(dict.fromkeys([18,19,20,21,22,23],40))
age_rating.update(dict.fromkeys([24,25,26,27,28,29],50))
age_rating.update(dict.fromkeys([30,31,32,33,34,35],60))
age_rating.update(dict.fromkeys([36,37,38,39,40,41],70))
age_rating.update(dict.fromkeys([42,43,44,45,46,47],80))
age_rating.update(dict.fromkeys([48,49,50,51,52,53,54,55,56,57,58,59],90))

# Function to get age rating from bscscan
def get_age_bsc(address="0x0000000000000000000000000000000000001004",api_token = "EHK917H6T8GF36B3H62T5MSWDMS4YT6HUA"):
    bsc = BscScan(api_token)
    first_transaction = bsc.get_normal_txs_by_address_paginated(address,page=1,offset=1,startblock=1,endblock=99999999,sort="asc")
    time.sleep(0.5)
    while first_transaction=="Max rate limit reached, please use API Key for higher rate limit":
        time.sleep(1)
        first_transaction = bsc.get_normal_txs_by_address_paginated(address,page=1,offset=1,startblock=1,endblock=99999999,sort="asc")
    if len(first_transaction) == 0:
        return 0
    old_date = datetime.fromtimestamp(int(first_transaction[0]['timeStamp']))
    current_date = datetime.now()
    delta = (current_date.year-old_date.year)*12 + (current_date.month-old_date.month)
    return age_rating.get(delta,0)


# Function to get age rating from etherscan
def get_age_eth(address="0x0000000000000000000000000000000000001004",api_token = "EHK917H6T8GF36B3H62T5MSWDMS4YT6HUA"):
    eth = Etherscan("WCPCQASVXMS68JNDCY2ZTCYTNCDPYXD1JD")
    first_transaction = eth.get_normal_txs_by_address_paginated(address,page=1,offset=1,startblock=1,endblock=99999999,sort="asc")
    time.sleep(0.5)
    while first_transaction=="Max rate limit reached, please use API Key for higher rate limit":
        time.sleep(1)
        first_transaction = eth.get_normal_txs_by_address_paginated(address,page=1,offset=1,startblock=1,endblock=99999999,sort="asc")
    if len(first_transaction) == 0:
        return 0
    old_date = datetime.fromtimestamp(int(first_transaction[0]['timeStamp']))
    current_date = datetime.now()
    delta = (current_date.year-old_date.year)*12 + (current_date.month-old_date.month)
    return age_rating.get(delta,0)

# Combine both rating
def get_age(address="0x0000000000000000000000000000000000001004",api_token = "EHK917H6T8GF36B3H62T5MSWDMS4YT6HUA"):
    rating_eth = get_age_eth(address=address,api_token=api_token)
    # If rating is alreay 100 then return 100
    if rating_eth==100:         
        return rating_eth
    # Else return which ever is larger
    else:
        rating_bsc = get_age_bsc(address=address,api_token=api_token)
        if rating_eth<rating_bsc:
            return rating_bsc
        else:
            return rating_eth

print (get_age("0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8"))
