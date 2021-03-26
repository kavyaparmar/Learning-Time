n=int(input("Enter Number: "))
k=1
for i in range(1,n):
    for j in range(1,i+1):        
        print(k,end=' ')
        k=k+1
    print()
