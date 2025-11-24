# student enrollment 

'''PYTHON
given a list of tuples with info(name, subject)
--> list all unique course
--> list student enrolled in english
--> create dictionary (student, set of course)
'''

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]


# --> problem 1 solution
# unique = set()

# for tup in info:
#     print(tup[1])
#     unique.add(tup[1])

# print(unique)

#--> problem 2 solution

# for tup in info:
#     if(tup[1] == "English"):
#         print(tup[0])

# --> problem 3 solution
dic = {}

for name,course in info:
    if(dic.get(name) == None):
        dic.update({name:set()})
        dic[name].add(course)
    else:
        dic[name].add(course)

print(dic)

