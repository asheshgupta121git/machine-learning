data = True
line = 1
word  = 'store'
with open('word.txt', 'r') as f:
    while(data):
        data =  f.readline()
        
        if(word in data):
            print(f"{word} found at line {line}")
            break

        print(data)
        line = line+1        
