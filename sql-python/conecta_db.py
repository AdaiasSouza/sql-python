import mysql.connector


class ConectaBancoDeDados:

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
        pass

    def create_database(self, name_database):
        pass

    def drop_database(self, name_database):
        pass

    def list_tables(self, database):
        pass

    def create_table(self, name_table):
        pass

    def drop_table(self, name_table):
        pass

    def query(self, table):
        pass
