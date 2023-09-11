import re

print(re.search(r"Py.*n", "Pygmalion"))
# Greedy behavior
print(re.search(r"Py.*n", "Python Programmin")) 
# Limitting greedy behavior
print(re.search(r"Py[a-z]*n", "Python Programmin"))

print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
