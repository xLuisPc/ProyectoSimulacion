if __name__ == "__main__":
    # ... aquí ya corre tu integración y gráficas de resultados ...

    # -----------------------------------------------------------------
    #  Sección opcional: tabla de parámetros y figura de compartimentos
    # -----------------------------------------------------------------
    import pandas as pd
    import matplotlib.pyplot as plt

    param_data = {
        "Símbolo": ["β_A", "β_B", "λ_A", "λ_B", "μ", "σ"],
        "Descripción": [
            "Propaganda masiva a favor de A",
            "Propaganda masiva a favor de B",
            "Influencia social de A",
            "Influencia social de B",
            "Tasa de olvido (fatiga)",
            "Contra-persuasión (fricción A-B)"
        ],
        "Tradicional": [0.040, 0.030, 0.20, 0.20, 0.03, 0.00],
        "Redes":       [0.005, 0.005, 1.00, 1.00, 0.03, 0.00],
        "Mixto":       [0.020, 0.020, 0.60, 0.60, 0.03, 0.00]
    }
    df = pd.DataFrame(param_data)
    print("\nTabla 1 – Parámetros del modelo\n")
    print(df.to_markdown(index=False))

    # ---- Diagrama ----
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlim(0, 4); ax.set_ylim(0, 3); ax.axis('off')
    pos = {"U": (2, 2.5), "A": (0.75, 0.5), "B": (3.25, 0.5)}
    for lbl,(x,y) in pos.items():
        ax.text(x, y, lbl, ha='center', va='center', fontsize=14,
                bbox=dict(boxstyle="circle", fc="white"))
    def arrow(src, dst, lbl):
        sx, sy = pos[src]; dx, dy = pos[dst]
        ax.annotate("", xy=(dx, dy), xytext=(sx, sy),
                    arrowprops=dict(arrowstyle="->"))
        ax.text((sx+dx)/2, (sy+dy)/2, lbl, fontsize=8, ha='center')
    arrow("U","A",r"$\beta_A+\lambda_A A$")
    arrow("U","B",r"$\beta_B+\lambda_B B$")
    arrow("A","U",r"$\mu$")
    arrow("B","U",r"$\mu$")
    arrow("A","B",r"$\sigma A B$")
    arrow("B","A",r"$\sigma A B$")
    plt.tight_layout(); plt.show()
