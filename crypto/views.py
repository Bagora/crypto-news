from django.shortcuts import render

import crypto

def home(request):
	import requests
	import json

	#get crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BNB,USDT,ADA,SOL,XRP,DOT,DOGE,USDC,SHIB,LUNA,AVAX,LTC,UNI,WBTC,LINK,BUSD,BCH,MATIC,ALGO,VET,XLM,AXS,ICP,CRO,FIL,TRX,ATOM,ETC,THETA,FTT,FTM,BTCB,HBAR,DAI,EGLD,NEAR,GRT,XTZ,XMR,MANA,EOS,HNT,CAKE,AAVE,FLOW,KLAY,LRC,MIOTA,KSM,XEC,NEO,BSV,KDA,RUNE,QNT,ONE,LEO,MKR,UST,CHZ,STX,WAVES,BTT,ENJ,ZEC,HOT,AMP,AR,DASH,SAND,OMG,CELO,COMP,TFUEL,NEXO,KCS,CRV,XEM,OKB,BAT,QTUM,HT,SUSHI,ICX,DCR,LPT,SCRT,RVN,ZIL,REV,BTG,AUDIO,YFI,TUSD,IOTX,MINA,SNX,TEL,PERP,ZEN,XDC,RENBTC,BNT,CEL,ZRX,SC,ANKR,ELON,ONT,SRM,UMA,REN,WAXP,USDP,DYDX,IOST,RAY,SKL,DGB,MOVR,XYO,1INCH,NANO,CELR,GNO,TRAC,VGX,VLX,WOO,CKB,MDX,FET,DENT,CHSB,NU,RSR,XDB,OCEAN,KAVA,USDN,WIN,GT,STORJ,GLM,INJ,POLY,REEF,ALPHA,WRX,FX,SXP,COTI,VTHO,LSK,NMR,XVG,BTCST,FEI,CTSI,OXT,BAKE,BCD,NKN,ASD,CHR,MED,RLC,CFX,AMPL,CEEK,OGN,FLUX,UOS,BADGER,SNT,ALICE,ERG,UBT,PAXG,ONG,ARDR,ROSE,CVC,HIVE,BAND,STMX,AGIX,PROM,ELF,XVS,CSPR,VRA,DAG,BORA,EWT,XPR,STRAX,REP&tsyms=USD,EUR")
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

def news(request):
	import requests
	import json
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'news.html', {'api' : api})