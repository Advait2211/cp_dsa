class Account:
    def __init__(self, name: float, id: float, balance: float):
        self.holder_name = name
        self.acc_id = id
        self.balance = balance

    def deposit(self, amount: float, interest_rate = 0) -> None:
        self.balance += amount
        if interest_rate > 0:
            self.balance += self.balance * interest_rate / 100
        

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            return -1.0
        else:
            self.balance -= amount
            return amount
        
class SavingAccount(Account):
    # i don't know how to use @property or whatever that starts with an '@'
    # so here's what i will do

    def deposit(self, amount: float, interest_rate: float):
        # do i add interest on the entire amount, or just the deposit? i am assuming the total balance
        return super().deposit(amount, interest_rate)


