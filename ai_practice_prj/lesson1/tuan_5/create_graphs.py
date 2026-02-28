#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def create_graph1():
    """Tạo đồ thị 1 có trọng số"""
    G = nx.DiGraph()
    
    # Thêm các đỉnh
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    G.add_nodes_from(nodes)
    
    # Thêm các cạnh có trọng số
    edges = [
        ('A', 'C', 9), ('A', 'D', 7), ('A', 'E', 13), ('A', 'F', 20),
        ('B', 'A', 5), ('B', 'G', 6),
        ('C', 'B', 4), ('C', 'H', 11),
        ('D', 'C', 2), ('D', 'E', 1), ('D', 'G', 8), ('D', 'I', 15),
        ('E', 'F', 3), ('E', 'I', 12),
        ('F', 'I', 9),
        ('G', 'H', 3), ('G', 'I', 4),
        ('H', 'B', 7), ('H', 'I', 10),
        ('I', 'F', 6)
    ]
    
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    
    # Vẽ đồ thị
    plt.figure(figsize=(12, 8))
    pos = {
        'A': (0, 1),
        'B': (2, 2), 
        'C': (1, 0.5),
        'D': (0.5, 0),
        'E': (0, -1),
        'F': (-1, -1),
        'G': (1.5, -0.5),
        'H': (2, 0.5),
        'I': (1, -1)
    }
    
    # Vẽ các đỉnh
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=800, alpha=0.9)
    
    # Vẽ các cạnh
    nx.draw_networkx_edges(G, pos, edge_color='gray', 
                          arrows=True, arrowsize=20, alpha=0.6)
    
    # Vẽ nhãn đỉnh
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    # Vẽ trọng số cạnh
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)
    
    plt.title('Đồ thị có hướng với trọng số - Bài 1', fontsize=16, pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('dothi1.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return G

def create_graph2():
    """Tạo đồ thị 2 cho thuật toán A* với heuristic"""
    G = nx.DiGraph()
    
    # Thêm các đỉnh
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    G.add_nodes_from(nodes)
    
    # Thêm các cạnh (giống graph1)
    edges = [
        ('A', 'C', 9), ('A', 'D', 7), ('A', 'E', 13), ('A', 'F', 20),
        ('B', 'A', 5), ('B', 'G', 6),
        ('C', 'B', 4), ('C', 'H', 11),
        ('D', 'C', 2), ('D', 'E', 1), ('D', 'G', 8), ('D', 'I', 15),
        ('E', 'F', 3), ('E', 'I', 12),
        ('F', 'I', 9),
        ('G', 'H', 3), ('G', 'I', 4),
        ('H', 'B', 7), ('H', 'I', 10),
        ('I', 'F', 6)
    ]
    
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    
    # Heuristic values (khoảng cách ước lượng đến B)
    heuristic = {'A': 14, 'B': 0, 'C': 8, 'D': 12, 'E': 18, 
                 'F': 25, 'G': 6, 'H': 5, 'I': 10}
    
    # Vẽ đồ thị với heuristic
    plt.figure(figsize=(12, 8))
    pos = {
        'A': (0, 1),
        'B': (2, 2), 
        'C': (1, 0.5),
        'D': (0.5, 0),
        'E': (0, -1),
        'F': (-1, -1),
        'G': (1.5, -0.5),
        'H': (2, 0.5),
        'I': (1, -1)
    }
    
    # Vẽ các đỉnh với các màu khác nhau
    node_colors = ['red' if node == 'A' else 'green' if node == 'B' 
                   else 'lightblue' for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                          node_size=1000, alpha=0.9)
    
    # Vẽ các cạnh
    nx.draw_networkx_edges(G, pos, edge_color='gray', 
                          arrows=True, arrowsize=20, alpha=0.6)
    
    # Vẽ nhãn đỉnh kèm heuristic
    labels = {node: f"{node}\nh={heuristic[node]}" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=12, font_weight='bold')
    
    # Vẽ trọng số cạnh
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)
    
    plt.title('Đồ thị với Heuristic h(n) - Thuật toán A*\n(Đỏ: Start A, Xanh: Goal B)', 
              fontsize=16, pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('dothi2.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return G, heuristic

if __name__ == "__main__":
    print("Đang tạo đồ thị...")
    create_graph1()
    print("Đã tạo dothi1.png")
    
    create_graph2()
    print("Đã tạo dothi2.png")
    
    print("Hoàn thành!")