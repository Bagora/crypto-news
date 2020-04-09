from django.shortcuts import render

def home(request):
	import requests
	import json

	#get crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,BSV,USDT,EOS,LTC,BNB,ADA,ETC,XLM,TRX,XMR,XTZ,DASH,LINK,LEO,ATOM,NEO,HEDG,HT,MIOTA,CRO,MKR,ZEC,USDC,ONT,XEM,VET,BAT,DOGE,FTT,PAX,BTG,DCR,QTUM,SNX,REP,RVN,ZRX,TUSD,MOF,ALGO,SXP,OKB,BCD,OMG,ZB,HOT,DAI,LSK,ICX,NANO,THETA,KCS,WAVES,ZEN,BTM,DGB,CKB,CENNZ,SEELE,MONA,MCO,BTT,ENJ,KMD,IOST,NEXO,HC,SC,VSYS,DGD,DX,STEEM,XVG,LUNA,ABBC,BTS,BCN,AE,ZIL,KNC,XZC,RIF,QNT,MAID,NRG,MATIC,ARDR,YAP,RLC,ETN,CRPT,GNT,SNT,MANA,SOLVE,ADK&tsyms=USD,EUR")
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
		notfound = "Enter a crypto currency symbol into search form.(e.g) btc,eth,ltc"
		return render(request, 'prices.html', {'notfound' : notfound})