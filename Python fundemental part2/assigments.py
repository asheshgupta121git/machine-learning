# question 1 


# def calculateTax(s):
#     if(s < 30000):
#         return (5*s)/100
#     elif(s>30000 and s<70000):
#         return (15*s)/100
#     else:
#         return(25*s)/100

# salary = int(input("enter salary : "))
# res = calculateTax(salary)
# print(res)


# question 2

# def allEven(a,b):
#     for i in range(a,b+1):
#         if (i%2 == 0):
#             print(i)
            
# num1 = int(input("enter num1  : "))
# num2 = int(input("enter num2  : "))
# allEven(num1 , num2)

# question 3

# def seperateDigits(num):
#     while(num  >0):
#         a = num%10
#         print(a)
#         num = num //10
    
# num = int(input("enter number : "))
# seperateDigits(num)

 # NOTE In Python, / gives the true (float) division result, while // gives the floor (integer) division result by discarding the fractional part.​

# Question4

# def count(num):
#     c = 0
#     while(num > 0):
#         c = c+1
#         num = num//10
#     print(c)

# count(int(input("enter the number : ")))


# Question 5

# def sum(num):
#     s = 0
#     while(num > 0):
#         s = s + num%10
#         num = num//10
#     print(s)

# sum(int(input("enter number : ")))

# Question 6 

# for i in range(1, 101):
#     if(i % 3 == 0 and i % 5 == 0):
#         print(i)

# Question 7

# while(True):
#     ask  = input("enter a number or 'quit' to exit : ")
#     if(ask == "quit"):
#         print("you quited")
#         break
#     else:
#         ask = int(ask)
#         if ask > 0 :
#             print("positive")
#         elif ask < 0 :
#             print("negative")
#         else:
#             print("zero")


# question 8

# def calc(num1, num2, operation):
#     match operation:
#         case '+':
#             print("output is : ", num1+num2)
#         case '-':
#             print("output is : ", num1-num2)
#         case '*':
#             print("output is : ", num1*num2)
#         case '/':
#             print("output is : ", num1//num2)
#         case _:
#             print("enter correct value")

# num1 = int(input("enter the frist value : "))
# operation = input("enter operation to perform : ")
# num2 = int(input("enter the second value : "))

# calc(num1, num2, operation)
            

# Question 9

# def prime(num):
#     if num < 1 :
#         return print(False)
#     for i in range(2,num):
#         if num % i == 0:
#             return print(False)
#     return print(True)

# prime(int(input("print prime : ")))

# Question 10

# guess = int(input("enter a guess : "))
# num = 23

# while(True):
#     if num == guess:
#         print("correct")
#         break
#     elif num > guess:
#         guess = int(input("Too small guess again : "))
#     else:
#         guess = int(input("Too Big guess again : "))
        




