import matplotlib.pyplot as plt
from ..models.base       import run_scenario
from ..scenarios.base    import SCENARIOS, DEFAULT_Y0, T_END
from ..utils.metrics     import auc, persuasion_number

fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

for ax, (name, pars) in zip(axs, SCENARIOS.items()):
    t, (U, A, B) = run_scenario(pars, T_END, DEFAULT_Y0)
    ax.plot(t, A, '--', label='A')
    ax.plot(t, B,  '-', label='B')
    ax.plot(t, U, ':',  label='Indecisos')
    ax.set_title(name)
    ax.set_xlabel('Días')
axs[0].set_ylabel('Fracción de la población')
axs[1].legend(loc='upper right')
plt.tight_layout()
plt.show()
