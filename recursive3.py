def list(n,idx=0):
    if(idx == len(n)):
        return 
    print(n[idx]+n)
    list(n,idx+1)
    return print(n +n)

number=[1,2,5,7]
list(number)