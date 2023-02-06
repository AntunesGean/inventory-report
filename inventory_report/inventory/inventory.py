from typing import Literal
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.csv_importer import CsvImporter


class Inventory:

    def import_data(file: str, type: Literal["simples", "completo"]):

        if "csv" in file:
            data = CsvImporter.import_data(file)
        elif "json" in file:
            data = JsonImporter.import_data(file)
        elif "xml" in file:
            data = XmlImporter.import_data(file)

        return (
            SimpleReport.generate(data)
            if type == "simples"
            else CompleteReport.generate(data)
        )
