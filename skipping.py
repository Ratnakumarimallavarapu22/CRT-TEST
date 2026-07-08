#skipping broken steps
#input
N = int(input("enter N: "))
for i in range(1, N + 1):
    if i % 4 != 0:
        print(i, end=" ")