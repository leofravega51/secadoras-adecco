import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QFont, QTextDocument
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QMessageBox, QPushButton
from database.connection import getData, getDataByDateAndInput
from functions import insertInDataTable, getDate, getFilterText, setColumnFilter, setBeginDate, setEndDate, drawChart, setChartDate, setChartInput, getTemperatures, exportToExcel, enableExportButton
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QDateTimeAxis
from PyQt5.QtCore import QPointF, Qt, QByteArray, QTextCodec
import datetime
from chart import Chart
from printer import Printer


class Weather(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/main.ui", self)

        self.data = getData()
        self.exportData = None
        self.input_data = None
        self.column_filter = None
        self.begin_date = None
        self.end_date = None
        self.chart_date = None
        self.chart_input = None
        self.temperaturas = None
        self.form_data = None
        self.documento = QTextDocument()


        """Obtenemos los datos de la BD y los mostramos en la tabla de la app"""
        insertInDataTable(self)
        beginDate = getDate(self.beginDateEdit)

        """Obtenemos el indice del select elegido (Operador, Secadora, Temp, etc.) y lo almacenamos"""
        self.columnFilterBox.currentIndexChanged.connect(
            lambda id: setColumnFilter(self, id))

        """Obtenemos el valor del input, lo guardamos y filtramos la tabla"""
        self.lineEdit.textChanged.connect(
            lambda text: getFilterText(self, text))

        """Obtenemos las fechas extremo para nuestro filtro por fechas y las guardamos. Luego filtramos"""
        self.beginDateEdit.dateChanged.connect(
            lambda date: setBeginDate(self, date))
        self.endDateEdit.dateChanged.connect(
            lambda date: setEndDate(self, date))

        """Seteamos los valores de la fecha y secadora ingresados para el grafico"""
        self.chartDate.dateChanged.connect(
            lambda date: setChartDate(self, date))
        self.chartComboBox.currentTextChanged.connect(
            lambda text: setChartInput(self, text))

        """Creamos un grafico de tendencias y lo mostramos"""
        self.drawChartButton.clicked.connect(lambda x: drawChart(self))


        """Evaluamos habilitar el boton de "Exportar a Excel" cada vez que se setea una fecha, campo a filtrar o dato"""
        self.beginDateEdit.dateChanged.connect(lambda x: enableExportButton(self))
        self.endDateEdit.dateChanged.connect(lambda x: enableExportButton(self))
        self.columnFilterBox.currentIndexChanged.connect(lambda x: enableExportButton(self))
        self.lineEdit.textChanged.connect(lambda x: enableExportButton(self))

        """Creamos el boton para exportar los registros entre las fechas previamente definidas, a Excel"""
        self.exportToExcelButton.clicked.connect(lambda x: exportToExcel(self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Weather()
    win.show()
    sys.exit(app.exec_())
