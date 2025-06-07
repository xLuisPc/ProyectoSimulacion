import matplotlib.pyplot as plt
from ..models.extended import run_ext
from ..scenarios.extended import EXT_SCENARIOS, Y0_EXT, T_END_EXT

fig, axs = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
for ax, (name, pars) in zip(axs, EXT_SCENARIOS.items()):
    t, (U, A, B, C, N) = run_ext(pars, T_END_EXT, Y0_EXT)
    ax.plot(t, A, '--', label='A')
    ax.plot(t, B,  '-', label='B')
    ax.plot(t, C,  ':', label='C')
    ax.plot(t, N,  '-.', label='N (Abst.)')
    ax.set_title(name)
    ax.set_xlabel('Días')
axs[0].set_ylabel('Fracción de la población')
axs[-1].legend(loc='upper right')
plt.tight_layout(); plt.show()
