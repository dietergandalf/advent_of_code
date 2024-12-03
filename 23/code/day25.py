# Day 25 Advent of Code 23

import networkx as nx

def solve(file, part=0):
   wires = [line.strip().split(': ') for line in open(file)]
   wires = [[line[0], line[1].split()] for line in wires]
   g = nx.Graph()
   for wire in wires:
      g.add_node(wire[0])
      for node in wire[1]:
         g.add_edge(wire[0], node)
   g.remove_edges_from(nx.minimum_edge_cut(g))
   a, b = nx.connected_components(g)
   print(len(a)*len(b))

if __name__ == '__main__':
   solve('C:/Users/malte/programming/advent_of_code/23/input/day25_test.txt', 0)
   solve('C:/Users/malte/programming/advent_of_code/23/input/day25.txt', 0)
