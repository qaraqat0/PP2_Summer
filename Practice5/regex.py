import re

text = input()

# 1
if re.fullmatch(r"ab*", text):
    print("Match")
else:
    print("No match")

# 2
if re.fullmatch(r"ab{2,3}", text):
    print("Match")
else:
    print("No match")

# 3
result = re.findall(r"[a-z]+_[a-z]+", text)
print(result)

# 4
result = re.findall(r"[A-Z][a-z]+", text)
print(result)

# 5
if re.fullmatch(r"a.*b", text):
    print("Match")
else:
    print("No match")

# 6
result = re.sub(r"[ ,.]", ":", text)
print(result)

# 7
result = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)
print(result)

# 8
result = re.split(r'(?=[A-Z])', text)
print(result)

# 9
result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)

# 10
result = re.sub(r"([A-Z])", r"_\1", text).lower().lstrip("_")
print(result)