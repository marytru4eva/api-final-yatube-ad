# game.py

from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(message):
    """Сохраняет результат игры в файл results.txt, используя with ... as."""
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(message + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делают {current_player}')

        # Бесконечный цикл для ввода координат
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
                    
                break  # Выходим из цикла, если всё правильно
                
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
            except CellOccupiedError:
                print('Ячейка занята. Введите другие координаты.')
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                print('Введите значения заново.')

        # Делаем ход
        game.make_move(row, column, current_player)
        game.display()
        
        # Проверка победы
        winner = game.check_winner()
        if winner:
            result_message = f'Победили {winner}'
            print(result_message)
            save_result(result_message)
            running = False
        elif game.is_full():
            result_message = 'Ничья!'
            print(result_message)
            save_result(result_message)
            running = False
        else:
            # Меняем игрока только если игра продолжается
            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()