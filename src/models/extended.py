import numpy as np
from scipy.integrate import solve_ivp

def voter_ode_ext(t, y, p):
    U, A, B, C, N = y
    (bA, bB, bC,
     lA, lB, lC,
     mu, alpha, sigma) = p
    # Reclutamiento desde indecisos
    infl_A = (bA + lA * A) * U
    infl_B = (bB + lB * B) * U
    infl_C = (bC + lC * C) * U
    # Ecuaciones
    dU = -infl_A - infl_B - infl_C - alpha * U + mu * (A + B + C)
    dA = infl_A - mu * A - sigma * A * (B + C)
    dB = infl_B - mu * B - sigma * B * (A + C)
    dC = infl_C - mu * C - sigma * C * (A + B)
    dN = alpha * U                    # abstención acumulada
    return (dU, dA, dB, dC, dN)

def run_ext(params, t_end=45, y0=(0.9, 0.03, 0.03, 0.03, 0.01), npts=300):
    t_eval = np.linspace(0, t_end, npts)
    sol = solve_ivp(voter_ode_ext, (0, t_end), y0, args=(params,), t_eval=t_eval)
    return t_eval, sol.y
