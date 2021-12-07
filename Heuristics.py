import numpy as np
from MazeProblem import MazeState, MazeProblem, compute_robot_direction
from Robot import UniformCostSearchRobot
from GraphSearch import NodesCollection


def tail_manhattan_heuristic(state: MazeState):
    return sum(abs(state.tail - state.maze_problem.tail_goal))*state.maze_problem.forward_cost


def center_manhattan_heuristic(state: MazeState):
     #TODO (EX 9.2), implement heuristic, delete exception
    center = (state.head + state.tail)//2
    center_goal = (state.maze_problem.head_goal + state.maze_problem.tail_goal)//2
    return sum(abs(center - center_goal)) * state.maze_problem.forward_cost

class ShorterRobotHeuristic:
    def __init__(self, maze_problem: MazeProblem, k):
        assert k % 2 == 0, "odd must be even"
        assert maze_problem.length - k >= 3, f"it is not possible to shorten a {maze_problem.length}-length robot by " \
                                             f"{k} units because robot length has to at least 3"
        self.k = k
        ################################################################################################################
        # TODO (EX. 13.2): replace all three dots, delete exception
        raise NotImplemented
        shorter_robot_head_goal, shorter_robot_tail_goal = ... #it doesnt matter?
        self.new_maze_problem = MazeProblem(maze_map=...,
                                            initial_head= compute_robot_direction(MazeState.head , MazeState.tail), #return the first
                                            initial_tail=compute_robot_direction(MazeState.head , MazeState.tail),#return the seconed
                                            head_goal=shorter_robot_head_goal,  # doesn't matter, don't change
                                            tail_goal=shorter_robot_tail_goal)  # doesn't matter, don't change
        self.node_dists = ...().solve(..., compute_all_dists=True)
        ################################################################################################################

        assert isinstance(self.node_dists, NodesCollection)

    def _compute_shorter_head_and_tails(self, head, tail):
        direction = compute_robot_direction(head, tail)
        step = direction*(self.k/2)

        return head - step, tail + step

    def __call__(self, state: MazeState):
        # TODO (EX. 13.3): replace each three dots, delete exception
        raise NotImplemented
        shorter_head_location, shorter_tail_location = ...
        new_state = MazeState(..., head=..., tail=...)
        if new_state in self.node_dists:
            node = self.node_dists.get_node(new_state)
            return ...
        else:
            return ...  # what should we return in this case, so that the heuristic would be as informative as possible
                        # but still admissible
