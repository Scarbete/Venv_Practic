from decouple import config
from game_logic import play_game


def start_game():
    initial_money = config('MY_MONEY', cast=int, default=5)
    play_game(initial_money=initial_money)


if __name__ == '__main__':
    start_game()
