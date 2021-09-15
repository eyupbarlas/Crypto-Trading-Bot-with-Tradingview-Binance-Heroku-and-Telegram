# Crypto Trading Bot by Bzzman
## Architecture
![Trading Bot Architecture](https://user-images.githubusercontent.com/72407947/126675086-99f049dc-3e4c-41f1-92b7-7cca4612ab0a.png)
## About Project
  ***Work in progress.*** This bot does automated trading operations with Binance. You need a Binance account to start trading. Then when you connect the API keys, trading will be automated using the real time data provided by Tradingview webhooks. You need to pick an indicator and set alerts. The bot will do the trading for you. After each operation, you'll get notifications via Telegram. Crypto trading is highly volatile. This project doesn't possess any trading advise. Trade carefully.
## Features
* Real time data from Tradingview using webhooks
* Automated market buy and sell operations.
* Telegram notifications when an operation gets executed.
* User interface ***on progress***.
## How To Use
### Required Libs
* [Python-Binance](https://python-binance.readthedocs.io/en/latest/ "python-binance")
```
pip install python-binance
```
* [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/ "Python Flask")
```
pip install Flask
```
### Deploying Python Flask App to Heroku
> [Useful documentation by Heroku](https://devcenter.heroku.com/articles/getting-started-with-python "python app deployment")
#### Useful terminal commands after deployment:
* After making a change on production: `git add .` + `git commit -am "your message"`
* Pushing the app to the cloud: `git push heroku master`
* Checking for logs: `heroku logs --tail`

### Setting Up Telegram Bot
To build a bot for Telegram, you need to talk to [BotFather](https://telegram.me/botfather "BotFather") and follow the simple steps. He will give you a token to start a chat with your bot. 

### Setting Up the Tradingview Webhook
![webhook](https://user-images.githubusercontent.com/72407947/126683597-e6a195bf-089f-41fc-99c3-7f05382db188.jpg)

To allow webhooks in Tradingview, you need to upgrade your account to Pro version. (A small price to pay for salvation:) )

## Related Links
### Inspiration and useful resources:
* https://github.com/hackingthemarkets/tradingview-binance-strategy-alert-webhook
* https://github.com/Haehnchen/crypto-trading-bot
* https://algotrading101.com/learn/binance-python-api-guide/

> **Personal Information**
> 
>> Eyüp Barlas  eyupbarlas2134@gmail.com
>> For more projects, [click here](https://github.com/eyupbarlas "my repos").
