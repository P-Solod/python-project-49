
def checking_answers(flag, answer, count, name):
    if answer == flag:
        print('Correct!')
        count += 1

        if count == 3:
            print(f'Congratulations, {name}!')
            return False

        return True

    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{flag}'.")
        print(f"Let's try again, {name}")
        return False