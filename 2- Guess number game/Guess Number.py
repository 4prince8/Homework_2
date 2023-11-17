import random
import math

# Counter
count = 0


# Recursive algorithm for binary search
def binary_search(target, low, high):
    global count
    count += 1

    middle = math.floor((low + high) / 2)
    print(count, '->', middle)
    if target == middle:
        return middle
    elif target < middle:
        return binary_search(target, low, middle - 1)
    else:
        return binary_search(target, middle + 1, high)


# Generate random number
target = random.randint(100, 999)

print("Random number:", target)
print("------------------------------------")

result = binary_search(target, 100, 999)

print("The entered number", result, "found.")
print("Numbers of searches:", count)

print("\n")
input("Press Enter to close...")
