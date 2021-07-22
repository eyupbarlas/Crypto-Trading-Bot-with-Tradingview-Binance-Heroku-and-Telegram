import hashlib

#! Tradingview Webhook Token 
pin = '1234'

#* Generating an unique key. For extra security
def get_token():
    token = hashlib.sha224(pin.encode('utf-8'))
    return token.hexdigest()

