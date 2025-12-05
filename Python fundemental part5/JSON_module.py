# json stands for javascript object notation
'''
it is quit similar to python dictionary. 
'''

import json

# py_obj = {
#     'name':"ashesh",
#     'isTeacher': True
# }

#to conver in json string formate

# py_str = json.dumps(py_obj)

# print(py_str)
# print(type(py_str))

# json_str = '{"name": "ashesh","isTeacher" :true}'

# to conver in python object 

# py_obj = json.loads(json_str)

# print(py_obj)
# print(type(py_obj))


# reading form data.json file 



# with open('data.json','r') as f:
#     py_obj = json.load(f)
#     print(py_obj)
#     print(type(py_obj))


# data over writing in file. 

d = {
    "name":"ashesh",
    "age":23,
    "student":True
}

with open('data.json','w') as f:
    py_obj = json.dump(d, f,indent=4, sort_keys=True)







