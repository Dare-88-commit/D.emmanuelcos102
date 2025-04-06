def modify_list(mylist):
    mylist.append(4)
    mylist = [7, 8, 9]
    mylist.append(10)
    return mylist


orignal = [1, 2, 3]
mod = modify_list(orignal)
print(orignal)
print(mod)
