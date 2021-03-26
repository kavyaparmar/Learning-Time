s=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n=int(input("Enter Number of Alphabet: "))

for i in range(n):
    for j in range(i,n):
        print('',end=' ')
    for j in range(i):
        print(s[i-1],end=' ')
    print()

for i in range(n):
    for j in range(i):
        print('',end=' ')
    for j in range(n-i):
        print(s[n-i],end=' ')
    print()


'''for i in range(n):
    for j in range(i):
        print(i,end='')
    print()'''


