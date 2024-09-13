
consumo_anual = float(input("Consumo anual (kWh): "))
eficiencia = float(input("Eficiencia del panel (ej: 0.15 para 15%): "))
area_panel = float(input("Área del panel (m²): "))
radiacion_solar =float(input("Radiación solar (kWh/m²/día): "))
horas_sol = float(input("Horas de sol por día: "))

energia_diaria_panel = (area_panel * radiacion_solar * horas_sol * eficiencia)
energia_anual_panel = energia_diaria_panel * 365
num_paneles = consumo_anual / energia_anual_panel
num_paneles = round(num_paneles)
area_total = num_paneles * area_panel

print(f"Paneles necesarios: {num_paneles}")
print(f"Área total requerida: {area_total:.2f} m²")

