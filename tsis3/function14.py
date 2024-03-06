from function1 import(grams_to_ounces, fahrenheit_to_centigrade, solve, is_prime, filter_prime,print_permutations, reverse_words, has_33, spy_game, sphere_volume, unique_elements, is_palindrome, histogram, guess_the_number)

grams = 100
print(grams_to_ounces(grams))

fahrenheit = 250
print(fahrenheit_to_centigrade)

numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)
print("Number of chickens:", solution[0])
print("Number of rabbits:", solution[1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))

print_permutations()

sentence = input()
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)

print(has_33([1, 3, 3]))   # True
print(has_33([1, 3, 1, 3])) # False
print(has_33([3, 1, 3]))    # False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False

radius = 5
print(sphere_volume(radius))

input_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
result_list = unique(list)
print(result_list)

print(is_palindrome("level"))  # True

histogram([5, 8, 1])