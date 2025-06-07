"""
Genera todas las figuras finales en ./figures (300 dpi)
Run: python -m src.experiments.make_figures
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from src.models.base       import run_scenario
from src.scenarios.base    import SCENARIOS, DEFAULT_Y0, T_END
from src.models.extended   import run_ext
from src.scenarios.extended import EXT_SCENARIOS, Y0_EXT, T_END_EXT
from src.experiments.sensitivity import beta_vals, lambda_vals

os.makedirs("figures", exist_ok=True)

# ---------- 1) Dos candidatos ----------
for name, pars in SCENARIOS.items():
    fig, ax = plt.subplots(figsize=(6, 4))
    t, (U, A, B) = run_scenario(pars, T_END, DEFAULT_Y0, npts=400)
    ax.plot(t, A, '--', label='A')
    ax.plot(t, B,  '-', label='B')
    ax.set_xlabel('Días'); ax.set_ylabel('Fracción')
    ax.set_title(f'Dinámica {name}'); ax.legend()
    fig.tight_layout()
    fig.savefig(f"figures/compare_AB_{name}.png", dpi=300)
    plt.close(fig)

# ---------- 2) Tres candidatos + abstención ----------
for name, pars in EXT_SCENARIOS.items():
    fig, ax = plt.subplots(figsize=(6, 4))
    t, (U, A, B, C, N) = run_ext(pars, T_END_EXT, Y0_EXT, npts=400)
    for series, ls, lab in [(A, '--', 'A'),
                            (B, '-',  'B'),
                            (C, ':',  'C'),
                            (N, '-.', 'N')]:
        ax.plot(t, series, ls, label=lab)
    ax.set_xlabel('Días'); ax.set_ylabel('Fracción')
    ax.set_title(f'Dinámica {name}'); ax.legend()
    fig.tight_layout()
    fig.savefig(f"figures/compare_ABCN_{name}.png", dpi=300)
    plt.close(fig)

# ---------- 3) Heat-map β_A × λ_A ----------
heat = np.loadtxt("calibration_results.csv", delimiter=',', skiprows=1,
                  usecols=(3,))  # columna final_A (25 filas si alpha único)
heat = heat.reshape(len(lambda_vals), len(beta_vals))

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(heat, origin='lower',
               extent=[beta_vals.min(), beta_vals.max(),
                       lambda_vals.min(), lambda_vals.max()],
               aspect='auto')
ax.set_xlabel(r'$\beta_A$ (propaganda)')
ax.set_ylabel(r'$\lambda_A$ (redes)')
ax.set_title('Heat-map β_A × λ_A')
cbar = fig.colorbar(im, ax=ax, label='Voto final A')
fig.tight_layout()
fig.savefig("figures/heatmap_beta_lambda_A.png", dpi=300)
plt.close(fig)

print("✔ Todas las figuras están en la carpeta 'figures'")
