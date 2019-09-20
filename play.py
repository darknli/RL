from env import env_maze
from Q_learning import Q_learning

def main():
    start = (0, 0)
    end = (5, 4)

    q = Q_learning()
    env = env_maze(start, end)
    while not env.finish:
        now_loc = env.now_loc
        next_steps = env.get_next_steps()
        next_status = q.get_choice(now_loc, next_steps)
        next_status = env.get_next_steps()
        q.update_award_mat(next_status, next_status, )


if __name__ == '__main__':
    main()