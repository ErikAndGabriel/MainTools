from ui.banner import banner_execucao1 
from config.APIS.apis_outras import APIS_OUTRAS
from core.config import timeout
from modulos.osint.formatters.formato import FORMATADORES
from core.clear import clear
import requests 

class Git:
  def __init__(self, git):
    self.git = git
    self.api_git = APIS_OUTRAS["git"]
    self.timeout = timeout("api")
    
  def GitBusca(self):
    if self.api_git in APIS_OUTRAS:
      url = APIS_OUTRAS[self.api_git]["url"].format(self.git)
      try:
        resposta = requests.get(
          url, 
          timeout=self.timeout
        )
        if resposta.status_code == 200:
          data = resposta.json()
        if resposta.status_code == 429:
          print("limite de request dessa api atingido")
          return False
        elif self.api_git in FORMATADORES:
          clear()
          print(banner_execucao1)
          FORMATADORES[self.api_git](data)
          return True  
        else:
          return "erro de conexão"
      except Exception as e:
        return f"erro: {e}"
