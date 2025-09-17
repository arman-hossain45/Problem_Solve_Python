
#folder name this is oopProject and 
#annd class name is bankaccount 
from oopProject import*
 
Arman=bankaccount(1000,"arman")
sara=bankaccount(200,"sara")

Arman.getBalance()
sara.getBalance()
Arman.deposit(1500)

Arman.withdraw(100000)
Arman.withdraw(100)
Arman.transfer(10000,sara)
Arman.transfer(100,sara)

jim=interestRewardsAcct(500,'jim')#when we create a obj of this childe class all the method call in this child class 
   #but here override deposit method of oarent class 
jim.getBalance()
jim.deposit(100)
jim.transfer(100,Arman)

shawon=savingAcct(400,"shawon")
shawon.getBalance()
shawon.deposit(100)
shawon.transfer(56,sara)
