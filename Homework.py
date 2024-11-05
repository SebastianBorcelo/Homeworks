# Exercise: Create a list of 5 of your favorite fruits. Print the list.

fruits = ["Dragon Fruit", "Tomato", "Guava", "Rambutan", "Durian"]
print(fruits)

# Exercise: Given the list colors = ['red', 'blue', 'green', 'yellow', 'purple'], print the first, third, and last color in the list.

colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[4])

# Exercise: Create a list numbers with values [10, 20, 30, 40, 50]. Change the second item to 25 and add 60 to the end of the list. Print the modified list.

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25

numbers.append(60)
print ("Modified List:",numbers)

# Exercise: Using the list names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma'], create a new list subset containing only the first three names. Print subset.

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']

subset = names[:3]
print(subset)

# Exercise: Create a list of numbers from 1 to 10 and use a loop to print each number squared.

numbers = list(range(1, 11))
print("Squares of numbers 1-10:")
for number in numbers:
    print(number ** 2)

# Exercise: Create an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list.

shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

# Exercise: Write a program to find the maximum and minimum values in the list numbers = [45, 22, 88, 56, 92, 33].

numbers = [45, 22, 88, 56, 92, 33]
print("Max number: ", max(numbers))
print("Min number: ", min(numbers))

# Exercise: Given the list letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd'], count how many times the letter 'a' appears in the list.

letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print("Count of 'a': ", letters.count('a'))

# Exercise: Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.

squares_of_even = [x ** 2 for x in range(11) if x % 2 == 0]
print(squares_of_even)

# Exercise: Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only.

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)