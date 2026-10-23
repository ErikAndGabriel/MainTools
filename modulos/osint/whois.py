import whois
from modulos.osint.formatters.formate_api import format_whois
from ui.banner import banner_execucao1 
from core.clear import clear 

class BuscarWhois:
  def __init__(self, servico):
    self.servico = servico
    
  def Buscar(self):
    try:
      clear()
      print(banner_execucao1)
      buscar = whois.whois(self.servico)
      format_whois(buscar)
      return True
    except Exception as e:
      return f"erro {e}"
