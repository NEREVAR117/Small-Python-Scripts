diameter_one = float(input("What's the first pizza's diameter (in inches)?"))
cost_one = float(input("How much does the first pizza cost? (in dollars and cents)"))
area_one = (diameter_one / 2) ** 2 * 3.14
total_one = round(cost_one / area_one, 2)

print("With this pizza, you're paying", total_one, "per square inch.")

diameter_two = float(input("What's the second pizza's diameter (in inches)?"))
cost_two = float(input("How much does the second pizza cost? (in dollars and cents)"))
area_two = (diameter_two / 2) ** 2 * 3.14
total_two = round(cost_two / area_two, 2)

print('With this pizza, you\'re paying', total_two, "per square inch.")

if total_one < total_two:
    print("The first pizza is a better value. Buy that one!")
elif total_two < total_one:
    print("The second pizza is the better deal - more pizza for the buck. Get that one!")
else:
    print("Same deal per square inch of pizza - they represent the same value.")