import random


def play_game(initial_money):
    money = initial_money

    while True:
        print(f'У вас на счету: {money}')

        try:
            picked_slot = int(input('Выберите слот от 1 до 30: '))
            if picked_slot > 30 or picked_slot < 1:
                raise ValueError
        except ValueError:
            print('Вы ввели не корректный слот!')
            continue

        try:
            picked_amount = int(input('Введите сумму ставки: '))
            if picked_amount > money or picked_amount <= 0:
                print('Вы ввели не корректную сумму!')
                continue
        except ValueError:
            print('Вы ввели не корректный слот!')
            continue

        winning_slot = random.randint(1, 30)

        print(f'Выигрышный слот: {winning_slot}')

        if picked_slot == winning_slot:
            print('Вы выиграли ставку!')
            money += picked_amount * 2
        else:
            print('Вы проиграли ставку!')
            money -= picked_amount

        is_repeat_again = input('Хотите ли вы сыграть еще? (Да, Нет) - ')

        if is_repeat_again != 'Да':
            print(f'У вас на счету: {money}')
            break
