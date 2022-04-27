rand_list = ["string", 1.234, 28]
print("rand_list =", rand_list)
one_to_ten = list(range(11))
rand_list = rand_list + one_to_ten
print("rand_list =", rand_list)
print("rand_list[0] =", rand_list[0])
print("List length:", len(rand_list))

first_3 = rand_list[0:3]
print("First 3:")
for i in first_3:
    print("{} : {}".format(first_3.index(i), i))

print("Index zero, three times")
print(first_3[0] * 3)
print("string" in first_3)
print("Index of string:", first_3.index("string"))
print("How many strings:", first_3.count("string"))
first_3[0] = "New String"
first_3.append("Another")
for i in first_3:
    print("{} : {}".format(first_3.index(i), i))
    
