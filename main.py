from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    for k in [2,4,6,8]:
        test_robot(WAStartRobot,[3,4],heuristic=ShorterRobotHeuristic, k=k)
    #test_robot(UniformCostSearchRobot, [99])
    #test_robot(WAStartRobot, [99], heuristic=tail_manhattan_heuristic)
    # test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=center_manhattan_heuristic)
    # solve_and_display(WAStartRobot, 2, blit=False, heuristic=tail_manhattan_heuristic)
    # w_experiment(2)

