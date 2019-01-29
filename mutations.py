def mutate_string(string, position, character):
    #convert string to list so we can insert elements:
    mylist = list(string)
    mylist[position] = character
    #convert list to string with zero spaces:
    mystring = ""
    mystring = "".join(mylist)
    return(mystring)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
