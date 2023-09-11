# Dicionário:

#dict.keys(): Retorna uma lista com as chaves do dicionário.
#dict.values(): Retorna uma lista com os valores do dicionário.
#dict.items(): Retorna uma lista de tuplas (chave, valor) do dicionário.
#dict.get(chave): Retorna o valor associado à chave especificada, ou um valor padrão se a chave não existir.
#dict.pop(chave): Remove a chave especificada e retorna o valor associado a ela.
#dict.popitem(): Remove e retorna um par chave-valor aleatório do dicionário.
#dict.update(outro_dict): Atualiza o dicionário com os pares chave-valor de outro dicionário.
#dict.clear(): Remove todos os pares chave-valor do dicionário, deixando-o vazio.
#len(dict): Retorna o número de pares chave-valor no dicionário.
#in: Verifica se uma chave está presente no dicionário.

lista = [1,2,3,4,5,5]

dicionario1 = {
  "nome": "Daniel",
  "profissao": "Professor",
  "empresa": "Ada"
}

print(dicionario1.values())

if 'profissao' in dicionario1:
  print(dicionario1['profissao'])


dicionario2 = {
  "nome": "Pedro",
  "profissao": "Mecanico",
  "empresa": "B"
}

lista_dicionario = [dicionario1, dicionario2]
print(lista_dicionario)


#print(dicionario1)
#print(type(dicionario1))
#print(dicionario1['nome'])
#
#dicionario1['nome'] = "Daniel Vieira"
#print(dicionario1['nome'])
#