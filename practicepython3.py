myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

isitbigger = int(input("Please enter a number: "))

for num in myList:
    if num < isitbigger:
        newList.append(num)

print(newList)

