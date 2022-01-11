from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from tkinter import messagebox
import sys
import mysql.connector as connector
import datetime
import json


config = {
    'user': 'root',
    'passwd': 'msi1324',
    'host': 'localhost',
    'database': 'registro_temp',
    
}

def dbConnection():
    db = None
    try:
        db = connector.connect(**config)
        print(f'Conexion con la BD realizada con exito!')
    except connector.Error as err:
        print(f'Error en la conexion con la BD. Error: {err}')
        sys.exit(1)
    return db

def getData():
    conn = dbConnection()
    cursor = conn.cursor(buffered=True)
    query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas"""
    time_format = f = '%Y-%m-%d %H:%M:%S'
    data = []

    try:
        cursor.execute(query)
        response = cursor.fetchall()

        for item in response:
            identif = item[0]
            format_time = item[1].strftime(time_format)
            secadora = item[2]
            temp = item[3]
            temp2 = item[4]
            humedad = item[5]
            operador = item[6]
            variedad = item[7]
            batch = item[8]
            
            json_line = {
                'id': identif,
                'fecha': format_time,
                'secadora': secadora,
                'temperatura': temp,
                'temperatura2': temp2,
                'humedad': humedad,
                'operador': operador,
                'variedad': variedad,
                'batch': batch
            }

            data.append(json_line)
        return data
    except:
        return "Error"
    finally:
        cursor.close()
        conn.close()