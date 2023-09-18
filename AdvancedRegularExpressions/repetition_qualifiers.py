import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeard"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeard"))

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeard"))

print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\b[r]{2,10}\b", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))

print(re.search(r"s\w{,20}", "I really like strawberries"))
