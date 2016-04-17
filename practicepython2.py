userInput_num = int(input("Pick a number, any number, and input"))
userInput_check = int(input("Pick a number, a second number, and input"))

if userInput_num % userInput_check == 0:
    print(str(userInput_num) + " is divisible by " + str(userInput_check))
else:
    print(str(userInput_num) + " is NOT divisible by " + str(userInput_check))
