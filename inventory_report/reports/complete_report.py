from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:

    def generate(list):

        simple_report = SimpleReport.generate(list)
        company_products = Counter(prod["nome_da_empresa"] for prod in list)
        stock = ""

        for company_n, company_quantity in company_products.items():
            stock += f"- {company_n}: {company_quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{stock}"
        )
