#i write a function where I am found the which number is even and which number is odd 
number=int(input('give me a number and I will tell you this number even or odd '))
def bush(a):
    if(a%2==0):
        print('the number is even')
    elif(a%2 !=0):
        print('The number is odd ')
    
bush(number)