class Board:
    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        # Проверка координат
        if row < 0 or row >= self.field_size or col < 0 or col >= self.field_size:
            print("Ошибка: координаты должны быть от 0 до 2!")
            return False
        
        # Проверка занятости
        if self.board[row][col] != ' ':
            print("Ошибка: эта клетка уже занята!")
            return False
        
        self.board[row][col] = player
        return True

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_winner(self):
        """Проверка победителя"""
        # Проверка строк
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None

    def is_full(self):
        """Проверка на ничью"""
        for row in self.board:
            if ' ' in row:
                return False
        return True