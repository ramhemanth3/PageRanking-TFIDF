import sys
import os
from htmltotext import *
from PyQt5 import QtWidgets, QtGui, QtCore
#import pymysql
#import mysql.connector

#3con = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Password_mysql',database = 'login_page')

#c = con.cursor()
"""con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='rdbidf1')"""
import sqlite3
con = sqlite3.connect('rdbidf1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_2.clicked.connect(self.docconvert)
     with con:
    
        cur = con.cursor()
        cur.execute('SELECT lnks FROM lnks;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox.addItem(row[0]))
   

  def docconvert(self):
    with con:
    
        cur = con.cursor()
        url1 = self.ui.comboBox.currentText()
        cmd1 = "python" + " " + "htext4.py" +" " + str(url1) + " > " + "urlx.txt"
        os.system(cmd1)
        print("Converted file successfully created as urlx.txt")
        con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



	
