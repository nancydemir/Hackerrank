def swap_case(s):
    newstring = str()
    for item in s:
        if item.islower():
            newstring += item.upper()
        elif item.isupper():
            newstring += item.lower()
        elif item.isspace():
            newstring += item
        else:
            newstring += item
        
    return(newstring)
    
  

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
