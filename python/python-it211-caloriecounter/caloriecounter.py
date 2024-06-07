# Calorie Counter program

import calorietracker

# main definition
def main():
    total = 0
    calorie_men = 2500
    calorie_women = 2000
    day = int(input('What day is it? '))
    calorietracker.calorietracker["day"] = day
    
    input_string = input("Enter the food you had today. (Separate with a space) ")
    food_list = input_string.split(" ")
    calorietracker.calorietracker["foods"] = food_list
    print("\n")
    print("List of food.")
    print('-------------')
    for name in food_list:
        print(name)
    print('\n')

    items = int(input('How many items did you enter? '))
    for x in range(items):
        calorie = int(input('Input the calories per item. '))
        total = total + calorie
    calorietracker.calorietracker["calories"] = total
    
    print('\n')    
    gender = input('What is you gender? (m/f) ')
    if gender == 'm':
        print('Your daily intake of calories should be', calorie_men)
        if total < calorie_men:
            print('You are', calorie_men - total, 'below your daily intake.')
        elif total > calorie_men:
            print('You are', total - calorie_men, 'above your daily intake.')
        elif total == calorie_men:
            print('You have met the daily intake recommendation!')
    elif gender == 'f':
        print('Your daily intake of calories should be', calorie_women)
        if total < calorie_women:
            print('You are', calorie_women - total, 'below your daily intake.')
        elif total > calorie_women:
            print('You are', total - calorie_women, 'above your daily intake.')
        elif total == calorie_men:
            print('You have met the daily intake recommendation!')    
    print('\n')    
    keep = input('Would you like to start another day (y/n)? ')
    if keep == 'y':
        print(calorietracker.calorietracker)
        main()
    elif keep == 'n':
        print('See you next time!')

#main program function
print('Welcome to your daily calorie counter.')
print('--------------------------------------')
main()