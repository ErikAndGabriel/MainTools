from ui.menus.osint.nome import menu_nome
from ui.prompt.prompt_osint import prompt_nome
from ui.mensagens import erro, outro
from core.clear import clear 
from modulos.osint.nome import NomeBusca

def painel_nome():
  while True:
    try:
      print(menu_nome)
      escolha = input(f"{prompt_nome}")
      if escolha == "0":
        clear()
        break
      elif escolha == "2":
        erro("sem logs disponíveis")
        outro()
      elif escolha == "1"
        try:
          nome = input(f"nome {prompt_nome}")          
          quantidade = int(input(f"quantidade {prompt_nome}"))
        except ValueError:
          erro("somente numeros")
          outro()
        user = NomeBusca(nome, quantidade)
        user.Buscar()
        outro()
    except Exception as e:
      erro(f"erro: {e}")
      outro()
