"""
BÀI 1: LIỆT KÊ TỔ HỢP (TOHOP.*)

"""


class ToHop:
    def __init__(self):
        self.n = 0
        self.k = 0
        self.elements = []
        self.result = []
    
    def input_data(self):
        """Nhập dữ liệu từ bàn phím"""
        self.n = int(input("Nhập N (số phần tử): "))
        self.k = int(input("Nhập K (chập): "))
        
        self.elements = []
        print(f"Nhập {self.n} phần tử:")
        for i in range(self.n):
            element = input(f"Phần tử {i+1}: ")
            self.elements.append(element)
    
    def backtrack(self, start, current):
        """
        Quay lui để liệt kê tổ hợp
        
        Args:
            start: Vị trí bắt đầu tìm kiếm
            current: Tổ hợp hiện tại đang xây dựng
        """
        # Điều kiện dừng: đã chọn đủ K phần tử
        if len(current) == self.k:
            self.result.append(current[:])
            return
        
        # Thử chọn từng phần tử từ vị trí start
        for i in range(start, self.n):
            # Chọn phần tử i
            current.append(self.elements[i])
            # Quay lui với các phần tử còn lại (từ i+1 trở đi)
            self.backtrack(i + 1, current)
            # Loại bỏ phần tử (backtrack)
            current.pop()
    
    def solve(self):
        """Giải bài toán liệt kê tổ hợp"""
        self.backtrack(0, [])
        return self.result
    
    def display_result(self):
        """Hiển thị kết quả"""
        print(f"\nKết quả: Tất cả tổ hợp chập {self.k} của {self.n} phần tử:")
        if not self.result:
            print("Không có tổ hợp nào!")
        else:
            for i, combo in enumerate(self.result, 1):
                print(f"{i}. {' '.join(combo)}")
        print(f"Tổng số tổ hợp: {len(self.result)}")


if __name__ == "__main__":
    print("="*60)
    print("BÀI 1: LIỆT KÊ TỔ HỢP")
    print("="*60)
    print("Ý tưởng: Sử dụng backtracking để liệt kê tất cả tổ hợp chập K của N phần tử")
    print("Ràng buộc: Không lặp lại, không tính thứ tự\n")
    
    tohop = ToHop()
    tohop.input_data()
    tohop.solve()
    tohop.display_result()
