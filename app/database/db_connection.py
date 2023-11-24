import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()


def create_server_connection():
    host_name = os.getenv("DB_HOST")
    user_name = os.getenv("DB_USERNAME")
    user_password = os.getenv("DB_PASSWORD")
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def create_db_connection():
    host_name = os.getenv("DB_HOST")
    user_name = os.getenv("DB_USERNAME")
    user_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_DATABASE")
    port = os.getenv("DB_PORT")
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port=port
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# server_connection = create_server_connection()

# db_connection = create_db_connection()
