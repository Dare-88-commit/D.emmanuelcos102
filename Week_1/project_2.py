rate = input("Rate: ")
n = input("n: ")
time = input("Time: ")
principal = input("Principal: ")
rate, n, time, principal = float(rate), float(n), float(time), float(principal)
power = n * time
c = (rate / 100) / n
m = 1 + c
amount = principal * m**power
print("A is :", amount)