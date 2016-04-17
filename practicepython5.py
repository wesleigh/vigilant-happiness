import random

List_1 = [int(100*random.random()) for i in range(100)]
List_2 = [int(100*random.random()) for i in range(100)]
commonNumbers = []

for num in List_1:
    if num in List_2:
        if num not in commonNumbers:
            commonNumbers.append(num)


print(str(commonNumbers) + " is in list 1 and list 2!")
    
        
