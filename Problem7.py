import math
x = []
for num in range(1,200000,2):
    prime = True
    for i in range(2,int(math.sqrt(num))+1):
        if (num%i==0):
            prime = False
    if prime:
      x.append(num)
print x[10000]
