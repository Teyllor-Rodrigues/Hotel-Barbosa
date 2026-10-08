import mysql.connector
from Conectar_banco import conectar

conexao = conectar()
cursor = conexao.cursor()

def validar_cpf(cpf):
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")

    def digito(base):
        soma = 0
        peso = len(base) + 1
        for n in base:
            soma += int(n) * peso
            peso -= 1
        dv = 11 - (soma % 11)
        return dv if dv < 10 else 0

    d1 = digito(cpf[:9])
    d2 = digito(cpf[:9] + str(d1))
    if len(set(cpf)) == 1:
        print("CPF inválido: todos os dígitos são iguais.")
        return False
    elif cpf[9:] == f"{d1}{d2}":
        print("CPF válido.")
        return True
    else:
        print("CPF inválido.")
        return False
    
def digitar_cpf():
    while True:
        cpf = input("Digite o CPF (somente números): ")
        if validar_cpf(cpf):
            return cpf
        else:
            print("CPF inválido. Tente novamente.")

def inserir_Hóspede():
    cpf = digitar_cpf()
    nome = input("Digite o nome do hóspede: ")
    telefone = input("Digite o telefone do hóspede: ")
    email = input("Digite o email do hóspede: ")
    data_nascimento = input("Digite a data de nascimento do hóspede (YYYY-MM-DD): ")

    inserir_hospede = """
    INSERT INTO Hospede (Nome, CPF, Telefone, Email, Data_Nascimento)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        inserir_hospede,
        (nome, cpf, telefone, email, data_nascimento)
    )
    conexao.commit()

    print("Hóspede inserido com sucesso!")

def remover_hóspede():
    nome = input("Digite o nome do hóspede que deseja remover: ")
    remover = """
        DELETE FROM Hospede
        WHERE Nome = %s
    """

    cursor.execute(remover, (nome,))
    conexao.commit()
    