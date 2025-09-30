# wordle-solver
A simple program that solves the wordle game with an average score of 3.64

The game can be played at https://bosorioo.github.io/wordle-unlimited/

The program suggests the best next guess based on information entropy and filters possible answers according to the feedback colors.

The optimal guess will be displayed with its expected information

`wordle.py` contains basic functions to help solving the wordle game

`solver.py` suggests the current optimal word

example usage:

```
Information needed: 11.173
Best guess is SOARE with expected information 5.885
Enter the guess: (Press enter to use the suggested word) SOARE
Enter the colors as a 5-digit number
Grey = 0, Yellow = 1, Green = 2: 01010

Information needed: 5.883
Best guess is CUTIN with expected information 4.060
Enter the guess: (Press enter to use the suggested word) CUTIN
Enter the colors as a 5-digit number
Grey = 0, Yellow = 1, Green = 2: 00000
['GROWL', 'PROXY', 'DROLL', 'FLOOR', 'BROOD', 'GROOM', 'DROOP', 'PROWL', 'DROOL', 'BROOM', 'BROOK', 'PROOF']

Information needed: 3.585
Best guess is GLOOP with expected information 3.189
Enter the guess: (Press enter to use the suggested word) GLOOP
Enter the colors as a 5-digit number
Grey = 0, Yellow = 1, Green = 2: 00220
['BROOD', 'BROOM', 'BROOK']

Information needed: 1.585
Best guess is ADEEM with expected information 1.585
Enter the guess: (Press enter to use the suggested word) ADEEM
Enter the colors as a 5-digit number
Grey = 0, Yellow = 1, Green = 2: 00000
['BROOK']
The correct answer is BROOK
Score: 5
```

To check the average score is indeed 3.64, run `main.py`

The program will play wordle against itself, looping through every possible answer:

```
--------- Game 1 ---------
Answer: CIGAR
Guessing: SOARE ⬜️⬜️🟨🟨⬜️
Guessing: RIYAL 🟨🟩️⬜️🟩️⬜️
Guessing: AARGH 🟨⬜️🟨🟨⬜️
Guessing: CIGAR 🟩️🟩️🟩️🟩️🟩️
Score: 4
--------- Game 2 ---------
Answer: REBUT
Guessing: SOARE ⬜️⬜️⬜️🟨🟨
Guessing: DIRER ⬜️⬜️🟨🟨⬜️
Guessing: BEECH 🟨🟩️⬜️⬜️⬜️
Guessing: REBUT 🟩️🟩️🟩️🟩️🟩️
Score: 4
--------- Game 3 ---------
Answer: SISSY
Guessing: SOARE 🟩️⬜️⬜️⬜️⬜️
Guessing: THILK ⬜️⬜️🟨⬜️⬜️
Guessing: AALII ⬜️⬜️⬜️🟨⬜️
Guessing: SISSY 🟩️🟩️🟩️🟩️🟩️
Score: 4
```
