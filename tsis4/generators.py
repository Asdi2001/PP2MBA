#1
def generator(N):
    for i in range(N):
        yield i**2
N = 5 #for example
squares = generator(N)
print(list(squares))

#2
def generator(N):
    for i in range(0, N+1, 2):
        yield i

n = int(input("Enter a number: "))
even = generator(n)
print(','.join(map(str, even)))

#3
def generator(start, end):
    for i in range(start, end+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

start = 1
end = 10
numbers = generator(start, end)
print(list(numbers))

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = 6
b = 7
print(list(squares(a, b)))

#5
def down(n):
    while n >= 0:
        yield n
        n -= 1

n = 3
print(list(down(n)))
