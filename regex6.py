import re

def test1():
    rand_str = "1. Dog 2. Cat 3. Turtle"
    regex = re.compile(r"\d\.\s(Dog|Cat)")
    matches = re.findall(regex, rand_str)
    print(len(matches))
    for i in matches: print(i)

def test2():    
    rand_str = "12345 12345-1234 1234 12346-333"
    regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
    matches = re.findall(regex, rand_str)
    print(len(matches))
    for i in matches: print(i)

def test3():    
    bd = input("Enter your birthday (mm-dd-yyyy): ")
    bd_regex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)
    print("You were born on", bd_regex.group())
    print("Birth Month", bd_regex.group(1))
    print("Birth Day", bd_regex.group(2))
    print("Birth Year", bd_regex.group(3))

def test4():    
    match = re.search(r"\d{2}", "The chicken weighed 13 lbs")
    print("Match:", match.group())
    print("Span:", match.span())
    print("Match:", match.start())
    print("Match:", match.end())

def test5():    
    rand_str = "December 21 1974"
    regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"
    matches = re.search(regex, rand_str)
    print("Month:", matches.group('month'))
    print("Day:", matches.group('day'))
    print("Year:", matches.group('year'))

def test6():    
    rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
    regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    matches = re.findall(regex, rand_str)
    print(len(matches))
    for i in matches: print(i)

rand_str = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"

regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-|\))?(\d{3})(-|)?(\d{4}|\d{4}))")
matches = re.findall(regex, rand_str)
for i in matches: print(i)
