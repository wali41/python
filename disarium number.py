# Program to check if a number is a Disarium number (without using functions)

# Step 1: Take input from user
num = int(input("Enter a number: "))

# Step 2: Convert to string to process each digit
num_str = str(num)
length = len(num_str)
sum_of_powers = 0

# Step 3: Loop through each digit with its position
for i in range(length):
    digit = int(num_str[i])
    # position starts at 1, so use i+1
    sum_of_powers += digit ** (i + 1)

# Step 4: Check if sum matches original number
if sum_of_powers == num:
    print(num, "is a Disarium number")
else:
    print(num, "is not a Disarium number")