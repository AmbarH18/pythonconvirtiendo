def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

yenes = exchange_money(300, 0.007)
print(f"300 USD equivale a {yenes:.2f} yenes japoneses.")

pesos = exchange_money(300, 0.051)
print(f"300 USD equivale a {pesos:.2f} pesos mexicanos.")

euros = exchange_money(300, 1.1376)
print(f"300 USD equivale a {euros:.2f} euros.")
libras = exchange_money(500, 1.25)  
print(f"500 USD equivale a {libras:.2f} libras esterlinas.")
libras = exchange_money(500, 1.25)
print(f"500 USD equivale a {libras:.2f} libras esterlinas.")
