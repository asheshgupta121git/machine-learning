# file Operation
# open, read and close.

# f = open("data.txt","r")
'''
data.txt -> filename -> path
"r" -> mode

NOTE-: once file open it return file object
'''

# f = open("sample.txt", "r")

# data = f.read()
# print(data)
# print(type(data))


# like read we have readline()
# data = f.readline()
# print(data)


# once file is open we need to close this also it is important 
# f.close()



# now to rewrite the file we have write method and it it done with write mode
# f = open("sample.txt", "w")

# f.write("this is re written file ")
# f.write('123')

# f.close()



#----------------------------------------
# modes in file I/O 

# append mode "a"

# f = open("sample.txt", "a")

# f.write('this is new file \n and this is new line') #\n is next line 

# f.close()

# "x" creates new file and open for writing.

# f = open("sample2.txt", "x")
# f.write("this is file created with with x mode")

# f.close()

# f = open("sample2.txt", "r+")
# f.write("123")

# print(f.read())

# f.close()


# f = open("sample2.txt", "a+")
# f.write("123")

# print(f.read())

# f.close()

# f = open("sample2.txt", "w+")
# f.write("123")

# print(f.read())

# f.close()


#-------------------------------------------------------
# with keyword is simplary way to open and close file.

# with open('sample.txt',"r") as f:
#     data = f.read()
#     print(data)
#     print(len(data))

# here we dont need to close file explecitely. 


# delete file 
# to delete file we use os module

# import os
# os.remove('sample2.txt')



