"""
BÀI 5: LIỆT KÊ HOÁN VỊ (HOANVI.*)

"""


class HoanVi:
    """Bài 5: Liệt kê hoán vị - Permutation Problem"""
    
    def __init__(self):
        self.n = 0
        self.elements = []
        self.result = []
        self.used = []
    
    def input_data(self):
        """Nhập dữ liệu từ bàn phím"""
        self.n = int(input("Nhập N (số phần tử): "))
        
        self.elements = []
        print(f"Nhập {self.n} phần tử:")
        for i in range(self.n):
            element = input(f"Phần tử {i+1}: ")
            self.elements.append(element)
        
        self.used = [False] * self.n
    
    def backtrack(self, current):
        """
        Quay lui để liệt kê hoán vị
        
        Args:
            current: Hoán vị hiện tại đang xây dựng
        """
        # Điều kiện dừng: đã chọn hết N phần tử
        if len(current) == self.n:
            self.result.append(current[:])
            return
        
        # Thử chọn từng phần tử chưa sử dụng
        for i in range(self.n):
            if not self.used[i]:
                # Đánh dấu phần tử đã sử dụng
                self.used[i] = True
                current.append(self.elements[i])
                
                # Quay lui với các phần tử còn lại
                self.backtrack(current)
                
                # Loại bỏ phần tử (backtrack)
                current.pop()
                self.used[i] = False
    
    def solve(self):
        """Giải bài toán liệt kê hoán vị"""
        self.backtrack([])
        return self.result
    
    def display_result(self):
        """Hiển thị kết quả"""
        print(f"\nKết quả: Tất cả hoán vị của {self.n} phần tử:")
        if not self.result:
            print("Không có hoán vị nào!")
        else:
            for i, perm in enumerate(self.result, 1):
                print(f"{i}. {' '.join(perm)}")
        print(f"Tổng số hoán vị: {len(self.result)}")


if __name__ == "__main__":
    print("="*60)
    print("BÀI 5: LIỆT KÊ HOÁN VỊ (HOANVI)")
    print("="*60)
    print("Ý tưởng: Sử dụng backtracking để liệt kê tất cả hoán vị của N phần tử")
    print("Ràng buộc: Mỗi phần tử được sử dụng đúng 1 lần\n")
    
    hoanvi = HoanVi()
    hoanvi.input_data()
    hoanvi.solve()
    hoanvi.display_result()
