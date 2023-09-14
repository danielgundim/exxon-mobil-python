def menu_cliente():
  validador_menu = True
  while validador_menu:
    print("Menu Cliente"
      "\n 1 - Cadastrar Cliente"
      "\n 2 - Alterar Cliente"
      "\n 3 - Buscar Cliente"
      "\n 4 - Deletar Cliente"
      "\n 5 - Listar Clientes"
      "\n 6 - Voltar ao menu anterior")
    opcao = int(input("Digite a opção desejada do menu cliente: "))
    if opcao == 1:
      print("Cliente. Problema resolvido")
    elif opcao == 2:
      pass
    elif opcao == 3:
      pass
    elif opcao == 4:
      pass
    elif opcao == 5:
      pass
    elif opcao == 6:
      print("Encerrando a execução do programa.")
      validador_menu = False
    else:
      print("Opção inválida.")