# Creating a dictionary where each key maps to a tuple of numbers
numbers_dict = {
    "evens": (2, 4, 6, 8, 10),
    "odds": (1, 3, 5, 7, 9),
    "primes": (2, 3, 5, 7, 11),
    "fibonacci": (0, 1, 1, 2, 3, 5, 8)
}

# Accessing elements
print("Even numbers:", numbers_dict["evens"])
print("First prime number:", numbers_dict["primes"][0])

# Adding a new key-value pair
numbers_dict["squares"] = (1, 4, 9, 16, 25)

# Looping through dictionary
for key, value in numbers_dict.items():
    print(f"{key}: {value}")