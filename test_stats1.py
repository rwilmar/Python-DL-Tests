import stat_qtls



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

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
secondLargest([1,2,7,2,3,5,4,2,7])
print (larger_than("2334","1234"))

print (RooksSafe([[1, 0, 1],[0, 0, 1],[0, 1, 0]]))

#print (avgCoord([10,2],[2,0],[6,3]))
#print(IsCasiPalindromo("uo0oh"))
#print(mostPopular(['sof','pepe','sof','mon'], 4))
