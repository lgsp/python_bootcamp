import random

def title(ex):
    print(ex)
    print('-' * len(ex))

print("=" * 75)    
intro = "Why should you use comprehension list?"
title(intro)
print()
    
ex1 = "Example #1"
title(ex1)
print("Lambda Function And Map:", end=" ")
print(list(map((lambda x: x * 2), range(1, 11))))

print("Comprehension List:", end=" ")
print([2 * x for x in range(1, 11)])

print("=" * 70)
print()

ex2 = "Example #2"
title(ex2)
print("Lambda Function And Filter:", end=" ")
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

print("Comprehension List:", end=" ")
print([x for x in range(1, 11) if x % 2 != 0])

print([i ** 2 for i in range(50) if i % 8 == 0])

print([x * y for x in range(1, 3) for y in range(11, 16)])

print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])


print([x for x in random.sample(range(1, 1001), 50) if x % 9 == 0])
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

multi_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

print([col[1] for col in multi_list])

print([multi_list[i][i] for i in range(len(multi_list))])

