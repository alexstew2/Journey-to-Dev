start = int(input("start:" ))
end = int(input("end:" ))

# Convert user input to ints
# add some if statements to check input as valid int
# if it isn't prompt for proper input

for i in range(start,end):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
