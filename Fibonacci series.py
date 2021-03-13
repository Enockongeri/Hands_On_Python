#the sum of two elements defines the next


a, b = 0, 1

while a < 10:
    print(a)
    a, b = b, a+b
i = 256*256
print('The value of i is',i)


a, b = 1, 0
while a < 1000:
    print(a, end=',')
    a+=1



