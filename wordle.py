import numpy as np
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)  # ignore the numpy warnings
from concurrent.futures import ProcessPoolExecutor

def load_wordlist(filepath: str) -> list[str]:
    """Load words from file, convert to uppercase"""
    with open(filepath, "r") as f:
        return [line.strip().upper() for line in f if line.strip()]

valid_words = load_wordlist("valid-wordle-words.txt")
valid_answers0 = load_wordlist("valid-wordle-answers.txt")

def compare(guess: str, answer: str) -> list[int]:
    """Return Wordle coloring as list of 5 values: 0=grey, 1=yellow, 2=green"""
    result = [0] * 5
    guess = list(guess)
    answer = list(answer)

    # Green
    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = 2
            guess[i] = '#'
            answer[i] = '$'

    # Yellow
    for i in range(5):
        for j in range(5):
            if guess[i] == answer[j]:
                result[i] = 1
                answer[j] = '$'

    return result

def ternary(color: list[int]) -> int:
    """Convert each wordle coloring to a unique number by ternary"""
    return sum([color[i] * 3**(4 - i) for i in range(5)])

def weighted_information(p: np.ndarray) -> np.ndarray:
    """Convert probabilities to information"""
    return np.where(p == 0, 0, p * np.log2(1 / p))

def calculate_entropy(guess: str, valid_answers: list[str]) -> float:
    """Calculate the entropy of guess, given the remaining possibilities of answers"""
    counts = np.zeros(3 ** 5, dtype=int)

    for answer in valid_answers:
        counts[ternary(compare(guess, answer))] += 1

    probs = counts / len(valid_answers)
    return np.sum(weighted_information(probs))

def find_best_guess(valid_words: list[str], valid_answers: list[str]) -> tuple[str, dict[str, float]]:
    """Return the current best guess as well as the dictionary containing all words with its entropy"""
    entropies = {}
    for word in valid_words:
        ent = calculate_entropy(word, valid_answers)
        entropies[word] = ent

    best_word = max(entropies, key=entropies.get)
    return best_word, entropies

def reduce_possibilities(guess: str, color: list[int], valid_answers: list[str]) -> list[str]:
    """Filter the possible answers"""
    return [word for word in valid_answers if compare(guess, word) == color]