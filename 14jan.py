# 1.Python program to interchange first and last element of the list.

def swaplist(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist

newlist = [8,4,5,2]
print(swaplist(newlist))    
