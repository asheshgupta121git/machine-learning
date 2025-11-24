# class Student:
#     subject = 'python'
#     college = "ABC"
#     year = "4th year"

# stu1 = Student()
# stu2 = Student()
# print(stu1) #<__main__.Student object at 0x000001F17B026A50>  this is memory address where our stu1 is stored.
# print(stu2) #<__main__.Student object at 0x00000240E4F54A50>  this is memory address where our stu2 is stored.

# now to verify it is from same Student class we can print their property using dot (.) operator.

# print(stu1.subject , stu1.college, stu1.year)
# print(stu2.subject , stu2.college, stu2.year)

# print(Student)


# -------------------------------------------------------

# CONSTRUCTOR 
# it is basically that function that used to create an object

# in python to create construtor we have special metjod called   -->  __init__ <--

# this _init_ is special method that get called every time when we create a object. 

# if in our call we dont write any init methods python will automatically made it. 

# class Student:
#     sub = "python" # here python automatically made init method and call it also
#     # how we can define out init method
#     def __init__(self): # here self parameter storing curent instance of class or it is storing the refrence to the current object and this self is complasary parameter which is always need to write in this
#         print("this is constructor")



# stu1 = Student()
# print(stu1.sub)

# now let suppose we want to store diffrent name for every object.

# class Student:
#     def __init__(self, name, cgpa):
#         self.name = name
#         self.cgpa = cgpa


# stu1 = Student("ajay", 9.9)
# stu2 = Student("rahul",9.8)
# stu3 = Student("jai",9.7)

# print(stu1.name, stu1.cgpa)
# print(stu2.name, stu2.cgpa)
# print(stu3.name, stu3.cgpa)

#like how create a constructor method just like that we can create another instance methods.

# now suppose we want to create a method that return any student cgpa. 

# class Student:
#     def __init__(self, name, cgpa, age):
#         self.name = name
#         self.cgpa = cgpa
#         self.age = age
    
#     def get_cgpa(self): # new instance that return cgpa
#         return self.cgpa
    
#     def get_age(self):  # another instance that return age
#         return self.age

# stu1 = Student("ajay", 9.9, 21)
# stu2 = Student("rahul",9.8,22)
# stu3 = Student("jai",9.7,23)

# print(f"stu1 cpda is {stu1.get_cgpa()}")
# print(f"stu3 age is {stu3.get_age()}")


#-------------------------------------------
# types of constructor in python 
# default constructor --> have only self parameter
# parameterised constructor --> have more than self parameter.



# ------------------------------------------
# ATTRIBUTES it is basically a properties
'''
they are mostly two types 
class attributes --> belong to class (they are common) 
instance attributes --> belong to object (can be uinque and different)


for eg. 
college software --> class
name subject cgpa --> instance 
'''


# class Student:
#     #class attributes
#     college_name = "AKTU"
#     pi = 3.14
#     #instance attributes
#     def __init__(self, name, sub, cgpa):
#         self.name = name
#         self.sub = sub
#         self.cgpa = cgpa
#         self.pi = 3.1432

# stu = Student("ashesh", "aiml", 9.9)

# print(stu.name) #only invoked by object name 

# print(Student.college_name, stu.college_name) #invoked by both calss and object name

# # NOTE two attribute have same name in both class and instance then priority goes to instance one

# print(stu.pi)


#--------------------------------------------------------

# METHODS
'''
they are mostly 3 types
instance --> 
>it has compalsory frist paremater called self 
>and they can access class and instance attributes

class -->
>it has also compalsory frist parameter called cls
>and they only access class attribute only and nothing else
>in this we also use some decorator @classmethod it is basically a type of function take another function and changes its behaviour and return it.

static -->
>we create this methods when we dont want to create class attribute or instance attribute.
>it has not any parameter
>it can not access instance attributes and class attributes also
> they have decorator called @staticmethod

'''


# class Laptop:
#     storage_type = "SSD"

#     def __init__(self, RAM, storage):
#         self.RAM = RAM
#         self.storge = storage
    
#     def get_info(self): #instanced methods
#         print(f"the RAM is {self.RAM} and storage is {self.storge} and storage type is {self.storage_type}")

#     @classmethod
#     def get_stofage_type(cls): #class methods
#         print(f"storage type is {cls.storage_type}")

#     @staticmethod
#     def get_discount(price, descount):
#         final_price = price - (descount * price /100)
#         print(f"discounted price is {final_price}")

# lap1 = Laptop("32GB","2TB")
# #instance methods
# lap1.get_info()

# #calss methods
# lap1.get_stofage_type() # call with object name
# Laptop.get_stofage_type() # also called with class name


# #static methods
# lap1.get_discount(50_000, 10)

'''
PROBLEM 

Product store
-->Design & create an online store for Products (name, price).
-->Track total products being created.
-->Create a static method to calculate discount on each product based on a % parameter.
'''



class Store:
    count = 0

    def __init__(self, name, price):
        self.name =  name
        self.price = price
        Store.count +=1
    
    def get_info(self): #instance method
        print(f"product is : {self.name} and price is : {self.price}")

    
    @classmethod
    def get_product_count(cls): #class methods
        print(f"product in store = {cls.count}")
    
    @staticmethod 
    def get_discount(price, discount): #static methods
        final_price = (price - (price * discount / 100))
        print(f"the discounted price is {final_price}")


p1 = Store("phone", 10_000)
p2 = Store("laptop", 50_000)
p3 = Store("tablet", 30_000)

p1.get_info()

Store.get_product_count()

p1.get_discount(10_000, 12)
p3.get_discount(p3.price, 12)