# Laço de repetição:

## For(Para):
#for interador in range(1,10):
#  print(interador * 2)
#
## Solicitar valor inicial e valor final;
## Solicitar valor multiplicador
## Multiplicar interador pelo multiplicador
#
#valor_inicial = int(input("Digite o valor inicial: "))
#valor_final = int(input("Digite o valor final: "))
#multiplicador = int(input("Digite o multiplicador: "))
#
#for interador in range(valor_inicial, valor_final):
#  print(interador * multiplicador)
#
#
## Pulo na execução:
#
#for interador in range(2,11,2):
#  print("Valores pares: ", interador) 
#
#valor_inicial = int(input("Digite o valor inicial: "))
#valor_final = int(input("Digite o valor final: "))
#valor_multiplicador = int(input("Digite o valor multiplicador: "))
#
#for interador in range (valor_inicial,valor_final+1):
#    print("Interador: ", interador, "x", valor_multiplicador, "=", interador * valor_multiplicador)
#   

# While:

condicao = True
while condicao:
   print("Estou em execucao em um while.")
   condicao = False

valor = 1
while valor < 5:
  if valor == 2:
    print("O valor é igual a 2.", valor)
  valor += 1
   
   