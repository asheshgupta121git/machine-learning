# [output for item in iterable if condition]

# suppose we need square of a number in range 

'''square = []

for i in range(1,6):
    square.append(i*i)

print(square)'''

# same above thisn we can do with list compharision

square = [i*i for i in range(6)]
print(square)

# now we want to store odd number square

oddSqr = [i*i for i in range (6) if i%2 != 0]

print(oddSqr)

# replace all negative number with zero. 

inp = [-2,-4,3,5,2,-1]

res = [0 if val<0 else val for val in inp]

print(res)

# convert the string in uppercase

inp2 = ["java", "python", "ml", "ai"]

res2 = [val.upper() for val in inp2]
print(res2)