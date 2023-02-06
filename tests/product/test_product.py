from inventory_report.inventory.product import Product


def test_cria_produto():
    pass
    product = Product(
        1,
        "CD Molejo 25 anos - O Baile É Sem Parar",
        "Columbia Records",
        "10/04/2014",
        "31/12/2099",
        "Molejo",
        "na Caçamba"
        )

    assert product.id == 1
    assert product.nome_do_produto == "CD Molejo 25 anos - O Baile É Sem Parar"
    assert product.nome_da_empresa == "Columbia Records"
    assert product.data_de_fabricacao == "10/04/2014"
    assert product.data_de_validade == "31/12/2099"
    assert product.numero_de_serie == "Molejo"
    assert product.instrucoes_de_armazenamento == "na Caçamba"
