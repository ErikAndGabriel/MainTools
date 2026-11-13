from ui.menus.osint.ip import menu_ip
from ui.prompt.prompt_osint import prompt_ip
from ui.mensagens import erro, outro
from modulos.osint.ip import Ip
from core.clear import clear
from config.APIS.apis_outras import APIS_OUTRAS 
def painel_git():
  while True:
    try:
      print(menu_ip)
      ot = int(input(prompt_ip))
      if ot == 0:
        clear()
        break
        
      elif escolha == 1:
        prompt = input(f"ip {prompt_ip}")
        user = Ip(prompt, nome)
        user.IpBusca()
        outro()
        continue
        
      else:
        erro("escolha invalida")
        continue
    except ValueError:
      erro("somente numeros")
      continue
    except Exception as e:
      erro(f"erro: {e}")
