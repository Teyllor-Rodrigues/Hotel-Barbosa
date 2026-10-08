from Conectar_banco import conectar


def listar_Ids_Quartos():
    conexao = conectar()
    cursor = conexao.cursor()
    quartos = "Select id_numero from Quartos"
    cursor.execute(quartos)
    quartos = cursor.fetchall()
    lista_ids = [quarto[0] for quarto in quartos]
    cursor.close()
    conexao.close()

    return lista_ids

def Inserir_Quartos():
    lista_quartos = listar_Ids_Quartos()       
    conexao = conectar()
    cursor = conexao.cursor()

    while True :
        Numero = int(input("\nDigite o Numero do quarto : "))

        if Numero in lista_quartos:
            print("O quarto ja exite, Digite outro :")
            continue
        else :
            break

    Capacidade = int(input("\nDigite a capacidade do Quarto : "))
    Banheiro = input("\nO quarto possui banheiro ? [s/n] : ").upper()
    if Banheiro == "S":
        Banheiro = True
    else :
        Banheiro = False

    inserir_banheiro = """
    insert into Quartos (id_numero, Capacidade, Banheiro)
    values(%s,%s,%s)
    """

    cursor.execute(
        inserir_banheiro,  
        (Numero,Capacidade, Banheiro)
        )
    conexao.commit()

    print("Quarto inserido com sucesso !!")

    cursor.close()
    conexao.close()

def remover_quarto():
    lista_quartos = listar_Ids_Quartos()       
    conexao = conectar()
    cursor = conexao.cursor()
    while True :
        Numero = int(input("\nDigite o Numero do quarto que queira remover : "))

        if Numero not in lista_quartos:
            print("\nDigite um numero de um quarto exixtente !!")
            continue
        else :
            break

    remover = """
        Delete from Quartos
        where id_numero = %s
    """

    cursor.execute(remover, (Numero,))
    conexao.commit()

    print("Quarto removido com sucesso !!")

    cursor.close()
    conexao.close()

listaq=listar_Ids_Quartos()
print(listaq)