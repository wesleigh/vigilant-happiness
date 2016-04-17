usernum = int(input("Please enter your number"))

for i in range(2, usernum):
    if usernum % i == 0:
        print(i)
