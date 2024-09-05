word_list = [
'türkiye ',
'madrid',
'korona',
'malatya',
'Kahramanmaraş',
'adana',
'hatay',
'adıyaman',
'fenerbahce',
'mercedes',
'istanbul',
'galatasaray',
'beşiktaş',
'şampiyon'
]
import random
lives =6
chosen_word = random.choice(word_list)
words_length = len(chosen_word)
answer = []
print(chosen_word)
for _ in range(words_length):
    answer+= "_"

output = []
is_game = False
while not is_game:
    guess = input("What is your guess : \n ").lower()
    for letters in range(words_length):
        letter = chosen_word[letters]
        if (letter == guess[0]):
            answer[letters]=guess[0]
            if ( "_" not in answer):
                print("you win")
                is_game=True
    if (guess not in chosen_word):
        lives -=1
        print(f"Try again '{guess[0]}' is not inside.You lost live. You have a {lives} live")
        if (lives == 0):
            print(f"You Lose answer is {chosen_word} ")
            is_game=True


    print(answer)