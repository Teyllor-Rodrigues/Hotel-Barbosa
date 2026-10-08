import mysql.connector
from Conectar_banco import conectar

conexao = conectar()
cursor = conexao.cursor()

sql_quarto = """ 
    create table if not exists Quartos(
        Id_Numero int primary key not null unique,
        Capacidade int not null,
        Banheiro BOOLEAN not null default false,
        Status ENUM('Livre', 'Ocupado', 'Manutencao') DEFAULT 'Livre'
        );
"""
sql_hospede = """
    create table if not exists Hospede(
        Id_Hospede int primary key auto_increment,
        Nome varchar(100),
        CPF varchar(14) not null unique,
        Telefone varchar(30),
        Email varchar(100),
        Data_Nascimento Date not null
    );
"""
sql_hospedagem = """
    Create Table if not exists Hospedagem(
        id_hospedagem int primary key auto_increment,
        Hospede_id int,
        Quarto_id int,
        Data_entrada Date not null,
        Data_saida Date,

        foreign key (hospede_id) references Hospede(Id_Hospede),
        foreign key (Quarto_id) references Quartos(Id_Numero)
    );
    """

cursor.execute(sql_quarto)
cursor.execute(sql_hospede)
cursor.execute(sql_hospedagem)

conexao.commit()

print("Tabelas criadas com sucesso!")

cursor.close()
conexao.close()