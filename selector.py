import os
import random
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def select_ad(n, m, trials, wins, score):
    p = []
    with open(os.path.join(BASE_DIR, "server.conf")) as f:
        m = int(f.readline())
        for i in range(n):
            p = [float(x) for x in f.readline().split()]

    pbeta = [0 for i in range(m)]
    for i in range(0, len(trials)):
      pbeta[i] = np.random.beta(wins[i]+1, trials[i]-wins[i]+1)
    choice = np.argmax(pbeta)

    trials[choice] += 1
    if p[choice] >= random.random():
        wins[choice] += 1
        score += 1
    
    return score  

def main():
    n = 1
    m = 10
    score = 0
    trials = [0 for n in range(m)]
    wins = [0 for n in range(m)]

    for i in range(10000):
        score = select_ad(n, m, trials, wins, score)
    print("your score={}.".format(score))
    print(wins)
    print(trials)


if __name__ == '__main__':
    main()
