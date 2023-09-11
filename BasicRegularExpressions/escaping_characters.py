import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

print(re.search(r"\w +\w", "ola mundo"))
print(re.search(r"\w +\w", "ola  mundo"))

print(re.search(r"\w +\w", "ola  mundo"))
print(re.search(r"\w +\w", "ola  mundo"))

# http://regex101.com