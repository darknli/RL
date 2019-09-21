import numpy as np


class Q_learning:
    def __init__(self, gamma=0.9, lr=0.7, epsilon=0.9):
        self.gamma = gamma
        self.lr = lr
        self.epsilon = epsilon
        self.Q = {}

    def update_Q(self, now_status, next_status, award, action):
        now_status = str(now_status)
        next_status = str(next_status)
        next_max_q = self.get_max_q(next_status)
        self.Q[now_status][action] = (1-self.lr)*self.Q[now_status][action] + self.lr*(award+self.gamma*next_max_q)


    def get_choice(self, status, actions):
        status = str(status)
        self.check_status(status)
        optional_choices = self.Q[status][actions]
        if (optional_choices == optional_choices[0]).all() or np.random.random() > self.epsilon:
            action = np.random.choice(np.where(actions)[0])
        else:
            action = np.argmax(self.Q[status])
        return action

    def check_status(self, status):
        if status not in self.Q:
            self.Q[status] = np.zeros((4, ))

    def get_max_q(self, status):
        self.check_status(status)
        return np.max(self.Q[status])

    def show_Q(self):
        for status, actions in self.Q.items():
            print(status, actions)