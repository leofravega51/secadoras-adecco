from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from database.connection import getData
import datetime
import sys
import pyqtgraph as pg
import pyqtgraph.exporters

class Chart(QWidget):
 
    def __init__(self, secadora, fecha, temperaturas, temp_min, temp_max):
        super().__init__()
        self.secadora = secadora
        self.fecha = fecha
        self.temperaturas = temperaturas
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.data = getData()

        """Spliteamos la fecha obtenida del select en 'Grafico de tendencia' para poder pasarla a datetime y compararla"""
        aux = self.fecha.split("-")
        y,m,d = int(aux[0]),int(aux[1]),int(aux[2])

        series = QLineSeries(name="Temperatura")
        series2 = QLineSeries(name="Temperatura 2")
        if(self.temp_min and self.temp_max):
            series3 = QLineSeries(name="Temperatura minima")
            series4 = QLineSeries(name="Temperatura maxima")
            series3 << QPointF(float(0), float(self.temp_min)) << QPointF(float(200), float(self.temp_min))
            series4 << QPointF(float(0), float(self.temp_max)) << QPointF(float(200), float(self.temp_max))


        for item in self.data:
            """Spliteamos cada fecha obtenida de la base de datos para luego convertirla en datetime y poder compararla"""
            sp1 = item['fecha'].split(" ")
            date = sp1[0].split("-")
            hour = sp1[1].split(":")
            itemDate = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

            if(itemDate == datetime.datetime(y,m,d) and item['secadora'] == self.secadora):
                series.append(QDateTime.fromString(item['fecha'], "yyyy-MM-dd hh:mm:ss").toMSecsSinceEpoch(), float(item['temperatura']))
                series2.append(QDateTime.fromString(item['fecha'], "yyyy-MM-dd hh:mm:ss").toMSecsSinceEpoch(), float(item['temperatura2']))

        # Create Chart and set General Chart setting
        chart = QChart()
        chart.addSeries(series)
        chart.addSeries(series2)
        if(self.temp_min and self.temp_max):
            chart.addSeries(series3)
            chart.addSeries(series4)
        chart.setTitle(f'Registros de temperatura secadora {self.secadora}')
        chart.setAnimationOptions(QChart.SeriesAnimations)
        

        # X Axis Settings   
        axisX = QDateTimeAxis()
        axisX.setTickCount(24)
        axisX.setFormat("HH:mm") #https://doc.qt.io/qt-5/qdatetime.html#toString-2
        axisX.setTitleText(f'Fecha: {self.fecha}')
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Y Axis Settings
        axisY = QValueAxis()
        axisY.setLabelFormat("%i")
        axisY.setTitleText("Temperatura °C")
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)
        series2.attachAxis(axisY)
        if(self.temp_max and self.temp_min):
            series3.attachAxis(axisY)
            series4.attachAxis(axisY)
        
        
        # Create a QChartView object with QChart as a parameter. This way we don't need to create the QGraphicsView scene ourselves. We also set the Antialiasing on to have the rendered lines look nicer.
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        chart.axisY(series).setRange(min(self.temperaturas)-5, max(self.temperaturas)+5)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart.setGeometry(0, 100, 1280, 700)

        layout = QVBoxLayout()
        layout.addWidget(chartView)
        self.setLayout(layout)
        self.setWindowTitle("Gráfico de tendencias")


# app = QApplication(sys.argv)
# chart = Chart()
# chart.resize(1280, 480)
# chart.show()
# sys.exit(app.exec_())       

    

