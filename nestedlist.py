

def main():
    score_array = []
    entries = int(input())
    #min_score = []
    for _ in range(entries):
        name = input()
        score = float(input())
        arr = [name,score] 
        score_array.append([name,score])     
    
        #set removes duplicates.  list turns it back to list.
        #sorted returns a list, even if it's passed a set:
        
    second_lowest = sorted(set([score for name, score in score_array]))[1] 
    #print("second lowest:",second_lowest)

    score_array.sort(key = lambda name:name[0])
    for name,score in score_array:
        if score == second_lowest:
            print(name)  
    
if __name__ == '__main__':
    main()    
