import itertools
def permut(s):
    
    res=[]
    permutations=itertools.permutations(s,len(s))
    for word in permutations:
        res.append("".join(word))
    
    return sorted(res)

    

s="0123456789"
print(permut(s)[999999])