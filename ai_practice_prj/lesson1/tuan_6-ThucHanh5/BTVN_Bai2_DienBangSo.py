class DienBangSo:

    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.solution = None

    def input_data(self):
        for i in range(9):
            line = input(f"Hàng {i+1}: ").strip()
            for j in range(9):
                if line[j] == '.':
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = int(line[j])

    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False
        for i in range(9):
            if self.board[i][col] == num:
                return False
        sr, sc = (row // 3) * 3, (col // 3) * 3
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def backtrack(self):
        empty = self.find_empty()
        if empty is None:
            self.solution = [row[:] for row in self.board]
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.backtrack():
                    return True
                self.board[row][col] = 0
        return False

    def solve(self):
        self.backtrack()
        return self.solution

    def display_result(self):
        if not self.solution:
            print("IMPOSSIBLE")
        else:
            for row in self.solution:
                print(''.join(str(x) for x in row))


# Test
dienbangso = DienBangSo()
dienbangso.input_data()
dienbangso.solve()
dienbangso.display_result()
