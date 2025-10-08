"""
Autor: José Alcalá
Fecha: 06/09/24
Nombre del archivo: CalcularViaje.py
Descripción: Funciones
"""

def calcular_tiempo (distancia,velocidad):
    tiempo_total_horas= distancia/velocidad #calcular el tiempo 
    horas=int(tiempo_total_horas) 
    minutos=int((tiempo_total_horas - horas)* 60)
    segundos=int(((tiempo_total_horas - horas)* 60 - minutos)* 60)
    return horas, minutos, segundos, 
def calcular_consumo(litros,distancia):
    
    return litros*distancia
    
distancia=int(input("Dame la distancia: "))
velocidad=int(input("Dame la velocidad: ")) 
consumo_kilometro=int(input("Dame el consumo: "))
horas, minutos, segundos= calcular_tiempo(distancia,velocidad)
print(f"El coche tardará {horas} horas, {minutos} minutos y {segundos} segundos")
consumo=calcular_consumo(litros,distancia)
print(f"El consumo total esperado es de {consumo} ")