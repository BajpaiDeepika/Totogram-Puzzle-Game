# Totogram-Puzzle-Game
A Totogram is a puzzle played on a board that has a graph structure, with edges connecting some pairs
of vertices. The edges of the graph form a rooted tree with a particular structure: the root has exactly
three children, every other non-leaf node has exactly two children, and the leaves are all at the same
depth k in the tree. This graph has the property that every vertex has exactly 1 or 3 neighbors. A
sample board with k = 3 is shown in Figure 1. (Note that a Totogram is almost a balanced binary tree,
except that the root has three subtrees instead of two.) To play the Totogram, the player arranges a
set of N tiles numbered from 1 to N, where N is the number of vertices in the graph (which, in turn,
is a function of k), on the vertices of the board. Their score is equal to the maximum absolute value of
the dierence between any pair of adjacent vertices, and the goal is to nd an arrangement that makes
the score as low as possible.

The aim of the program is to find the best (lowest-cost) solution that it can for a given k. The
program should run on the command line like:
python totogram.py k
The final two lines of output will be (1) the space-delimited tile arrangement, in breadth-rst search
order, and (2) the score for this arrangement. For example,
4
5 4 7 8 1 2 3 6 9 10
