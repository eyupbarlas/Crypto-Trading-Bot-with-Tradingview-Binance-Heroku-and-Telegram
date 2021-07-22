import requests, pprint, requests, time
from config import *
from binance.client import Client
from binance.enums import *
from binance.streams import BinanceSocketManager
from twisted.internet import reactor

"""
          .-.         .--''-.
        .'   '.     /'       `.
        '.     '. ,'          |
     o    '.o   ,'        _.-'
      \.--./'. /.:. :._:.'
     .'    '._-': ': ': ': ':
    :(#) (#) :  ': ': ': ': ':>-
     ' ____ .'_.:' :' :' :' :'
      '\__/'/ | | :' :' :'
            \  \ \
            '  ' '      The Bzzman.
"""


#! Client init
client = Client(API_KEY, SECRET_KEY)

currentPrice = {'error' : False}

#! Global variables for trading purposes
TRADE_SYMBOL = 'your trade symbol' # enter a symbol like: SOLBUSD or ETHUSDT
TRADE_QUANTITY = 1  # enter your amount     #! Be careful! You have to give a value larger than 'MIN_NOTIONAL'  

#! Live coin price
def live_message(msg):
    if msg['e'] != 'error':
        currentPrice['price'] = msg['p']
    else:
        currentPrice['error'] = True


#! Telegram Notification
def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = BOT_CHATID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)


#! Limit Buy Order
def limitBuyOrder(symbol, quantity, price):
    try:
        print("**Sending Limit Buy Order**")
        order = client.order_limit_buy(
            symbol=symbol,
            quantity=quantity,
            price=price
        )
        pprint.pprint(order)

    except Exception as e:
        print("Exception occured: {}".format(e))
        return False

    return True


#! Limit Sell Order
def limitSellOrder(symbol, quantity, price):
    try:
        print("**Sending Limit Sell Order**")
        order = client.order_limit_sell(
            symbol=symbol,
            quantity=quantity,
            price=price
        )
        pprint.pprint(order)

    except Exception as e:
        print("Exception occured: {}".format(e))
        return False

    return True


#! Market Buy Order
def marketBuyOrder(symbol, quantity):
    try:
        print("**Sending Market Buy Order**")
        order = client.order_market_buy(
            symbol=symbol,
            quantity=quantity
        )
        pprint.pprint(order)

    except Exception as e:
        print("Exception occured: {}".format(e))
        return False
    
    return True


#! Market Sell Order
def marketSellOrder(symbol, quantity):
    try:
        print("**Sending Market Sell Order**")
        order = client.order_market_sell(
            symbol=symbol,
            quantity=quantity
        )
        pprint.pprint(order)

    except Exception as e:
        print("Exception occured: {}".format(e))
        return False
    
    return True


#! Web Socket for live prices
def WebSocketManager(client):
    #* Live coin prices via Binance Socket Manager
    bsm = BinanceSocketManager(client=client, user_timeout=60)
    conn_key = bsm.start_trade_socket(TRADE_SYMBOL, live_message)
    bsm.start()

    #* Terminating WebSocket after 3 secs
    time.sleep(3)
    bsm.stop_socket(conn_key=conn_key)
    reactor.stop()