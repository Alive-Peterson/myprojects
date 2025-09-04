import mysql.connector
import csv
import matplotlib

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="llawlietnate",
        database="projects"
    )

def add_expense():
    date=input("Enter Date (DD-MM-YYYY):")
    amount=float(input("Enter the amount:"))
    category=input("Enter Category:")
    notes=input("Enter notes(Optional):")

    conn = get_connection()
    cursor = conn.cursor()

