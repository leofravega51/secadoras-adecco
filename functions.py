from PyQt5 import QtWidgets, QtGui, QtCore
from database.connection import getDataByDateAndInput, getDataBetweenDate, getDataByInput
import datetime
from chart import Chart
from tkinter import messagebox
import pandas as pd


def insertInDataTable(self):

    for item in self.data:
        rowPosition = self.dataTable.rowCount()
        columnCount = self.dataTable.columnCount()
        self.dataTable.insertRow(rowPosition)

        self.dataTable.setItem(
            rowPosition, 0, QtWidgets.QTableWidgetItem(str(item['id'])))
        self.dataTable.setItem(
            rowPosition, 1, QtWidgets.QTableWidgetItem(str(item['fecha'])))
        self.dataTable.setItem(
            rowPosition, 2, QtWidgets.QTableWidgetItem(str(item['secadora'])))
        self.dataTable.setItem(
            rowPosition, 3, QtWidgets.QTableWidgetItem(str(item['temperatura'])))
        self.dataTable.setItem(
            rowPosition, 4, QtWidgets.QTableWidgetItem(str(item['temperatura2'])))
        self.dataTable.setItem(
            rowPosition, 5, QtWidgets.QTableWidgetItem(str(item['humedad'])))
        self.dataTable.setItem(
            rowPosition, 6, QtWidgets.QTableWidgetItem(str(item['operador'])))
        self.dataTable.setItem(
            rowPosition, 7, QtWidgets.QTableWidgetItem(str(item['variedad'])))
        self.dataTable.setItem(
            rowPosition, 8, QtWidgets.QTableWidgetItem(str(item['batch'])))
        
        if(float(item["temperatura"]) < 30):
            setColorToRow(self.dataTable, rowPosition, columnCount, QtGui.QColor(135,206,235))
        elif(float(item["temperatura"]) >= 30 and float(item["temperatura"]) < 60):
            setColorToRow(self.dataTable, rowPosition, columnCount, QtGui.QColor(180,255,159))
        else:
            setColorToRow(self.dataTable, rowPosition, columnCount, QtGui.QColor(218,18,18))
        
def setColorToRow(dataTable, rowPosition, columnCount, color):
    for col in range(columnCount):
        dataTable.item(rowPosition, col).setBackground(color)


def getDate(dateEdit):
    date = dateEdit.date().toPyDate()
    return date


def setColumnFilter(self, id):
    self.column_filter = id+1
    return self.column_filter


def setBeginDate(self, date):
    self.begin_date = date.toPyDate().strftime(f'%Y-%m-%d')
    return self.begin_date


def setEndDate(self, date):
    self.end_date = date.toPyDate().strftime(f'%Y-%m-%d')

    return self.end_date


def setChartDate(self, date):
    self.chart_date = date.toPyDate().strftime(f'%Y-%m-%d')
    return self.chart_date


def setChartInput(self, text):
    self.chart_input = text

    """Obtenemos los datos de temperaturas basados en la secadora seleccionada."""
    getTemperatures(self)
    return self.chart_input


def getFilterText(self, text):
    self.input_data = text

    return self.input_data


def filterTable(self):
    """Filtramos la tabla segun las opciones cargadas para filtrar (entre fechas, entre fechas y segun una columna, segun una columna)"""

    if(self.begin_date != None and self.end_date != None and self.begin_date <= self.end_date):
        if(self.column_filter != None and self.input_data != None):
            sortByDatesAndInput(self)
        else:
            sortByDates(self.dataTable, 1, self.begin_date, self.end_date)
    else:
        if(self.column_filter != None and self.input_data != None):
            self.form_data = sortByInput(
                self.dataTable, self.column_filter, self.input_data)


def sortByDatesAndInput(self):
    
    for rowIndex in range(self.dataTable.rowCount()):
        twItem = self.dataTable.item(rowIndex, 1)
        inputItem = self.dataTable.item(rowIndex, self.column_filter)

        sp1 = twItem.text().split(" ")
        date = sp1[0].split("-")
        itemDate = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

        splitBeginDate = self.begin_date.split("-")
        splitEndDate = self.end_date.split("-")
        by, bm, bd = int(splitBeginDate[0]), int(
            splitBeginDate[1]), int(splitBeginDate[2])
        ey, em, ed = int(splitEndDate[0]), int(
            splitEndDate[1]), int(splitEndDate[2])
        bDate = datetime.datetime(by, bm, bd)
        eDate = datetime.datetime(ey, em, ed)


        if bDate == eDate and bDate == itemDate and str.startswith(str(inputItem.text()), str(self.input_data)):
            self.dataTable.setRowHidden(rowIndex, False)
        elif itemDate >= bDate and itemDate <= eDate and str.startswith(str(inputItem.text()), str(self.input_data)):
            self.dataTable.setRowHidden(rowIndex, False)
        else:
            self.dataTable.setRowHidden(rowIndex, True)


