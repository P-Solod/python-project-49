import random

import prompt

from brain_games.scripts.hello_user import weclome_user
from brain_games.scripts.helper_script import checking_answers


def main():
    name = weclome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0

    while True:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)

        print(f'Question: {number_1} {number_2}')
        answer = prompt.integer('Your answer: ')

        while number_1 != 0 and number_2 != 0:
            if number_1 > number_2:
                number_1 = number_1 % number_2
            else:
                number_2 = number_2 % number_1

        flag = number_1 + number_2

        if not checking_answers(flag, answer, count, name):
            break
        count += 1


if __name__ == '__main__':
    main()