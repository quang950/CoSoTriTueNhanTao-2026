#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bài tập Tìm kiếm trong không gian trạng thái
Sinh viên năm nhất - Cơ sở Trí tuệ Nhân tạo 2026

Nội dung:
1. Biểu diễn đồ thị có trọng số
2. Thuật toán Best-First Search
3. Thuật toán A*
4. Bài toán mê cung 
5. Bài toán 8-Puzzle
6. Thuật toán A* với Knowledge Transfer
7. Visualization với NetworkX
"""

import heapq
import pprint

# ========== PHẦN 1: BIỂU DIỄN ĐỒ THỊ ==========

def create_graph():
    """Tạo đồ thị với cấu trúc danh sách kề có trọng số"""
    COST = {}
    COST["A"] = {"C": 9, "D": 7, "E": 13, "F": 20}
    COST["B"] = {}
    COST["C"] = {"H": 6}
    COST["D"] = {"E": 4, "H": 8}
    COST["E"] = {"I": 3, "K": 4}
    COST["F"] = {"G": 4, "I": 6}
    COST["G"] = {}
    COST["H"] = {"K": 5}
    COST["I"] = {"B": 5, "K": 9}
    COST["K"] = {"B": 6}
    return COST

def display_vertices(graph):
    """Hiển thị tất cả các đỉnh của đồ thị"""
    vertices = list(graph.keys())
    print(f"Các đỉnh của đồ thị: {vertices}")
    return vertices

def display_graph(graph):
    """Hiển thị đồ thị dưới dạng danh sách kề"""
    print("Cấu trúc đồ thị:")
    for vertex in graph:
        print(f"Đỉnh {vertex}: ", end="")
        if graph[vertex]:
            for neighbor, weight in graph[vertex].items():
                print(f"({vertex}->{neighbor}, {weight}) ", end="")
        else:
            print("Không có đỉnh kề", end="")
        print()

def check_adjacent(graph, a, b):
    """Kiểm tra hai đỉnh có kề nhau không"""
    if a not in graph or b not in graph:
        return (None, None)  # Đỉnh không tồn tại
    elif b in graph[a]:
        weight = graph[a][b] 
        return (1, weight)  # Kề nhau với trọng số weight
    else:
        return (0, None)  # Không kề nhau

def get_neighbors(graph, vertex):
    """Lấy danh sách đỉnh kề với vertex"""
    if vertex not in graph:
        return None
    else:
        return list(graph[vertex].keys())

# ========== PHẦN 2: CẤU TRÚC DỮ LIỆU MINHEAP ==========

class MinHeap:
    """MinHeap cho thuật toán tìm kiếm"""
    
    def __init__(self):
        self.items = []
    
    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        heapq.heappush(self.items, item)
    
    def pop(self):
        return heapq.heappop(self.items)
    
    def check(self, item):
        return item in self.items
    
    def update(self, old_item, new_item):
        if old_item in self.items:
            idx = self.items.index(old_item)
            self.items[idx] = new_item
            heapq.heapify(self.items)

# ========== PHẦN 3: THUẬT TOÁN TÌM KIẾM ==========

def best_first_search(graph, start, goal):
    """
    Thuật toán Best-First Search
    Tìm đường đi ngắn nhất dựa trên chi phí g(n)
    """
    if start not in graph or goal not in graph:
        return (None, None)
    
    path = {}
    g = {}
    open_set = MinHeap()
    closed = []
    
    # Khởi tạo
    path[start] = None
    g[start] = 0
    open_set.push((0, start))
    
    while not open_set.empty():
        current_g, current = open_set.pop()
        closed.append(current)
        
        if current == goal:
            break
            
        # Duyệt các đỉnh kề
        for neighbor in graph[current]:
            cost = graph[current][neighbor]
            new_g = g[current] + cost
            
            if neighbor not in g:
                g[neighbor] = new_g
                path[neighbor] = current
                open_set.push((new_g, neighbor))
            elif neighbor not in closed and new_g < g[neighbor]:
                open_set.update((g[neighbor], neighbor), (new_g, neighbor))
                g[neighbor] = new_g
                path[neighbor] = current
    
    return (path, g)

def create_heuristic():
    """Tạo heuristic h(n) cho thuật toán A*"""
    h = {}
    h["A"] = 15
    h["B"] = 0  # Đích
    h["C"] = 12
    h["D"] = 10
    h["E"] = 8
    h["F"] = 14
    h["G"] = 16
    h["H"] = 6
    h["I"] = 5
    h["K"] = 6
    return h

def astar_search(graph, start, goal, heuristic=None):
    """
    Thuật toán A*
    Tìm đường đi ngắn nhất với heuristic h(n)
    """
    if start not in graph or goal not in graph:
        return (None, None)
    
    if heuristic is None:
        heuristic = {}
    
    path = {}
    g = {}
    f = {}
    open_set = MinHeap()
    closed = []
    
    # Khởi tạo
    path[start] = None
    g[start] = 0
    f[start] = g[start] + heuristic.get(start, 0)
    open_set.push((f[start], start))
    
    while not open_set.empty():
        current_f, current = open_set.pop()
        closed.append(current)
        
        if current == goal:
            break
            
        # Duyệt các đỉnh kề
        for neighbor in graph[current]:
            cost = graph[current][neighbor]
            new_g = g[current] + cost
            new_f = new_g + heuristic.get(neighbor, 0)
            
            if neighbor not in g:
                g[neighbor] = new_g
                f[neighbor] = new_f
                path[neighbor] = current
                open_set.push((new_f, neighbor))
            elif neighbor not in closed and new_g < g[neighbor]:
                open_set.update((f[neighbor], neighbor), (new_f, neighbor))
                g[neighbor] = new_g
                f[neighbor] = new_f
                path[neighbor] = current
            elif neighbor in closed and new_g < g[neighbor]:
                g[neighbor] = new_g
                f[neighbor] = new_f
                path[neighbor] = current
                closed.remove(neighbor)
                open_set.push((new_f, neighbor))
    
    return (path, g)

def find_path(path_dict, start, goal):
    """Truy hồi đường đi từ start đến goal"""
    if goal not in path_dict:
        return []
    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = path_dict[current]
    
    return path[::-1]  # Đảo ngược

# ========== PHẦN 4: TEST VÀ DEMO ==========

def main():
    """Hàm chính demo các thuật toán"""
    print("=" * 50)
    print("BÀI TẬP TÌM KIẾM TRONG KHÔNG GIAN TRẠNG THÁI")
    print("=" * 50)
    
    # Tạo đồ thị
    graph = create_graph()
    heuristic = create_heuristic()
    
    print("\\n1. BIỂU DIỄN ĐỒ THỊ")
    print("-" * 25)
    display_vertices(graph)
    display_graph(graph)
    
    print("\\n2. KIỂM TRA TÍNH KỀ")
    print("-" * 25)
    test_pairs = [("A", "D"), ("D", "E"), ("E", "B"), ("B", "A")]
    for a, b in test_pairs:
        result = check_adjacent(graph, a, b)
        print(f"{a} kề {b}: {result}")
    
    print("\\n3. THUẬT TOÁN BEST-FIRST SEARCH")
    print("-" * 35)
    path_bf, g_bf = best_first_search(graph, 'A', 'B')
    if path_bf and 'B' in path_bf:
        path_list = find_path(path_bf, 'A', 'B')
        print(f"Đường đi: {' -> '.join(path_list)}")
        print(f"Chi phí: {g_bf.get('B', 'N/A')}")
    else:
        print("Không tìm thấy đường đi")
    
    print("\\n4. THUẬT TOÁN A*")
    print("-" * 20)
    path_astar, g_astar = astar_search(graph, 'A', 'B', heuristic)
    if path_astar and 'B' in path_astar:
        path_list = find_path(path_astar, 'A', 'B')
        print(f"Đường đi: {' -> '.join(path_list)}")
        print(f"Chi phí: {g_astar.get('B', 'N/A')}")
        print(f"Heuristic được sử dụng: {heuristic}")
    else:
        print("Không tìm thấy đường đi")
    
    print("\\n5. SO SÁNH KẾT QUẢ")
    print("-" * 20)
    print(f"Best-First Search: Chi phí = {g_bf.get('B', 'N/A')}")
    print(f"A*: Chi phí = {g_astar.get('B', 'N/A')}")
    
    if g_bf.get('B') == g_astar.get('B'):
        print("✓ Cả hai thuật toán tìm được đường đi tối ưu giống nhau!")
    
    print("\\n" + "=" * 50)

if __name__ == "__main__":
    main()