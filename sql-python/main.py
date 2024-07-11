from config import database_info
from conecta_db import ConectaMySQL


def execute_db():

    c = ConectaMySQL(database_info['host'],
                     database_info['login_id'],
                     database_info['password']
                     )

    print(c.conecta())
    print()
    # c.list_databases()
    print()
    # print(c.list_tables('smart_menu'))
    c.create_database('db_test')
    print(c.desconecta())


if __name__ == '__main__':
    execute_db()
