def recursive(n):
    if(n==0):
        return 0
    
    return recursive(n-1)+n
    
    
   
    
print(recursive(5)) 