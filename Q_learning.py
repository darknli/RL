import numpy as np


class Q_learning:
    def __init__(self, gamma=0.9, lr=0.3, epsilon=0.9):
        self.gamma = gamma
        self.lr = lr
        self.epsilon = epsilon
        self.score_mat = {}

    def update_award_mat(self, status, next_steps, now_award, old_status):
        next_award = []
        status = str(status)
        old_status = str(old_status)
        for step in next_steps:
            step = str(step)
            self.check_status(status, step)
            next_award.append(self.score_mat[status][step])
        max_award = max(next_award)
        update_score = now_award + self.gamma * max_award
        self.score_mat[old_status][status] = self.lr*update_score + (1 - self.lr)*self.score_mat[old_status][status]

    def get_choice(self, status, next_steps):
        if len(next_steps) == 0:
            return None
        awards = []
        for step in next_steps:
            step = str(step)
            self.check_status(status, step)
            awards.append(self.score_mat[status, step])
        awards = np.array(awards)
        if (awards == awards[0]).all() or np.random.random() > self.epsilon:
            index = np.random.randint(0, len(next_steps)-1)
        else:
            index = np.argmax(awards)
        return next_steps[index]

    def check_status(self, status, step):
        if step not in self.score_mat:
            self.score_mat[status][step] = 0
