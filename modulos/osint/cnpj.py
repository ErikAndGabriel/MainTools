from ui.banner import banner_execucao1 
from config.APIS.apis_cnpj import APIS_CNPJ
from core.config import timeout
from modulos.osint.formatters.formato import FORMATADORES
from core.clear import clear
import json 
import requests 

class Cnpj:
  def __init__(self, cnpj, api):
    self.cnpj = cnpj
    self.apis_cnpj = api
    self.timeout = timeout("api")
    
  def CNPJBusca(self):
    if self.api_cnpj in APIS_CNPJ:
      url = APIS_CNPJ[self.apis_cnpj]["url"].format(self.cnpj)
      try:
        resposta = requests.get(
          url, 
          timeout=self.timeout
        )
        if resposta.status_code == 200:
          data = resposta.json()
          if self.apis_cnpj in FORMATADORES:
            clear()
            print(banner_execucao1)
            FORMATADORES[self.apis_cnpj](data)
            return True
          else:
            return "erro de api invalida"  
        else:
          return "erro de conexão"
      except Exception as e:
        return f"erro: {e}"
