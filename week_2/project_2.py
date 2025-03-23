import math
import cmath

operation = input("What type of operation do you want to perform? ").lower()

# Quadratic Equation: ax^2 + bx + c = 0
if operation == "quadratic equation":
    a = int(input("Input coefficient of x^2: "))
    b = int(input("Input coefficient of x: "))
    c = int(input("Input constant: "))

    dis = b ** 2 - 4 * a * c

    if dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")

    elif dis == 0:
        x = -b / (2 * a)
        print(f"One real root: x = {x}")

    else:
        x1 = (-b + cmath.sqrt(dis)) / (2 * a)
        x2 = (-b - cmath.sqrt(dis)) / (2 * a)
        print(f"Two complex roots: x1 = {x1}, x2 = {x2}")

# Cubic Equation: ax^3 + bx^2 + cx + d = 0
elif operation == "cubic equation":
    a = int(input("Input coefficient of x^3: "))
    b = int(input("Input coefficient of x^2: "))
    c = int(input("Input coefficient of x: "))
    d = int(input("Input constant: "))

    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
    dis = (q / 2) ** 2 + (p / 3) ** 3

    if dis > 0:
        u = (-q / 2 + cmath.sqrt(dis)) ** (1 / 3)
        v = (-q / 2 - cmath.sqrt(dis)) ** (1 / 3)
        x1 = u + v - b / (3 * a)
        print(f"One real root: x = {x1}")

    elif dis == 0:
        x1 = (3 * q) / (2 * p) - b / (3 * a)
        x2 = (-3 * q) / (2 * p) - b / (3 * a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")

    else:
        r = math.sqrt(-p / 3)
        theta = math.acos(-q / (2 * r**3))
        x1 = 2 * r * math.cos(theta / 3) - b / (3 * a)
        x2 = 2 * r * math.cos((theta + 2 * math.pi) / 3) - b / (3 * a)
        x3 = 2 * r * math.cos((theta + 4 * math.pi) / 3) - b / (3 * a)
        print(f"Three real roots: x1 = {x1}, x2 = {x2}, x3 = {x3}")

# Quartic Equation: ax^4 + bx^3 + cx^2 + dx + e = 0
elif operation == "quartic equation":
    a = int(input("Input coefficient of x^4: "))
    b = int(input("Input coefficient of x^3: "))
    c = int(input("Input coefficient of x^2: "))
    d = int(input("Input coefficient of x: "))
    e = int(input("Input constant: "))

    p = (8 * a * c - 3 * b**2) / (8 * a**2)
    q = (b**3 - 4 * a * b * c + 8 * a**2 * d) / (8 * a**3)
    r = (-3 * b**4 + 256 * a**3 * e - 64 * a**2 *
         b * d + 16 * a * b**2 * c) / (256 * a**4)

    A = 1
    B = 2 * p
    C = p**2 - 4 * r
    D = -q**2

    delta0 = B**2 - 3 * A * C
    delta1 = 2 * B**3 - 9 * A * B * C + 27 * A**2 * D
    dis = (delta1**2 - 4 * delta0**3) / -27

    if dis.real > 0:
        C_val = ((delta1 + math.sqrt(dis.real)) / 2) ** (1 / 3)
    elif dis.real == 0:
        C_val = (delta1 / 2) ** (1 / 3)
    else:
        C_val = ((delta1 + cmath.sqrt(dis)) / 2) ** (1 / 3)

    z = -1 / (3 * A) * (B + C_val + delta0 / C_val)
    sqrt_z = cmath.sqrt(z) if z.real < 0 else math.sqrt(z.real)

    dis1 = sqrt_z**2 - 4 * (p / 2 + z - q / (2 * sqrt_z))
    dis2 = sqrt_z**2 - 4 * (p / 2 + z + q / (2 * sqrt_z))

    if dis1.imag != 0:
        y1 = (-sqrt_z + cmath.sqrt(dis1)) / 2
        y2 = (-sqrt_z - cmath.sqrt(dis1)) / 2
    else:
        y1 = (-sqrt_z + math.sqrt(dis1.real)) / 2
        y2 = (-sqrt_z - math.sqrt(dis1.real)) / 2

    if dis2.imag != 0:
        y3 = (sqrt_z + cmath.sqrt(dis2)) / 2
        y4 = (sqrt_z - cmath.sqrt(dis2)) / 2
    else:
        y3 = (sqrt_z + math.sqrt(dis2.real)) / 2
        y4 = (sqrt_z - math.sqrt(dis2.real)) / 2

    x1 = y1 - b / (4 * a)
    x2 = y2 - b / (4 * a)
    x3 = y3 - b / (4 * a)
    x4 = y4 - b / (4 * a)

    print(
        f"Roots of the quartic equation: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
