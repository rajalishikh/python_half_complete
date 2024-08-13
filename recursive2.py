def  list_item(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    list_item(list,idx+1)

list1=['apple','lichi','banana',]
list_item(list1)