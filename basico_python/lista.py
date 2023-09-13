# Listas:

#append(): Adiciona um elemento ao final da lista.
#extend(): Adiciona os elementos de outra lista ao final da lista atual.
#insert(): Insere um elemento em uma posição específica da lista.
#remove(): Remove o primeiro elemento com um valor específico da lista.
#pop(): Remove e retorna o elemento em uma posição específica da lista.
#index(): Retorna o índice da primeira ocorrência de um valor específico na lista.
#count(): Conta quantas vezes um valor específico aparece na lista.
#sort(): Ordena a lista em ordem ascendente.
#reverse(): Inverte a ordem dos elementos na lista.

lista = [16,5,52,3,44,44,4,10,5,44,6,14,15]
lista.append(77)
print(lista)
print(lista.index(44))
print(lista[4])
lista.sort()
print(lista)
lista.reverse()
print(lista)

#len(): Retorna o número de elementos em uma lista.
#max(): Retorna o elemento máximo em uma lista.
#min(): Retorna o elemento mínimo em uma lista.
#sum(): Retorna a soma dos elementos em uma lista.

print(len(lista))
print(max(lista))
print(min(lista))
print(sum(lista))

lista_string = ['daniel', 'carlos,', 'larissa', 'roberto', 'acabaxi']

lista_string.sort()
print(lista_string)
print(max(lista_string))
#print(sum(lista_string))


#lista_complexa = [2,'daniel', 'ronaldo', 18.4, 3.14, 'melao']
#
#print(lista)
#print(type(lista))
#print(lista[5])
#
#
#print(lista_string)
#print(type(lista_string))
#print(lista_string[2])
#
#print(lista_complexa)
#print(type(lista_complexa))
#print(lista_complexa[4])
#

lista_laco = []
print("Lista laço vazia: ", lista_laco)
for interador in range(0,10):
  lista_laco.append(interador)
print("Lista laço preenchida: ", lista_laco)