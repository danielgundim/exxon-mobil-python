# Exercício:

  # Solicitar quantas notas o aluno teve. Receber cada uma dessas notas e armazenar em
  # uma lista. Realizar média do aluno e verificar se ele foi aprovado. Caso tenha nota abaixo ou igual
  # de 6 
  # será reprovado, se a nota for 7 ficará de recuperação senão será aprovado. Exibir um dicionário
  # informando: média, maior nota, menor nota e status que deve informar se foi aprovado, recuperado
  # ou se está em reprovado.


quantidade_notas = int(input("Digite a quantidade de notas do aluno: "))
lista_notas = []

for interador in range(1, quantidade_notas + 1):
  lista_notas.append(int(input("Digite a nota: ")))

media = sum(lista_notas) / quantidade_notas
maior_nota = max(lista_notas)
menor_nota = min(lista_notas)

aluno = {
  "Media" : media,
  "Maior nota" : maior_nota,
  "Menor nota" : menor_nota
}

if media <= 6:
  aluno['status'] = "Reprovado"
elif media <= 7:
  aluno['status'] = "Recuperação"
elif media > 7:
  aluno['status'] = "Aprovado"

print(aluno)












