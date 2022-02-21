from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from tkinter import messagebox
import sys
import mysql.connector as connector
import datetime
import json
import random


config = {
    'user': 'root',
    'passwd': 'msi1324',
    'host': '192.168.0.181',
    'port': '3306',
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

def hardcodearTemperaturas():

    data = getData()
    conn = dbConnection()
    cursor = conn.cursor(buffered=True)

    for item in data:
        if(item['secadora'] == "AGRIMAQ 3"):
            temp_random = random.uniform(float(item['temperatura'])-2, float(item['temperatura'])+2)
            updateQuery = f'UPDATE temperaturas SET Temperatura2={temp_random} WHERE id={item["id"]} AND Secadora="{item["secadora"]}"'
            cursor.execute(updateQuery)
        elif(item['secadora'] == "KW 325"):
            temp_random = random.uniform(float(item['temperatura'])-2, float(item['temperatura'])+2)
            updateQuery = f'UPDATE temperaturas SET Temperatura2={temp_random} WHERE id={item["id"]} AND Secadora="{item["secadora"]}"'
            cursor.execute(updateQuery)
        elif(item['secadora'] == "FARM 7"):
            temp_random = random.uniform(float(item['temperatura'])-2, float(item['temperatura'])+2)
            updateQuery = f'UPDATE temperaturas SET Temperatura2={temp_random} WHERE id={item["id"]} AND Secadora="{item["secadora"]}"'
            cursor.execute(updateQuery)
        elif(item['secadora'] == "FARM 9"):
            temp_random = random.uniform(float(item['temperatura'])-2, float(item['temperatura'])+2)
            updateQuery = f'UPDATE temperaturas SET Temperatura2={temp_random} WHERE id={item["id"]} AND Secadora="{item["secadora"]}"'
            cursor.execute(updateQuery)

    conn.commit()

    cursor.close()
    conn.close()

# hardcodearTemperaturas()