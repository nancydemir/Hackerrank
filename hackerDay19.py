class AdvancedArithmetic(object):
    def divisorSum(n):
         raise NotImplementedError
        
        
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sumsofar=0
        getsums = 0
        i = 1
        while i <= n:
            if n % i == 0:
                getsums += i
            i+=1
        return(getsums)
       
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
    
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
    
    
