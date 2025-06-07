import numpy as np
from scipy.integrate import solve_ivp

def voter_ode(t, y, p):
    U, A, B = y
    bA, bB, lA, lB, mu, sigma = p
    dU = -(bA + lA*A)*U - (bB + lB*B)*U + mu*(A + B)
    dA = (bA + lA*A)*U - mu*A - sigma*A*B
    dB = (bB + lB*B)*U - mu*B - sigma*A*B
    return (dU, dA, dB)

def run_scenario(params, t_end=45, y0=(0.9, 0.05, 0.05), npts=300):
    t_eval = np.linspace(0, t_end, npts)
    sol = solve_ivp(voter_ode, (0, t_end), y0, t_eval=t_eval, args=(params,))
    return t_eval, sol.y
