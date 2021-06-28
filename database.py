import asyncio
import logging
import psycopg2

from data.config import PG_HOST, PG_PASS, PG_USER


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


def create_db():
    create_db_command = open("utils/db_api/create_db.sql", "r").read()

    logging.info("Connecting to database...")
    connection = psycopg2.connect(user=PG_USER,
                                  password=PG_PASS,
                                  host=PG_HOST,
                                  port=5432,
                                  database="postgres")
    cursor = connection.cursor()
    cursor.execute(create_db_command)
    connection.commit()
    connection.close()
    logging.info("Table users created")


if __name__ == '__main__':
    create_db()
