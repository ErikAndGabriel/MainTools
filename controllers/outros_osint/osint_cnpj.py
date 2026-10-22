from ui.menus.osint.ip import menu_ip
from ui.prompt.prompt_osint import prompt_ip
from ui.mensagens import erro, outro
from modulos.osint.cnpj import Cnpj
from core.clear import clear
from config.ferramentas.ip import ferramentas_cnpj
from config.APIS.apis_cnpj import APIS_CNPJ
def painel_cnpj():
  while True:
    try:
      print(menu_ip)
      ot = int(input(prompt_ip))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas_cnpj:
        nome = ferramentas_cnpj[str(ot)]
        prompt = input(f"ip {prompt_ip}")
        user = Cnpj(prompt, nome)
        user.CnpjBusca()
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
