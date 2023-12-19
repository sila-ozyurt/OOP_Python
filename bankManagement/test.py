from BankAccount import BankAccount
from Customer import Customer
from BankManager import BankManager

cus1=Customer("hediye","ozyurt",21,"woman")
print(cus1.getCustomerId())


cus2=Customer("ali","ozyurt",30,"man")
print(cus2.getCustomerId())




account1=BankAccount(cus1,"psw")
print(account1.getAccountNumber())

account1.deposit(10001,"psw",1000)
account1.withdrawal(10001,"psw",1)
print(account1.getBalance())

account1.viewTransactionHistory()

cus1.getAnAccount(10001)

account1=BankAccount(cus1,"psw2")
cus1.getAllBankAccounts()

manager=BankManager()
manager.deleteCustomerAccount(cus1,10001)

cus1.getAllBankAccounts()