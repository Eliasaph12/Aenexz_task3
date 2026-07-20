numbers = list(map(int, input("Enter numbers separated by space: ").split()))

count = 0

for i in numbers:
    if i % 2 == 0:
        count += 1

print("Even numbers =", count)
