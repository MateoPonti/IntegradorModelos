import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as ExcelImage
from datetime import time

horas = [time(6, 0), time(6, 15), time(6, 30), time(6, 45), time(7, 0)]
frecuencias = [3, 5, 2, 4, 7]

df = pd.DataFrame({
    "Hora_HHMM": [h.strftime("%H:%M") for h in horas],
    "CantidadDeViajes": frecuencias
})

# === 3. Graficar ===
plt.figure(figsize=(10, 5))
plt.plot(df["Hora_HHMM"], df["CantidadDeViajes"], marker='o')
plt.xticks(rotation=90)
plt.xlabel("Hora")
plt.ylabel("Cantidad de Viajes")
plt.title("Viajes por horario")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_viajes.png")
plt.close()

archivo_excel = "viajes_resultado.xlsx"
df.to_excel(archivo_excel, index=False)

wb = load_workbook(archivo_excel)
ws = wb.active

hora_establecida = "07:30"
alpha = 0.05
hora_max = "08:00"
hora_min = "06:00"

semaforos = {
    'A': {'verde': 30, 'rojo': 45, 'amarillo': 5},
    'B': {'verde': 25, 'rojo': 50, 'amarillo': 6},
    'C': {'verde': 20, 'rojo': 60, 'amarillo': 7}
}

# Escribir parámetros
ws["E1"] = "Parámetros"
ws["E2"] = f"horaEstablecida: {hora_establecida}"
ws["E3"] = f"alpha: {alpha}"
ws["E4"] = f"horaMaxEsperada: {hora_max}"
ws["E5"] = f"horaMinEsperada: {hora_min}"



img = ExcelImage("grafico_viajes.png")
img.anchor = "G2"
ws.add_image(img)

wb.save(archivo_excel)