from typing import List

class Bank:
    
    def CheckStatus(self, account, money):
        if not 0 < account <= self.n:
            return False 
        if self.balance[account-1] < money:
            return False  
        return True

    def __init__(self, balance: List[int]):
        self.n=len(balance)
        self.balance=balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if False == (self.CheckStatus(account1, money) and self.CheckStatus(account2, 0)):
            return False
        self.withdraw(account1,money)
        self.deposit(account2,money)
        return True 

    def deposit(self, account: int, money: int) -> bool:
        status=self.CheckStatus(account, 0)
        if False==status:
            return False
        self.balance[account-1]+=money
        return True      

    def withdraw(self, account: int, money: int) -> bool:
        status=self.CheckStatus(account, money)
        if False==status:
            return False
        self.balance[account-1]-=money
        return True 
      