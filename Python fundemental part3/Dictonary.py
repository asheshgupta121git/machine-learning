# store unique key:value pair

info = {
    "name" : "ashesh",
    "cgpa":7.3,
    "subject": ["cse","aiml"],
    3.14:"pi"
}

# print(info)
# print(info[3.14])
# print(info["name"])

# # by nature they are mutable we can upate value

# info["name"] = 'ashesh gupta'
# print(info)


# -----------------------------------------

# methods
print(info.keys()) # return all keys 
print(type(info.keys())) #  type is <class 'dict_keys'>

# type case into list also 

print(list(info.keys()))
print(type(list(info.keys())))

print(info.values())  # return all values

print(info.items()) # return key value pari

print(info.get("cgpa2")) # retrurn val acc. to key 

info.update({"city":"varansi"}) # update value of dicti..
print(info)
print("end of code")