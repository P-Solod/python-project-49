import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0

    while count < 3:
        numbers = random.randint(1, 100)
        if numbers % 2 == 0:
            flag = 'yes'
        else:
            flag = 'no'

        print(f'Question: {numbers}')
        answer = prompt.string('Your answer: ')

        if answer == flag:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{flag}'.")
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()