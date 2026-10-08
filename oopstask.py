#Level 1 — Basic Class & Object
'''1. Student Class
Create a class Student with:
name
age
Create two objects and display their details.
Expected idea:
Student 1 → Rahul, 20
Student 2 → Priya, 21'''
# class Student:
#     name = ""
#     roll = 0
# s1 = Student()
# s1.name = "Rahul"
# s1.roll = 20
# print(s1.name,s1.roll)
# s2 = Student()
# s2.name = "Priya"
# s2.roll = 21
# print(s2.name,s2.roll)

'''2. Employee Class
Create a class Employee with:
name
salary
Create three employee objects and display their details.'''
# class Employee():
#     name = ""
#     sal = 0
# e1 = Employee()
# e1.name = "Vamsi"
# e1.sal = 50000
# print(e1.name,e1.sal)
# e2 = Employee()
# e2.name = "Lavanya"
# e2.sal = 30000
# print(e2.name,e2.sal)
# e3 = Employee()
# e3.name = "Akash"
# e3.sal = 40000
# print(e3.name,e3.sal)

'''3. Car Class
Create a class Car with:
brand
model
price
Create two objects and print their details.'''
# class Car:
#     brand = ""
#     model = ""
#     price = 0
# c1 = Car()
# c1.brand = "Mahindra"
# c1.model = "Thar"
# c1.price = 700000
# print(c1.brand,c1.model,c1.price)
# c2 = Car()
# c2.brand = "Mahindra"
# c2.model = "Scorpio"
# c2.price = 600000
# print(c2.brand,c2.model,c2.price)


#Level 2 — Constructor + Instance Variables
'''4. Student Details
Create a Student class with a constructor that accepts:
name
branch
age
Create three students and display their details.'''
# class Student:
#     def __init__(self,name,branch,age):
#         self.n = name
#         self.b = branch
#         self.a = age
# s1 = Student("Chitti","CSE",22)
# print(s1.n,s1.b,s1.a)
# s2 = Student("Lavu","ECE",22)
# print(s2.n,s2.b,s2.a)
# s3 = Student("Moni","ECE",22)
# print(s3.n,s3.b,s3.a)

'''5. Rectangle
Create a class Rectangle.
The constructor should accept:
length
breadth
Create a method area() that returns the area.
Example:
Input:
length = 10
breadth = 5
Output:
Area = 50'''
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.len = length
#         self.bre = breadth
#     def area(self):
#         area = self.len*self.bre
#         print(area)
# r = Rectangle(10,5)
# r.area()

'''6. Bank Account
Create a class BankAccount with:
account holder name
account number
balance
Create methods:
display()
deposit(amount)
withdraw(amount)
Use the constructor to initialize the account details.'''
# class Bank:
#     def __init__(self,aname,ano,bal):
#         self.name = aname
#         self.num = ano
#         self.bal = bal
#     def display(self):
#         print(self.name)
#         print(self.num)
#         print(self.bal)
#     def deposit(self,amount):
#         self.bal += amount
#         print(self.bal)
#     def withdraw(self,amount):
#         self.bal -= amount
#         print(self.bal)
# b = Bank("Lavanya",98765421567,1000)
# b.display()
# b.deposit(500)
# b.withdraw(200)

#Level 3 — Instance Methods + Parameters + Return
'''7. Calculator
Create a class Calculator with methods:
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
Each method should return the result.'''
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def subtract(self,a,b):
#         return a-b
#     def multiply(self,a,b):
#         return a*b
#     def divide(self,a,b):
#         return a/b
# c = Calculator()
# print(c.add(10,5))
# print(c.subtract(10,5))
# print(c.multiply(10,5))
# print(c.divide(10,5))

'''8. Student Result
Create a class Student with:
name
marks
Create a method:
get_result()
Return:
"Pass" → marks >= 40
"Fail" → marks < 40'''
# class Student:
#     def __init__(self,name,marks):
#         self.n = name
#         self.m = marks
#     def get_result(self):
#         if self.m >= 40:
#             return "Pass"
#         else:
#             return "Fail"
# s = Student("Lavanya",56)
# print(s.get_result())

'''9. Student Grade
Create a class Student with:
name
marks
Create a method get_grade() that returns:
90–100 → A
75–89  → B
60–74  → C
40–59  → D
Below 40 → Fail'''
# class Student:
#     def __init__(self,name,marks):
#         self.n = name
#         self.m = marks
#     def get_grade(self):
#         if self.m >= 90:
#             return "A"
#         elif self.m >= 75:
#             return "B"
#         elif self.m >= 60:
#             return "C"
#         elif self.m >= 40:
#             return "D"
#         else:
#             return "Fail"
# s = Student("Lavanya",77)
# print(s.get_grade())

#Level 4 — Class Variables + Class Methods
'''10. College Details
Create a class Student with:
college = "10000 Coders"
Create a class method:
show_college()
which displays the college name.
Create two student objects and call the class method.'''
# class Student:
#     college = "10000 Coders"
#     @classmethod
#     def show_college(cls):
#         print(cls.college)
# s1 = Student()
# s1.show_college()
# s2 = Student()
# s2.show_college()

'''11. Company Employees
Create a class Employee with:
company = "ABC Technologies"
Each employee should have:
name
salary
Create:
display_employee()
show_company()
display_employee() should display individual employee information.
show_company() should display the common company name.'''
# class Employee:
#     company = "ABC TECHNOLOGIES"
#     def __init__(self,name,sal):
#         self.n = name
#         self.s = sal
#     def display_employee(self):
#         print(self.n)
#         print(self.s)
#     @classmethod
#     def show_company(cls):
#         print(cls.company)
# e1 = Employee("Lavanya",30000)
# e1.show_company()
# e1.display_employee()
# e2 = Employee("Akash",40000)
# e2.show_company()
# e2.display_employee()
        
