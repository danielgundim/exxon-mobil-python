import pyodbc

def retornar_cursor_banco_dados():
  connection = pyodbc.connect(retorna_string_conexao_banco_dados())
  cursor = connection.cursor()
  return cursor, connection
  
def retorna_string_conexao_banco_dados():
  return(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-T62N7HC\SQLEXPRESS;"
    "DATABASE=exxonmobil;"
    "UID=daniel;"
    "PWD=daniel;"
  )

def select_banco_dados():
  cursor, connection = retornar_cursor_banco_dados()
  cursor.execute("select * from cliente;")
  clientes = cursor.fetchall()
  print(clientes)
  connection.commit()


def insert_banco_dados(cliente):
  cursor, connection = retornar_cursor_banco_dados()
  insert_query = """
  INSERT INTO cliente (nome, cpf)
  VALUES (?, ?);
  """

  values = (cliente['Nome'], cliente['CPF'])
  cursor.execute(insert_query, values)
  connection.commit()


def delete_banco_dados(cpf):
  cursor, connection = retornar_cursor_banco_dados()
  delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
  cursor.execute(delete_query)
  connection.commit()  

cliente = {"Nome": "Julio", "CPF": "789456123"}
#insert_banco_dados(cliente)

select_banco_dados()
delete_banco_dados(cliente["CPF"])
select_banco_dados()