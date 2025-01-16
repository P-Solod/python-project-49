import random

from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0

    while True:
        if count == 3:
            print(f'Congratulations, {user_name}!')
            break

        else:
            numbers = random.randint(1, 100)
            if numbers % 2 == 0:
                flag = 'yes'
            else:
                flag = 'no'

            print(f'Question: {numbers}')
            answer = input('Your answer: ')

            if answer == flag:
                print('Correct!')
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{flag}'.")
                print(f"Let's try again, {user_name}!")
                break


if __name__ == '__main__':
    main()
