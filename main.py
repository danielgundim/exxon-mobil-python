from cliente import menu_cliente

def exibir_menu():
  validador_menu = True
  while validador_menu:
    print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da ExxonMobil."
      "Selecione uma das opções abaixo:"
      "\n 1 - Cliente"
      "\n 2 - Ordem"
      "\n 3 - Realizar análise da carteira"
      "\n 4 - Imprimir relatório da carteira"
      "\n 5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
      menu_cliente()
    elif opcao == 2:
      pass
    elif opcao == 3:
      pass
    elif opcao == 4:
      pass
    elif opcao == 5:
      print("Encerrando a execução do programa.")
      validador_menu = False
    else:
      print("Opção inválida.")

exibir_menu()