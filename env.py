import numpy as np

class env_maze():
    def __init__(self, start, end, maze=None):
        if maze is None:
            maze = self.get_defualt_maze()
        elif isinstance(maze, list):
            maze = np.array(maze)
        elif not isinstance(maze, np.ndarray):
            raise ValueError("妹子的er格式不对呀")

        self.maze = self.make_env(maze)

        if len(start) != 2:
            print('起点start请正确地输入坐标x, y值')
        if len(end) != 2:
            print('终点end请正确地输入坐标x, y值')
        self.start = start
        self.now_loc = start
        self.end = end
        self.finish = True if start == end else False

    def make_env(self, maze):
        maze[maze==0] = -1
        maze[self.end] = 10
        maze[maze==1] = 0
        return maze.astype(np.float)

    def get_defualt_maze(self):
        maze = np.array([[0, 0, 0, 0, 0],
                         [0, 0, 1, 1, 0],
                         [0, 1, 1, 0, 0],
                         [1, 0, 0, 0, 1],
                         [0, 0, 1, 0, 1],
                         [0, 1, 1, 0, 0]])
        return maze

    def get_next_steps(self):
        next_steps = []
        x, y = self.now_loc
        if self.maze[x, y+1] != 0:
            next_steps.append((x, y+1))
        if self.maze[x, y-1] != 0:
            next_steps.append((x. y-1))
        if self.maze[x+1, y] != 0:
            next_steps.append((x+1, y))
        if self.maze[(x-1, y)]:
            next_steps.append((x-1, y))
        return next_steps

    def update_location(self, tmp_loc):
        self.now_loc = tmp_loc
        if tmp_loc == self.end:
            self.finish = False

    def get_award(self):
        return