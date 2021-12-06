import random

import numpy as np

from MazeProblem import create_problem
from Heuristics import *
from Robot import *
import pandas as pd

# maze_problem = create_problem(f"maze_{0}")
# print("head", maze_problem.initial_state.head)
# print("tail", maze_problem.initial_state.tail)
# print(ShorterRobotHeuristic(maze_problem=maze_problem,k=2)._compute_shorter_head_and_tails(head=maze_problem.initial_state.head, tail=maze_problem.initial_state.tail))

def getRobotLocation(n, k):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    head_x, head_y = random.randint(a=0, b=(n - 1)), random.randint(0, n - 1)
    direction_x, direction_y = directions[random.randint(0, len(directions)-1)]


    if head_x + direction_x * k >= n or head_x + direction_x * k < 0 or head_y + direction_y * k >= n or head_y + direction_y * k < 0:
        return None

    return head_x, head_y, head_x + direction_x*(k-1),  head_y + direction_y*(k-1)

def generateNewProblem(n: int, k : int, iters: int, F = 10, R = 1):
    problem = np.zeros((n, n))

    r_coords = None
    for i in range(iters):
        r_coords = getRobotLocation(n, k)
        if r_coords is not None:
            break

    problem[r_coords[0]][r_coords[1]] = 1
    problem[r_coords[2]][r_coords[3]] = 2

    t_coords = None
    for i in range(iters):
        t_coords = getRobotLocation(n, k)
        if t_coords is not None:
            break

    problem[t_coords[0]][t_coords[1]] = 3
    problem[t_coords[2]][t_coords[3]] = 4

    map = problem.copy()
    tail = np.argwhere(problem == 1)[0]
    head = np.argwhere(problem == 2)[0]
    tail_goal = np.argwhere(problem == 3)[0]
    head_goal = np.argwhere(problem == 4)[0]
    problem[tail[0], tail[1]] = 0
    problem[head[0], head[1]] = 0
    problem[tail_goal[0], tail_goal[1]] = 0
    problem[head_goal[0], head_goal[1]] = 0
    maze_problem = MazeProblem(map, head, tail, head_goal, tail_goal, F, R)
    return maze_problem, map

def runContest(iters: int = 10):
    problems = []

    for i in range(iters):
        try:
            problem, map = generateNewProblem(10, 5, 10)
            UCS_r = UniformCostSearchRobot()
            WAS_r = WAStartRobot(heuristic=tail_manhattan_heuristic)

            UCS_sol = UCS_r.solve(problem)
            WAS_sol = WAS_r.solve(problem)
            print(f"{UCS_r.name} solved maze in {round(UCS_sol.solve_time, 2)} seconds. "
                  f"solution cost = {UCS_sol.cost}, "
                  f"expanded {UCS_sol.n_node_expanded} nodes.")
            print(f"{WAS_r.name} solved maze in {round(WAS_sol.solve_time, 2)} seconds. "
                  f"solution cost = {WAS_sol.cost}, "
                  f"expanded {WAS_sol.n_node_expanded} nodes.")
            print()
            if WAS_sol.cost > UCS_sol.cost:
                problems.append(map)

        except:
            print("Error: ")

    return problems

maps = runContest(25)
# if len(maps) != 0:
    # pd.DataFrame(maps[0]).to_csv("Mazes/maze_99.csv")
