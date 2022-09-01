from zipfile import ZIP_MAX_COMMENT


print("hello world!")

# Print name
first_name = "Zac" 
last_name = "Sibson"
print(first_name, last_name)

# Print age
age = 25 
print(age)

# Conditional logic
if age >= 18:
    print("I am an adult")
elif age < 13:
    print("I am a child")
else:
    print("I am a teenager")

favorite_numbers = [57, 12, 8, 22, "hi bob", False, 2.0]
print(favorite_numbers)

for numbers in favorite_numbers:
    print(numbers)
