from ui.menus.osint.whois import menu_whois
from ui.mensagens import erro, outro
from core.clear import clear
from modulos.osint.whois import BuscarWhois 
from ui.prompt.prompt_osint import prompt_whois
def painel_whois():
  while True:
    try:
      print(menu_whois)
      escolha = input(prompt_whois)
      if escolha == "0":
        clear()
        break
      elif escolha == "1":
        dominio = input(f"dominio {prompt_whois}")
        user = BuscarWhois(dominio)
        user.Buscar()
        outro()
        continue
      else:
        erro("escolha invalida")
        outro()
    except Exception as e:
      erro(f"erro: {e}")
      outro()
      continue
