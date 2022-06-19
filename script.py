import random


def run():
    random_number = random.randint(1, 100)
    user_number = int(input('Choose a number in a 1 - 100 range 😼: '))
    while user_number != random_number:
        if(user_number < random_number):
            print('Wrong 😥, choose a higher number')
        else: 
            print('Wrong 😥, choose a smaller number')
        user_number = int(input('Try it again 🤞🏻: '))
    print('---------------')
    print('You got it 🥇')
    print('Its ' + str(random_number) + ' 🥳')


if __name__ == '__main__':
    run()