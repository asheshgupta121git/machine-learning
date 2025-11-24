# question 1 Solution 

# str = input("enter string: ")
# str2 = ""
# for ch in str:
#     print(ch)
#     str2 = ch + str2
#     print(ch,str2)

# print(f"str = {str} and str2 = {str2}") 
# if(str == str2):
#     print(True)
# else:
#     print(False)

# Question 2 solution

# list = [1,2,3,4,5,6]
# sum = 0
# for i in list:
#     sum += i

# avg = sum / len(list)

# print(avg)

# Question 3 Solution

# n = int(input("enter the size of list1: "))

# list1 = []
# for i in range(n):
#     val = int(input("enter the value of list: "))
#     list1.append(val)

# m = int(input("enter the size of list2: "))

# list2 = []
# for i in range(m):
#     val = int(input("enter the value of list: "))
#     list2.append(val)

# print(f"list one is {list1} and list two is {list2}")
# print(f"after merging the is result is {list1 +  list2}")
# merged_list =  list1+ list2
# merged_list.sort()
# print(f"merged list after sorting {merged_list}")


# Question 4 solution 

# tup = (1,2,3,4,5,6,7,8,9)
# even = []
# odd = []
# for val in tup:
#     if(val%2 == 0):
#         even.append(val)
#     else:
#         odd.append(val)

# even = tuple(even)
# odd = tuple(odd)
# print(f"even is {even} and odd is {odd}")


# question 5 solution 

# info = {
#     "ajay" : 12,
#     "rahul":34,
#     "jai" : 45
# }

# while True:
#     print(type(info))
#     ops = input("enter the operation to perform from A B C D : ")
#     match (ops):
#         case "A":
#             print("add stu")
#             stu = input("enter student name: ")
#             marks = int(input("enter student marks: "))
#             info.update({stu:marks})
#             print(info)
#         case "B":
#             print("update marks")
#             stu = input('input student name to update marks : ')
#             if(info.get(stu) != None):
#                 mark = input('enter marks to update : ')
#                 info[stu] = mark
#             print(info)
#         case "C":
#             print("search stu")
#             stu = input("enter student to search: ")
#             if(info.get(stu) != None):
#                 print(info.get(stu))
#         case "D":
#             print(info)
#             break

# Question 6 Solution

# word = ["apple","banana","kiwi","cherry","mango"]
# fruits = {}
# for fruit in word:
#     size = len(fruit)
#     fruits.update({fruit:size})

# print(fruits)

# Question 7 Solution

# str = input("enter the string : ")
# count = 0
# for ch in str:
#     if ch == " ":
#         count+=1

# print(count)

# Question 8 Solution

# list1 = [1,2,3,4] # givem list one
# list2 = [5,6,7,8] # given list two
# list3 = list1 +  list2
# print(list3)
# set = set(list1 +  list2)
# print(set)
# set = list(set)
# print(set)
# print(list3 == set)

# Question 9 Solution

# list = [1,2,2,3,4,4,5,3]

# duplicate = set() # empty set to store duplicate
# is_present = set() # if not prenest the store in this 

# '''
# so the approach is that we check the element is already present in is_present list if it is present then we will store it in duplicate set and if it is not present then we will store it in the is_present set
# '''

# for elem in list:
#     if elem in is_present:
#         duplicate.add(elem)
#     else:
#         is_present.add(elem)
# print(duplicate)


# Question 10 Solution. 

# str = input("enter the string : ")
# print(str)
# set = set(str)
# print(set)
# print(len(set))