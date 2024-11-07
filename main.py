import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from PyQt6.QtWidgets import QLineEdit, QTextEdit

from ui import Ui_MainWindow

from controler import buscar_prestamos_vencidos

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.libros_tabla.setColumnWidth(0, 175)
        self.ui.libros_tabla.setColumnWidth(1, 150)
        self.ui.libros_tabla.setColumnWidth(2, 100)
        self.ui.libros_tabla.setColumnWidth(3, 150)
        self.ui.libros_tabla.setColumnWidth(4, 150)
        self.ui.libros_tabla.setColumnWidth(5, 150)
    


    def on_libros_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_autor_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_usuarios_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_reportes_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

        filas = buscar_prestamos_vencidos()
        self.ui.tableWidget.setRowCount(len(filas))
        for i, fila in enumerate(filas):
            for j, dato in enumerate(fila):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(dato)))
    def on_regUsuario_btn_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
    def on_volverReg_btn_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        for widget in self.ui.stackedWidget_2.widget(0).findChildren((QLineEdit, QTextEdit)):
            widget.clear()





    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
