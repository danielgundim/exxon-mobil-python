# Funções:

lista = []


def insert_composto(dado):
  if type(dado) == type("str"):
    lista.append(dado)
    return lista
  else:
    print("Dado não é uma string. Formato inválido.")


print(insert("daniel"))


