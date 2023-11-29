from csv import *
from PyQt6.QtWidgets import *
from gui import *


class Logic (QMainWindow, Ui_MainWindow):

    def __init__(self):
        super.__init__()
        self.setupUi(self)

        self.verify.clicked.connect(lambda: self.verify_account())
        self.submit.clicked.connect(lambda: self.account_modify())

# verify account info (check name, account number, PIN)
# display current amount if account verified
    def verify_account(self):
        first_name = self.input_first.lower()
        last_name = self.input_last.lower()
        account_num = int(self.input_account)
        account_pin = int(self.input_pin)

# deposit/withdraw amount from current account
# display error/succession and final amount in account
    def account_modify(self):
        pass

