headers = ["Name", "Age", "Height", "Score"]


girls = [
    ["Evelyn", 17, 5.5, 80],
    ["Jessica", 16, 6.0, 85],
    ["Somto", 17, 5.4, 70],
    ["Edith", 18, 5.9, 60],
    ["Liza", 16, 5.6, 76],
    ["Madonna", 18, 5.6, 66],
    ["Waje", 17, 6.1, 87],
    ["Tola", 20, 6.0, 95],
    ["Aisha", 19, 5.7, 50],
    ["Latifa", 17, 5.5, 49],
]

boys = [
    ["Chinedu", 19, 5.7, 74],
    ["Liam", 16, 5.9, 87],
    ["Wale", 18, 5.8, 75],
    ["Gbenga", 17, 6.1, 68],
    ["Abiola", 20, 5.9, 66],
    ["Kola", 19, 5.5, 78],
    ["Kunle", 16, 6.1, 87],
    ["George", 18, 5.4, 98],
    ["Thomas", 17, 5.8, 54],
    ["Wesley", 19, 5.7, 60],
]

print("| {:<12} | {:<5} | {:<7} | {:<5} |".format(
    headers[0], headers[1], headers[2], headers[3]))
print("-" * 42)

for girl in girls:
    print("| {:<12} | {:<5} | {:<7} | {:<5} |".format(
        girl[0], girl[1], girl[2], girl[3]))

print("-" * 42)

for boy in boys:
    print("| {:<12} | {:<5} | {:<7} | {:<5} |".format(
        boy[0], boy[1], boy[2], boy[3]))

print("-" * 42)
