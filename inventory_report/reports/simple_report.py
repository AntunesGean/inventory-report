from statistics import mode


class SimpleReport:

    @classmethod
    def generate(self, list):

        manufac_date = min([prod["data_de_fabricacao"] for prod in list])
        expirat_date = min([prod["data_de_validade"] for prod in list])
        more_products = mode(
            [prod["nome_da_empresa"] for prod in list])

        return(
            f"Data de fabricação mais antiga: {manufac_date}\n"
            f"Data de validade mais próxima: {expirat_date}\n"
            f"Empresa com mais produtos: {more_products}"
        )
