number_of_staff = 2500


for i in range(number_of_staff):
    print(f"\nEnter details for Staff {i + 1}:")
    yoe = int(input("Years of experience: "))  # yoe = years of experience
    age = int(input("Age: "))

    if yoe > 25 and age >= 55:
        print("The Annual Tax Revenue is N5,600,000")
    elif yoe > 20 and age >= 45:
        print("The Annual Tax Revenue is N4,480,000")
    elif yoe > 10 and age >= 35:
        print("The Annual Tax Revenue is N1,500,000")
    else:
        print("The Annual Tax Revenue is N550,000")
