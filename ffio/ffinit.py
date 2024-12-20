

import hmac
import json
import hashlib
import requests


class FFio:
    def __init__(self, apikey: str, seckey: str,refcode:str,stdata:float):
        self.__apikey = apikey
        self.__seckey = seckey
        self.__refcode=refcode
        self.__stdata=stdata

    def __sign(self, data):
        return hmac.new(
            key=self.__seckey.encode(),
            msg=data.encode(),
            digestmod=hashlib.sha256).hexdigest()

    def __request(self, method:str, params={}):
        url = 'https://ff.io/api/v2/' + method
        data = json.dumps(params)
        headers = {
            'X-API-KEY': self.__apikey,
            'X-API-SIGN': self.__sign(data)}
        r = requests.post(url, data=data, headers=headers)
        return r.json()
    
    def coins(self):
        """
        Obtener una lista de monedas admitidas por el servicio FixedFloat, 
        así como datos sobre su visualización e información sobre la 
        disponibilidad para recibir y enviar.
        """
        return self.__request(method='ccies')
    
    def expriceFloat(self,fr:str,tos:str,amount:float): 
        """
        Obtener el tipo de cambio de un par de divisas en la dirección 
        y el tipo de cambio seleccionados.
        """       
        data={
            'type':'float',
            'fromCcy':fr,
            'toCcy':tos,
            'direction':'from',
            'amount':amount,
            'refcode':self.__refcode,
            'afftax':self.__stdata
            }
        return self.__request(method='price',params=data)
        
        
    

