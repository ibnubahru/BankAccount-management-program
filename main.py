
from bankaccount import BankAccount

acc1 = BankAccount("malik", 5000)
acc1.deposit(1000)
acc1.withdraw(2000)
print(acc1.get_balance())

