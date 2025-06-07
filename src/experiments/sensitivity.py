import numpy as np
import matplotlib.pyplot as plt
from ..models.base import run_scenario
from ..scenarios.base import SCENARIOS, DEFAULT_Y0, T_END

# --- base en "Medios", variamos solo β_A y λ_A ---
beta_vals   = np.linspace(0.005, 0.05, 10)   # eje X
lambda_vals = np.linspace(0.10, 1.20, 10)    # eje Y

heat = np.zeros((len(lambda_vals), len(beta_vals)))

base = list(SCENARIOS["Medios"])  # mutable copia

for i, lam in enumerate(lambda_vals):
    for j, beta in enumerate(beta_vals):
        pars = base.copy()
        pars[0] = beta   # β_A
        pars[2] = lam    # λ_A
        _, (_, A, _) = run_scenario(tuple(pars), T_END, DEFAULT_Y0, npts=200)
        heat[i, j] = A[-1]   # voto final de A

fig, ax = plt.subplots()
im = ax.imshow(heat, origin='lower',
               extent=[beta_vals.min(), beta_vals.max(),
                       lambda_vals.min(), lambda_vals.max()],
               aspect='auto')
ax.set_xlabel(r'$\beta_A$ (propaganda masiva)')
ax.set_ylabel(r'$\lambda_A$ (influencia social)')
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Voto final de A')
plt.tight_layout()
plt.show()
