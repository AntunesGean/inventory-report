import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    def import_data(file: str):

        if not file.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(file, encoding="utf-8") as data:
            dataJSON = json.load(data)
            return dataJSON
