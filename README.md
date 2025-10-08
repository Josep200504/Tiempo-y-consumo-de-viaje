# 🧭 Calcular Viaje – Python

**Autor:** José Alcalá  
**Fecha:** 06/09/24  
**Archivo:** `CalcularViaje.py`  
**Descripción:** Programa en Python que calcula el tiempo total y el consumo estimado de un viaje con base en la distancia, velocidad y consumo de combustible del vehículo.

---

## 🚀 Descripción general

Este script permite calcular:
- El **tiempo total del viaje** expresado en horas, minutos y segundos.
- El **consumo total estimado de combustible** según los litros consumidos por unidad de distancia.

Es ideal para ejercicios básicos de funciones en Python, manejo de entradas del usuario y operaciones aritméticas simples.

---

## 📄 Código fuente

```python
"""
Autor: José Alcalá
Fecha: 06/09/24
Nombre del archivo: CalcularViaje.py
Descripción: Funciones
"""

def calcular_tiempo(distancia, velocidad):
    tiempo_total_horas = distancia / velocidad  # calcular el tiempo
    horas = int(tiempo_total_horas)
    minutos = int((tiempo_total_horas - horas) * 60)
    segundos = int(((tiempo_total_horas - horas) * 60 - minutos) * 60)
    return horas, minutos, segundos

def calcular_consumo(litros, distancia):
    return litros * distancia

# Entradas del usuario
distancia = int(input("Dame la distancia: "))
velocidad = int(input("Dame la velocidad: "))
litros = int(input("Dame el consumo: "))

# Cálculos
horas, minutos, segundos = calcular_tiempo(distancia, velocidad)
print(f"El coche tardará {horas} horas, {minutos} minutos y {segundos} segundos")

consumo = calcular_consumo(litros, distancia)
print(f"El consumo total esperado es de {consumo}")
