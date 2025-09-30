from wordle import *

def plus_one(nums: list[int]) -> list[int]:
    if nums[-1] == 2:
        return plus_one(nums[:-1]) + [0]
    else:
        nums[-1] += 1
        return nums

def generate() -> list[list[int]]:
    """Generate a list containing all possible wordle colorings"""
    result = []
    curr_list = [0, 0, 0, 0, 0]
    while curr_list != [2, 2, 2, 2, 2]:
        result.append(curr_list[:])
        curr_list = plus_one(curr_list)
    result.append([2, 2, 2, 2, 2])
    return result

def load(color: list[int]) -> tuple[str, str]:
    """Input a wordle coloring, output that coloring together with the best guess"""
    valid_answers = reduce_possibilities('SOARE', color, valid_answers0)
    entropies = {}
    for word in valid_words:
        ent = calculate_entropy(word, valid_answers)
        entropies[word] = ent

    best_word = max(entropies, key=entropies.get)
    return ''.join(map(str, color)), best_word

def load_second_guess() -> dict[str, str]:
    """Use concurrent.futures to create a dictionary that gives the best second guess"""
    with ProcessPoolExecutor() as executor:
        results = executor.map(load, generate())
    return dict(results)

# if __name__ == '__main__':
#     print(load_second_guess())
