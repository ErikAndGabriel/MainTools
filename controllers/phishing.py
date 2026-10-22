from ui.menus.menus import menu_phishing
from ui.prompt.prompt import prompt_phishing
from ui.mensagens import erro
from core.clear import clear

def painel_phishing():
  while True:
    try:
      print(menu_phishing)
      ot = int(input(prompt_phishing))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas:
        clear()
        ferramentas[str(ot)]()
          
      else:
        erro("somente numeros")
        continue
    except ValueError:
      erro("erro, somente numeros")
      continue
    except KeyboardInterrupt:
      exit()
    except Exception as e:
      erro(f"erro: {e}")
