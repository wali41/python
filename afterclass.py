# Program to print a power series using for loop up to n terms

# Step 1: Accept number of terms from the user
n = int(input("Enter the number of terms to print in the power series: "))

# Step 2: Print a message
print("Power series looks like this:")

# Step 3: Generate and print the power series using a for loop
for i in range(1, n + 1):
    term = i ** i  # each number raised to the power of itself
    if i != n:
        print(term, end=", ")
    else:
        print(term)  # no comma after the last term