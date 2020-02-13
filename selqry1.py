import sys
import os
from selqry import *
from PyQt5 import QtWidgets, QtGui, QtCore
import pymysql

con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='rdbidf1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_2.clicked.connect(self.qryadd)
     with con:
    
        cur = con.cursor()
        cur.execute('SELECT qury FROM qury;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox.addItem(row[0]))
   

  def qryadd(self):
    with con:
    
        cur = con.cursor()
        text1 = self.ui.comboBox.currentText()
        cur.execute('INSERT INTO qryselected VALUES(%s)',(text1))
        con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



	
