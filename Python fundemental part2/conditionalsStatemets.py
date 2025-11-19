# if, elif, else

# age = int(input("enter age "))

# if age >= 18 :
#     print("you can vote")
# else:
#     print("user can not vote")

#-------------------------------------------

# color = input("enter color ")

# if color == "red":
#     print("stop")
# elif color == "green":
#     print("go")
# elif color == "yellow":
#     print("look")
# else:
#     print("enter right color")


#-----------------------------

# age = int(input("enter age "))

# if age < 13:
#     print("child")
# elif age>=13 and age<18:
#     print("teenager")
# else:
#     print("adult")

#--------------------------------------------

# username = input("enter user name ")
# password = input("enter user password ")

# if username == "admin" and password == "pass":
#     print("logedin sucessfully")
# elif username != "admin":
#     print("user name is not correct")
# elif username != "admin" and password != "pass":
#     print("username and password are not correct")
# else:
#     print("password is not correct")


#--------------------------------------------

# num = int(input("enter number "))

# if (num % 5) != 0:
#     print("num is not multiple of 5")
# else:
#     print("number is multiple of 5")


#--------------------- 

# num = int(input("enter a number "))

# if num%2 == 0:
#     print("even")
# else:
#     print("odd")


# Nesting

# username = input("enter user name ")
# password = input("enter user password ")

# if (username == "admin" and password == "pass"):
#     print("logedin sucessfully")
# else:
#     if (username != "admin"):
#         print("usernaem is not correct")
#     else:
#         print("password if not correct")


# Match Case 
# is alternative for if-elif-else case.

color = input("enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("Wrong Case")