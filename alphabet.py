s=['A','B','C','D','E','F','G','H']
n=int(input("Enter Alphabet Number= "))

for i in range(n):
    for j in range(i):
        print(s[i-1],end=' ')
    print()

