import random

import prompt

from brain_games.scripts.hello_user import weclome_user
from brain_games.scripts.helper_script import checking_answers


def main():
    name = weclome_user()
    print('What number is missing in the progression?')
    count = 0

    while True:
        number = random.randint(1, 100)
        arithmetic_progression = [number]
        progression_difference = random.randint(1, 10)

        while len(arithmetic_progression) != 10:
            number = number + progression_difference
            arithmetic_progression.append(number)

        list_item = random.randint(0, 9)
        flag = arithmetic_progression[list_item]

        arithmetic_progression_copy = arithmetic_progression.copy()
        arithmetic_progression_copy[list_item] = ('..')

        print(f'Question: {arithmetic_progression_copy}')
        answer = prompt.integer('Your answer: ')

        if not checking_answers(flag, answer, count, name):
            break
        count += 1


if __name__ == '__main__':
    main()