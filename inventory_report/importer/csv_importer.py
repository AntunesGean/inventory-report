import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):

    def import_data(file: str):

        if not file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file, encoding="utf-8") as file:
            data = csv.DictReader(file)
            return list(data)
