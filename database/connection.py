import sys
import mysql.connector as connector
import random


config = {
    'user': 'root',
    'passwd': 'msi1324',
    'host': 'localhost',
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

def getDataByDateAndInput(begin_date, end_date, column_filter, input_data):
    conn = dbConnection()
    cursor = conn.cursor(buffered=True)
    
    if(begin_date == end_date):
        tuple = (begin_date, "%" + input_data + "%")

        if(column_filter==2):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE DATE(Fecha)=%s AND Secadora LIKE %s; """
        if(column_filter==3):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE DATE(Fecha)=%s AND Temperatura LIKE %s; """
        if(column_filter==4):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE DATE(Fecha)=%s AND Temperatura2 LIKE %s; """
        if(column_filter==5):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE DATE(Fecha)=%s AND Humedad LIKE %s; """
        if(column_filter==6):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE DATE(Fecha)=%s AND Operador LIKE %s; """
        if(column_filter==7):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE DATE(Fecha)=%s AND Variedad LIKE %s; """
        if(column_filter==8):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE DATE(Fecha)=%s AND Batch LIKE %s; """
    else:
        tuple = (begin_date, end_date, "%" + input_data + "%")

        if(column_filter==2):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s AND Secadora LIKE %s; """
        if(column_filter==3):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s AND Temperatura LIKE %s; """
        if(column_filter==4):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s AND Temperatura2 LIKE %s; """
        if(column_filter==5):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s AND Humedad LIKE %s; """
        if(column_filter==6):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s AND Operador LIKE %s; """
        if(column_filter==7):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s AND Variedad LIKE %s; """
        if(column_filter==8):
            query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s AND Batch LIKE %s; """        
        
    time_format = f = '%Y-%m-%d %H:%M:%S'
    data = []
    
    try:
        print(tuple)
        print(query)
        cursor.execute(query, tuple)

        response = cursor.fetchall()
        print(response)

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
        return "Error getDataByDateAndInput"
    finally:
        cursor.close()
        conn.close()

def getDataBetweenDate(begin_date, end_date):
    conn = dbConnection()
    cursor = conn.cursor(buffered=True)

    time_format = f = '%Y-%m-%d %H:%M:%S'
    data = []
    query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Fecha BETWEEN %s AND %s; """
    tuple = (begin_date, end_date)

    try:
        cursor.execute(query, tuple)
        response = cursor.fetchall()
        print(response)

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
        return "Error getDataBetweenDate"
    finally:
        cursor.close()
        conn.close()


def getDataByInput(column_filter, input_data):
    conn = dbConnection()
    cursor = conn.cursor(buffered=True)

    if(column_filter==2):
        query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Secadora LIKE %s; """
    if(column_filter==3):
        query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Temperatura LIKE %s; """
    if(column_filter==4):
        query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Temperatura2 LIKE %s; """
    if(column_filter==5):
        query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Humedad LIKE %s; """
    if(column_filter==6):
        query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Operador LIKE %s; """
    if(column_filter==7):
        query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Variedad LIKE %s; """
    if(column_filter==8):
        query = """SELECT id, Fecha, Secadora, Temperatura, Temperatura2, Humedad, Operador, Variedad, Batch FROM temperaturas WHERE Batch LIKE %s; """        
    
    
    time_format = f = '%Y-%m-%d %H:%M:%S'
    data = []
    tuple = ("%" + input_data + "%",)
    try:
        cursor.execute(query, tuple)
        response = cursor.fetchall()
        print(response)

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
        return "Error getDataByInput"
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
        elif(item['secadora'] == "FARM 6"):
            temp_random = random.uniform(float(item['temperatura'])-2, float(item['temperatura'])+2)
            updateQuery = f'UPDATE temperaturas SET Temperatura2={temp_random} WHERE id={item["id"]} AND Secadora="{item["secadora"]}"'
            cursor.execute(updateQuery)

    conn.commit()

    cursor.close()
    conn.close()

# hardcodearTemperaturas()