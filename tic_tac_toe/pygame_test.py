# game.py

import pygame

# Импортируем класс Board из пакета gameparts
from gameparts import Board

# Константы для графического интерфейса
CELL_SIZE = 100  # Размер одной ячейки в пикселях
BOARD_SIZE = 3  # Размер поля 3x3
WIDTH = CELL_SIZE * BOARD_SIZE  # Ширина окна
HEIGHT = CELL_SIZE * BOARD_SIZE  # Высота окна
LINE_WIDTH = 5  # Толщина линий
FPS = 60  # Частота обновления экрана

# Цвета в формате RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
clock = pygame.time.Clock()


def draw_grid():
    """Рисует сетку игрового поля."""
    # Рисуем вертикальные линии
    for x in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            BLACK,
            (x * CELL_SIZE, 0),
            (x * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )
    
    # Рисуем горизонтальные линии
    for y in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            BLACK,
            (0, y * CELL_SIZE),
            (WIDTH, y * CELL_SIZE),
            LINE_WIDTH
        )


def draw_figures(board):
    """Рисует крестики и нолики на поле."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                # Рисуем крестик
                start_pos1 = (col * CELL_SIZE + 15, row * CELL_SIZE + 15)
                end_pos1 = ((col + 1) * CELL_SIZE - 15, (row + 1) * CELL_SIZE - 15)
                start_pos2 = ((col + 1) * CELL_SIZE - 15, row * CELL_SIZE + 15)
                end_pos2 = (col * CELL_SIZE + 15, (row + 1) * CELL_SIZE - 15)
                pygame.draw.line(screen, RED, start_pos1, end_pos1, LINE_WIDTH)
                pygame.draw.line(screen, RED, start_pos2, end_pos2, LINE_WIDTH)
            
            elif board[row][col] == 'O':
                # Рисуем нолик
                center = (col * CELL_SIZE + CELL_SIZE // 2, 
                         row * CELL_SIZE + CELL_SIZE // 2)
                pygame.draw.circle(screen, BLUE, center, CELL_SIZE // 2 - 15, LINE_WIDTH)


def save_result(message):
    """Сохраняет результат игры в файл."""
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(message + '\n')


def main():
    """Главная функция игры."""
    game = Board()
    current_player = 'X'
    running = True
    
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Обработка клика мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Получаем координаты клика
                x, y = pygame.mouse.get_pos()
                
                # Определяем номер строки и столбца
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                
                # Проверяем, что ячейка пуста
                if game.board[row][col] == ' ':
                    # Делаем ход
                    game.make_move(row, col, current_player)
                    
                    # Проверяем победу
                    winner = game.check_winner()
                    if winner:
                        print(f'Победили {winner}')
                        save_result(f'Победили {winner}')
                        # Здесь можно добавить задержку или перезапуск
                        running = False
                    
                    # Проверяем ничью
                    elif game.is_full():
                        print('Ничья!')
                        save_result('Ничья!')
                        running = False
                    
                    # Меняем игрока
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'
        
        # Отрисовка
        screen.fill(WHITE)  # Заливаем фон белым
        draw_grid()  # Рисуем сетку
        draw_figures(game.board)  # Рисуем фигуры
        
        # Обновляем экран
        pygame.display.flip()
        clock.tick(FPS)
    
    # Завершение работы
    pygame.quit()


if __name__ == '__main__':
    main()