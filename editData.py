# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditData.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_3.addWidget(self.calendarWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Edit Data"))
        self.radioButton.setText(_translate("Dialog", "Income"))
        self.radioButton_2.setText(_translate("Dialog", "Outcome"))
        self.label.setText(_translate("Dialog", "Item"))
        self.label_2.setText(_translate("Dialog", "Money"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))

