#State Bird quiz

right = 0
wrong = 0
print('This program will test your knowledge of state brids.')

#create state bird dictionary
birds = {'Alabama':'Yellowhammer',
        'Montana':'Western Meadowlark',
        'Alaska':'Willow Ptarmigan',
        'Nebraska':'Western Meadowlark',
        'Arizona':'Cactus Wren',
        'Nevada':'Mountain Bluebird',
        'Arkansas':'Mockingbird',
        'New Hampshire':'Purple Finch',
        'California':'California Valley Quail',
        'New Jersey':'Eastern Goldfinch',
        'Colorado':'Lark Bunting',
        'New Mexico':'Roadrunner',
        'Connecticut':'Robin',
        'New York':'Bluebird',
        'Delaware':'Blue Hen Chicken',
        'North Carolina':'Cardinal',
        'Florida':'Mockingbird',
        'North Dakota':'Western Meadowlark',
        'Georgia':'Brown Thrasher',
        'Ohio':'Cardinal',
        'Hawaii':'Nene',
        'Oklahoma':'Scissor-tailed Flycatcher',
        'Idaho':'Mountain Bluebird',
        'Oregon':'Western Meadowlark',
        'Illinois':'Cardinal',
        'Pennsylvania':'Ruffed Grouse',
        'Indiana':'Cardinal',
        'Rhode Island':'Rhode Island Red',
        'Iowa':'Eastern Goldfinch',
        'South Carolina':'Great Carolina Wren',
        'Kansas':'Western Meadowlark',
        'South Dakota':'Ring-necked Pheasant',
        'Kentucky':'Cardinal',
        'Tennessee':'Mockingbird',
        'Louisiana':'Eastern Brown Pelican',
        'Texas':'Mockingbird',
        'Maine':'Chickadee',
        'Utah':'Common American Gull',
        'Maryland':'Baltimore Oriole',
        'Vermont':'Hermit Thrush',
        'Massachusetts':'Chickadee',
        'Virginia':'Cardinal',
        'Michigan':'American Robin',      
        'Washington':'Willow Goldfinch',
        'Minnesota':'Common Loon',
        'West Virginia':'Cardinal',
        'Mississippi':'Mockingbird',
        'Wisconsin':'Robin',
        'Missouri':'Bluebird',
        'Wyoming':'Western Meadowlark'}

#Boolean to control when the program ends
done = False

#start quiz
while not done and len(birds) > 0:
    state, bird = birds.popitem()
    print('What is the state bird of', state + '? Press q to quit.')
    guess = input('Enter guess: ')

    if guess.lower() == 'q':
        done = True
    elif guess == bird:
        right += 1
        print('Correct!')
    else:
        wrong += 1
        print('Incorrect. The state bird of', state, 'is', bird + '.\n')

if len(bird) == 0:
    print('You have completed all the states.')

print('Number of correct answers is: ', right)
print('Number of incorrect answers is: ', wrong)