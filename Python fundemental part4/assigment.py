# Question 1 solution 

# class BankAcc:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
    
#     def deposit(self, deposite):
#         self.balance = self.balance + deposite
    
#     def withdraw(self, withdraw):
#         self.balance = self.balance - withdraw
    
#     def check_balance(self):
#         print(self.balance)


# ac1 = BankAcc("x0x0x0", "ashesh", 10_000)

# print(ac1.account_number, ac1.owner_name, ac1.balance)

# ac1.deposit(10_000)
# ac1.check_balance()

# ac1.withdraw(5_000)
# ac1.check_balance()


# Question 2 Solution

# class Book:
#     count = 0
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.list_of_reviews = []
    
#     def new_review(self, new_review):
#         self.list_of_reviews.append(new_review)
    
#     def count_reviews(self):
#         print(len(self.list_of_reviews))
    
#     def all_reviews(self):
#         print(self.list_of_reviews)

# b1 = Book("harry potter", "jk rolling")

# print(b1.author, b1.title)

# b1.new_review('good book')
# b1.new_review('best novel')
# b1.new_review('just magical')
# b1.new_review('best seller')
# b1.count_reviews()
# b1.all_reviews()


# Question 3 Solution 

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self._name = name
#         self._roll_no= None
#         self._marks = None

#         self.set_name(name)
#         self.set_roll(roll_no)
#         self.set_marks(marks)

#     # setter functions

#     def set_marks(self, newmarks):
#         if newmarks >= 0:
#             self._marks = newmarks
#         else:
#             print("can't enter negative number")
        
    
#     def set_roll(self, rollNo):
#         if rollNo > 0 and rollNo<=100:
#             self._roll_no = rollNo
#         else:
#             print("roll can't be more that 100 and less than 0")
    
#     def set_name(self, name):
#         if name.strip() != "":
#             self._name = name
#         else:
#             print("please enter name")
    
#     # getter functions

#     def stu_info(self):
#         print(self._name, self._roll_no, self._marks)

# st1 = Student("ashesh", -21, 12)

# st1.set_roll(34)
# st1.stu_info()


# Question 4 Solution 

# class Shape:
#     def area(self):
#         print("this is area")

# class Circle(Shape):
#     def area(self):
#         print("this is circle area")

# class Rectangele(Shape):
#     def area(self):
#         print("this is Rectangle area")

# class Trinagle(Shape):
#     def area(self):
#         print("this is Trinagle area")


# c1 = Circle()
# c1.area()



# Question 5 Solution.

# class Vechile:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
# class Car(Vechile):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

# class Bike(Vechile):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc


# b1 = Bike("hero", 2025, "350cc")
# print(b1.model, b1.brand, b1.engine_cc)

# c1 = Car("BMW", 2025, 4)
# print(c1.model, c1.brand, c1.seats)


# Question 6 Solution 
# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self,amt):
#         pass

# class Intern(Employee):
#     def calculate_salary(self, amt):
#         self.amt = amt*1
#         print(self.amt)


# class FullTimeEmployee(Employee):
#     def calculate_salary(self,amt):
#         self.amt = amt*2
#         print(self.amt)


# class ContractEmployee(Employee):
#     def calculate_salary(self, amt):
#         self.amt = amt*3
#         print(self.amt)

# i1 = Intern()
# i1.calculate_salary(34)

# f1 = FullTimeEmployee()
# f1.calculate_salary(34)

# c1 = ContractEmployee()
# c1.calculate_salary(34)

# Question 7 Solution

# class Person:
#     def __init__(self, name, age = None, address = None):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def get_person_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Address:", self.address)

# p1 = Person("ashesh")
# p1.get_person_info()

# p2 = Person("ashesh", 23)
# p2.get_person_info()

# p3 = Person("ashesh", 23, "varansi")
# p3.get_person_info()


# Question 8 Solution 

# class Person:
#     player_count = 0

#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#         Person.player_count +=1
    
#     @classmethod
#     def playerCreated(cls):
#         print(cls.player_count)

# p1 = Person("ajay", 1)
# p2 = Person("aja", 2)
# p3 = Person("aj", 3)

# Person.playerCreated()


# Question 9 Solution

# class Herbivore:
#     eat = "plants"

#     def teeth(cls):
#         print("have usually flat teeth")

# class Carnivore:
#     lives = "jungle"

# class Omnivore:
#      def eatin_habits(cls):
#          print("eats both plant and animals")

# class Bear(Herbivore, Carnivore, Omnivore):
#     honey = "honey lovers"

# b1 = Bear()
# print(b1.eat, b1.honey, b1.lives)
# b1.teeth()
# b1.eatin_habits()


# Question 10 Solution 
# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_count = 1  # simple count

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_count
        Message.message_count += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)  # Show message to all users

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()


# ---------------------------------------
# Example Usage
# ---------------------------------------
if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")
    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()

