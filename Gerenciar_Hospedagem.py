import mysql.connector
from Conectar_banco import conectar

def listar_hospedagens():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        SELECT h.id_hospedagem, ho.Nome, q.Id_Numero, h.Data_entrada, h.Data_saida
        FROM Hospedagem h
        JOIN Hospede ho ON h.Hospede_id = ho.Id_Hospede
        JOIN Quartos q ON h.Quarto_id = q.Id_Numero
    """
    cursor.execute(sql)
    hospedagens = cursor.fetchall()
    cursor.close()
    conexao.close()

    return hospedagens


hospedes = listar_hospedagens()

for row in hospedes:
        print(f"""
        ID Hospedagem: {row[0]}
        Nome do Hóspede: {row[1]}
        Número do Quarto: {row[2]}
        Data de Entrada: {row[3]}
        Data de Saída: {row[4]}
        """)
