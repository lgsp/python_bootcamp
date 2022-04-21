import re
from functools import reduce

rand_str = "The cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches: print(i)


rand_str = "<a href='#><b>The Link</b></a>"
regex = re.compile(r"<b>(.*?)</b>")
rand_str = re.sub(regex, r"\1", rand_str)
print(rand_str)


rand_str = "412-555-1212"
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
rand_str = re.sub(regex, r"(\1)\2", rand_str)
print(rand_str)

rand_str = "https://www.youtube.com http://www.google.com"

regex = re.compile(r"(https?://([\w.]+))")
rand_str = re.sub(regex, r"<a href='\1>\2</a>\n", rand_str)
print(rand_str)

rand_str = "One two three four"
regex = re.compile(r"\w+(?=\b)")
matches = re.findall(regex, rand_str)
for i in matches: print(i)


rand_str = "1. Bread 2. Apples 3. Lettuce"
regex = re.compile(r"(?<=\d.\s)\w+")
matches = re.findall(regex, rand_str)
for i in matches: print(i)


rand_str = "<h1>I'm Important</h1> <h1>So am I</h1>"
regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")
matches = re.findall(regex, rand_str)
for i in matches: print(i)



rand_str = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, rand_str)
for i in matches: print(i)

matches = [int(i) for i in matches]
print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))
