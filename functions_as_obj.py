def mult_by_2(num):
    return num * 2

times_two = mult_by_2
print("4 * 2 =", times_two(4))

def do_math(func, num):
    return func(num)

print("8 * 2 =", do_math(mult_by_2, 8))

def affine(a, b, x): return a*x + b
def square(x): return x**2
def cube(x): return x**3

c = cube
a, b = 2, 3
f = affine
for x in range(10):
    disp = f"x = {x}   2*{x}**3 + 3 = {f(a, b, c(x))}"
    disp += f"   (2*{x} + 3)**3 = {c(f(a, b, x))}"
    print(disp)

def get_func_mult_by_num(num):
    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)
print("5 * 9 = ", generated_func(9))

list_of_funcs = [times_two, generated_func]

for i in range(1, 11): print("5 *",  i, "=", list_of_funcs[1](i))

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
def change_list(liste, func):
    odds = []
    for i in liste:
        if func(i): odds.append(i)
    return odds

print(change_list([1, 2, 3, 4, 5, 6], is_it_odd))
print(change_list(list(range(10)), is_it_odd))

def random_func(name: str, age: int, weight: float) -> str:
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)
    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))
print(random_func(41, "Derek", 165.5))
print(random_func.__annotations__)


      
