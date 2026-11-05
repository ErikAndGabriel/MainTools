from ui.menus.osint.ip import menu_git
from ui.prompt.prompt_osint import prompt_git
from ui.mensagens import erro, outro
from modulos.osint.git import Git
from core.clear import clear
from config.APIS.apis_outras import APIS_OUTRAS
def painel_git():
  while True:
    try:
      print(menu_git)
      ot = int(input(prompt_git))
      if ot == 0:
        clear()
        break

      elif escolha == 1:
        prompt = input(f"git {prompt_git}")
        user = Git(prompt, nome)
        user.GitpBusca()
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
