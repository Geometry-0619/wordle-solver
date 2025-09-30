from second_guess import *

# Calculate the average score obtained by the algorithm through all words
if __name__ == '__main__':
    boxes = ["⬜️", "🟨", "🟩️"]
    freq = []
    print('Loading second guess...')
    second_guess = load_second_guess()

    for i in range(len(valid_answers0) - 1):
        print(f"--------- Game {i + 1} ---------")
        valid_answers = valid_answers0[:]
        answer = valid_answers[i]
        print(f"Answer: {answer}")
        count = 0

        while True:
            if len(valid_answers) == 1:
                print(f"Guessing: {valid_answers[0]} {"🟩️🟩️🟩️🟩️🟩️"}")
                print(f"Score: {count + 1}")
                freq.append(count + 1)
                break

            if count == 0:
                best_word = 'SOARE'
            elif count == 1:
                best_word = second_guess[''.join(map(str, color))]
            else:
                best_word = find_best_guess(valid_words, valid_answers)[0]

            guess = best_word
            color = compare(guess, answer)
            print(f"Guessing: {guess} {''.join([boxes[int(i)] for i in color])}")
            valid_answers = reduce_possibilities(guess, color, valid_answers)
            count += 1

    print(f"Average score: {sum(freq) / len(valid_answers0)}")
