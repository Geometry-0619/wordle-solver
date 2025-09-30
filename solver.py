from wordle import *

if __name__ == '__main__':
    count = 0
    valid_answers = valid_answers0[:]

    while True:
        if len(valid_answers) == 1:
            print(f"The correct answer is {valid_answers[0]}")
            print(f"Score: {count + 1}")
            break

        print(f'Information needed: {np.log2(len(valid_answers)):.3f}')

        if count == 0:
            best_word = 'SOARE'
            print(f"Best guess is {best_word} with expected information {5.885}")
        else:
            best_word, entropies = find_best_guess(valid_words, valid_answers)
            print(f"Best guess is {best_word} with expected information {entropies[best_word]:.3f}")

        x = input('Enter the guess: (Press enter to use the suggested word) ')
        if x == '':
            guess = best_word
        else:
            guess = x.upper()

        print('Enter the colors as a 5-digit number')
        color = input('Grey = 0, Yellow = 1, Green = 2: ')
        color = [int(c) for c in color]

        valid_answers = reduce_possibilities(guess, color, valid_answers)
        if len(valid_answers) <= 20:
            print(valid_answers)

        count += 1