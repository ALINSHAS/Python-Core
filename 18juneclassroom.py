# 1. Given a string
s = "I am learning Python"

# Find the length of the string
print(len(s))

# Find the reverse of the string
print(s[::-1])

# Find the last character of the string
print(s[-1])

# Find the 13th character
print(s[12])

# Print the characters from 2nd index to 15th index
print(s[2:16])

# Combine the string with the word "programming"
s += " programming"     
print(s)


# 2. Given a list
l = ['Guitar', 'Piano', 'Violin', 'Drums', 'Flute']

# Add a new item 'Veena' to the list
l.append('Veena')
print(l)


# 3. Declare a list of 5 food items
Foods = ['Appam', 'Dosha', 'Idli', 'Chappathi', 'Puttu']
print(Foods)

# Add new food item
Foods.append('Porotta')
print(Foods)

# Change the second food item
Foods[1] = "Idiyappam"
print(Foods)

# Print the updated list
print(Foods)

# Print the last food item
print(Foods[-1])

# Print the number of food items
print(len(Foods))


# 4. Given a string
s = "python is a programming language"

# Remove the first 10 characters and print the remaining
print(s[10:])

# Print the last 5 characters
print(s[-5:])


# 5. Given a list
l = [10, 56, 23, 67, 19, 70]

# Interchange 2nd index and 5th index numbers
l[2], l[5] = l[5], l[2]
print(l)


# 6. Given a set
s = {10, 20, 30, 40}

# Add a new number 50 to the set
s.add(50)
print(s)