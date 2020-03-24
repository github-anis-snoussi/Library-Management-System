from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import MySQLdb


ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()
        self.Show_Catagory()
        self.Show_Publisher()
        self.Show_Author()
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.Show_Ctagory_ComboBox()
        self.Show_Author_ComboBox()
        self.Show_Publisher_ComboBox()

    def Handle_UI_Changes(self):
        self.Hide_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hide_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_4.clicked.connect(self.Open_Users_Tab)
        self.pushButton_3.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)

        self.pushButton_14.clicked.connect(self.Add_Catagory)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hide_Themes(self):
        self.groupBox_3.hide()

    #################################################
    ################# Changing Pages ################

    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    #################################################
    #################### Books ######################

    def Add_New_Book(self):

        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_3.text()
        book_code = self.lineEdit_2.text()
        book_price = self.lineEdit_4.text()
        book_author = self.comboBox_3.currentIndex()
        book_publisher = self.comboBox_4.currentIndex()
        book_catagory = self.comboBox_5.currentIndex()
        book_description = self.textEdit_2.toPlainText()

        self.cur.execute(''' INSERT INTO book(book_name , book_description , book_code , book_catagory , book_author , book_publisher , book_price) VALUES (%s , %s , %s , %s , %s , %s , %s)''',(book_title , book_description , book_code , book_catagory , book_author , book_publisher , book_price))
        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        book_title = self.lineEdit_3.setText('')
        book_code = self.lineEdit_2.setText('')
        book_price = self.lineEdit_4.setText('')
        book_description = self.textEdit_2.setPlainText('')
        book_author = self.comboBox_3.setCurrentIndex(0)
        book_publisher = self.comboBox_4.setCurrentIndex(0)
        book_catagory = self.comboBox_5.setCurrentIndex(0)

    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass
    
    def Delete_Books(self):
        pass

    #################################################
    #################### Users ######################

    def Add_New_User(self):
        pass

    def Login(self):
        pass

    def Edit_User(self):
        pass

    #################################################
    #################### Settings ###################
    def Add_Catagory(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        catagory_name = self.lineEdit_19.text()

        self.cur.execute(''' INSERT INTO catagory (catagory_name) VALUES (%s) ''' , (catagory_name,))

        self.db.commit()
        self.statusBar().showMessage('New Catagory Added')
        self.lineEdit_19.setText('')
        self.Show_Catagory()
        self.Show_Ctagory_ComboBox()

    def Show_Catagory(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT catagory_name FROM catagory ''')
        data = self.cur.fetchall()
        if data :
            self.tableWidget_2.setRowCount(0)
            rows = 0
            for row , form in enumerate(data):
                self.tableWidget_2.insertRow(rows)
                for column , item in enumerate(form):
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1
                rows = self.tableWidget_2.rowCount()

    def Add_Author(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        author_name = self.lineEdit_20.text()

        self.cur.execute(''' INSERT INTO authors (author_name) VALUES (%s) ''' , (author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')
        self.lineEdit_20.setText('')
        self.Show_Author()
        self.Show_Author_ComboBox()

    def Show_Author(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT author_name FROM authors ''')
        data = self.cur.fetchall()
        if data :
            self.tableWidget_3.setRowCount(0)
            rows = 0
            for row , form in enumerate(data):
                self.tableWidget_3.insertRow(rows)
                for column , item in enumerate(form):
                    self.tableWidget_3.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1
                rows = self.tableWidget_3.rowCount()

    def Add_Publisher(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        publisher_name = self.lineEdit_21.text()

        self.cur.execute(''' INSERT INTO publisher (publisher_name) VALUES (%s) ''' , (publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added')
        self.lineEdit_21.setText('')
        self.Show_Publisher()
        self.Show_Publisher_ComboBox()

    def Show_Publisher(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()
        if data :
            self.tableWidget_4.setRowCount(0)
            rows = 0
            for row , form in enumerate(data):
                self.tableWidget_4.insertRow(rows)
                for column , item in enumerate(form):
                    self.tableWidget_4.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1
                rows = self.tableWidget_4.rowCount()

    #################################################
    ############# Add Data to ComboBoxes ############

    def Show_Ctagory_ComboBox(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT catagory_name FROM catagory ''')
        data = self.cur.fetchall()
        self.comboBox_5.clear()
        self.comboBox_8.clear()
        for catagory in data:
            self.comboBox_5.addItem(catagory[0])
            self.comboBox_8.addItem(catagory[0])

    def Show_Author_ComboBox(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors ''')
        data = self.cur.fetchall()
        self.comboBox_6.clear()
        self.comboBox_3.clear()
        for catagory in data:
            self.comboBox_6.addItem(catagory[0])
            self.comboBox_3.addItem(catagory[0])

    def Show_Publisher_ComboBox(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()
        self.comboBox_4.clear()
        self.comboBox_7.clear()
        for catagory in data:
            self.comboBox_4.addItem(catagory[0])
            self.comboBox_7.addItem(catagory[0])


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    window.setFixedSize(window.size())
    app.exec_()

if __name__ == '__main__':
    main()