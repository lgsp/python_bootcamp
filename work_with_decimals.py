from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
print("Sum = ", sum)

sum_1 = D(0)
sum_1 += D("0.011111111111111")
sum_1 += D("0.011111111111111")
print("Sum =", sum_1)
sum_1 -= D("0.022222222222222")
print("Sum =", sum_1)
