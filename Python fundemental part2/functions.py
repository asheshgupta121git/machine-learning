# function are block of statement that perform spefic task 
# it has 2 parts 
# function definition
# function calling 


# function to print hello

def hello():
    print("hello")

hello()


# value we take in function called parameter of function

def sum(a,b):
    return a+b

print(sum(3,4))

# function take 3 number as input and return their average

def calAvg(a,b,c):
    return (a+b+c)/3

print(calAvg(2,3,4))


# for parameter we can pass default value also to out parameter. 

def defaultSum(a,b=5):
    return a+b

print(defaultSum(3))

# Types of function in python 
'''
built in funcion 
print() input() type() range()

user defined function --> this is created by us.
'''


# Lambda function -- these are anonmous function created by lambda keyword.

# lambda a,b,c : expression

lambdaSum  = lambda a,b : a+b

print(lambdaSum(4.0,2.3))

# the lambda function main usage in high order function. 
# high order function is that function that passed as an argument to another function. 

# wap to print factorial of number n


def fact(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

num = int(input("enter number : "))
print(fact(num))