a = int(input('первое число: '))
b = int(input('второе число: '))
c = int(input('третье число: '))
if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
elif a!=b!=c:
    print(0)
else:
    print(0)
