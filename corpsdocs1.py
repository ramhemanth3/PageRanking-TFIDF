import sys
import os
#from corpsdocs import *
from PyQt5 import QtWidgets, QtGui, QtCore
import pymysql

con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='rdbidf1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_2.clicked.connect(self.getvalues)
     self.ui.label_7.setText('<a href="http://www.english-for-students.com/falcon-saved-his-friend-the-king.html">Link_1</a>')
     self.ui.label_7.setOpenExternalLinks(True)
     self.ui.label_8.setText('<a href="http://www.english-for-students.com/greediness-can-make-a-man-blind.html">Link_2</a>')
     self.ui.label_8.setOpenExternalLinks(True)
     self.ui.label_9.setText('<a href="http://www.english-for-students.com/alaudeen-and-the-magical-lamp.html">Link_3</a>')
     self.ui.label_9.setOpenExternalLinks(True)
     self.ui.label_10.setText('<a href="http://www.english-for-students.com/alibaba-and-the-forty-thieves.html">Link_4</a>')
     self.ui.label_10.setOpenExternalLinks(True)
     self.ui.label_11.setText('<a href="http://www.english-for-students.com/banished-son-saves-his-brothers.html">Link_5</a>')
     self.ui.label_11.setOpenExternalLinks(True)	     
   
  def getvalues(self):
         
     with con:
    
        cur = con.cursor()
        for k in range(1,6):
          cur.execute('SELECT docdesc FROM docs where docid = %s;', k);
          result = cur.fetchall()
          #print(result)
          for row in result:
            #result1 = row[0]
            if (k == 1) : 
              (self.ui.lineEdit_4.setText(str(k)))
              (self.ui.lineEdit_9.setText(row[0]))
            if (k == 2) : 
              (self.ui.lineEdit_5.setText(str(k)))
              (self.ui.lineEdit_10.setText(row[0]))
            if (k == 3) : 
              (self.ui.lineEdit_6.setText(str(k)))
              (self.ui.lineEdit_11.setText(row[0]))
            if (k == 4) : 
              (self.ui.lineEdit_7.setText(str(k)))
              (self.ui.lineEdit_12.setText(row[0]))
            if (k == 5) : 
              (self.ui.lineEdit_8.setText(str(k)))
              (self.ui.lineEdit_13.setText(row[0]))		  
	      
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



	
