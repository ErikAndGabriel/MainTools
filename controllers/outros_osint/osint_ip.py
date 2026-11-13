from ui.menus.osint.ip import menu_ip
from ui.prompt.prompt_osint import prompt_ip
from ui.mensagens import erro, outro
from modulos.osint.ip import Ip
from core.clear import clear
from config.ferramentas.ip import ferramentas_ip
from config.APIS.apis_ip import APIS_IP
def painel_ip():
  while True:
    try:
      print(menu_ip)
      ot = int(input(prompt_ip))
      if ot == 0:
        clear()
        break
        
      elif str(ot) in ferramentas_ip:
        api = ferramentas_ip[str(ot)]
        ip = int(input(f"ip {prompt_ip}"))
        user = Cep(ip, api)
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
