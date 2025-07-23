# # #
# class Car:
#     brand = "BMW"
    
#     # def__init__(self):
#     # print("car obj has been started.")
    
#     def Start(self):
#         print(f"{self.brand} car has started....")
#         print(self)
        
# car1 = Car()
# print(car1)

# car1.Start()

# # #
# class Student:
#     college_name="DKTE"
    
#     def __init__(self, name, age, marks):#self(keyword)
#         self.name= name
#         self.age= age
#         self.marks= marks
    
#     def student_info(self):
#         print(f"Name= {self.name}")
#         print(f"Age= {self.age}")
#         print(f"Marks= {self.marks}")
#         print(f"College= {self.college_name}")
#         print("-----------")
        
# s1=Student("Pratiksha",21, 90)
# s1.student_info()

# s2=Student("Nikita",22, 95)
# s2.student_info()

# s3=Student("Rajnandini",20,85)
# s3.student_info()

# 1
class Student:
    name = "Patu"
    age= 000000
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
        
    @staticmethod # To ignore the compulsion of self keyword
    def welcome_msg():
        print(f"Welcome Student")
        
    @classmethod # Use cls as keyword
    def changeName(cls):
        cls.name= "Karan"
        cls.age= 24
        
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum += i
        
        avg= sum / 3
        return avg
    
s1=Student("Pratiksha", [95,90,85])
s1.welcome_msg()
ans= s1.get_avg()
print(f"{s1.name}'s avearage score is {ans}")
print("------------")

s2=Student("Nikita", [100,80,85])
s2.welcome_msg()
ans= s2.get_avg()
print(f"{s2.name}'s avearage score is {ans}")
print("------------")

s3=Student("Rajnandini", [80,90,97])
s3.welcome_msg()
ans= s3.get_avg()
print(f"{s3.name}'s avearage score is {ans}")
print("------------")

     
        
    

    

    
        