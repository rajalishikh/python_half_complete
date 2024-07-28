tuple=(1,4,9,16,25,36,49,64,81,100,36)
x=int(input('please give me a any Integer number :'))
idx=0
while idx<len(tuple):
    if(tuple[idx] == x):
        print('we found the value in this index',idx)
    else:
        print('dont found')
    idx=idx+1