'''12. School Student Counter 
Create a class Student.
Every time a student object is created, increase the number of students.
Example:
s1 = Student("Rahul")
s2 = Student("Priya")
s3 = Student("Anil")
Create a class method:
show_count()
Expected output:
Total Students: 3'''
# class Student:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         Student.count += 1
#     @classmethod
#     def show_count(cls):
#         print("Total Students:",cls.count)
# s1 = Student("Rahul")
# s2 = Student("Priya")
# s3 = Student("Anil")
# Student.show_count()

#Level 5 — Static Methods
'''13. Calculator Static Methods
Create a class Calculator with static methods:
add(a, b)
multiply(a, b)
square(n)
Call them without creating an object.
Example:
Calculator.add(10, 20)'''
# class Calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @staticmethod
#     def mult(a,b):
#         return a*b
#     @staticmethod
#     def square(n):
#         return n*n
# print(Calculator.add(10,20))
# print(Calculator.mult(2,5))
# print(Calculator.square(8))

'''14. Number Checker
Create a class NumberChecker with static methods:
is_even(n)
is_odd(n)
is_positive(n)
Each method should return True or False.'''
# class NumberChecker:
#     @staticmethod
#     def is_even(n):
#         if n%2==0:
#             return True
#         else:
#             return False
#     @staticmethod
#     def is_odd(n):
#         if n%2!=0:
#             return True
#         else:
#             return False
#     @staticmethod
#     def is_positive(n):
#         if n>=0:
#             return True
#         else:
#             return False
# print(NumberChecker.is_even(7))
# print(NumberChecker.is_odd(7))
# print(NumberChecker.is_positive(7))

#Level 6 — Combined Questions 🔥
'''15. Student Management
Create a Student class with:
Class variable:
college = "10000 Coders"
Instance variables:
name
branch
marks
Create:
display()
get_result()
methods.
Also create a class method:
show_college()
And a static method:
is_valid_marks(marks)
Use all of them with student objects.'''
# class Student:
#     college = "10000 coders"
#     def __init__(self,name,branch,marks):
#         self.n = name
#         self.b = branch
#         self.m = marks
#     def display(self):
#         print(self.n)
#         print(self.b)
#         print(self.m)
#     def get_result(self):
#         if self.m >= 35:
#             return "PASS"
#         else:
#             return "FAIL"
#     @classmethod
#     def show_college(cls):
#         print(cls.college)
#     @staticmethod
#     def is_valid_marks(n):
#         if n>0 and n<100:
#             print("Valid marks")
#         else:
#             print("Not valid marks")
# s = Student("Lavanya","ECE",77)
# s.display()
# print(s.get_result())
# s.show_college()
# s.is_valid_marks(-2)

'''16. Bank Management ⭐
Create a BankAccount class with:
Instance variables:
name
account_number
balance
Instance methods:
deposit()
withdraw()
check_balance()
Class variable:
bank_name = "ABC Bank"
Class method:
show_bank_name()
Static method:
validate_amount(amount)
Students should use all three types of methods.'''
# class BankAccount:
#     bank_name = "ABC Bank"
#     def __init__(a,name,account_number,balance):
#         a.name = name
#         a.account_number = account_number
#         a.balance = balance
#     def deposit(a,amount):
#         a.balance += amount
#         print(amount)
#     def withdraw(a,amount):
#         if amount <= a.balance:
#             a.balance -= amount
#             print(amount)
#         else:
#             print("Insufficient balance")
#     def check_balance(a):
#         print(a.balance)
#     @classmethod
#     def show_bank_name(cls):
#         print(cls.bank_name)
#     @staticmethod
#     def validate_amount(amount):
#         if amount > 0:
#             return True
#         else:
#             return False
# b = BankAccount("Lavanya",3876598765,5000)
# b.deposit(1000)
# b.withdraw(2000)
# b.check_balance()
# b.show_bank_name()
# print(BankAccount.validate_amount(500))

'''17. Product Management 🔥
Create a Product class with:
product_name
price
quantity
Create an instance method:
calculate_total()
which returns:
price × quantity
Create a class variable:
company = "ABC Store"
Create a class method:
show_company()
Create a static method:
is_valid_price(price)
which returns True if price is greater than 0.'''
# class Product:
#     company = "ABC STORE"
#     @classmethod
#     def show_company(cls):
#         print(cls.company)
#     def __init__(self,product_name,price,quantity):
#         self.pname = product_name
#         self.price = price
#         self.quan = quantity
#     def calculate_total(self):
#         return self.price * self.quan
#     @staticmethod
#     def is_valid_price(price):
#         if price>0:
#             print("Valid Price")
#         else:
#             print("Not a valid Price")
# p = Product("Panipuri",20,2)
# p.show_company()
# print(p.calculate_total())
# p.is_valid_price(20)

'''18. Employee Salary System 🔥
Create an Employee class with:
name
basic_salary
Create a method:
calculate_salary()
Return the salary after adding:
HRA = 20% of basic salary
DA = 10% of basic salary
Also create:
company = "ABC Technologies"
and a class method to display the company.'''
class Employee:
    company = "ABC Technologies"
    @classmethod
    def show_company(cls):
        print(cls.company)
    def __init__(self,name,basic_salary):
        self.n = name
        self.sal = basic_salary
    def calculate_salary(self):
        HRA = self.sal *(20/100)
        DA = self.sal *(10/100)
        total = self.sal + HRA + DA
        print(total)
e = Employee("Lavanya",30000)
e.show_company()
e.calculate_salary()

