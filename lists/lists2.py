import math

even_list = [i*2 for i in range(5)]
for k in even_list:
    print(k, end=", ")
print()

num_list = [1, 2, 3, 4, 5]
list_of_values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in num_list]

for k in list_of_values:
    print(k)
print()

mult_d_list = [[0] * 5 for i in range(5)]
mult_d_list[0][1] = 5
print(mult_d_list[0][1])

for i in range(5):
    for j in range(5):
        mult_d_list[i][j] = "{} : {}".format(i, j)

for i in range(5):
    for j in range(5):
        print(mult_d_list[i][j], end=" || ")
    print()

time_tables = [[i * j for j in range(1, 10)] for i in range(1, 10)]
for i in range(9):
    for j in range(9):
        print(time_tables[i][j], end=", ")
    print()

