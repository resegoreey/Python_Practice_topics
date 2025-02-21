# function that takes a list of numbers as an argument and returns the sum of all the elements. 
def sum_elements(numbers):
    
    for num in numbers:
        total = sum(numbers)
    return total
numbers = [3, 6, 9, 12, 15]
print(sum_elements(numbers))

# function that takes a list of numbers as an argument and returns the largest element in the list
def find_largest_num(numbers):
    for num in numbers:
        return max(numbers)
numbers = [12, 1, 34, 0, 55]
print(find_largest_num(numbers))

#  Write a function that takes a string as an argument and returns the number of vowels in the string
def count_vowels(word):
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count
print(count_vowels("Ompeilekae"))

