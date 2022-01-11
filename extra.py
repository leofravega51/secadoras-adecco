"""Codigo extra para agregar a main.py, por cada vez que convirtamos main.ui a main.py"""


from database.connection import getData
from functions import insertInDataTable
"""Obtenemos los datos de la BD y los mostramos en la tabla de la app"""
    data = getData()
    insertInDataTable(self.dataTable, data)
    beginDate = getDate(self.beginDateEdit)
