from sys_args import parse_args

my_args = parse_args()
if my_args.rl == 'q_learing':
    from Q_learning import Q_learning
    q = Q_learning(my_args.learning_rate, my_args.gamma, my_args.epsilon)
else:
    raise ValueError('rl没有%s选项！' % my_args.rl)
if my_args.env == 'maze':
    from env import env_maze
    my_env = env_maze
else:
    raise ValueError('env没有%s选项' % my_args.env)

def one_epoch():
    start = (0, 0)
    end = (5, 4)
    env = my_env(start, end, show_loc=my_args.show_location)
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
    # q.show_Q()


if __name__ == '__main__':
    for i in range(my_args.epoch):
        one_epoch()
