class BankAcct:
  def __init__(self, money):
    self.money= money
    
  def withdraw(self, taken):
    self.money -= taken + 2

  def deposit(self, putin):
    self.money += putin

a = BankAcct(10000)
b = BankAcct(50000000000000)

a.withdraw(2)
a.deposit(500)
b.withdraw(923499395692)
b.deposit(20)

print(a.money, b.money)
  
    
