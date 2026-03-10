"""
BÀI 4: TÔ MẫU ĐỒ THỊ (TOMAT.*)

"""


class ToMauDoThi:
    """Bài 4: Tô màu đồ thị - Graph Coloring Problem"""
    
    def __init__(self, vertices, edges):
        """
        Args:
            vertices: Số đỉnh (từ 0 đến vertices-1)
            edges: Danh sách các cạnh [[u1, v1], [u2, v2], ...]
        """
        self.vertices = vertices
        self.edges = edges
        self.adj = [[] for _ in range(vertices)]
        
        # Xây dựng danh sách kề
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        self.colors = [-1] * vertices
        self.num_colors = 0
        self.solutions = []
    
    def is_safe(self, vertex, color):
        """Kiểm tra xem có thể tô đỉnh vertex bằng color"""
        for neighbor in self.adj[vertex]:
            if self.colors[neighbor] == color:
                return False
        return True
    
    def backtrack(self, vertex, max_color):
        """Quay lui để tô màu"""
        # Đáy của quay lui: tô xong tất cả đỉnh
        if vertex == self.vertices:
            # Lưu lại lời giải
            self.solutions.append((max_color + 1, self.colors[:]))
            return
        
        # Thử tô đỉnh vertex bằng từng màu
        for color in range(max_color + 1):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                self.backtrack(vertex + 1, max(max_color, color))
                self.colors[vertex] = -1
    
    def solve(self, max_colors=None):
        """Tìm cách tô màu với số màu tối thiểu"""
        if max_colors is None:
            max_colors = self.vertices
        
        # Tìm số màu tối thiểu
        for num_colors in range(1, max_colors + 1):
            self.colors = [-1] * self.vertices
            self.solutions = []
            self.backtrack(0, num_colors - 1)
            
            if self.solutions:
                self.num_colors = num_colors
                return True
        
        return False
    
    def display_result(self):
        """Hiển thị kết quả"""
        print(f"Tô màu đồ thị:")
        print(f"Số đỉnh: {self.vertices}")
        print(f"Số cạnh: {len(self.edges)}")
        print(f"Cạnh: {self.edges}\n")
        
        if self.solutions:
            colors_used, coloring = self.solutions[0]
            print(f"Số màu cần dùng: {colors_used}")
            print(f"Cách tô màu:")
            for vertex in range(self.vertices):
                print(f"  Đỉnh {vertex}: Màu {coloring[vertex]}")
        else:
            print("Không tìm thấy cách tô màu nào")


if __name__ == "__main__":
    print("="*60)
    print("BÀI 4: TÔ MẫU ĐỒ THỊ")
    print("="*60)
    
    # Ví dụ 1: Đồ thị từ bài tập
    vertices1 = 6
    edges1 = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
    
    tm1 = ToMauDoThi(vertices1, edges1)
    tm1.solve()
    print("\nVí dụ 1:")
    tm1.display_result()
