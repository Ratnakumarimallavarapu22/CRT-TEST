#secret number door
#input
secret_number = 7
maximum_attempts = 3
for i in range(maximum_attempts):
    number = int(input("enter a number:"))
    if number == secret_number:
        print("door opened")
        break
else:
    print("access denied")