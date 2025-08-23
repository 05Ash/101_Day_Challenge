from services.configS import server_connect
import psycopg2
from time import sleep

while True:
    try:
        connection = server_connect()
        cursor = connection.cursor()
        print("Connection Successful.")
        break
    except Exception as error:
        print("Connection to database failed.")
        print("Error: ",error)
        sleep(2)
