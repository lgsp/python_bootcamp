def add_numbers(num_1, num_2):
    return num_1 + num_2

print("5 + 4 =", add_numbers(5, 4))

def assign_name():
    name = "Doug"

def change_name(name):
    name = "Mark"

def change_name2():
    return "Mark"    

name = "Tom"    
change_name(name)
print(name)
name = change_name2()
print(name)

gbl_name = "Sally"
def change_name3():
    global gbl_name
    gbl_name = "Sam"

change_name3()
print(gbl_name)    

def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

pi = 3.14
print(f"Is {pi} (type(pi) = {type(pi)}) a Float: {is_float(pi)}")
pi = "3.14"
print(f"Is {pi} a (type(pi) = {type(pi)}) Float: {is_float(pi)}")
pi = "314/100"
print(f"Is {pi} a (type(pi) = {type(pi)}) Float: {is_float(pi)}")
pi_num = 314
print(f"Is {pi_num} a (type(pi_num) = {type(pi_num)}) Float: {is_float(pi_num)}")
pi_denom = 100
print(f"Is {pi_denom} a (type(pi_denom) = {type(pi_denom)}) Float: {is_float(pi_denom)}")
pi = pi_num/pi_denom
print(f"Is {pi_num}/{pi_denom} = {pi} a (type(pi) = {type(pi)}) Float: {is_float(pi)}")
pi_num = "314"
print(f"Is {pi_num} a (type(pi_num) = {type(pi_num)}) Float: {is_float(pi_num)}")
pi_denom = "100"
print(f"Is {pi_denom} a (type(pi_denom) = {type(pi_denom)}) Float: {is_float(pi_denom)}")

def solve_eq(equation):
    x, add, num_1, equal, num_2 = equation.split()
    num_1, num_2 = int(num_1), int(num_2)
    return "x = " + str(num_2 - num_1)

print(solve_eq("x + 4 = 9"))

def mult_divide(num_1, num_2):
    return (num_1 * num_2), (num_1 / num_2)

mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def get_primes(max_number):
    list_of_primes = []
    for num_1 in range(2, max_number):
        if is_prime(num_1):
            list_of_primes.append(num_1)
    return list_of_primes

max_num_to_check = int(input("Search for Primes up to: "))

list_of_primes = get_primes(max_num_to_check)
for prime in list_of_primes:
    print(prime)

def sum_all(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1

print("1 + 2 + 3 + 4 =", sum_all(1, 2, 3, 4))
n = int(input("n = "))
sum_1_n = sum_all(*range(1, n+1))
print(f"1 + 2 + ... + {n} = {sum_1_n}")

