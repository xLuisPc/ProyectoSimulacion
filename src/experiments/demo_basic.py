import matplotlib.pyplot as plt
from ..models.base import run_scenario
from ..scenarios.base import SCENARIOS, DEFAULT_Y0, T_END
from ..utils.metrics import auc, persuasion_number

fig, ax = plt.subplots()

results = {}

for name, pars in SCENARIOS.items():
    t, (U, A, B) = run_scenario(pars, T_END, DEFAULT_Y0)
    ax.plot(t, A, '--', label=f'A ({name})')
    ax.plot(t, B,  '-', label=f'B ({name})')
    results[name] = {
        "final_A": A[-1],
        "final_B": B[-1],
        "auc_A": auc(A, t),
        "auc_B": auc(B, t),
        "Rp": persuasion_number(pars[0], pars[2], pars[4])  # (beta+lambda)/mu  para A
    }

ax.set_xlabel('Días')
ax.set_ylabel('Fracción de la población')
ax.legend()
plt.tight_layout()
plt.show()

# --- imprime resumen numérico ---
for name, res in results.items():
    print(f'\n=== {name} ===')
    for k, v in res.items():
        print(f'{k}: {v:.4f}')