def sortByDates(dataTable, columnOfInterest, beginDate, endDate):
    """Filtrado de datos en tabla dado por 2 fechas extremo"""

    for rowIndex in range(dataTable.rowCount()):
        twItem = dataTable.item(rowIndex, columnOfInterest)
        sp1 = twItem.text().split(" ")
        date = sp1[0].split("-")
        itemDate = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

        splitBeginDate = beginDate.split("-")
        splitEndDate = endDate.split("-")
        by, bm, bd = int(splitBeginDate[0]), int(
            splitBeginDate[1]), int(splitBeginDate[2])
        ey, em, ed = int(splitEndDate[0]), int(
            splitEndDate[1]), int(splitEndDate[2])
        bDate = datetime.datetime(by, bm, bd)
        eDate = datetime.datetime(ey, em, ed)

        if bDate == eDate and bDate == itemDate:
            dataTable.setRowHidden(rowIndex, False)
        elif itemDate >= bDate and itemDate <= eDate:
            dataTable.setRowHidden(rowIndex, False)
        else:
            dataTable.setRowHidden(rowIndex, True)


def sortByInput(dataTable, columnOfInterest, valueOfInterest):
    """valueOfInteres: hace referencia al valor ingresado para buscar en la tabla
       columnOfInterest: hace referencia a la columna en la cual queremos buscar el valor, la obtenemos
        desde el select

        Este algoritmo se encarga de "esconder" todas las filas que no coincidan con la busqueda.
    """
    form_data = []
    for rowIndex in range(dataTable.rowCount()):
        twItem = dataTable.item(rowIndex, columnOfInterest)

        if str.startswith(str(twItem.text()), str(valueOfInterest)):
            dataTable.setRowHidden(rowIndex, False)
            # form_data += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % twItem[0]
            # form_data.append(QTreeWidgetItem((str(twItem[0]), str(twItem[1]), str(twItem[2]), str(twItem[3]), str(twItem[4]), str(twItem[5]), str(twItem[6]), str(twItem[7]), str(twItem[8]))))
        else:
            dataTable.setRowHidden(rowIndex, True)

    return form_data


def clearFilterTable(self):
    """Limpiamos los filtros realizados previamente"""

    for rowIndex in range(self.dataTable.rowCount()):
        self.dataTable.setRowHidden(rowIndex, False)

def setMinTemp(self, min):
    self.temp_min = min

def setMaxTemp(self, max):
    self.temp_max = max

def drawChart(self):
    if(self.chart_input and self.chart_date and self.chart_input != "Secadora"):
        self.chart = Chart(
            self.chart_input, self.chart_date, self.temperaturas, self.temp_min, self.temp_max)
        self.chart.resize(1280, 700)
        self.chart.show()
    else:
        messagebox.showinfo(
            message="Error! La fecha y/o secadora no fueron cargadas", title="Gráfico de tendencias")


def getTemperatures(self):
    """Obtenemos las temperaturas de la secadora seleccionada previamente y las almacenamos en formato array"""
    array = []
    for item in self.data:
        if(self.chart_input == item['secadora']):
            array.append(float(item['temperatura']))
    self.temperaturas = array


def exportToExcel(self):
    columnHeaders = ["Id", "Fecha", "Secadora", "Temperatura",
                     "Temperatura 2", "Humedad", "Operador", "Variedad", "Batch"]
    jsonHeaders = ["id", "fecha", "secadora", "temperatura",
                   "temperatura2", "humedad", "operador", "variedad", "batch"]

    if(self.begin_date and self.end_date):
        if(self.column_filter and self.input_data):
            print("Buscando datos entre fechas e input")
            self.exportData = getDataByDateAndInput(
                self.begin_date, self.end_date, self.column_filter, self.input_data)
        else:
            print("Buscando datos entre fechas")
            self.exportData = getDataBetweenDate(
                self.begin_date, self.end_date)
    else:
        if(self.column_filter and self.input_data):
            print("Buscando datos por input")
            self.exportData = getDataByInput(
                self.column_filter, self.input_data)

    # create column header list
    # for j in range(self.dataTable.model().columnCount()):
    #     columnHeaders.append(self.dataTable.horizontalHeaderItem(j).text())

    df = pd.DataFrame(columns=columnHeaders)

    fecha = str(datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S"))

    # create dataframe object recordset
    for row in range(len(self.exportData)):
        for col in range(len(columnHeaders)):
            df.at[row, columnHeaders[col]
                  ] = self.exportData[row][jsonHeaders[col]]

    df.to_excel('Registro ' + fecha + '.xlsx', index=False)
    print('Excel file exported')

    self.begin_date = None
    self.end_date = None


def enableButton(self, button):
    """Habilitamos el boton de Exportar a Excel luego de evaluar que se haya registrado una fecha rango o un filtro por columna"""

    if((self.begin_date and self.end_date) or (self.column_filter and self.input_data) or (self.begin_date and self.end_date and self.column_filter and self.input_data)):
        button.setEnabled(True)
    else:
        button.setEnabled(False)


