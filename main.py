
num = int(input("Enter your number of rows"))
count = 1 

for c in range(1, num+1):
    for d in range(c):
        print(count, end="")
        count = count+1
    print()