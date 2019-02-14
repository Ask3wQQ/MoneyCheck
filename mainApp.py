from mainWindow import Ui_MainWindow
import insertData
import editData

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem

import sqlite3
from datetime import datetime

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.Initial_UI()

    def Initial_UI(self):
        self.setupUi(self)
        self.Load_Database()
        self.show()
        self.pushButton_3.clicked.connect(self.Show_Insert_Dialog)
        self.pushButton_2.clicked.connect(self.Show_Edit_Dialog)
        self.pushButton.clicked.connect(self.Delete_Data)

    def Delete_Data(self):
        content = 'SELECT DATE, TIME, ITEM, MONEY FROM account'
        res = conn.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                tDate = data[0]
                tTime = data[1]
                tItem = data[2]
                tMoney = data[3]
                curs.execute("DELETE FROM account WHERE DATE=? AND TIME=? AND ITEM=? AND MONEY=?", (tDate, tTime, tItem, tMoney))
                conn.commit()
                self.Load_Database()


    def Show_Edit_Dialog(self):
        self.editing = EditDialog()
        self.editing.pushButton.clicked.connect(self.Edit_Data)
        self.editing.pushButton_2.clicked.connect(self.Clear_Edit_Data)
        if self.tableWidget.currentRow() == -1:
            row = 0
        else:
            row = self.tableWidget.currentRow()
        if self.tableWidget.item(row, 3):
            money = self.tableWidget.item(row, 3).text()
            if money[0] == "-":
                money = money[1:]
            self.editing.lineEdit.setText(self.tableWidget.item(row, 2).text())
            self.editing.lineEdit_2.setText(money)
            self.editing.exec_()

    def Clear_Edit_Data(self):
        self.editing.lineEdit.clear()
        self.editing.lineEdit_2.clear()

    def Edit_Data(self):
        if self.tableWidget.currentRow() == -1:
            rowCurrent = 0;
        else:
            rowCurrent = self.tableWidget.currentRow()
        editDate = self.editing.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        nowDate = datetime.now().strftime("%Y-%m-%d")
        editTime = datetime.now().strftime("%H:%M:%S")
        if editDate != nowDate:
            editTime = "--:--:--"
        editItem = self.editing.lineEdit.text()
        editMoney = self.editing.lineEdit_2.text()
        if self.editing.radioButton.isChecked():
            editType = 1
        elif self.editing.radioButton_2.isChecked():
            editType = 0
            editMoney = "-" + editMoney
        content = 'SELECT DATE, TIME, TYPE, ITEM, MONEY FROM account'
        res = conn.execute(content)
        for row in enumerate(res):
            if row[0] == rowCurrent:
                data = row[1]
                tDate = data[0]
                tTime = data[1]
                tType = data[2]
                tItem = data[3]
                tMoney = data[4]
                curs.execute("UPDATE account set DATE=?, TIME=?, TYPE=?, ITEM=?, MONEY=? WHERE DATE=? AND TIME=? AND TYPE=? AND ITEM=? AND MONEY=?", (editDate, editTime, editType, editItem, editMoney, tDate, tTime, tType, tItem, tMoney))
                conn.commit()
                self.Load_Database()
        self.editing.close()

    def Show_Insert_Dialog(self):
        self.adding = InsertDialog()
        self.adding.pushButton.clicked.connect(self.Insert_Data)
        self.adding.pushButton_2.clicked.connect(self.Clear_Insert_Data)
        self.adding.exec_()

    def Clear_Insert_Data(self):
        self.adding.lineEdit.clear()
        self.adding.lineEdit_2.clear()

    def Insert_Data(self):
        addDate = self.adding.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        nowDate = datetime.now().strftime("%Y-%m-%d")
        addTime = datetime.now().strftime("%H:%M:%S")
        if addDate != nowDate:
            addTime = "--:--:--"
        addItem = self.adding.lineEdit.text()
        addMoney = self.adding.lineEdit_2.text()
        if self.adding.radioButton.isChecked():
            addType = 1
        elif self.adding.radioButton_2.isChecked():
            addType = 0
            addMoney = "-" + addMoney
        try:
            curs.execute("INSERT INTO account(DATE, TIME, TYPE, ITEM, MONEY) VALUES(?, ?, ?, ?, ?)", (addDate, addTime, str(addType), addItem, addMoney))
            conn.commit()
            print('DONE')
            self.adding.lineEdit.clear()
            self.adding.lineEdit_2.clear()
            self.Load_Database()
            self.adding.close()
        except Exception as error:
            print(error)

    def Load_Database(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        col_data = 0
        content = 'SELECT DATE, TIME, ITEM, MONEY, (SELECT SUM(MONEY) FROM account Lin WHERE Lin.ID <= Lout.ID) AS TOTAL FROM account Lout ORDER BY ID;'
        res = conn.execute(content)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        self.label_2.setText("Total Money: " + str(col_data))
        return

class InsertDialog(QDialog, insertData.Ui_Dialog):
    def __init__(self, parent=None):
        super(InsertDialog, self).__init__(parent)
        self.setupUi(self)

class EditDialog(QDialog, editData.Ui_Dialog):
    def __init__(self, parent=None):
        super(EditDialog, self).__init__(parent)
        self.setupUi(self)


# db connect
conn = sqlite3.connect('tableDB.db')
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS account(ID INTEGER PRIMARY KEY AUTOINCREMENT, DATE TEXT, TIME TEXT, TYPE NUMERIC, ITEM TEXT, MONEY REAL)')
print("Database is on...")


# start

app = QApplication([])
win = MainApp()
app.exec_()