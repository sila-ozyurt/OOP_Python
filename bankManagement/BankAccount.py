import datetime as dt
import Customer 
import BankManager

class BankAccount():

    def __init__(self,customer,password,balance=0):
        bankManager=BankManager.BankManager()
        self.customer=customer
        #account number is assigned by bankmanager class
        self.accountNumber=bankManager.assignAccountNumber()
        self.password=password
        self.balance=balance
        #transaction history list will contain all transactions done by the customer
        self.__transactionHistory=[]

        # Add the BankAccount to the associated Customer's bankAccounts list
        self.customer.bankAccounts.append(self)

    #function to check if there is a customer which fills the bill
    def __checkCustomer(self):
        if not isinstance(self.customer,Customer.Customer):
          raise ValueError("BankAccount must be associated with a Customer")

    #function to check accountnumber and password, not to let a confusion
    def __checkAccountNumber(self,accountNumber,password):
        if accountNumber !=self.accountNumber and password!=self.password:
            print("please enter your account number and password correctly")
            return
    

    #function to withdraw from a certain account
    def withdrawal(self,accountNumber,password,amount):

        #first we need to check if there is a customer with these attributes
        self.__checkCustomer()
        #then this person needs to know the account number and password correctly
        self.__checkAccountNumber(self.accountNumber,password)

        if amount>self.balance:
            print("insufficient funds in your bank account!!!")
            return

        self.balance -= amount
        self.__transactionRecord("withdrawal",amount)
        print(f"{amount} TL is withdrawn.NEW BALANCE {self.balance} TL ")

        isDemanded=input("would you like to have an information receipt?(yes/no)")
        if isDemanded.lower()=="yes":
            self.__takeReceipt()



    def deposit(self,accountNumber,password,amount):

        #first we need to check if there is a customer with these attributes
        self.__checkCustomer()
        #then this person needs to know the account number and password correctly
        self.__checkAccountNumber(self.accountNumber,password)
       

        for account in self.customer.bankAccounts:
            if account.accountNumber == accountNumber and account.password == password:
                account.balance += amount
                print(f"{amount} TL is deposited successfully. NEW BALANCE {account.balance} TL")
                # Assuming you implement transactionRecord method
                account.__transactionRecord("deposit", amount)

                isDemanded = input("Would you like to have an information receipt? (yes/no)")
                if isDemanded.lower() == "yes":
                    # Assuming you implement __takeReceipt method
                    account.__takeReceipt()
                return

        print("Account not found.")

    #function to add element into the transaction history list
    def __transactionRecord(self,transactionType,amount):

        transaction={
            "type":transactionType,
            "amount":amount,
            "timeStamp": dt.datetime.now()
        }

        self.__transactionHistory.append(transaction)
    
    
    #this function can be called only inside of deposit and withdrawal function
    def __takeReceipt(self):
        print("INFORMATION RECEIPT".center(50,"*"))
        print(f"TRANSACTION TYPE IS : {self.__transactionHistory[-1]["type"]}")
        print(f"DATE : {dt.datetime.now()}")
        print(f"ACCOUNT NUMBER : {self.accountNumber}")
        print(f"TRANSACTION AMOUNT : {self.__transactionHistory[-1]["amount"]}")
        print(f"NEW BALANCE : {self.balance}")
        print("*"*50)


    def viewTransactionHistory(self):
        print("*"*20)
        for i in self.__transactionHistory:
            print(f"Type: {i["type"]}")
            print(f"Amount: {i["amount"]} TL")
            print(f"Timestamp: {i["timeStamp"]}")
            print("*"*20)

    
    def getAccountNumber(self):
        return "your account number is: "+str(self.accountNumber)


    def getBalance(self):
        return "current balance is : "+str(self.balance)
    



