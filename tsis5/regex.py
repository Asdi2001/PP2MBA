#1
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
word = r'ab*'
result = re.findall(word, data)
for i in result:
    print(i)
    
#2
import re
file = open('row.txt', 'r', encoding = 'utf-8')
data = file.read()
word = r'ab{2,3}?'
result = re.findall(word,data)
for i in result:
    print(i)
    
#3
import re

file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
word_pattern = r'\b[a-z]+_[a-z]+\b'
result = re.findall(word_pattern, data)
for i in result:
    print(i)
    
#4
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
word_pattern = r'\b[A-Z][a-z]+\b'
result = re.findall(word_pattern, data)
for i in result:
    print(i)

#5
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
pattern = r'a.*b$'
result = re.findall(pattern, data)
for i in result:
    print(i)
    
#6
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
pattern = r'[ ,.]'
result = re.sub(pattern, ':', data)

print(result)

#7
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
words = data.split('_')
result = words[0] + ''.join(word.capitalize() for word in words[1:])
print(result)

#8
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
pattern = r'[A-Z][^A-Z]*'
result = re.findall(pattern, data)
for i in result:
    print(i)

#9
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
def capital(data):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", data)
result = capital(data)
print(result)

#10
import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

camel_string = "convertCamelCase"
snake_string = camel_to_snake(camel_string)
print(snake_string)
