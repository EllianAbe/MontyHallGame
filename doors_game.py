import random


def play():
    available_doors = set([1, 2, 3])

    # there is a car behind a random door
    car_door = random.choice(list(available_doors))

    # the user picks a door
    user_choice = int(input('choose door:'))

    # monty hall shows you a goat behind another door
    goat_door = random.choice(
        list(available_doors - set([car_door]) - set([user_choice])))

    print('there is a goat in door ' + str(goat_door))

    available_doors.remove(goat_door)

    # monty hall asks if you want to switch
    switch_choice = input('want to switch? (empty for no, anything for yes)')
    switch_choice = not switch_choice == ''

    if switch_choice:
        user_choice = list(available_doors - set([user_choice]))
        user_choice = user_choice[0]

    print('you chose door: ' + str(user_choice))

    # you win if you chose the car door
    trophy = 'car' if user_choice == car_door else 'goat'

    print('you won a', trophy)

    return [user_choice, switch_choice, trophy]


def multiple(number):
    results = []
    for i in range(number):
        result = play()
        results.append(result)
