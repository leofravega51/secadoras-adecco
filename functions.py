import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from database.connection import getData
import datetime
from chart import Chart
from tkinter import messagebox


def insertInDataTable(self):

    for item in self.data:
        rowPosition = self.dataTable.rowCount()
        self.dataTable.insertRow(rowPosition)

        self.dataTable.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(item['id'])))
        self.dataTable.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(item['fecha'])))
        self.dataTable.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(item['secadora'])))
        self.dataTable.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(str(item['temperatura'])))
        self.dataTable.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(item['temperatura2'])))
        self.dataTable.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(str(item['humedad'])))
        self.dataTable.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(str(item['operador'])))
        self.dataTable.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(str(item['variedad'])))
        self.dataTable.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(str(item['batch'])))

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
    if(self.begin_date != None and self.begin_date <= self.end_date):
        sortByDates(self.dataTable, 1, self.begin_date, self.end_date)
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
    if(self.column_filter != None):
        sortByInput(self.dataTable, self.column_filter, self.input_data)
    
def sortByDates(dataTable, columnOfInterest, beginDate, endDate):
    """"""

    for rowIndex in range(dataTable.rowCount()):
        twItem = dataTable.item(rowIndex, columnOfInterest)
        sp1 = twItem.text().split(" ")
        date = sp1[0].split("-")
        itemDate = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

        splitBeginDate  = beginDate.split("-")
        splitEndDate = endDate.split("-")
        by,bm,bd = int(splitBeginDate[0]), int(splitBeginDate[1]), int(splitBeginDate[2])
        ey,em,ed = int(splitEndDate[0]), int(splitEndDate[1]), int(splitEndDate[2])
        bDate = datetime.datetime(by,bm,bd)
        eDate = datetime.datetime(ey,em,ed)


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
    """
    for rowIndex in range(dataTable.rowCount()):
        twItem = dataTable.item(rowIndex, columnOfInterest)
        if str.startswith(str(twItem.text()), str(valueOfInterest)):
            dataTable.setRowHidden(rowIndex, False)
        else:
            dataTable.setRowHidden(rowIndex, True)
    

def drawChart(self):
    if(self.chart_input and self.chart_date and self.chart_input != "Secadora"):
        self.chart = Chart(self.chart_input, self.chart_date, self.temperaturas)
        self.chart.resize(1280, 700)
        self.chart.show()
    else:
        messagebox.showinfo(message="Error! La fecha y/o secadora no fueron cargadas", title="Gráfico de tendencias")

def getTemperatures(self):
    """Obtenemos las temperaturas de la secadora seleccionada previamente y las almacenamos en formato array"""
    array = []
    for item in self.data:
        if(self.chart_input == item['secadora']):
            array.append(float(item['temperatura']))
    self.temperaturas = array