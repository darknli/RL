from env import env_maze
from Q_learning import Q_learning

EPOCH = 15
LEARING_RATE = 0.7
GAMMA = 0.9
EPSILON = 0.9
IS_SHOW_LOCATION = True

q = Q_learning(GAMMA, LEARING_RATE, EPSILON)

def one_epoch():
    start = (0, 0)
    end = (5, 4)
    env = env_maze(start, end, show_loc=IS_SHOW_LOCATION)
    step = 0
    while not env.finish:
        now_loc = env.now_loc
        actions = env.get_actions()
        action = q.get_choice(now_loc, actions)
        next_loc, award = env.update_location(action)
        q.update_Q(now_loc, next_loc, award, action)
        step += 1
    print('到达目的地， 用了%d 步'%step)
    # env.show_action()
    q.show_Q()


if __name__ == '__main__':
    for i in range(EPOCH):
        one_epoch()
