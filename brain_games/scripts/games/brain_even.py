import random

import prompt

from brain_games.scripts.hello_user import weclome_user
from brain_games.scripts.helper_script import checking_answers


def main():
    name = weclome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while True:
        number = random.randint(1, 100)
        if number % 2 == 0:
            flag = 'yes'
        else:
            flag = 'no'

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if not checking_answers(flag, answer, count, name):
            break
        count += 1


if __name__ == '__main__':
    main()