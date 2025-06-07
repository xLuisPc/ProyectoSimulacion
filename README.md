
# Proyecto de simulación del comportamiento de votantes

Este repositorio contiene dos modelos ODE:
* **models.base** – 2 candidatos (A, B) + indecisos
* **models.extended** – 3 candidatos (A, B, C) + indecisos + abstención

## Instalación

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución rápida

```bash
python -m src.experiments.compare_basic
python -m src.experiments.compare_extended
python -m src.experiments.sensitivity
python -m src.experiments.calibration
```

Los gráficos se guardarán en pantalla o en la carpeta **figures/**.
