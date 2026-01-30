# Problem 27: Create a list of squares
# Find and fix the error

squares = []
n = int(input("Enter a number n: "))
for i in range(1, n + 1):
    squares.append(i * i)

print(f"Squares of first {n} numbers: {squares}")

