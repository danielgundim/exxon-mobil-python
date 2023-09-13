# 1. int: Variáveis int são usadas para armazenar números inteiros. Exemplo: x = 5
# 2. float: Variáveis float são usadas para armazenar números de ponto flutuante (números com casas decimais). Exemplo: pi = 3.14159
# 3. str: Variáveis str (cadeias de caracteres) são usadas para armazenar texto. Exemplo: nome = "João"
# 4. bool: Variáveis bool são usadas para armazenar valores booleanos True (verdadeiro) ou False (falso). Exemplo: ativo = True
# 5. list: Variáveis list são usadas para armazenar sequências mutáveis de elementos. Exemplo: números = [1, 2, 3, 4, 5]
# 6. tuple: Variáveis tuple são usadas para armazenar sequências imutáveis de elementos. Exemplo: coordenadas = (3, 4)
# 7. dict: Variáveis dict (dicionário) são usadas para armazenar pares chave-valor. Exemplo: pessoa = {'nome': 'Maria', 'idade': 30}
# 8. set: Variáveis set (conjunto) são usadas para armazenar coleções de elementos únicos e não ordenados. Exemplo: frutas = {'maçã', 'banana', 'laranja'}
# 9. NoneType: A variável None é usada para representar a ausência de valor ou um valor nulo. Exemplo: vazio = None

#String
cep = "04578-180"

#Numeros
idade = 18
dolar = 4.96

#Bool
condicional = True

#Exemplo variável Java - Estático
# String nome = "Daniel"
# Integer idade = 18

#Linguagem Dinâmica:
#Exemplo Python. Não é necessário definir tipo de variável.

#Funcões
#Print - Irá printar o valor recebido como parâmetro na tela.
print(18)
print(True)

#Input - Irá receber um valor do usuário e armazenar em uma variável.
nome_usuario = input("Digite o nome do usuário: ")
print("O nome do usuário é: ", nome_usuario)


primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
soma = primeiro_valor + segundo_valor

print("O resultado da soma é: ", soma)

# Operadores Aritméticos:
# +	Adição	Realiza a soma de ambos operandos.
# -	Subtração	Realiza a subtração de ambos operandos.
# *	Multiplicação	Realiza a multiplicação de ambos operandos.
# /	Divisão	Realiza a Divisão de ambos operandos.
# //	Divisão inteira	Realiza a divisão entre operandos e a parte decimal de ambos operandos.
# %	Módulo	Retorna o resto da divisão de ambos operandos.
# **	Exponenciação	Retorna o resultado da elevação da potência pelo outro.

divisao = 5 % 2 == 0

# Operador	Equivalente a
# =	x = 1
# +=	x = x + 1
# -=	x = x - 1
# *=	x = x * 1
# /=	x = x / 1
# %=	x = x % 1

valor = 2
valor += 2
print("Valor: ", valor)