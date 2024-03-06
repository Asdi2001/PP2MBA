#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
#2
def fahrenheit_to_centigrade(fahrenheit):
    centigrate= (5/9)*(fahrenheit - 32)
    return centigrate
#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return 0
    
#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

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

#7
def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == 3 and nums[i - 1] == 3:
            return True
    return False

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

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


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








