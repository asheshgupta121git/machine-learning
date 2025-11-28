# oop pillars 
# there are 4 mail pillars in this.
'''
1- encapsulation
2-  Abstraction
3- inheritance
4- polymorphism
'''

# Encaspusulation
# wrapping data and function into single unit. 
# basically we bing our data and methods in single calss
# in this we do data hiding measn securing senstive information. 

'''data higing arrtibutes -> 
1. public attribute (who are accessible by every function inside and outside of class)
2. protected -> access in class and in sub class.
3. private -> only accessible inside the class. 
'''

'''
to make any attribute protected we have to use underscore(_)
and to make any attribute private we have to use double underscore (__)
'''

# class bankAccount:
#     def __init__(self, name, balance,accountNo):
#         self.name = name  # public
#         self._balance = balance #protected (only access in calss and subclass)
#         self.__accountNo = accountNo # private (only accessible by calss) --> this lead to data manging

#     def get_accountNo(self): # this is getter function
#         return self.__accountNo
    
#     def set_accountNo(self, newAccount):
#         self.__accountNo = newAccount

# acc1 = bankAccount("rahul", 100_000,"x0x0x0x")
'''now by convention we can create protected attribute but cant force it be protected it is just convention that if create any attribute protected then we dont have to access it directly.

but in the case of private it works so to give the access to private attribute we have to use getters and setters
'''
# print(acc1.name, acc1._balance)

# print(acc1.get_accountNo()) # getting private account number using getter method
# acc1.set_accountNo("o0o0o0") # setting value of private account number using setter method
# print(acc1.get_accountNo())

'''
NOTE in python if we want we can access the private attribute directly aslo. like below
objName._calssName__privateAttributeName
'''
# print(acc1._bankAccount__accountNo)

#NOTE thats why in python their is noting like true protect or true private attribute it is just layer who all developers follow.

#---------------------------
# INHERITANCE
#reusing attribute and methods from parent(base) class.


# class EMP:
#     start_time = "10AM"
#     end_time = "6PM"

#     def change_time(self, newEndTime):
#         self.end_time = newEndTime

# class Teacher(EMP):
#     def __init__(self, subject):
#         self.subject  = subject

# class AdminStaff(EMP):
#     def __init__(self, role):
#         self.role = role

# t1 = Teacher("maths")
# t1.change_time("9PM")

# print(t1.subject , t1.start_time, t1.end_time) # access all the property of EMP class  also

# admin1 = AdminStaff("manager")

# print(admin1.role, admin1.start_time, admin1.end_time)

'''
Type of inheritance 
-->singel level inheritance 
-->multi level inheritance
--> multiple inheritance
'''

# multilevel inheritance 
# class EMP:
#     start_time =  "10AM"
#     end_time = "6PM"

# class AdminStaff(EMP):
#     def __init__(self, role):
#         self.role =  role

# class Accounts(AdminStaff):
#     def __init__(self, salary, role):
#         self.salary = salary
#         super().__init__(role) #with the super keyword we cal call the constructor of parent class

# acc1 = Accounts(10_000, "manager")

# print(acc1.salary, acc1.role, acc1.start_time, acc1.end_time)

# multiple inheritance 
# class Student:
#     def __init__(self, gpa):
#         self.gpa = gpa

# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary

# class TA(Student, Teacher):
#     def __init__(self, gpa, salary, name):
#         super().__init__(gpa)
#         Teacher.__init__(self,salary)
#         self.name = name

# Ta1 = TA(9.4, 40_000, "rajan")

# print(Ta1.name,Ta1.salary, Ta1.gpa)


#-----------------------------------------------

#Abstraction
#Hiding internal details & show only essential features.
# in this we talk about abstract class that is basically blueprint for other class.

# from abc import ABC, abstractmethod


# class Animal(ABC):
#   @abstractmethod
#     def sound(self):
#         pass

# class Lion(Animal):
#     def sound(self):
#         print("roar")

# class Cow(Animal):
#     def sound(self):
#         print("moo")


# Lion = Lion()
# Lion.sound()

# Cow = Cow()
# Cow.sound()


# --------------------------------------

# Polymorphism
# in this we create multiple methods with same name but with different functions. 

# operator overloading -> like + opearator used for add of number and concation of string.

# function overridding 
'''
in only done where inheritance invoved means if a function present in parent and we re define that function in child class then it is function over ridding.
--> redefining parent class function in child class
'''

# class Emp:
#     def get_designation(self):
#         print("get designation = emp")

# class Teacher(Emp):
#     def get_designation(self):
#         print("get designation = teacher")

# t1 = Teacher()
# t1.get_designation()


#ducktuping

# walks like a duck and quacks like a duck
class Teacher():
    def get_designation(self):
        print("get designation = teacher")

class Accountant():
    def get_designation(self):
        print("get designation = accoutant")


t1 = Teacher()
t1.get_designation()

a1 = Accountant()
a1.get_designation()