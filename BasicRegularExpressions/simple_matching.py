import re

# r: rawstring, python interpreter does not interpret special characters
result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)

# using seach special characters
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
