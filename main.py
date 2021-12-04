from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    # test_robot(UniformCostSearchRobot, [0, 1, 2, 3, 4, 5])
    #  test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=tail_manhattan_heuristic)
    #  test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=center_manhattan_heuristic)
    # solve_and_display(WAStartRobot, 2, blit=False, heuristic=tail_manhattan_heuristic)
    w_experiment(2)
