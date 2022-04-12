def fib_rec(num):
    if num == 0: return 0
    elif num == 1: return 1
    else: return fib_rec(num-1) + fib_rec(num-2)

for num in range(30): print(f"Fibonacci #{num} = {fib_rec(num)}")
    
