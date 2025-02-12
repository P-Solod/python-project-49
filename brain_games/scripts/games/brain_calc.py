from brain_games.scripts.hello_user import weclome_user
from brain_games.scripts.helper_script import checking_answers
import random
import prompt

def main():
    name = weclome_user()
    print('What is the result of the expression?')
    count = 0

    while True:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        symbol = random.choice(['+', '-', '*'])

        if symbol == '+':
            flag = number_1 + number_2
        elif symbol == '-':
            flag = number_1 - number_2
        else:
            flag = number_1 * number_2

        print(f'Question: {number_1} {symbol} {number_2}')
        answer = prompt.integer('Your answer: ')

        if not checking_answers(flag, answer, count, name):
            break
        count += 1

if __name__ == '__main__':
    main()