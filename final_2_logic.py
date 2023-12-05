import csv
from PyQt6.QtWidgets import *
from gui import *


class Logic (QMainWindow, Ui_MainWindow):
    a = 1
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.verify.clicked.connect(lambda: self.verify_account())  # account verification
        self.submit.clicked.connect(lambda: self.account_modify())  # lead to balance change
        self.deposit.clicked.connect(lambda: self.show_frame())  # show frame
        self.withdraw.clicked.connect(lambda: self.show_frame())  # show frame
        self.button_clear.clicked.connect(lambda: self.clear())  # clearing values and hiding frames

# verify account info (check name, account number, PIN) import information from accounts.csv (try/except)
# display current amount if account verified
    def verify_account(self):
        self.current_amount.clear()
        try:
            first_name = str(self.input_first.text()).strip().upper()
            last_name = str(self.input_last.text()).strip().upper()
            account_num = str(self.input_account.text()).strip()
            pin = str(self.input_pin.text()).strip()
            information = [first_name, last_name, account_num, pin]
            with open('accounts.csv', newline='') as csvfile:
                reader = csv.reader(csvfile)
                i = 1
                row_list = []
                for row in reader:
                    row_list.append(row)
            while i < len(row_list):
                if row_list[i][0] == information[0]:
                    if row_list[i][1] == information[1]:
                        if row_list[i][2] == information[2]:
                            if row_list[i][3] == information[3]:
                                self.current_amount.insertPlainText(f'Your account balance is {row_list[i][4]} (USD).')
                                self.frame_2.show()
                                current_balance = float(row_list[i][4])
                                self.a = i
                                return current_balance
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

    def show_frame(self):  # showing frame to input the amount of money to put in or take out from bank account
        self.frame.show()
        return True

# convert any foreign currency if any radio button is selected other than USD and return the converted money
# USD is set as default currency
    def currency_conversion(self):
        self.money_in_usd.clear()
        try:
            money = float(self.input_amount.text())
            if money <= 0.00:
                self.money_in_usd.insertPlainText(f'Please input valid amount to proceed.')
                return False
            else:
                if self.rb_cyn.isChecked():
                    money_usd = money / 7.024500
                    money_usd = round(money_usd, 2)
                    self.money_in_usd.insertPlainText(f'{money:.2f} CYN is equivalent to {money_usd:.2f} USD.')
                    return money_usd
                elif self.rb_eur.isChecked():
                    money_usd = money / 0.911826
                    money_usd = round(money_usd, 2)
                    self.money_in_usd.insertPlainText(f'{money:.2f} EUR is equivalent to {money_usd:.2f} USD.')
                    return money_usd
                elif self.rb_cad.isChecked():
                    money_usd = money / 1.360670
                    money_usd = round(money_usd, 2)
                    self.money_in_usd.insertPlainText(f'{money:.2f} CAD is equivalent to {money_usd:.2f} USD.')
                    return money_usd
                elif self.rb_gbp.isChecked():
                    money_usd = money / 0.788832
                    money_usd = round(money_usd, 2)
                    self.money_in_usd.insertPlainText(f'{money:.2f} GBP is equivalent to {money_usd:.2f} USD.')
                    return money_usd
                elif self.rb_mxn.isChecked():
                    money_usd = money / 17.187900
                    money_usd = round(money_usd, 2)
                    self.money_in_usd.insertPlainText(f'{money:.2f} MXN is equivalent to {money_usd} USD.')
                    return money_usd
                elif self.rb_jpy.isChecked():
                    money_usd = money / 147.608000
                    money_usd = round(money_usd, 2)
                    self.money_in_usd.insertPlainText(f'{money:.2f} JPY is equivalent to {money_usd:.2f} USD.')
                    return money_usd
                elif self.rb_krw.isChecked():
                    money_usd = money / 1260.740000
                    money_usd = round(money_usd, 2)
                    self.money_in_usd.insertPlainText(f'{money:.2f} KRW is equivalent to {money_usd:.2f} USD.')
                    return money_usd
                else:
                    self.money_in_usd.insertPlainText(f'No conversion is needed. The amount is {money:.2f} USD.')
                    return money
        except:
            self.money_in_usd.insertPlainText(f'Please put in valid value.')
            return False

# deposit the amount of money input and return updated balance
    def deposit_money(self, amount):  # add money to original account by adding input amount to original balance
        money_to_add = amount
        original_balance = self.verify_account()
        updated_balance = original_balance + money_to_add
        return updated_balance

# withdraw the amount of money input and return updated balance
    def withdraw_money(self, amount):  # withdraw from account by subtracting input amount from original balance
        money_to_subtract = amount
        original_balance = self.verify_account()
        updated_balance = original_balance - money_to_subtract
        return updated_balance

# modify currency (if foreign -> USD)
# deposit/withdraw amount from current account calling another function
# display error/succession and final amount in account
    def account_modify(self):
        self.final_message.clear()
        csv_row = int(self.a)
        amount = self.currency_conversion()
        if self.deposit.isChecked() and self.currency_conversion():
            current_balance = self.deposit_money(amount)
            current_balance = round(current_balance, 2)
            self.final_message.insertPlainText(f"Your transaction was successful. "
                                               f"The current account balance is {current_balance:.2f} USD.")
            self.overwrite_account_balance('accounts.csv', csv_row, 4, current_balance)
            return True
        elif self.withdraw_money(amount) and self.currency_conversion():
            current_balance = self.withdraw_money(amount)
            current_balance = round(current_balance, 2)
            self.final_message.insertPlainText(f"Your transaction was successful. "
                                               f"The current account balance is {current_balance:.2f} USD.")
            self.overwrite_account_balance('accounts.csv', csv_row, 4, current_balance)
            return True
        else:
            self.final_message.insertPlainText(f"Your transaction was unsuccessful.")
            return False

#  updating the csv file by rewriting  the entire file but updating only the account balance modified
    def overwrite_account_balance(self, file_name, row_num, column_num, new_balance):
        rows = []
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        if row_num < len(rows) and column_num < len(rows[row_num]):
            rows[row_num][column_num] = new_balance
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        else:
            self.final_message.insertPlainText(f"Your transaction was unsuccessful.")
            return False

    def clear(self):  # clear input
        self.input_first.clear()
        self.input_last.clear()
        self.input_account.clear()
        self.input_pin.clear()
        self.input_amount.clear()
        self.current_amount.clear()
        self.money_in_usd.clear()
        self.final_message.clear()
        self.rb_usd.setChecked(True)
        self.frame.setHidden(True)
        self.frame_2.setHidden(True)
