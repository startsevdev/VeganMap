import logging
import psycopg2

from data.config import PG_HOST, PG_PASS, PG_USER


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


def create_connection():
    logging.info("Connecting to database...")
    connection = psycopg2.connect(user=PG_USER,
                                  password=PG_PASS,
                                  host=PG_HOST,
                                  database="postgres")
    return connection


def create_database():
    connection = create_connection()
    create_db_command = open("utils/db_api/create_db.sql", "r").read()
    cursor = connection.cursor()
    cursor.execute(create_db_command)
    connection.commit()
    cursor.close()
    connection.close()
    logging.info("Table restaurants created")


if __name__ == '__main__':
    create_database()
