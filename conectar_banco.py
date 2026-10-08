import mysql.connector

def conectar():
    try : 
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password= "root",
            database="Hotel_Barbosa"
        )

        if conexao.is_connected():
            print("Conectado ao MySQL!")
            return conexao

    except mysql.connector.Error as erro:
        print("Erro ao conectar:", erro)
        return None