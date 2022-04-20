import re

rand_str = "cat cats"
regex = re.compile("[cat]+s?")
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)

rand_str = "doctor doctors doctor's"
regex = re.compile("[doctor]+['s]*")
print("Matches:", len(matches))

regex = re.compile("[doctor]+['s]{0,2}")
print("Matches:", len(matches))

long_str = '''Just some words
and some more\r
and more
'''

print("Matches:", len(re.findall(r"[\w\s]+[\r]?\n", long_str)))
matches = re.findall("[\w\s]+[\r]?\n", long_str)

for i in matches:
    print(i)

rand_str = "<name>Life On Mars</name><name>Freaks and Geeks</name>"
regex = re.compile(r"<name>.*</name>")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches:
    print(i)

regex = re.compile(r"<name>.*?</name>")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches:
    print(i)
    
rand_str = "ape at the apex"
regex = re.compile(r"ape")
regex_2 = re.compile(r"\bape\b")
matches = re.findall(regex, rand_str)
matches_2 = re.findall(regex_2, rand_str)
print("Matches 1:", len(matches))
print("Matches 2:", len(matches_2))

