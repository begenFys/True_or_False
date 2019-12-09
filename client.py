from game import Game
from game_result import GameResult
from game_status import GameStatus


def end_of_game_handrel(result: GameResult):
    print(f"Questions asked: {result.questions_passed}. Mistakes made: {result.mistakes_made}.")
    print(f"You won!" if result.won else "You lost!")


game = Game("..\\True_or_False\\data\\Questions.csv", 2, end_of_game_handrel)

while game.game_status == GameStatus.IN_PROGRESS:
    if game.is_last_question():
        print('no more question')
        break

    q = game.get_next_question()
    print("Do you believe in the next statement or question? Enter 'y' or 'n'")

    print(q.text)
    answer: bool = input() == 'y'

    if q.is_true == answer:
        print("Good job! You're right ")
    else:
        print("Oops, actually you're mistaken. Here is the explanation")
        print(q.explanation)

    game.give_answer(answer)
