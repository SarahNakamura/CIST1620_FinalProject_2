# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 703)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.web_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.web_title.setGeometry(QtCore.QRect(170, 20, 321, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.web_title.setFont(font)
        self.web_title.setObjectName("web_title")
        self.first_message = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.first_message.setGeometry(QtCore.QRect(170, 60, 256, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.first_message.setFont(font)
        self.first_message.setObjectName("first_message")
        self.first_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.first_name.setGeometry(QtCore.QRect(79, 110, 101, 20))
        self.first_name.setObjectName("first_name")
        self.last_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.last_name.setGeometry(QtCore.QRect(80, 150, 101, 16))
        self.last_name.setObjectName("last_name")
        self.account_number = QtWidgets.QLabel(parent=self.centralwidget)
        self.account_number.setGeometry(QtCore.QRect(80, 190, 111, 16))
        self.account_number.setObjectName("account_number")
        self.pin = QtWidgets.QLabel(parent=self.centralwidget)
        self.pin.setGeometry(QtCore.QRect(80, 230, 91, 16))
        self.pin.setObjectName("pin")
        self.current_amount = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.current_amount.setGeometry(QtCore.QRect(170, 260, 256, 21))
        self.current_amount.setObjectName("current_amount")
        self.deposit = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.deposit.setGeometry(QtCore.QRect(160, 350, 100, 20))
        self.deposit.setObjectName("deposit")
        self.second_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.second_message.setGeometry(QtCore.QRect(170, 300, 251, 16))
        self.second_message.setObjectName("second_message")
        self.withdraw = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.withdraw.setGeometry(QtCore.QRect(330, 350, 171, 20))
        self.withdraw.setObjectName("withdraw")
        self.input_first = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_first.setGeometry(QtCore.QRect(210, 110, 211, 21))
        self.input_first.setObjectName("input_first")
        self.input_last = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_last.setGeometry(QtCore.QRect(210, 150, 211, 21))
        self.input_last.setObjectName("input_last")
        self.input_account = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_account.setGeometry(QtCore.QRect(210, 190, 211, 21))
        self.input_account.setObjectName("input_account")
        self.input_pin = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_pin.setGeometry(QtCore.QRect(210, 230, 113, 21))
        self.input_pin.setObjectName("input_pin")
        self.amount = QtWidgets.QLabel(parent=self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(80, 380, 60, 16))
        self.amount.setObjectName("amount")
        self.input_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(210, 380, 113, 21))
        self.input_amount.setObjectName("input_amount")
        self.currency = QtWidgets.QLabel(parent=self.centralwidget)
        self.currency.setGeometry(QtCore.QRect(80, 420, 60, 16))
        self.currency.setObjectName("currency")
        self.rb_usd = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rb_usd.setGeometry(QtCore.QRect(170, 420, 121, 20))
        self.rb_usd.setObjectName("rb_usd")
        self.rb_cyn = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rb_cyn.setGeometry(QtCore.QRect(330, 420, 151, 20))
        self.rb_cyn.setObjectName("rb_cyn")
        self.rb_eur = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rb_eur.setGeometry(QtCore.QRect(520, 420, 100, 20))
        self.rb_eur.setObjectName("rb_eur")
        self.rb_cad = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rb_cad.setGeometry(QtCore.QRect(170, 450, 161, 20))
        self.rb_cad.setObjectName("rb_cad")
        self.rb_gbp = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rb_gbp.setGeometry(QtCore.QRect(330, 450, 191, 20))
        self.rb_gbp.setObjectName("rb_gbp")
        self.rb_jpn = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rb_jpn.setGeometry(QtCore.QRect(170, 480, 141, 20))
        self.rb_jpn.setObjectName("rb_jpn")
        self.bp_mxn = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.bp_mxn.setGeometry(QtCore.QRect(530, 450, 151, 20))
        self.bp_mxn.setObjectName("bp_mxn")
        self.rb_krw = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rb_krw.setGeometry(QtCore.QRect(330, 480, 171, 20))
        self.rb_krw.setObjectName("rb_krw")
        self.final_message = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.final_message.setGeometry(QtCore.QRect(170, 510, 256, 91))
        self.final_message.setObjectName("final_message")
        self.amount_change = QtWidgets.QFrame(parent=self.centralwidget)
        self.amount_change.setEnabled(False)
        self.amount_change.setGeometry(QtCore.QRect(60, 290, 641, 331))
        self.amount_change.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.amount_change.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.amount_change.setObjectName("amount_change")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.web_title.setText(_translate("MainWindow", "Welcome to Maverick Bank"))
        self.first_message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">Please enter fist name, last name, account number, and PIN below.</span></p></body></html>"))
        self.first_name.setText(_translate("MainWindow", "First Name"))
        self.last_name.setText(_translate("MainWindow", "Last Name"))
        self.account_number.setText(_translate("MainWindow", "Account Number"))
        self.pin.setText(_translate("MainWindow", "PIN"))
        self.deposit.setText(_translate("MainWindow", "Deposit"))
        self.second_message.setText(_translate("MainWindow", "How can I help you today?"))
        self.withdraw.setText(_translate("MainWindow", "Withdraw"))
        self.amount.setText(_translate("MainWindow", "Amount"))
        self.currency.setText(_translate("MainWindow", "Currency"))
        self.rb_usd.setText(_translate("MainWindow", "USD (US dollar)"))
        self.rb_cyn.setText(_translate("MainWindow", "CNY (Chinese yuan)"))
        self.rb_eur.setText(_translate("MainWindow", "EUR (euro)"))
        self.rb_cad.setText(_translate("MainWindow", "CAD (Canadian Dollar)"))
        self.rb_gbp.setText(_translate("MainWindow", "GBP (British pound sterling)"))
        self.rb_jpn.setText(_translate("MainWindow", "JPN (Japanese yen)"))
        self.bp_mxn.setText(_translate("MainWindow", "MXN (Mexican peso)"))
        self.rb_krw.setText(_translate("MainWindow", "KRW (South Korean won)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
