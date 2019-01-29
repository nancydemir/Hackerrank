if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
   
    #remove doesn't work on maps, so we turned it into a list
    maxSofar = max(arr) 
    for x in range(n):
        for item in arr:
            if item == maxSofar:
                arr.remove(item)
                #print("item removed: ", item)
    runnerUp = max(arr)
    print("runnerup is: ",runnerUp)
        

        
  
