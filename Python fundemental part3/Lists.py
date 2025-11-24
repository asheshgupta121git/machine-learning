# mutable sequence of values. 

# marks = [99,88,77,66,22]

# print(marks)
# print(len(marks)) #length 
# print(marks[4]) # single value
# print(type(marks)) # type of list 

# marks[3] =55  # value updation
# print(marks)


# slicing in list 

# it is done same as string
# print(marks[1:5])

#--------------------------------

# list methods.

# nums = [1,3,2,4]

# nums.append(6)
# print(nums)

# # insert at desired place 
# nums.insert(4,5)
# print(nums)

# # to sort list 
# nums.sort()
# print(nums)

# # sort reverse order 
# nums.sort(reverse=True)
# print(nums)

# # print list in reverse order 

# nums.reverse()
# print(nums)


# ---------------------

# list with loops 

# nums = [1,2,3,4,5]

# for val in nums:
#     print(val)


# wap to print index of 10 using loops in list 
arr = [1,4,3,6,7,9,10,32,15,23]
x = 10
idx = 0

for val in arr:
    if (x == val):
        print(f"{x} found at index {idx}")
        break
    else:
        idx +=1



