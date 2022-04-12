input_str = input("Enter a string: ")
str_to_list = input_str.split()
acronym = ""
for word in str_to_list:
    acronym += word[0]
print(acronym)
