def median(data):
    len2=int(len(data)/2)
    if (len(data)%2==0):
        return (data[len2]+data[len2-1])/2
    else:
        return data[len2]

def stadev(data):
    sdval=0
    mn=getmean(data)
    for i in data:
        sdval=sdval+(i-mn)**2
    return (sdval/len(data))**0.5

def getmean(data):
    dmean=0
    for i in numbers:
        dmean=dmean+i
    return(dmean/len(data))

def splitListByMdn(data, mdnVal):
    l=[]
    u=[]
    for i in data:
        if i<mdnVal:
            l.append(i)
        if i>mdnVal:
            u.append(i)
    return (l,u)

def splitList(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

size = int("6")
numbers = list(map(int, "6 12 8 10 20 16".split()))
numbers.sort()
mdn=median(numbers)
(low, high) = splitListByMdn(numbers,mdn)
print(median(low))
print(mdn)
print(median(high))
print(stadev(numbers))

#interquartile range

dat=[]
numbers = list(map(int, "10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10".split()))
freqs = list(map(int, "1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20".split()))
for n in range(len(numbers)):
    for i in range(freqs[n]):
        dat.append(numbers[n])
dat.sort()
#mdn=median(dat)
(low, high) = splitList(dat)

print(median(low), median(high))


