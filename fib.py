def prime():
    n=19
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print(n,'prime number')
    else:
        print('not a prime')
prime()



n1=20
n2=70
for i in range(n1,n2):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count = count + 1
    if count==2:
         print(i,'prime')


