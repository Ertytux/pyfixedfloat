from ffio.ffinit import FFio
import os
import pandas as pd

#Get actives coins
apikey=os.getenv('ffapi')
seckey=os.getenv('ffsec')
refcode='va9kxaja'
afftax=0.3

ff=FFio(apikey=apikey,seckey=seckey,refcode=refcode,stdata=afftax)

coins=ff.coins()

if coins.get('code')==0:
    df=pd.DataFrame(coins.get('data'))
    df.to_csv('coins.csv')    
    if 'BTCLN' in df.code.values and 'USDTBSC' in df.code.values:
        print(ff.priceFloat(fr='BTCLN',tos='USDTBSC',amount=0.001))
    
