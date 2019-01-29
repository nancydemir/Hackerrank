if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for x in range(N):
        args=input().strip().split()
        print("args:",args)
        args[1:]=map(int,args[1:])
        try:
            getattr(my_list,args[0])(*args[1:])
        except AttributeError:
            print(mylist)
