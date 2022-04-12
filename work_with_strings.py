def disp_str(msg, rand_string):
    print(msg)
    print('-' * len(msg))
    print()
    print(rand_string)
    print()
    
rand_string = "  There is space on my left... there is space on my right...   "
msg = "Before anything:"
disp_str(msg, rand_string)

rand_lstrip = rand_string.lstrip()
msg = "After .lstrip():"
disp_str(msg, rand_lstrip)

rand_rstrip = rand_string.rstrip()
msg = "After .rstrip():"
disp_str(msg, rand_rstrip)

rand_strip = rand_string.strip()
msg = "After .strip():"
disp_str(msg, rand_strip)

rand_cap = rand_string.strip().capitalize()
msg = "After .strip() and .capitalize():"
disp_str(msg, rand_cap)

rand_up = rand_string.strip().upper()
msg = "After .strip() and .upper():"
disp_str(msg, rand_up)

print("=" * 50)
print("List to string with .join()")
print("List:")
a_list = ["Bunch", "of", "random", "words"]
print(a_list)
print("String:")
print(" ".join(a_list))

print("=" * 50)
print("String to list with .split()")
a_list_2 = rand_string.split()
print(a_list_2)

print("=" * 50)
print("How many occurence of some string with .count()")
print("Where is:", rand_string.count("is"))

print("=" * 50)
print("First occurence of some string with .find()")
print("Where is:", rand_string.find("is"))

print("=" * 50)
print(".replace()")
print("Where is:", rand_string.replace("space", "room"))

