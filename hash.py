
if __name__ == '__main__':
    
         n = int(input())
         integer_list = map(int, input().split())
         #convert integer list to a tuple of lists, since lists are not hashable:
         t = tuple(integer_list)
         print(hash(t))
         
        
        
         
             
