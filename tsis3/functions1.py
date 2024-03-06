#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    
#2
def fahrenheit_to_centigrade(fahrenheit):
    centigrate= (5/9)*(fahrenheit - 32)

#3
def solve(numheads, numlegs):
    numrabbits = numheads - (numlegs - 2 * numheads) / 2
    numchickens = numheads - numrabbits
    
#4
def filter_prime(numbers):
    return [num for num in numbers if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

#5
def print_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print(''.join(perm))

#6
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

sentence = input()
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)

#7
def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == 3 and nums[i - 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))   # True
print(has_33([1, 3, 1, 3])) # False
print(has_33([3, 1, 3]))    # False

#8
def spy_game(nums):
    zero1_found = False
    zero2_found = False
    seven_found = False

    for num in nums:
        if num == 0 and not zero1_found:
            zero1_found = True
        elif num == 0 and zero1_found and not zero2_found:
            zero2_found = True
        elif num == 7 and zero1_found and zero2_found:
            seven_found = True
            break 

    return zero1_found and zero2_found and seven_found

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False

#9
def sphere_volume(radius):
    return (4/3) * 3,14 * radius**3

#10
def unique(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
result_list = unique(list)
print(result_list)

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("level"))  # True


#12
def histogram(numbers):
    for number in numbers:
        print("*" * number)

#13
import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    guesses = 0

    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

guess_the_number()








