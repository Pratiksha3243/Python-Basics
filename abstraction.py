# # # Abstraction
# class Car:
    
#     def __init__(self):
#         self.acc= False
#         self.clutch= False
#         self.brake= False
        
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car has started....")
        
#     def stop(self):
#         self.acc= False
#         self.brake= True
#         print("Car has stopped....")
        
# c1= Car()
# c1.start()
# c1.stop()
    
# # # Encapsulation
# class Account:
    
#     def __init__(self, accNo, acc_pass):
#         self.accNo = accNo
#         self.__acc_pass = acc_pass
        
#     def checkPass(self):
#         print(self.__acc_pass)
        
# a1 = Account("123456" , "Pratiksha")
# print(a1.accNo)
# a1.checkPass()

# 1
# class Account:
    
#     def __init__(self, balance, accNo, acc_pass):
#         self.balance = balance
#         self.accNo = accNo
#         self.acc_pass = acc_pass
    
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Rs.{amount} has been credited")
           
#     def withdraw(self , amount):
#         if(self.balance > 0):
#             self.balance -= amount
#             print(f"Rs. {amount} has been debited")
        
        
#     def check_balanace(self):
#         print(f"Total Amount is Rs {self.balance}")
        
#     def checkPass(self):
#         print(f"Your password is {self.acc_pass}")
        
        
# a1 = Account("123456789" , "Patu" , "30_000")
# a1.deposit(20_000)
# a1.withdraw(40_000)
# a1.check_balance()
        
# 