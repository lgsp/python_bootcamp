import re


rand_str = "F.B.I. I.R.S. CIA"
print("Matches:", len(re.findall(".\..\..", rand_str)))

rand_str = """This is a long
string that goes
on for many lines"""
print(rand_str)
regex = re.compile("\n")
rand_str = regex.sub(" ", rand_str)
print(rand_str)

rand_str = "12345"
print("Matches:", len(re.findall("\d", rand_str)))
if re.search("\d{5}", rand_str):
    print("It is a zip code")

rand_str = "123 12345 123456 1234567"
print("Matches:", len(re.findall("\d{5,7}", rand_str)))

ph_num = "412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}", ph_num):
    print("It is a phone number")

if re.search("\w{2,20}", "Ultraman"):
    print("It is a valid name")


if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid name")

print("Matches:", len(re.findall("a+", "a as ape bug")))

# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

email_list = "db@aol.com m@.com @apple.com db@.com"

print("Email Matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email_list)))
    

    
