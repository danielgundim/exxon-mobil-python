import pyodbc


def acesso_banco():
  connection = pyodbc.connect(retorna_conexao_banco_dados())
  cursor = connection.cursor()
  cursor.execute("select * from cliente;")
  clientes = cursor.fetchall()
  print(clientes)

def retorna_conexao_banco_dados():
  return(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-T62N7HC\SQLEXPRESS;"
    "DATABASE=exxonmobil;"
    "UID=daniel;"
    "PWD=daniel;"
  )

acesso_banco()