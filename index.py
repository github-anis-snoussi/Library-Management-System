from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import datetime
import MySQLdb


ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()
        self.Dark_Theme()

        self.Show_Catagory()
        self.Show_Publisher()
        self.Show_Author()
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.Show_Ctagory_ComboBox()
        self.Show_Author_ComboBox()
        self.Show_Publisher_ComboBox()
        self.Show_Operations()

    def Handle_UI_Changes(self):
        self.Hide_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_36.clicked.connect(self.Hide_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_4.clicked.connect(self.Open_Users_Tab)
        self.pushButton_3.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_9.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)
        self.pushButton_10.clicked.connect(self.Delete_Books)

        self.pushButton_14.clicked.connect(self.Add_Catagory)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_12.clicked.connect(self.Login)
        self.pushButton_13.clicked.connect(self.Edit_User)

        self.pushButton_32.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_33.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_35.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_34.clicked.connect(self.Dark_Theme)
        self.pushButton_6.clicked.connect(self.Handle_Day_Operations)

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
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        book_title = self.lineEdit_8.text()

        sql = ''' SELECT * FROM book WHERE book_name = %s '''
        self.cur.execute(sql , [(book_title)])
        data = self.cur.fetchone()
        self.lineEdit_6.setText(data[1])
        self.textEdit.setPlainText(data[2])
        self.lineEdit_5.setText(data[3])
        self.comboBox_8.setCurrentIndex(data[4])
        self.comboBox_6.setCurrentIndex(data[5])
        self.comboBox_7.setCurrentIndex(data[6])
        self.lineEdit_7.setText(str(data[7]))


    def Edit_Books(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_6.text()
        book_code = self.lineEdit_5.text()
        book_price = self.lineEdit_7.text()
        book_author = self.comboBox_6.currentIndex()
        book_publisher = self.comboBox_7.currentIndex()
        book_catagory = self.comboBox_8.currentIndex()
        book_description = self.textEdit.toPlainText()

        search_book_title = self.lineEdit_8.text()
        self.cur.execute('''
            UPDATE book SET book_name = %s , book_description = %s, book_code = %s, book_catagory =%s, book_author =%s, book_publisher =%s, book_price = %s WHERE book_name = %s
        ''', (book_title , book_description, book_code , book_catagory , book_author , book_publisher , book_price , search_book_title))
        self.db.commit()
        self.statusBar().showMessage('Book Updated')


    
    def Delete_Books(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        book_title = self.lineEdit_8.text()
        warning = QMessageBox.warning(self , 'Delete Book' , 'Are you sure you want to delete ?' , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes : 
            self.cur.execute('''DELETE FROM book WHERE book_name = %s''', [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

    #################################################
    #################### Users ######################

    def Add_New_User(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        confirm_password = self.lineEdit_12.text()

        if password == confirm_password :
            self.cur.execute(''' INSERT INTO users(user_name , user_email , user_password) VALUES (%s , %s , %s) ''',(username , email , password))
            self.db.commit()
            self.statusBar().showMessage("New User Added")
        else : 
            self.label_30.setText("passwords don't match")

    def Login(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        username = self.lineEdit_13.text()
        password = self.lineEdit_14.text()

        sql = ''' SELECT * FROM users '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data : 
            if username == row[1] and password == row[3] :
                self.statusBar().showMessage("You can start editing...")
                self.groupBox_4.setEnabled(True)
                self.lineEdit_15.setText(row[1])
                self.lineEdit_17.setText(row[2])




    def Edit_User(self):
        old_username = self.lineEdit_13.text()
        username = self.lineEdit_15.text()
        email = self.lineEdit_17.text()
        password = self.lineEdit_18.text()
        confirm_password = self.lineEdit_16.text()

        if password == confirm_password :
            self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
            self.cur = self.db.cursor()
            self.cur.execute(''' UPDATE users SET user_name = %s , user_email = %s , user_password = %s WHERE user_name = %s ''' , (username , email , password , old_username))
            self.db.commit()
            self.statusBar().showMessage("User Updated.")
        else :
            self.statusBar().showMessage("Passwords don't match")

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

    #################################################
    ################### UI Themes ###################

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Theme(self):
        style = open('themes/dark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    #################################################
    ################ Day Operations #################

    def Handle_Day_Operations(self):
        book_title = self.lineEdit.text()
        op_type = self.comboBox.currentText()
        op_days = self.comboBox_2.currentIndex() +1
        date = str(datetime.date.today())
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        self.cur.execute(''' INSERT INTO dayoperations(book_name , type , days ,date) VALUES (%s , %s , %s , %s) ''' ,(book_title , op_type, op_days , date) )
        self.db.commit()
        self.statusBar().showMessage("Operation Added")
        self.Show_Operations()

    def Show_Operations(self):
        self.db = MySQLdb.connect( host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT book_name , type , days , date FROM dayoperations ''')
        data = self.cur.fetchall()

        if data :
            self.tableWidget.setRowCount(0)
            rows = 0
            for row , form in enumerate(data):
                self.tableWidget.insertRow(rows)
                for column , item in enumerate(form):
                    self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1
                rows = self.tableWidget.rowCount()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    window.setFixedSize(window.size())
    app.exec_()

if __name__ == '__main__':
    main()