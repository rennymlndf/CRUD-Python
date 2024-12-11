from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem

class UI_Form(object):
    def SetupUI(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 428)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 111, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.idCategory = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.idCategory.setObjectName("idCategory")
        self.verticalLayout.addWidget(self.idCategory)
        self.categoryName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.categoryName.setObjectName("categoryName")
        self.verticalLayout.addWidget(self.categoryName)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 10, 261, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.idCategoryEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.idCategoryEdit.setObjectName("idCategoryEdit")
        self.verticalLayout_2.addWidget(self.idCategoryEdit)
        self.nameCategoryEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.nameCategoryEdit.setObjectName("nameCategoryEdit")
        self.verticalLayout_2.addWidget(self.nameCategoryEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 110, 381, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.insertButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.insertButton.setObjectName("insertButton")
        self.horizontalLayout.addWidget(self.insertButton)
        self.deleteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.updateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.loadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 150, 381, 16))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 170, 381, 181))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 370, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.insertButton.clicked.connect(self.insertkategori)
        self.loadButton.clicked.connect(self.loadkategori)
        self.updateButton.clicked.connect(self.updatekategori)
        self.deleteButton.clicked.connect(self.deletekategori)
        self.tableWidget.cellClicked.connect(self.getById)
        self.searchButton.clicked.connect(self.searchkategori)
        
    def insertkategori(self):
        try:
            mydb = mc.connect(
                host ="localhost",
                port="3306",
                user="root",
                password="root",
                database ="db_penjualan"
            )
            cursor = mydb.cursor()
            id_kategori = self.idCategoryEdit.text()
            nama_kategori= self.nameCategoryEdit.text()
            sql = "INSERT INTO kategori (id,name) VALUES (%s,%s)"
            val = (id_kategori, nama_kategori)
            cursor.execute(sql,val)
            mydb.commit()
            self.label.setText("Data Kategori Berhasil Disimpan")
            self.idCategoryEdit.setText("")
            self.nameCategoryEdit.setText("")
        except mc.Error as e:
            self.label.setText("Data Kategori Gagal Disimpan")
            
    def loadkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="root",
                database="db_penjualan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM kategori ORDER BY ID ASC")
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.label.setText("Data Kategori Berhasil Ditampilkan")
        except mc.Error as err:
            self.label.setText("Data Kategori Gagal DiLoad")
            
    def updatekategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="root",
                database="db_penjualan"
            )
            cursor = mydb.cursor()
            id_kategori = self.idCategoryEdit.text()
            nama_kategori = self.nameCategoryEdit.text()
            sql = "UPDATE kategori SET name = %s WHERE id = %s"
            val = (nama_kategori, id_kategori)
            cursor.execute(sql, val)
            mydb.commit()
            self.label.setText("Data Kategori Berhasil Diperbarui")
            self.idCategoryEdit.setText("")
            self.nameCategoryEdit.setText("")
        except mc.Error as e:
            self.label.setText("Data Kategori Gagal Diperbarui")
            
    def deletekategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="root",
                database="db_penjualan"
            )
            cursor = mydb.cursor()
            id_kategori = self.idCategoryEdit.text()
            sql = "DELETE FROM kategori WHERE id = %s"
            val = (id_kategori, )
            cursor.execute(sql, val)
            mydb.commit()
            self.label.setText("Data Kategori Berhasil Dihapus")
            self.idCategoryEdit.setText("")
            self.nameCategoryEdit.setText("")
        except mc.Error as e:
            self.label.setText("Data Kategori Gagal Dihapus")
            
    def getById(self, row, column):
        id_kategori = self.tableWidget.item(row, 0).text()
        namekat = self.tableWidget.item(row, 1).text()
        self.idCategoryEdit.setText(id_kategori)
        self.nameCategoryEdit.setText(namekat)
        
    def searchkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="root",
                database="db_penjualan"
            )
            mycursor = mydb.cursor()
            search_value = self.lineEdit.text()
            query = "SELECT * FROM kategori WHERE id LIKE %s OR name LIKE %s ORDER BY ID ASC"
            mycursor.execute(query, ('%' + search_value + '%', '%' + search_value + '%'))
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.label.setText("Data Kategori Berhasil Dicari")
        except mc.Error as err:
            self.label.setText("Data Kategori Gagal Dicari")
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.idCategory.setText(_translate("Form", "ID Kategori"))
        self.categoryName.setText(_translate("Form", "Nama Kategori"))
        self.insertButton.setText(_translate("Form", "INSERT"))
        self.deleteButton.setText(_translate("Form", "DELETE"))
        self.updateButton.setText(_translate("Form", "UPDATE"))
        self.loadButton.setText(_translate("Form", "LOAD DATA"))
        self.label.setText(_translate("Form", "Text Label"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name Kategori"))
        self.searchButton.setText(_translate("Form", "SEARCH"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UI_Form()
    ui.SetupUI(Form)
    Form.show()
    sys.exit(app.exec_())