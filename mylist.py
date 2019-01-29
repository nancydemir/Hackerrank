if __name__ == '__main__':
    N = int(input())
    mylist = []
    splitlist = []
 
    for e in range(N):
        splitlist = input().strip().split()
        command = splitlist[0]
        #split used to split a string into a list of words or items.
        #The strip() method returns a copy of the string with both
        #leading and trailing characters removed 
        splitlist[1:] = map(int,splitlist[1:])
        if len(splitlist) == 1:
            try:
                getattr(mylist,command)(*splitlist[1:])
            except:
                print("mylist:",mylist)
        else:
            
        #When calling a function, the * operator can be used to unpack
        #an iterable into the arguments in the function call:
        #below, all of the items in splitlist[1] and beyond are passed in to
        #the getattr function. Still need to unpack even if the list is of fixed length.
            try:
                getattr(mylist,command)(*splitlist[1:])
            except:
                print("mylist:",mylist) 
        

