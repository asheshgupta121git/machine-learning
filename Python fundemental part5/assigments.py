# Question 1 solution

# with open("names.txt", 'w') as f:
#     for i in range(5):
#         f.writelines([f"{input("enter name = ")}\n"])

# with open('names.txt', 'r') as f :
#     print(f.read())
#     


# Question 2 solution 

# with open('log.txt', 'a') as f:
#     f.write(f'{input("enter log = ")}\n')

# with open('log.txt', 'r')  as f:
#     print(f.read())

# question 3 solution

# list =  [5,10,15,20,25]

# ans = [val for val in list if val >15]
# print(ans)

# Question 4 solution 
import json

# d = {
#     "varansi":20_000,
#     "delhi":34_000,
#     "mumbai" :34_3400
# }

# with open('cities.json','w') as f:
#     json.dump(d, f, indent=4)

# with open('cities.json', 'r') as f:
#     cities =json.load(f)

# for city, population in cities.items():
#     print(city, "->", population)

# new_city = input('new city ')
# new_pop = input('new population ')
# cities[new_city] = new_pop

# with open("cities.json", "w") as f:
#     json.dump(cities, f, indent=4)

# for city, population in cities.items():
#     print(city, "->", population)



# Question 5 solution

try:
    with open('data.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('file not found')
else:
    print(f.read())
finally:
    print('program executionm complete')