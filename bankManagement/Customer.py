import BankManager 

class Customer:
    def __init__(self,firstName,lastName,age,gender):
        #we need to create an object of manager to assign cust id uniquely
        bankManager=BankManager.BankManager()
        self.customerId=bankManager.assignCustomerId()
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.gender=gender
        #variable below comprises of all accounts which customer owns
        self.bankAccounts= []    

        #add new customer to the customers list which is created in BankManager class
        bankManager.allCustomers.append(self)


    def getAllBankAccounts(self):

        print("ALL ACCOUNTS YOU OWN WILL BE LISTED BELOW ")
        for account in self.bankAccounts:
            print("*"*20)
            print(f"Customer Name: {account.customer.firstName+" "+account.customer.lastName}\n"
                      f"Age: {account.customer.age}\n"
                      f"Gender: {account.customer.gender}\n"
                      f"Account Number: {account.accountNumber}\n"
                      f"Balance: {account.balance}\n")
        print("*"*20)


    def getAnAccount(self,accountNum):

        for account in self.bankAccounts:
            if account.accountNumber==accountNum:
                print("*"*20)
                print(f"Customer Name: {account.customer.firstName+" "+account.customer.lastName}\n"
                      f"Age: {account.customer.age}\n"
                      f"Gender: {account.customer.gender}\n"
                      f"Account Number: {account.accountNumber}\n"
                      f"Balance: {account.balance}\n")
                print("*"*20)
                return
            
        print("Account not found.")

    def getCustomerId(self):
        return "your customer id is: "+str(self.customerId)
   
