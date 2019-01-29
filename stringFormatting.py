def print_formatted(number):
   
    # your code goes here
   
    w = len(str(bin(number)[2:]))
    
    #formatted to the width of the binary number, sine that will take the most room
    for x in range(1,number+1):
        deci = str(x).rjust(w)
        octa = str(oct(x)).replace('0o','').rjust(w)
        hexa = str(hex(x)).replace('0x','').rjust(w)
        bina = str(bin(x)).replace('0b','').rjust(w)
        
        print(deci,octa,hexa.upper(),bina)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
