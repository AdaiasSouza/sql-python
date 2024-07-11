import mysql.connector


class ConectaMySQL:

    """docstring for ConectaBancoDeDados"""

    def __init__(self, host, user, password):
        print("Iniciando conexao...")
        self.host = host
        self.user = user
        self.password = password
        self.conect = None

    def conecta(self):
        try:
            self.conect = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            return f'MySQL conectado: {self.conect}'

        except Exception as e:
            return f'Erro na conexao: {e}'

    def desconecta(self):
        try:
            self.conect.close()
            return f'MySQL desconectado'

        except Exception as e:
            return f'MySQL não conectado: {e}'

    def list_databases(self):
        try:
            cursor = self.conect.cursor()
            cursor.execute('SHOW DATABASES')
            databases = []
            for database in cursor:
                databases.append(database)
            return databases
        except Exception as e:
            return f'Erro: {e}'

    def create_database(self, name_database):
        try:
            cursor = self.conect.cursor()
            create_db = str('CREATE DATABASE') + ' ' + str(name_database)
            cursor.execute(create_db)
            return f'{name_database} criado...'
        except Exception as e:
            return f'Erro na criação: {e}'

    def drop_database(self, name_database):
        pass

    def list_tables(self, database):
        try:
            cursor = self.conect.cursor()
            cursor.execute('USE ' + str(database))
            cursor.execute('SHOW TABLES')
            tables = []
            for table in cursor:
                tables.append(table)
            return tables
        except Exception as e:
            return f'Erro: {e}'

    def create_table(self, name_table, database):
        try:
            cursor = self.conect.cursor()
            cursor.execute('USE ' + str(database))
            create_db = str('CREATE TABLE') + ' ' + str(database)
            cursor.execute(create_db)
            return f'{database} criado...'
        except Exception as e:
            return f'Erro na criação: {e}'

    def drop_table(self, name_table):
        pass

    def query(self, table):
        pass


class ConectaOracle:
    pass


class ConectaSQLServer:
    pass


class ConectaPostgreSQL:
    pass
