#bankaccount project
class balanceException(Exception):
    pass
class bankaccount:
    def __init__(self,initialAmount,accName):
        self.balance=initialAmount
        self.name=accName
        print(f"\n Account {self.name} created.\nBalance ={self.balance:.2f} ")
    def getBalance(self):
        print(f"\nAccount {self.name} balance= {self.balance}")
    def deposit(self,amount):
        self.balance=self.balance +amount
        print(f"\nDposit complete.\nAccount '{self.name}' balance = {self.balance:.2f}")

    #withdraw money here you check that there is anought momey to withdraw
    def viableTransaction(self,amount):
        if self.balance>= amount:#check that acc has anought money to withdraw if it has no anought mmoney then show   an error 

            return
        else:
            raise balanceException(f"\nSorry, account '{self.name}'only has a balance of '{self.balance:.2f}'")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)#if has anought money than call it again and decrese amount to the main account 

            self.balance=self.balance-amount
            print("\nWithdraw complete")
            self.getBalance()# then show the amount after withdraw

        except balanceException as error:
            print(f"\nwithdraw interrupted : {error}")

    def transfer(self,amount,account):#here acc is  sara  we wanr to rransfer this amount to sara 
        try:
            print("\n***********\n\nBeginning Transfer..")
            self.viableTransaction(amount)#checl anought money to send sara
            self.withdraw(amount)#if anought monet then  withdraw the money and send sara 
            account.deposit(amount)#deposit the money to sara account 
            print("\nTransfer Complete!\n\n*******")#then print complete that successfully transfer

        except balanceException as error:
            print(f"\nTransfer interruped {error}")

class interestRewardsAcct(bankaccount):#when we create a obj of this childe class all the method call in this child class 
#but here override deposit method of oarent class 
    def deposit(self,amount):
        self.balance=self.balance+(amount*1.05)
        self.getBalance()
#inherit all the class of parent clas  
class savingAcct(interestRewardsAcct):
    def __init__(self,initialAmount,accName):
        super().__init__(initialAmount,accName)
        self.fee=5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\neithdraw complete")
            self.getBalance()
        except balanceException as error:
            print(f"\nwithdraw interrupted: {error}")
        

     
                
            

