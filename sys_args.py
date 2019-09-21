import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='强化学习设定参数',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--learning_rate', help='参数更新的学习率',
                        default='0.7', type=float)
    parser.add_argument('--gamma', help='gamma值越大代表算法越重视远见',
                        default='0.9', type=float)
    parser.add_argument('--epoch', help='学习轮数',
                        default='15', type=int)
    parser.add_argument('--epsilon', help='算法稳定系数', default='0.9', type=float)
    parser.add_argument('--show_location', help='显示每一步位置', default='True', type=bool)
    parser.add_argument('--rl', help='强化学习算法选择，可选择选项是：q_learning：Q Learning强化学习算法',
                        default='q_learing', type=str)
    parser.add_argument('--env', help='环境选择可选择选项是：maze', default='maze', type=str)

    args = parser.parse_args()

    return args