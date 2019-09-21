import numpy as np

class env_maze():
    def __init__(self, start, end, maze=None, show_loc=False):
        if maze is None:
            maze = self.get_defualt_maze()
        elif isinstance(maze, list):
            maze = np.array(maze)
        elif not isinstance(maze, np.ndarray):
            raise ValueError("妹子的er格式不对呀")

        self.maze = maze

        if len(start) != 2:
            print('起点start请正确地输入坐标x, y值')
        if len(end) != 2:
            print('终点end请正确地输入坐标x, y值')
        self.start = start
        self.now_loc = start
        self.end = end
        self.finish = True if start == end else False
        self.show_loc = show_loc

    def make_env(self, maze):
        maze[maze == 0] = -1
        maze[self.end] = 10
        maze[maze == 1] = 0
        return maze.astype(np.float)

    def get_defualt_maze(self):
        maze = np.array([[0, 0, 0, 0, 0],
                         [0, 0, 1, 1, 0],
                         [0, 1, 1, 0, 0],
                         [1, 0, 0, 0, 1],
                         [0, 0, 1, 0, 1],
                         [0, 1, 1, 0, 0]])
        return maze

    def get_actions(self):
        x, y = self.now_loc
        up = x - 1 >= 0 and self.maze[x-1, y] == 0
        down = self.maze.shape[0] > x+1 and self.maze[x+1, y] == 0
        left = y - 1 >= 0 and self.maze[x, y-1] == 0
        right = self.maze.shape[1] > y+1 and self.maze[x, y+1] == 0
        return np.array((up, down, left, right), np.bool)

    def update_location(self, action):
        x, y = self.now_loc
        if action == 0:
            self.now_loc = (x-1, y)
        elif action == 1:
            self.now_loc = (x+1, y)
        elif action == 2:
            self.now_loc = (x, y-1)
        elif action == 3:
            self.now_loc = (x, y+1)
        else:
            raise ValueError('动作错误')
        if self.now_loc == self.end:
            self.finish = True
        if self.show_loc:
            print('当前位置由', (x, y), '更新为：', self.now_loc)
        return self.now_loc, self.get_award()

    def get_award(self):
        return 100 if self.now_loc == self.end else 0

    def show_action(self):
        x, y = self.maze.shape
        for i in range(x):
            for j in range(y):
                self.now_loc = (i, j)
                print((i, j), self.get_actions())
