from ui.menus.osint.cnpj import menu_cnpj
from ui.prompt.prompt_osint import prompt_cnpj
from ui.mensagens import erro, outro
from modulos.osint.cnpj import Cnpj
from core.clear import clear
from config.ferramentas.ip import ferramentas_cnpj
from config.APIS.apis_cnpj import APIS_CNPJ
def painel_cnpj():
  while True:
    try:
      print(menu_cnpj)
      ot = int(input(prompt_cnpj))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas_cnpj:
        nome = ferramentas_cnpj[str(ot)]
        prompt = input(f"cnpj {prompt_cnpj}")
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
