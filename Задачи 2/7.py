class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def put_money(self, amount):
        commission = amount * 0.01
        self.balance += (amount - commission)
        print('Пополнено на ', amount, '. Комиссия: ', commission)

    def withdraw_money(self, amount):
        commission = amount * 0.01
        total_withdraw = amount + commission
        self.balance -= total_withdraw
        print('Снято ', amount, '. Комиссия: ', commission)

    def check_balance(self):
        print('Текущий баланс: ', self.balance)
