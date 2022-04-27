import random
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 9))

def test_list():
    for k in num_list:
        print(k, end=", ")
    print()

print("Imitially")
test_list()

print("Sort")
num_list.sort()
test_list()

print("Reverse")
num_list.reverse()
test_list()

print("Insert value")
num_list.insert(5, 10)
test_list()

print("Remove value")
num_list.remove(10)
test_list()

print("Remove last value")
num_list.pop(2)
test_list()



