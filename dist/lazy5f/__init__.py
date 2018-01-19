import numpy as np


def ran_walk():
    return np.cumsum(np.random.choice([-1,+1], 10))


if __name__ == '__main__':
    print(ran_walk())
