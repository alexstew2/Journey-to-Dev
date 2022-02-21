weight = float(input("What is your weight? "))
unit = input("(K)g or (L)bs: ")
if unit == 'K' or unit == 'k':
    weight = weight * 2.2
    print(f'Weight in lbs: {weight}')
elif unit == 'L' or unit == 'l':
    weight = weight / 2.2
    print(f'Weight in Kgs: {weight}')
else:
    print("Unknown unit")
