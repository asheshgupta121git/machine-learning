# to do same task again and again

# While loop 
# it will do a task untill the condition it true

# counter = 1  #iterator

# while (counter<=5):
#     print("hello world", counter)
#     counter+=1

#------------------------

# i = 5

# while (i>=1):
#     print(i)
#     i-=1

# NOTE majorty loops start with one


#-----------------------------------

# Table of any number n 

# num = int(input("enter number: "))

# i=1
# while (i<=10):
#     print(num, "*",i," = ", i*num)
#     i += 1

#-------------------------------------

# break and Continue
#break is used to terminate the loop

# when number is 6 get out of loop

# i=0

# while (i<10):
#     if (i == 6):
#         break
#     print(i)
#     i += 1

# print("outside of loop")


# numbe is 6 skip it

# i=0

# while (i<10):
#     if (i == 6):
#         i+=1
#         continue
#     print(i)
#     i += 1

# print("outside of loop")

#------------------------------
# print all odd number from 1 to 10

# i = 1

# while (i <= 10):
#     if(i % 2 == 0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# -----------------------------------------

# For loops 
# generally we use for loop for sequential traversal

# string = "ashesh"

# in is here membership operator it work is to check presence.
# for ch in string:
#     print(ch)

# and to run for loop in sequence of number 

# print number form 0 to 5
# for i in range(5):
#     print(i)


# ------------------------------
# print number of i in string 

# word =  "artificial intelligence"

# ans = 0 
# for i in word:
#     if(i == "i"):
#         ans +=1

# print(ans)


# ---------------------------------------
# Print vowel count of a given string

# word = "artificiale"

# ans = 0
# for i in word:
#     if( i == "a" or  i == "e" or  i == "i" or  i == "o" or  i == "u"):
#         ans +=1

# print(ans)

#------------------------------
# range() function
'''
it is used for sequence generation
it have 3 values start stop and step 
eg - range(start, stop, step)
in this stop is mendiator to give.
and by defalut value of start is 0 and step is +1

some eg. 
range(5) -- 0,1,2,3,4
range(1,6) -- 1,2,3,4,5
range(1,10,2) -- 1,3,5,7,9
'''

# for i in range(5):
#     print(i)

# print("----------------")
# for i in range(1,6):
#     print(i)

# print("----------------")
# for i in range(1,10,2):
#     print(i)

# print("----------------")

# ---------------------------------
# print sum of frist n natural numbers

num = int(input("enter the number "))

sum = 0 
for i in range(1,num+1):
    sum +=i  

print("sum of n natural number is : ",sum)
