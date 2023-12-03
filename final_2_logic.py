import csv
from PyQt6.QtWidgets import *
from gui import *


# check line 104 to change frame status
class Logic (QMainWindow, Ui_MainWindow):
    def __init__(self, balance=0):
        super().__init__()
        self.setupUi(self)
        self.clear()
        self.verify.clicked.connect(lambda: self.verify_account())
        self.submit.clicked.connect(lambda: self.account_modify())
        self.deposit.clicked.connect(lambda: self.show_frame())
        self.withdraw.clicked.connect(lambda: self.show_frame())

        self.__account_balance = balance

# verify account info (check name, account number, PIN) import information from accounts.csv (try/except)
# display current amount if account verified
# display error if account info mismatch instead of current account amount
    def verify_account(self):
        try:
            first_name = str(self.input_first.text()).strip().upper()
            last_name = str(self.input_last.text()).strip().upper()
            account_num = str(self.input_account.text()).strip()
            pin = str(self.input_pin.text()).strip()
            information = [first_name, last_name, account_num, pin]
            with open('accounts.csv', newline='') as csvfile:
                reader = csv.reader(csvfile)
                i = 1
                j = 0
                row_list = []
                for row in reader:
                    row_list.append(row)
            while i < len(row_list):
                if row_list[i][0] == information[0]:
                    if row_list[i][1] == information[1]:
                        if row_list[i][2] == information[2]:
                            if row_list[i][3] == information[3]:
                                print('D')
                                self.current_amount.insertPlainText(f'Your account balance is {row_list[i][4]} (USD).')
                                self.frame_2.show()
                                return True
                            else:
                                i += 1
                        else:
                            i += 1
                    else:
                        i += 1
                else:
                    i += 1
            if i == len(row_list):
                raise Exception
        except:
            self.current_amount.insertPlainText(f'Please input correct account information.')

    def show_frame(self):
        self.frame.show()
        return True

# convert any foreign currency if any radio button is selected other than USD
    def currency_conversion(self):
        try:
            money = float(self.input_amount.text())
            if money < 0:
                raise Exception
            else:
                if self.rb_cyn.isChecked():
                    money_usd = money / 7.024500
                    self.money_in_usd.insertPlainText(f'{money:.2f}CYN is equivalent to {money_usd:.}USD.')
                elif self.rb_eur.isChecked():
                    money_usd = money / 0.911826
                    self.money_in_usd.insertPlainText(f'{money:.2f}EUR is equivalent to {money_usd:.}USD.')
                elif self.rb_cad.isChecked():
                    money_usd = money / 1.360670
                    self.money_in_usd.insertPlainText(f'{money:.2f}CAD is equivalent to {money_usd:.}USD.')
                elif self.rb_gbp.isChecked():
                    money_usd = money / 0.788832
                    self.money_in_usd.insertPlainText(f'{money:.2f}GBP is equivalent to {money_usd:.}USD.')
                elif self.rb_mxn.isChecked():
                    money_usd = money / 17.187900
                    self.money_in_usd.insertPlainText(f'{money:.2f}MXN is equivalent to {money_usd:.}USD.')
                elif self.rb_jpy.isChecked():
                    money_usd = money / 147.608000
                    self.money_in_usd.insertPlainText(f'{money:.2f}JPY is equivalent to {money_usd:.}USD.')
                elif self.rb_krw.isChecked():
                    money_usd = money / 1260.740000
                    self.money_in_usd.insertPlainText(f'{money:.2f}KRW is equivalent to {money_usd:.}USD.')
                else:
                    self.money_in_usd.insertPlainText(f'No conversion is needed. The amount is {money:.2f}')
        except:
            self.money_in_usd.insertPlainText(f'Please input valid value.')

    def deposit_money(self,amount):
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw_money(self, amount):
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

# modify currency (if foreign -> USD)
# deposit/withdraw amount from current account
# display error/succession and final amount in account
    def account_modify(self):
        self.currency_conversion()
        amount = self.verify_account()
        if self.deposit.isChecked():
            if self.deposit_money(amount) is True:
                self.final_message.insertPlainText(f"Your transaction was successful. "
                                                   f"The current account balance is {amount:.2f}")
            else:
                self.final_message.insertPlainText(f"Your transaction was unsuccessful.")
        else:
            if self.withdraw_money(amount) is True:
                if self.deposit_money(amount):
                    self.final_message.insertPlainText(f"Your transaction was successful. "
                                                       f"The current account balance is {amount:.2f}")
                else:
                    self.final_message.insertPlainText(f"Your transaction was unsuccessful.")

    def clear(self):
        self.input_first.clear()
        self.input_last.clear()
        self.input_account.clear()
        self.input_pin.clear()
        self.current_amount.clear()
        self.rb_usd.isChecked()
        self.money_in_usd.clear()
        self.final_message.clear()

