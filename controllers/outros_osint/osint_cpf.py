from modulos.osint.cpf import SisregConsulta
from ui.menus.osint.cpf import menu_cpf 
from ui.prompt.prompt_osint import prompt_cpf
from ui.mensagens import erro, outro
from ui.banner import banner_execucao1 
from core.clear import clear
def painel_cpf():
  while True:
    try:
      print(menu_cpf)
      escolha = int(input(prompt_cpf))
      if escolha == 0:
        clear()
        break
      elif escolha == 1:
        cpf = input(f"cpf {prompt_cpf}")
        clear()
        print(banner_execucao1)
        usuario = SisregConsulta(cpf)
        outro()
        continue
      else:
        erro("escolha invalida!")
        outro()
        continue
    except Exception as e:
      erro(f"erro: {e}")
      continue
    except ValueError:
      erro("somente numeros")
      outro()
      continue
