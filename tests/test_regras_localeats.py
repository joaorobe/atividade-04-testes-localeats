import pytest

from src.regras_localeats import (
    pedido_atingiu_valor_minimo,
    quantidade_itens_valida,
)


def test_pedido_exatamente_no_valor_minimo_e_aprovado():
    assert pedido_atingiu_valor_minimo(30) is True


def test_pedido_abaixo_do_valor_minimo_nao_e_aprovado():
    assert pedido_atingiu_valor_minimo(29.99) is False


def test_pedido_com_valor_negativo_gera_value_error():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-1)


def test_quantidade_maxima_de_itens_e_valida():
    assert quantidade_itens_valida(10) is True


def test_quantidade_acima_do_limite_nao_e_valida():
    assert quantidade_itens_valida(11) is False


def test_quantidade_zero_nao_e_valida():
    assert quantidade_itens_valida(0) is False


def test_quantidade_negativa_gera_value_error():
    with pytest.raises(ValueError):
        quantidade_itens_valida(-1)
