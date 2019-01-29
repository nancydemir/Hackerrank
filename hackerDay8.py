# Enter your code here. Read input from STDIN. Print output to STDOUT
# input string:
'''
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
'''
phoneBook = {}
names_to_search = []
entries = int(input())
for i in range(entries):
    name,phone_number  = list(map(str,input().strip().split()))
    phoneBook.update({name:phone_number}) 

def name_search(search_name):
    if search_name in phoneBook:
        print('',search_name,"=",phoneBook[search_name],'',sep = '')
    else:
        print("Not found")

for i in range(entries):
    search_name = str(input())
    name_search(search_name)
    





