# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rdbidf.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 312)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 210, 271, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 250, 271, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 10, 271, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 90, 271, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 50, 271, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 130, 271, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 170, 271, 31))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ranking of Documents Based on IDF"))
        self.pushButton.setText(_translate("MainWindow", "IDFs calculation"))
        self.pushButton_2.setText(_translate("MainWindow", "Ranking of DOCs"))
        self.pushButton_5.setText(_translate("MainWindow", "Docs.  in Corpus"))
        self.pushButton_3.setText(_translate("MainWindow", "Preprocess the text"))
        self.pushButton_4.setText(_translate("MainWindow", "HTML to Text"))
        self.pushButton_6.setText(_translate("MainWindow", "Lemmatization"))
        self.pushButton_7.setText(_translate("MainWindow", "Select Query"))
