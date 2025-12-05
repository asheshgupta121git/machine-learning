# try, except, else, finally

try:
    x = int(input('enter x : ')) 
    ans = 10/x

except ZeroDivisionError:
    print('divide by zero not allowed')

except ValueError:
    print('invalie inputt')

else:
    print(ans)

finally:
    print("execution done")
    