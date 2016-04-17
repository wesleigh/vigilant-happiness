import time


ageYear = int(input("What year were you born? "))
print("You'll be 100 years old in the year " + str(ageYear+100))
print("\n")
time.sleep(0.5)
print(time.strftime("This information is correct as of %d/%M/%Y. \nDid we get it wrong? \nSue us..."))
