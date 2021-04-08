from django.shortcuts import render

def home(request):
	import requests
	import json

	#get crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BNB,XRP,USDT,ADA,DOT,UNI,LTC,LINK,THETA,BCH,XLM,USDC,FIL,TRX,WBTC,DOGE,KLAY,SOL,VET,BTT,LUNA,EOS,CRO,MIOTA,XMR,BSV,AAVE,XTZ,NEO,FTT,ATOM,BUSD,HOT,AVAX,KSM,XEM,ALGO,DAI,EGLD,HT,CAKE,DASH,BTCB,CHZ,HBAR,ENJ,COMP,DCR,SNX,RUNE,ZIL,ETC,MKR,NEAR,GRT,LEO,STX,ZEC,TFUEL,BAT,SUSHI,MATIC,CEL,UST,NPXS,YFI,DENT,ONE,RVN,MANA,NEXO,ONT,QTUM,ICX,UMA,HNT,ZRX,SC,OMG,WAVES,BTG,BNT,FLOW,DGB,OKB,CHSB,FTM,REV,RSR,ANKR,REN,CFX,WRX,AR,1INCH,VGX,BTMX,PAX&tsyms=USD,EUR")
	price = json.loads(price_request.content)

	#get crypto news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price':  price })

  
def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote': quote, 'crypto' : crypto})

	else:
		notfound = "Enter a crypto currency symbol into search form.(e.g) btc,eth,bnb"
		return render(request, 'prices.html', {'notfound' : notfound})