import re

def sep_ex():    
    print()    
    print("=" * 60)
    print()
    
print('re.search("ape", "The ape was at the apex")')
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

sep_ex()

print('re.findall("ape", "The ape was at the apex")')    
all_apes = re.findall("ape", "The ape was at the apex")
for i in all_apes:
    print(i)

sep_ex()

print('re.finditer("ape.", the_str)')
the_str = "The ape was at the apex"
for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])

sep_ex()

print('re.findall("[crmfp]at", animal_str)')
animal_str = "Cat rat mat fat pat"
all_animals = re.findall("[crmfp]at", animal_str)
for i in all_animals:
    print(i)

sep_ex()

print('re.findall("[c-mC-M]at", animal_str)')
animal_str = "Cat rat mat fat pat"
some_animals = re.findall("[c-mC-M]at", animal_str)
for i in some_animals:
    print(i)

sep_ex()

print('re.findall("[^Cr]at", animal_str)')
animal_str = "Cat rat mat fat pat"
some_animals = re.findall("[^Cr]at", animal_str)
for i in some_animals:
    print(i)
    
sep_ex()

owl_food = "rat cat mat pat"
regex = re.compile("[cr]at")
print('regex = re.compile("[cr]at")')
owl_food = regex.sub("owl", owl_food)
print('regex.sub("owl", owl_food)')
print(owl_food)

sep_ex()

rand_str = "Here is \\stuff"
print('re.search("\\stuff", rand_str)')
print("Find \\stuff:", re.search("\\stuff", rand_str))

sep_ex()

rand_str = "Here is \\stuff"
print('re.search("\\\\stuff", rand_str)')
print("Find \\stuff:", re.search("\\\\stuff", rand_str))

sep_ex()

rand_str = "Here is \\stuff"
print('re.search(r"\\stuff", rand_str)')
print("Find \\stuff:", re.search(r"\\stuff", rand_str))

      
