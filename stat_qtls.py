import math

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
        if secPop[0]<popular[0]:
            return secPop[0]
        else:
            return popular[0]
    #print ("2nd num: ",out[1])




