import os
import random
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def Thompson_Sampling(m, p, trials, wins, score):
    pbeta = [0 for i in range(m)]
    for i in range(0, len(trials)):
      pbeta[i] = np.random.beta(wins[i]+1, trials[i]-wins[i]+1)
    choice = np.argmax(pbeta)

    trials[choice] += 1
    if p[choice] >= random.random():
        wins[choice] += 1
        score += 1
    
    return score  

def random_select(m, p, score):
    choice = random.randint(0, m-1)

    if p[choice] >= random.random():
        score += 1
    
    return score


def main():
    n = 1
    score_Th = 0
    score_Ra = 0
    scores_Th = []
    scores_Ra = []
    with open(os.path.join(BASE_DIR, "server.conf")) as f:
        m = int(f.readline())
        for i in range(n):
            p = [float(x) for x in f.readline().split()]
    trials = [0 for i in range(m)]
    wins = [0 for i in range(m)]

    for i in range(10000):
        score_Th = Thompson_Sampling(m, p, trials, wins, score_Th)
        score_Ra = random_select(m, p, score_Ra)
        scores_Th.append(score_Th)
        scores_Ra.append(score_Ra)
    print("Random score={}.".format(score_Ra))
    print("Thompson Sampling score={}.".format(score_Th))
    print(wins)
    print(trials)

    plt.plot(scores_Th, label='Thompson Sampling')
    plt.plot(scores_Ra, label='Random Select')
    plt.xlabel('Trials')
    plt.ylabel('Score')
    plt.title('Score Comparison between Thompson Sampling and Random Selection')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
