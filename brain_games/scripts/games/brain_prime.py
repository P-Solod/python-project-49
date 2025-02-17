import random

import prompt

from brain_games.scripts.hello_user import weclome_user
from brain_games.scripts.helper_script import checking_answers


def prime(number):
    if number == 1:
        flag = 'no'
        return flag
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            flag = 'no'
            return flag
    else:
        flag = 'yes'
        return flag


def main():
    name = weclome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0

    while True:
        number = random.randint(1, 1000)
        flag = prime(number)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if not checking_answers(flag, answer, count, name):
            break
        count += 1


if __name__ == '__main__':
    main()