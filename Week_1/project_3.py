pmt = input("Periodic payment: ")
rate = input("Rate: ")
time = input("Time: ")
n = input("n: ")
n, pmt, rate, time = float(n), float(pmt), float(rate), float(time)
c = (rate / 100) / n
d = (1 + c) ** (n * time)
f = d - 1
m = f / c
amount = pmt * m
print("A is:", amount)
