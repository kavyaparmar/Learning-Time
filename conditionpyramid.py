ShapeList = ['Triangle','Square','Pyramid','DownsidePyramid','Diamond']

for num,word in enumerate (ShapeList):
    print(num+1,word)

n=(int(input("Select Number From Menu: ")))
x=(int(input("Enter Number: ")))


if n == 1: #this is for triangle
    for i in range(x):
        for j in range(i):
            print(i,end=' ')
        print()

elif n == 2: #this is for squre
    for i in range(x):
        for j in range(3):
            print(j,end=' ')
        print()

elif n == 3: #this is for pyramid
    for i in range(x):
        for j in range(x-i):
            print('',end=' ')
        for j in range(i):
            print(i,end=' ')
        print()

elif n == 4:  #this is for Downside Pyramid
    for i in range(x):
        for j in range(i):
            print('',end=' ')
        for j in range(x-i):
            print(i,end=' ')
        print()

elif n == 5: #Diamond
    for i in range(x):
        for j in range(i,x):
            print('',end=' ')
        for j in range(i):
            print(i,end=' ')
        print()

    for i in range(x):
        for j in range(i):
            print('',end=' ')
        for j in range(x-i):
            print(x-i,end=' ')
        print()

else:
    print("Shape Not Well Defined")

