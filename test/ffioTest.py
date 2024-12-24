from ffio.ffinit import FFio
import os

#Get actives coins
apikey=os.getenv('ffapi')
seckey=os.getenv('ffsec')
refcode='va9kxaja'
afftax=0.3

ff=FFio(apikey=apikey,seckey=seckey,refcode=refcode,stdata=afftax)

print(ff.coins())