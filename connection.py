import psycopg as pg
from password import password

def connecting():
    connection=pg.connect(
                host="localhost",
                dbname="Expense_Tracker",
                user="postgres",
                password=password(),
                port=5432)
    
    cursor=connection.cursor()

    return connection , cursor