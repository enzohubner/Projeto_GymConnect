def salvar_lista_arquivo(lista):
  arquivo = open("mytask.txt", 'w')
  for item in lista:
    arquivo.write(f'{item}\n')
  arquivo.close()


def adicionar_valor_arquivo(valor):
  arquivo = open("mytask.txt", 'a')
  arquivo.write(f'{valor}\n')
  arquivo.close()


def ler_arquivo():
  arquivo = open("mytask.txt", 'r')
  lista = arquivo.readlines()
  arquivo.close()
  return lista
