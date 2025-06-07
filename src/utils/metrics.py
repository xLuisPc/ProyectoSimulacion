import numpy as np

def auc(series, t):
    return np.trapz(series, t)

def persuasion_number(beta, lam, mu):
    return (beta + lam) / mu
