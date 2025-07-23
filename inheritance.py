# # # Polymorphism
# class Complex:
    
#     def __init__(self, real,img):
#         self.real = real
#         self.img = img
        
#     def get_output(self):
#         print(f"{self.img}i + {self.real}j")
        
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal,newImg)
    
# c1 = Complex(3,2)
# c1.get_output()

# c2 = Complex(4,5)
# c2.get_output()

# c3 = c1 + c2
# c3.get_output()

# class Complex:
    
#     def __init__(self, real,img):
#         self.real = real
#         self.img = img
        
#     def get_output(self):
#         print(f"{self.img}i + {self.real}j")
        
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal,newImg)
    
# c1 = Complex(3,2)
# c1.get_output()

# c2 = Complex(2,1)
# c2.get_output()

# c3 = c1 - c2
# c3.get_output()

# 1
# class Circle:
    
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         Area=3.14*self.radius**2
#         return Area
    
#     def peri(self):
#         Peri=2*3.14*self.radius
#         return Peri
    
# c1= Circle(5)
# print(f"Area of the circle : {c1.area()}")
# print(f"Perimeter of the circle : {c1.peri()}")

# # # Inheritance    
# 2
# class Employee:
    
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
        
#     def showDetails(self):
#         print(f"Role is : {self.role}")
#         print(f"Department is : {self.department}")
#         print(f"Salary is : {self.salary}")
        
# class Engineer(Employee):
    
#     def __init__(self, name, age, role, department, salary):
#         super.__init__(role, department, salary)
#         self.name= name
#         self.age= age
        
#     def showDetails(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Role: {self.role}")
#         super.showDetails()
        
# e1= Engineer("Pratiksha", 21, "Student", "CSE", 30_000)
# e1.showDetails()
     
# # # Lambda Function
# Addition
# add=lambda a,b:a+b
# print(add(3,2))

# Max a,b
# mx=lambda a,b:a
# print(mx(10,5))

# # # Exception Handling
# print(2/0)

# try:
#     a=int(input("Enter a number:"))
#     result = 10/a
#     print("Result",result)

# except ZeroDivisionError:
#     print("Error: You can't divisible by zero")
    
# except ValueError:
#     print("Error: Invalid input, please enter a valid number.")
    
# except Exception as e:
#     print(f"unexceptrg ERROR")

# else:
#     print(f"NO ERROR!!!")

# finally:
#     print(f"I will always be executed.")

# age=20
# if(age < 18 or age > 60):
#     raise Exception("age is not according to requirement")
# print(age)