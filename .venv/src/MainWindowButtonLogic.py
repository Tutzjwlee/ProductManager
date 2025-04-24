from PySide6.QtWidgets import QWidget, QTableWidgetItem
 
class ButtonLogic(QWidget):
    def __init__(self, tableWidget):
        super().__init__()
        self.tableWidget = tableWidget

    def on_add_product_clicked(self):
        print("Add Product button clicked")
        # Lógica para adicionar ou remover um produto
        # Exemplo: adicionar uma linha na tabela
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem("New Product"))

    def on_add_subtract_clicked(self):
        print("Add or Subtract Product button clicked")
        # Lógica para adicionar ou subtrair produtos
        pass

    def on_edit_product_clicked(self):
        print("Edit Product button clicked")
        # Lógica para editar o produtodef on_add_remove_clicked(self):
        print("Add or Remove Product button clicked")
        # Lógica para adicionar ou remover um produto
        # Exemplo: adicionar uma linha na tabela
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem("New Product"))

    def on_add_subtract_clicked(self):
        print("Add or Subtract Product button clicked")
        # Lógica para adicionar ou subtrair produtos
        pass

    def on_edit_product_clicked(self):
        print("Edit Product button clicked")
        # Lógica para editar o produto
        pass