Conversor de Monedas en Python
Este es un proyecto sencillo que hice para practicar funciones en Python. El programa convierte una cantidad en dólares (USD) a otra moneda según la tasa de cambio que se le indique.

Descripción de la función

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate
La función se llama exchange_money y recibe dos parámetros:

budget: el monto en dólares que quiero cambiar.

exchange_rate: la tasa de cambio de la moneda a la que quiero convertir.

Devuelve el valor equivalente en la otra moneda.

Ejemplos que incluí
Convertí 300 USD a varias monedas para probar cómo funciona:

yenes = exchange_money(300, 0.007)
print(f"300 USD equivale a {yenes:.2f} yenes japoneses.")

pesos = exchange_money(300, 0.051)
print(f"300 USD equivale a {pesos:.2f} pesos mexicanos.")

euros = exchange_money(300, 1.1376)
print(f"300 USD equivale a {euros:.2f} euros.")

libras = exchange_money(500, 1.25)
print(f"500 USD equivale a {libras:.2f} libras esterlinas.")
Cómo lo uso
Guardé todo en un archivo llamado convirtiendo.py.

Desde la terminal, lo ejecuto con:

python convirtiendo.py
Este ejercicio me ayudó a practicar el uso de funciones, parámetros y formateo de salida en Python.