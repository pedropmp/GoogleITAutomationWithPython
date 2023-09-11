import re

print(re. search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the high way"))
print(re.search(r"[a-z]way", "What a way to go"))

# three seraching ranges
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.findall(r"cat|dog", "I like both cats and dogs"))


