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
        book_author = self.comboBox_3.CurrentText()
        book_publisher = self.comboBox_4.CurrentText()
        book_catagory = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_4.text()
        book_description = self.plainTextEdit.text()

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

    def Add_Author(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        author_name = self.lineEdit_20.text()

        self.cur.execute(''' INSERT INTO authors (author_name) VALUES (%s) ''' , (author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')

    def Add_Publisher(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        publisher_name = self.lineEdit_21.text()

        self.cur.execute(''' INSERT INTO publisher (publisher_name) VALUES (%s) ''' , (publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added')


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()