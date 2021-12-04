import numpy as np

from Heuristics import ShorterRobotHeuristic
from MazeProblem import create_problem

maze_problem = create_problem(f"maze_{0}")
print("head", maze_problem.initial_state.head)
print("tail", maze_problem.initial_state.tail)
print(ShorterRobotHeuristic(maze_problem=maze_problem,k=2)._compute_shorter_head_and_tails(head=maze_problem.initial_state.head, tail=maze_problem.initial_state.tail))