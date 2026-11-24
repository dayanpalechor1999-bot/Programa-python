
#DAYAN ALEXIS PALECHOR TIMANA
#INGENIERIA DE TELECOMUNICACIONES
#PROBLEMA 2: PROMOCIONES DEL MENÚ

"""Promociones del menú con precios aproximados en pesos colombianos."""

DESCUENTO = 0.15
CATEGORIAS_OBJETIVO = {"Plato fuerte"}
UMBRAL_PRECIO = 20_000

# Precios de referencia aproximados; pueden variar según ciudad y restaurante.
menu = [
	["Empanadas de Pipian", "Entrada", 3_000],
	["Sancocho de Gallina", "Plato fuerte", 25_000],
	["Lulada", "Bebida", 8_000],
	["Pechuga a la plancha", "Plato fuerte", 28_000],
	["Lechona Tolimense", "Plato fuerte", 20_000],
	["Salpicon de Payanes", "Postre", 9_000],
]


def calcular_precio_final(producto):
	"""Aplica el descuento solo si categoría y precio cumplen las condiciones."""
	_, categoria, precio_base = producto
	if categoria in CATEGORIAS_OBJETIVO and precio_base > UMBRAL_PRECIO:
		return round(precio_base * (1 - DESCUENTO))
	return precio_base


print("Menú promocional (precios en COP)")
print(f"{'Producto':<25} | {'Categoría':<15} | {'Precio base':>16} | {'Precio final':>16}")
print("-" * 84)
for nombre, categoria, precio_base in menu:
	precio_final = calcular_precio_final([nombre, categoria, precio_base])
	print(
		f"{nombre:<25} | {categoria:<15} | "
		f"${precio_base:>14,.0f} | ${precio_final:>14,.0f}"
	)
