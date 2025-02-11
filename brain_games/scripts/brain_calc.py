import random

import prompt

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    count = 0

    while count < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        symbols = ['+', '-', '*']
        symbol = random.choice(symbols)

        if symbol == '+':
            result = number_1 + number_2
        elif symbol == '-':
            result = number_1 - number_2
        else:
            result = number_1 * number_2

        print(f'Question: {number_1} {symbol} {number_2}')
        answer = prompt.integer('Your answer: ')

        if answer == result:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}")
            break

    else:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()