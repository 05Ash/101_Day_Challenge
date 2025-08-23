import psycopg2
from psycopg2.extras import RealDictCursor

def server_connect():
    return psycopg2.connect(
            host='172.17.177.84',
            port='5432',
            database='windows',
            user='windows_admin',
            password='Password123',
            cursor_factory=RealDictCursor
            )
