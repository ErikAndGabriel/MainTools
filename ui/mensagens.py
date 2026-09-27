from ui.color import vermelho, verde, amarelo, roxo 
from core.clear import clear
def outro():
  input("precione [ENTER]")
  clear()

def personalizar_loop(data):
  print(roxo, data)
  
def erro(data):
  print(vermelho, data)
  outro()
  
def sucesso(data):
  print(verde, data)
  outro()
  
def mensagem(data):
  print(amarelo, data)
  outro()
  
def personalizar(data):
  print(roxo, data)
  outro()

def sucesso_loop(data):
  print("\r", verde, data)

def erro_loop(data):
  print("\r", vermelho, data)
