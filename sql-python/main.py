from config import database_info
from conecta_db import ConectaBancoDeDados


def execute_db():

    c = ConectaBancoDeDados(database_info['host'],
                            database_info['login_id'],
                            database_info['password']
                            )

    print(c.conecta())
    print()
    print(c.desconecta())


if __name__ == '__main__':
    execute_db()
