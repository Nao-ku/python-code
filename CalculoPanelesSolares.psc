Proceso CalculoPanelesSolares
    Definir consumo_anual, eficiencia_panel, superficie_panel, radiacion_solar, horas_sol, potencia_diaria, potencia_anual, num_paneles, area_total Como Real
	
    consumo_anual <- 12000 
    eficiencia_panel <- 0.18 
    superficie_panel <- 1.6 
    radiacion_solar <- 5 
    horas_sol <- 5 
   
    potencia_diaria <- eficiencia_panel * superficie_panel * radiacion_solar * horas_sol
	
    potencia_anual <- potencia_diaria * 365

    area_total <- num_paneles * superficie_panel
	
    
    Escribir "Potencia diaria generada por un panel solar: ", potencia_diaria, " kWh"
    Escribir "Potencia anual generada por un panel solar: ", potencia_anual, " kWh"
    Escribir "Número de paneles necesarios: ", num_paneles
    Escribir "Área total necesaria para instalar los paneles solares: ", area_total, " m^2"
FinProceso
