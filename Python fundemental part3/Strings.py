# String store sequence of charactor
# word = "python"
# to print length we have len function

# print(len(word))

# contication adding two or more string
# word2 = "data science"
# print(word +" "+ word2)


# indexing string can be printed by indexing also

# print(word2[2])

# we can also use for loop 

# for ch in word2:
#     print(ch)


# --------------------------------------------
# Operation in string.

# Slicing.
# used to slice string (give  a protion)

# str = "python"
# print(str[2:4])

# str2 = "Ashesh Gupta"
# print(str2[2:])
# print(str2[:])



# String Formatting. 

# formate() --> intoduced in python3 in this we use placeholders.
# a = 5
# b = 8
# sum = a+b

# print("sum of a and b is {} ".format(sum))
# print("language is {}".format("python")) # we can passing string also
# print("sum of {} and {} is {}".format(a,b,sum))

#index based formating
# print("sum of {1} and {0} is {2}".format(a,b,sum))

#value based formating. 
# print("sum of {c} and {d}".format(c=10,d=20))

# f-string --> introduced in version 3.6 in this we use literal string interpolation.

a= 5
b= 4

print(f"sum of {a} and {b} is {a+b}")
