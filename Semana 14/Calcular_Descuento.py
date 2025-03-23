def calcula_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total.

    Args:
        monto_total: El monto total de la compra.
        porcentaje_descuento: El porcentaje de descuento a aplicar (default 10%)

    Returns:
        El monto del descuento calculado.
    """
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamadas a la función
monto1 = 100
descuento1 = calcula_descuento(monto1)
monto_final1 = monto1 - descuento1

monto2 = 200
porcentaje2 = 15
descuento2 = calcula_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2


# Salida de resultados
print(f"Compra 1: Monto total = {monto1}, Descuento = {descuento1:.2f}, Monto final = {monto_final1:.2f}")
print(f"Compra 2: Monto total = {monto2}, Descuento = {descuento2:.2f}, Monto final = {monto_final2:.2f}")