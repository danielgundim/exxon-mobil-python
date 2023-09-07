#Condicional
# Operador de comparação:
# ==	Igual a	Verifica se um valor é igual ao outro
# !=	Diferente de Verifica se um valor difere ao outro
# >	Maior que	Verifica se um valor é maior que outro
# >=	Maior ou igual	Verifica se um valor é maior ou igual ao outro
# <	Menor que	Verifica se um valor é menor que outro
# <=	Menor ou igual	Verifica se um valor é menor ou igual ao outro


numero = int(input("Digite um número: "))
tipo_numero = type(numero)
print(tipo_numero)

print(type(2))
if numero <= 5: 
  print("Verdadeiro.")
elif numero > 9:
  print("Maior que 9")
else:
  print("Falso.")

nome = input("Digite o nome: ")
if nome != "daniel":
  print("Sim, o nome é diferente.")
else:
  print("Não, o nome não é diferente.") 


# Criar um validador de balada. Deve ser solicitado ao usuario a sua idade e verificar se a idade
# atende os seguintes requisitos:
# Menor de 18 anos: Não pode entrar na balada;
# Maior ou igual a 18 anos: Pode entrar com restrições;
# Maior que 21 anos: Pode entrar sem restrições.

# Resposta:

idade_usuario = int(input("Digite a idade do usuário: "))

if idade_usuario > 21:
  print("Pode entrar sem restrições")
elif idade_usuario >= 18:
  print("Pode entrar com restrições.")
else:
  print("Não pode entrar na balada.")
  
# Operadores Lógicos:
# and	Retorna True se ambas as afirmações forem verdadeiras
# or	Retorna True se uma das afirmações for verdadeira
# not	retorna Falso se o resultado for verdadeiro

idade_usuario = int(input("Digite a idade do usuário: "))

if idade_usuario > 18 or idade_usuario > 21:
  print("Pode entrar na balada.")
elif idade_usuario < 18:
  print("Não pode entrar na balada.")