#question: prints n to 1 backwards 
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# question :prints n to 1 forward 

# def show2(n2):
#     if( n2 == 6):
#         return 1 
#     print(n2)
#     return  show2(n2+1)+n2

# result=show2(1)
# print(result)

# question :calculate factorial 

# def factorial(n):
#     if(n == 0 or n== 1):
#         return 1
#     return factorial(n-1)*n
# print(factorial(5))

# question : print all elements in a list using recursive function 
def list_name(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    list_name(list,(idx+1))
name=['raj','barat','yousufe']
list_name(name,idx=0)


