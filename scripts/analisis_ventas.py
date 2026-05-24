import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Rutas
ruta_datos = BASE_DIR / "datos" / "ventas.csv"
ruta_resultados = BASE_DIR / "resultados"

# Leer datos
ventas = pd.read_csv(ruta_datos, parse_dates=["sales_date"])

# Ventas totales
ventas_totales = ventas["sales_amount"].sum()

# Ventas por mes
ventas["mes"] = ventas["sales_date"].dt.to_period("M")
ventas_por_mes = ventas.groupby("mes")["sales_amount"].sum()

# Guardar resumen
with open(ruta_resultados / "resumen.txt", "w", encoding="utf-8") as f:
    f.write(f"Ventas totales: ${ventas_totales}\n")

# Gráfico
ventas_por_mes.plot(kind="bar")
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto vendido")
plt.tight_layout()

plt.savefig(ruta_resultados / "ventas_por_mes.png")
plt.close()