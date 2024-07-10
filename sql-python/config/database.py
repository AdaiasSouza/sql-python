import os
from dotenv import load_dotenv

load_dotenv()

database_info = {
    'login_id': os.getenv('MY_LOGIN_MYSQL'),
    'password': os.getenv('MY_PASSWORD_MYSQL'),
    'host': os.getenv('HOST_MYSQL')
}
