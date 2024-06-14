import os

from dotenv import load_dotenv
import psycopg2

load_dotenv()


def create_connection_string():
    db_user_name = os.environ.get("POSTGRES_USER")
    db_password = os.environ.get("POSTGRES_PASSWORD")
    db_database_name = os.environ.get("POSTGRES_DB")
    db_port = os.environ.get("POSTGRES_PORT")

    env_variables = db_user_name and db_password and db_database_name and db_port

    if not env_variables:
        raise KeyError('One of the required variables are missing')

    connection_string = f"postgresql://{db_user_name}:{db_password}@database:{db_port}/{db_database_name}"

    return connection_string


def open_database():
    try:
        conn_url = create_connection_string()
        connection = psycopg2.connect(conn_url)
        connection.autocommit = True

    except psycopg2.DatabaseError as exception:
        raise exception

    return connection


def connection_handler(function_to_wrap):
    def wrapper(*args, **kwargs):

        try:
            with open_database() as connection:
                with connection.cursor() as cursor:
                    value = function_to_wrap(cursor, *args, **kwargs)

        finally:
            cursor.close()
            connection.close()

        return value

    return wrapper
