import sys
import os
from rdbidf import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.calcidf)
     self.ui.pushButton_2.clicked.connect(self.rankdoc)
     self.ui.pushButton_3.clicked.connect(self.preproc)
     self.ui.pushButton_4.clicked.connect(self.htext)
     self.ui.pushButton_5.clicked.connect(self.corpsdocs)
     self.ui.pushButton_6.clicked.connect(self.lemmat)
     self.ui.pushButton_7.clicked.connect(self.seqry)
       

  def calcidf(self):
    os.system("python idf1.py")

  def rankdoc(self):
    os.system("python rank1.py")

  def preproc(self):
    cmd1 = "python" + " " + "htext2.py" +" " + "urlx.txt" + " > " + "urlx1.txt"
    os.system(cmd1)
    print("Converted file successfully created as urlx1.txt")   

  def htext(self):
    os.system("python htmltotext1.py")

  def corpsdocs(self):
    os.system("python corpsdocs1.py")
	
  def lemmat(self):
    os.system("python lemmat1.py")
	
  def seqry(self):
    os.system("python selqry1.py")


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
