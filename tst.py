import math

def secondLargest(arr):
    out=[]
    for j in reversed(range(max(arr)+1)):
        for i in range(len(arr)):
            if (arr[i]==j):
                out.append(arr[i])
            if len(out)==3:
                break

    print ("2nd num: ",out[1])

def larger_than(n1, n2):
    if len(n1)>len(n2):
        return True
    elif len(n1)==len(n2):
        for e in reversed(range(len(n1))):
            if n1[e]>n2[e]:
                return True
        return False
    else:
        return False

def RooksSafe(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            play=0
            if board[row][col]==1:
                #print("player on [", row,",",col,"]")
                play+=1
                if (sum(board[row])>1):
                    return False
            if play>1:
                return False
    return True

def avgCoord (coord1, coord2, coord3):
    d1=math.sqrt((coord2[0] - coord1[0])**2 - (coord2[1] - coord1[1])**2) #entre coord1 y coord2
    d2=math.sqrt((coord3[0] - coord2[0])**2 - (coord3[1] - coord2[1])**2) #entre coord2 y coord3
    d3=math.sqrt((coord1[0] - coord3[0])**2 - (coord1[1] - coord3[1])**2) #entre coord3 y coord1
    return (d1+d2+d3)/3

def IsCasiPalindromo(text):
    notEqual=0
    ln=len(text)
    for cix in range(ln):
        if cix>ln/2:
            return True
        if text[cix]!=text[ln-1-cix]:
            notEqual+=1
        if notEqual>1:
            return False
    return True 


def mostPopular(arr, len):
    out={}
    popular=[0,0]
    secPop=[0,0]
    for i in arr:
        if i in out:
            out[i]+=1
        else:
            out[i]=1
    for ppl in out:
        if out[ppl]>popular[1]:
            popular[0]=ppl
            popular[1]=out[ppl]
            secPop=[0,0]
        elif out[ppl]==popular[1]:
            secPop[0]=ppl
            secPop[1]=out[ppl]
    if secPop[1]==0:
        return popular[0]
    else:
        return secPop[0]
    #print ("2nd num: ",out[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
secondLargest([1,2,7,2,3,5,4,2,7])
print (larger_than("2334","1234"))

print (RooksSafe([[1, 0, 1],[0, 0, 1],[0, 1, 0]]))

#print (avgCoord([10,2],[2,0],[6,3]))

#print(IsCasiPalindromo("uo0oh"))

print(mostPopular(['sof','pepe','sof','mon'], 4))

