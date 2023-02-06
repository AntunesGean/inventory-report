import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    def import_data(file: str):

        if not file.endswith("xml"):
            raise ValueError("Arquivo inválido")
        with open(file, encoding="utf-8") as file:
            xml = file.read()
            list = xmltodict.parse(xml)
            data = list["dataset"]["record"]
            return data
