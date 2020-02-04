import numpy as np
from scipy import stats

print("hola esta es una prueba")
size = int(input())
numbers = list(map(int, input().split()))

dmean=0
dmedian=0
dmode={}
numbers.sort()

for i in numbers:
    dmean=dmean+i
    if i in dmode:
        dmode[i]+=1
    else:
        dmode[i]=1
        
dmean=dmean/len(numbers)
print(dmean)
#print(np.mean(numbers))


len2=int(len(numbers)/2)
if (len(numbers)%2==0):
    print((numbers[len2]+numbers[len2-1])/2)
else:
    print(numbers[len2])

#print(np.median(numbers))

dmode=sorted(dmode.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
print(dmode[0][0])
print(int(stats.mode(numbers)[0]))