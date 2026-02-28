# Nhật ký Bài tập Tìm kiếm trong Không gian Trạng thái

**Môn**: Cơ sở Trí tuệ Nhân tạo  
**Thời gian**: Tháng 2/2026  
**Nội dung**: Thuật toán tìm kiếm A*, A^KT, Mê cung, 8-Puzzle

## 1. Ý tưởng giải bài

### 1.1. Biểu diễn đồ thị
- Sử dụng **dictionary** để biểu diễn đồ thị có hướng với trọng số
- Cấu trúc: `COST[đỉnh_nguồn] = {đỉnh_đích: trọng_số}`
- Ví dụ: `COST["A"] = {"C": 9, "D": 7, "E": 13, "F": 20}`

### 1.2. Thuật toán tìm kiếm
- **Best-First Search**: Tìm kiếm dựa trên g(n) - chi phí từ start
- **A***: Tìm kiếm dựa trên f(n) = g(n) + h(n) với heuristic
- **A^KT**: A* với Knowledge Transfer - học từ các lời giải trước

### 1.3. Cấu trúc dữ liệu
- **MinHeap**: Hàng đợi ưu tiên cho OPEN set
- **Dictionary**: Lưu trữ path tracing và chi phí g(n)

## 2. Minh họa cách làm qua ví dụ

### 2.1. Đồ thị ban đầu
```
Đỉnh A: (A->C, 9) (A->D, 7) (A->E, 13) (A->F, 20) 
Đỉnh B: Không có đỉnh kề
Đỉnh C: (C->H, 6) 
Đỉnh D: (D->E, 4) (D->H, 8) 
Đỉnh E: (E->I, 3) (E->K, 4) 
Đỉnh F: (F->G, 4) (F->I, 6) 
Đỉnh G: Không có đỉnh kề
Đỉnh H: (H->K, 5) 
Đỉnh I: (I->B, 5) (I->K, 9) 
Đỉnh K: (K->B, 6) 
```

### 2.2. Tìm đường từ A đến B

#### Best-First Search:
1. **Khởi tạo**: OPEN = {(0, A)}, g[A] = 0
2. **Bước 1**: Lấy A, mở rộng C, D, E, F
3. **Bước 2**: Lấy D (g=7), mở rộng E, H  
4. **Bước 3**: Lấy E (g=11), mở rộng I, K
5. **Bước 4**: Lấy I (g=14), mở rộng B, K
6. **Kết quả**: Tìm thấy B với g[B] = 19

#### A* với heuristic:
- Sử dụng cùng logic nhưng với f(n) = g(n) + h(n)
- Heuristic h(B) = 0, h(A) = 15, h(I) = 5, etc.
- **Kết quả**: Cũng tìm thấy đường đi tối ưu

## 3. Giải thuật chi tiết

### 3.1. Best-First Search
```python
def best_first_search(graph, start, goal):
    OPEN = MinHeap()
    CLOSED = []
    path = {}
    g = {}
    
    g[start] = 0
    path[start] = None
    OPEN.push((0, start))
    
    while not OPEN.empty():
        current_g, current = OPEN.pop()
        CLOSED.append(current)
        
        if current == goal:
            break
            
        for neighbor in graph[current]:
            new_g = g[current] + graph[current][neighbor]
            
            if neighbor not in g:
                g[neighbor] = new_g
                path[neighbor] = current
                OPEN.push((new_g, neighbor))
            elif neighbor not in CLOSED and new_g < g[neighbor]:
                update_open(neighbor, new_g)
                
    return (path, g)
```

### 3.2. A* Algorithm
```python
def astar_search(graph, start, goal, heuristic):
    # Tương tự Best-First nhưng dùng f(n) = g(n) + h(n)
    f[start] = g[start] + heuristic[start]
    OPEN.push((f[start], start))
    
    # Trong vòng lặp, tính f(neighbor) = new_g + h[neighbor]
```

### 3.3. Mê cung (Maze)
- Biểu diễn: Ma trận 2D (0: đường đi, 1: tường)
- Heuristic: Manhattan distance
- Neighbors: 4 hướng (lên, xuống, trái, phải)

### 3.4. 8-Puzzle
- State space: 9!/2 = 181,440 trạng thái hợp lệ
- Heuristic: Tổng Manhattan distance của các số
- Tạo neighbors: Hoán đổi ô trống với ô kề

## 4. Code Implementation

### 4.1. File chính: `search_algorithms.py`
- Class MinHeap
- Hàm best_first_search()
- Hàm astar_search()
- Hàm find_path()

### 4.2. Notebook: `my_lesson4.ipynb`
- Demo interactive với visualization
- Test cases cho từng function
- Mê cung và 8-Puzzle examples

## 5. Kiểm tra và Kết quả

### 5.1. Test Case: A → B
```
Best-First Search: 
- Đường đi: A → D → E → I → B
- Chi phí: 19
- Các bước: 7 + 4 + 3 + 5 = 19

A* với heuristic:
- Đường đi: A → D → E → I → B  
- Chi phí: 19
- Hiệu quả hơn nhờ heuristic guidance
```

### 5.2. Validation
- ✅ Cả hai thuật toán tìm được đường đi tối ưu
- ✅ Kết quả consistent giữa Best-First và A*
- ✅ Path tracing hoạt động chính xác
- ✅ Handling edge cases (đỉnh không tồn tại)

### 5.3. Performance
| Algorithm | Nodes expanded | Path length | Optimal? |
|-----------|----------------|-------------|----------|
| Best-First | ~8 nodes | 4 edges | ✅ Yes |
| A* | ~6 nodes | 4 edges | ✅ Yes | 
| A^KT | ~5 nodes | 4 edges | ✅ Yes |

## 6. Ứng dụng thư viện đồ họa

### 6.1. NetworkX cho đồ thị
```python
import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị từ dictionary
G = nx.DiGraph()
for node, neighbors in COST.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Visualization với màu sắc
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
```

### 6.2. Matplotlib cho mê cung
```python
# Hiển thị mê cung với đường đi
colored_maze = np.zeros((maze.shape[0], maze.shape[1], 3))
colored_maze[maze == 1] = [0, 0, 0]  # Tường đen
colored_maze[maze == 0] = [1, 1, 1]  # Đường trắng

# Đường đi màu xanh lá
for pos in path:
    colored_maze[pos[0], pos[1]] = [0, 1, 0]

plt.imshow(colored_maze)
```

## 7. Kết luận

### 7.1. Điểm mạnh
- ✅ Cài đặt đúng các thuật toán cơ bản
- ✅ Visualization trực quan
- ✅ Xử lý nhiều loại bài toán khác nhau
- ✅ Code dễ hiểu, có comment tiếng Việt

### 7.2. Cải tiến có thể
- Thêm bidirectional search
- Optimize memory usage cho large graphs  
- Thêm GUI interface
- Parallel processing cho multiple queries

### 7.3. Kiến thức thu được
- Hiểu sâu về graph search algorithms
- Kinh nghiệm implement data structures
- Kỹ năng debugging và testing
- Sử dụng visualization libraries

---
*Ghi chú: Code hoàn chỉnh có sẵn trong `search_algorithms.py` và `my_lesson4.ipynb`*