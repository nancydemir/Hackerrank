Tests = int(input())
index = 0


for t in range(1,Tests+1):
    list_even = []
    list_odd  = []
    list_input = input()
    if 2 <= len(list_input) <= 10000:
        for letter in list_input:
            if (index % 2 == 0) or (index == 0):
                list_even += letter           
            else:
                list_odd += letter
            index += 1
        print(''.join(list_even),end = " ")
        print(''.join(list_odd))
    else:
      break

 
  




