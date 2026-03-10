"""
BÀI 2: XẾP HẬU (NQUEEN PROBLEM - XEPHAU.*)


"""


class XepHau:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.col = set()  # Tập cột đã sử dụng
        self.diag1 = set()  # Tập đường chéo chính (row - col)
        self.diag2 = set()  # Tập đường chéo phụ (row + col)
    
    def input_data(self):
        """Nhập dữ liệu từ bàn phím"""
        self.n = int(input("Nhập N (kích thước bàn cờ NxN): "))
    
    def is_safe(self, row, col):
        """
        Kiểm tra xem có thể đặt quân hậu tại (row, col)
        
        Args:
            row: Hàng
            col: Cột
            
        Returns:
            True nếu an toàn, False nếu không
        """
        # Kiểm tra cột
        if col in self.col:
            return False
        
        # Kiểm tra đường chéo chính (row - col)
        if row - col in self.diag1:
            return False
        
        # Kiểm tra đường chéo phụ (row + col)
        if row + col in self.diag2:
            return False
        
        return True
    
    def backtrack(self, row, current_solution):
        """
        Quay lui để tìm cách xếp hậu
        
        Args:
            row: Hàng hiện tại
            current_solution: Lưu vị trí hậu trên từng hàng
        """
        # Điều kiện dừng: đã xếp hết N quân hậu
        if row == self.n:
            self.solutions.append(current_solution[:])
            return
        
        # Thử đặt quân hậu ở hàng row tại từng cột
        for col in range(self.n):
            if self.is_safe(row, col):
                # Đặt quân hậu tại (row, col)
                current_solution.append(col)
                self.col.add(col)
                self.diag1.add(row - col)
                self.diag2.add(row + col)
                
                # Quay lui với hàng kế tiếp
                self.backtrack(row + 1, current_solution)
                
                # Loại bỏ quân hậu (backtrack)
                current_solution.pop()
                self.col.remove(col)
                self.diag1.remove(row - col)
                self.diag2.remove(row + col)
    
    def solve(self):
        """Giải bài toán xếp hậu"""
        if self.n < 1:
            return []
        
        self.backtrack(0, [])
        return self.solutions
    
    def display_result(self, show_all=False):
        """
        Hiển thị kết quả
        
        Args:
            show_all: Nếu True, hiển thị tất cả bàn cờ. Nếu False, chỉ hiển thị a vài
        """
        print(f"Kết quả: Tất cả cách xếp {self.n} quân hậu trên bàn cờ {self.n}x{self.n}:")
        
        if not self.solutions:
            print(f"Không có cách xếp nào cho N={self.n}")
        else:
            num_to_display = min(3, len(self.solutions)) if not show_all else len(self.solutions)
            
            for idx in range(num_to_display):
                solution = self.solutions[idx]
                print(f"\n--- Cách xếp {idx+1} ---")
                self.draw_board(solution)
            
            if len(self.solutions) > num_to_display:
                print(f"\n... (Còn {len(self.solutions) - num_to_display} cách xếp khác)")
        
        print(f"\nTổng số cách xếp: {len(self.solutions)}")
    
    def draw_board(self, solution):
        """
        Vẽ bàn cờ từ lời giải
        
        Args:
            solution: Danh sách cột của quân hậu trên từng hàng
        """
        board = [['.' for _ in range(self.n)] for _ in range(self.n)]
        
        # Đặt quân hậu trên bàn cờ
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        
        # In bàn cờ
        for row in board:
            print(' '.join(row))


if __name__ == "__main__":
    print("="*60)
    print("BÀI 2: XẾP HẬU (N-QUEEN)")
    print("="*60)
    print("Ý tưởng: Sử dụng backtracking để xếp N quân hậu trên bàn cờ NxN")
    print("Ràng buộc: Không có 2 quân hậu trên cùng hàng/cột/đường chéo\n")
    
    xephau = XepHau(4)
    xephau.solve()
    xephau.display_result()
