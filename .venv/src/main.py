# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ProductManager_ui import Ui_MainWindow 
from ButtonLogic import ButtonLogic

class ProductManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Product Manager")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductManagerApp()
    window.show()
    sys.exit(app.exec())
