import re

# ^ : Matches the beginning of a string
# $ : Matches the end of a string

rand_str = "Match everything up to @"
regex = re.compile(r"^.*[^@]")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches: print(i)


rand_str = "@ Get this string"
regex = re.compile(r"[^@\s].*$")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches: print(i)


rand_str = '''Ape is big
Turtle is slow
Cheetah is fast
'''
regex = re.compile(r"(?m)^.*?\s")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches: print(i)


rand_str = "My number is 412-555-1212"
regex = re.compile(r"412-(.*)")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches: print(i)


rand_str = "412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches: print(i)


rand_str = "My number is 412-555-1212"
regex = re.compile(r"412-(.*)-(.*)")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
print(matches[0][0])
print(matches[0][1])

