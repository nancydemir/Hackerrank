#def testEqual(mystr):


    
def revstring(mystr):
    revstr = ''
    # your code here
    mystack = Stack()
    for l in mystr:
        mystack.push(l)
    print(mystack)
    while not mystack.isEmpty():
        revstr += mystack.pop()
    return revstr

revstring('apple')
#testEqual(revstring('apple'),'elppa')
#testEqual(revstring('x'),'x')
#testEqual(revstring('1234567890'),'0987654321')
