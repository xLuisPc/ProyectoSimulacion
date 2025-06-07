import csv, itertools, numpy as np
from ..models.extended import run_ext
from ..scenarios.extended import Y0_EXT, T_END_EXT

beta_vals = np.linspace(0.005, 0.05, 5)    # β_A
lambda_vals = np.linspace(0.1, 1.0, 5)      # λ_A
alpha_vals = [0.01]                 # abstención

header = ['beta_A', 'lambda_A', 'alpha', 'final_A', 'final_B', 'final_C', 'final_N']
with open('calibration_results.csv', 'w', newline='') as f:
    writer = csv.writer(f); writer.writerow(header)
    for beta, lam, alp in itertools.product(beta_vals, lambda_vals, alpha_vals):
        p = (beta, 0.015, 0.005, lam, 0.20, 0.10, 0.03, alp, 0.0)
        t, Y = run_ext(p, T_END_EXT, Y0_EXT, npts=200)
        writer.writerow([beta, lam, alp] + [Y[i, -1] for i in range(1, 5)])
print("CSV listo: calibration_results.csv")
