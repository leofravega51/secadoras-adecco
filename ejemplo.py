from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from database.connection import getData
import datetime
import sys


class Chart(QWidget):
    def __init__(self, secadora, fecha, temperaturas):
        super().__init__()
        self.secadora = secadora
        self.fecha = fecha
        self.temperaturas = temperaturas
        self.data = getData()
