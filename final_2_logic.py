from csv import *
from PyQt6.QtWidgets import *
from gui import *

# check line 104 to change frame status

class Logic (QMainWindow, Ui_MainWindow):

    def __init__(self):
        super.__init__()
        self.setupUi(self)

        self.verify.clicked.connect(lambda: self.verify_account())
        self.submit.clicked.connect(lambda: self.account_modify())

# verify account info (check name, account number, PIN) import information from accounts.csv (try/except)
# display current amount if account verified
# display error if account info mismatch instead of current account amount
    def verify_account(self):
        first_name = self.input_first.lower()
        last_name = self.input_last.lower()
        account_num = int(self.input_account)
        account_pin = int(self.input_pin)

        try:
            pass
        except:
            pass

    def currency_conversion(self):
        try:
            money = float(self.input_amount)
            if self.rb_cyn.isChecked():
                pass
            elif self.rb_eur.isChecked():
                pass
            elif self.rb_cad.isChecked():
                pass
            elif self.rb_gbp.isChecked():
                pass
            elif self.rb_mxn.isChecked():
                pass
            elif self.rb_jpn.isChecked():
                pass
            elif self.rb_krw.isChecked():
        except:
            self.final_message.insertPlainText(f'Please input valid value.')


    def deposit_money(self):
        pass

    def withdraw_money(self):
        pass


# modify currency (if foreign -> USD)
# deposit/withdraw amount from current account
# display error/succession and final amount in account
    def account_modify(self):
        self.currency_conversion()
        if self.deposit.isChecked():
            self.deposit_money()
        else:
            self.withdraw_money()

