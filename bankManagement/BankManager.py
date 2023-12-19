import Customer
import BankAccount

uniqueId=0
uniqueAccountNum=10000

class BankManager:

    #customers can be accessible by all manager objects
    allCustomers=[]


    # def __init__(self):
    #     pass


    def assignCustomerId(cls):
        global uniqueId
        uniqueId+= 1
        return uniqueId
    
    def assignAccountNumber(cls):
        global uniqueAccountNum 
        uniqueAccountNum+= 1
        return uniqueAccountNum


    #this function deletes the account of a specific customer 
    def deleteCustomerAccount(self,customer,accountNumber):
        
        for account in customer.bankAccounts:
            if account.accountNumber == accountNumber:
                confirmationToDelete=input(f"Dear {customer.firstName +" "+customer.lastName}\n"
                                        "Are you sure that you request to delete the account below\n"
                                        f"Account Number: {account.accountNumber}\n"
                                        f"Balance: {account.balance}\n"     
                                        "(yes/no): ")
                
                if confirmationToDelete.lower()=="yes":
                    customer.bankAccounts.remove(account)
                    print("Account deleted successfully.")
                    return
                elif confirmationToDelete.lower()=="no":
                    return
                
                else:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                

        #if for loop is done and it is not broken, it means there is no such account number
        raise ValueError("NO SUCH ACCOUNT")
