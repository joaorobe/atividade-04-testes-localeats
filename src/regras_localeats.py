def pedido_atingiu_valor_minimo(valor_pedido: float) -> bool:
    """Informa se o pedido alcança o valor mínimo de R$ 30,00."""
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= 30


def quantidade_itens_valida(quantidade: int) -> bool:
    """Informa se a quantidade está entre 1 e 10 itens."""
    if quantidade < 0:
        raise ValueError("A quantidade de itens não pode ser negativa.")
    return 1 <= quantidade <= 10
