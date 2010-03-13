# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdlg.ui'
#
# Created: Sat Mar 13 22:50:56 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(376, 188)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Name = QtGui.QLabel(Dialog)
        self.label_Name.setObjectName("label_Name")
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.label_Number = QtGui.QLabel(Dialog)
        self.label_Number.setObjectName("label_Number")
        self.gridLayout.addWidget(self.label_Number, 2, 0, 1, 1)
        self.label_UnitPrice = QtGui.QLabel(Dialog)
        self.label_UnitPrice.setObjectName("label_UnitPrice")
        self.gridLayout.addWidget(self.label_UnitPrice, 2, 2, 1, 1)
        self.label_Date = QtGui.QLabel(Dialog)
        self.label_Date.setObjectName("label_Date")
        self.gridLayout.addWidget(self.label_Date, 3, 2, 1, 1)
        self.dateEdit_Date = QtGui.QDateEdit(Dialog)
        self.dateEdit_Date.setCalendarPopup(True)
        self.dateEdit_Date.setObjectName("dateEdit_Date")
        self.gridLayout.addWidget(self.dateEdit_Date, 3, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.doubleSpinBox_InCome = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_InCome.setMinimum(-99999999.99)
        self.doubleSpinBox_InCome.setMaximum(99999999.99)
        self.doubleSpinBox_InCome.setObjectName("doubleSpinBox_InCome")
        self.gridLayout.addWidget(self.doubleSpinBox_InCome, 2, 3, 1, 1)
        self.comboBox_Name = QtGui.QComboBox(Dialog)
        self.comboBox_Name.setEditable(True)
        self.comboBox_Name.setObjectName("comboBox_Name")
        self.gridLayout.addWidget(self.comboBox_Name, 1, 1, 1, 1)
        self.label_Category = QtGui.QLabel(Dialog)
        self.label_Category.setObjectName("label_Category")
        self.gridLayout.addWidget(self.label_Category, 1, 2, 1, 1)
        self.comboBox_Category = QtGui.QComboBox(Dialog)
        self.comboBox_Category.setEditable(True)
        self.comboBox_Category.setObjectName("comboBox_Category")
        self.gridLayout.addWidget(self.comboBox_Category, 1, 3, 1, 1)
        self.doubleSpinBox_OutCome = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_OutCome.setMinimum(-99999999.99)
        self.doubleSpinBox_OutCome.setMaximum(99999999.99)
        self.doubleSpinBox_OutCome.setObjectName("doubleSpinBox_OutCome")
        self.gridLayout.addWidget(self.doubleSpinBox_OutCome, 2, 1, 1, 1)
        self.label_Total = QtGui.QLabel(Dialog)
        self.label_Total.setObjectName("label_Total")
        self.gridLayout.addWidget(self.label_Total, 3, 0, 1, 1)
        self.doubleSpinBox_Total = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_Total.setMinimum(-99999999.99)
        self.doubleSpinBox_Total.setMaximum(99999999.99)
        self.doubleSpinBox_Total.setObjectName("doubleSpinBox_Total")
        self.gridLayout.addWidget(self.doubleSpinBox_Total, 3, 1, 1, 1)
        self.label_Number_2 = QtGui.QLabel(Dialog)
        self.label_Number_2.setObjectName("label_Number_2")
        self.gridLayout.addWidget(self.label_Number_2, 0, 0, 1, 1)
        self.spinBox_Number = QtGui.QSpinBox(Dialog)
        self.spinBox_Number.setMinimum(1)
        self.spinBox_Number.setMaximum(99999999)
        self.spinBox_Number.setObjectName("spinBox_Number")
        self.gridLayout.addWidget(self.spinBox_Number, 0, 1, 1, 1)
        self.label_Name.setBuddy(self.comboBox_Name)
        self.label_Number.setBuddy(self.doubleSpinBox_OutCome)
        self.label_UnitPrice.setBuddy(self.doubleSpinBox_InCome)
        self.label_Date.setBuddy(self.dateEdit_Date)
        self.label_Category.setBuddy(self.comboBox_Category)
        self.label_Total.setBuddy(self.doubleSpinBox_Total)
        self.label_Number_2.setBuddy(self.spinBox_Number)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox_Name, self.comboBox_Category)
        Dialog.setTabOrder(self.comboBox_Category, self.doubleSpinBox_OutCome)
        Dialog.setTabOrder(self.doubleSpinBox_OutCome, self.doubleSpinBox_InCome)
        Dialog.setTabOrder(self.doubleSpinBox_InCome, self.doubleSpinBox_Total)
        Dialog.setTabOrder(self.doubleSpinBox_Total, self.dateEdit_Date)
        Dialog.setTabOrder(self.dateEdit_Date, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "编辑", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Name.setText(QtGui.QApplication.translate("Dialog", "品名(&N)：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Number.setText(QtGui.QApplication.translate("Dialog", "出账(&U)：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_UnitPrice.setText(QtGui.QApplication.translate("Dialog", "入账(&I)：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Date.setText(QtGui.QApplication.translate("Dialog", "日期(&D)：", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit_Date.setDisplayFormat(QtGui.QApplication.translate("Dialog", "yyyy-MM-dd", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Category.setText(QtGui.QApplication.translate("Dialog", "类别(&C)：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Total.setText(QtGui.QApplication.translate("Dialog", "余额(&T)：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Number_2.setText(QtGui.QApplication.translate("Dialog", "编号(&I)", None, QtGui.QApplication.UnicodeUTF8))

import pygrid_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

