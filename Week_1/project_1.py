rate = input("Rate: ")
time = input("Time: ")
principal = input("Principal: ")
rate, time, principal = float(rate), float(time), float(principal)
per = rate/100
c = per * time
amount = principal * (1+ c)
print("A is :", amount)
