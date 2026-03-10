"""
BÀI 3: MÃ DI TUẦN (MADIUAN.*)
"""


class MaDiTuan:
    """Bài 3: Mã di tuần - Horse Tour Problem"""
    
    def __init__(self, n, start_x, start_y):
        self.n = n
        self.start_x = start_x
        self.start_y = start_y
        self.board = [[-1 for _ in range(n)] for _ in range(n)]
        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                      (1, 2), (1, -2), (-1, 2), (-1, -2)]
        self.solution = None
        self.count = 0
    
    def is_valid(self, x, y):
        """Kiểm tra xem ô (x, y) hợp lệ"""
        return 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == -1
    
    def backtrack(self, x, y, step):
        """Quay lui để tìm lộ trình"""
        self.board[x][y] = step
        
        # Đã thăm hết N² ô
        if step == self.n * self.n - 1:
            self.solution = [row[:] for row in self.board]
            self.count += 1
            self.board[x][y] = -1
            return True
        
        # Thử từng nước đi
        for dx, dy in self.moves:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                if self.backtrack(nx, ny, step + 1):
                    self.board[x][y] = -1
                    if self.solution is not None:
                        return True
        
        self.board[x][y] = -1
        return False
    
    def solve(self):
        """Giải bài toán mã di tuần"""
        if self.is_valid(self.start_x, self.start_y):
            self.backtrack(self.start_x, self.start_y, 0)
        return self.solution
    
    def display_result(self):
        """Hiển thị kết quả"""
        print(f"Mã di tuần trên bàn cờ {self.n}x{self.n}, bắt đầu từ ({self.start_x}, {self.start_y}):")
        if self.solution:
            print("\nLộ trình (thứ tự thăm các ô):")
            for row in self.solution:
                print(' '.join(f'{x+1:2d}' if x >= 0 else ' .' for x in row))
            print(f"\nTìm thấy lộ trình")
        else:
            print("Không tìm thấy lộ trình nào")


if __name__ == "__main__":
    print("="*60)
    print("BÀI 3: MÃ DI TUẦN")
    print("="*60)
    
    # Ví dụ: bàn cờ 5x5
    mdt = MaDiTuan(5, 0, 0)
    mdt.solve()
    mdt.display_result()
