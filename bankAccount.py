
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