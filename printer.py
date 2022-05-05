from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
from PyQt5.QtGui import QStandardItemModel
from database.connection import getData


class Printer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.model = QStandardItemModel()
        self.table = QtWidgets.QTableWidget(self)
        self.data = getData()

        headers = ["ID", "Fecha", "Secadora", "Temperatura",
            "Temperatura 2", "Humedad", "Operador", "Variedad", "Batch"]

        self.model.setHorizontalHeaderLabels(headers)

        for item in self.data:
            rowPosition = self.table.rowCount()
            self.table.insertRow(rowPosition)

            self.table.setItem(
                rowPosition, 0, QtWidgets.QTableWidgetItem(str(item['id'])))
            self.table.setItem(
                rowPosition, 1, QtWidgets.QTableWidgetItem(str(item['fecha'])))
            self.table.setItem(
                rowPosition, 2, QtWidgets.QTableWidgetItem(str(item['secadora'])))
            self.table.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(
                str(item['temperatura'])))
            self.table.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(
                str(item['temperatura2'])))
            self.table.setItem(
                rowPosition, 5, QtWidgets.QTableWidgetItem(str(item['humedad'])))
            self.table.setItem(
                rowPosition, 6, QtWidgets.QTableWidgetItem(str(item['operador'])))
            self.table.setItem(
                rowPosition, 7, QtWidgets.QTableWidgetItem(str(item['variedad'])))
            self.table.setItem(
                rowPosition, 8, QtWidgets.QTableWidgetItem(str(item['batch'])))

        self.table.setHorizontalHeaderLabels(headers)
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        print(self.table.rowCount(), self.table.columnCount())
        table = cursor.insertTable(
            self.table.rowCount(), self.table.columnCount())
        
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.table.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Printer()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())