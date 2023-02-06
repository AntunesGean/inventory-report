from abc import ABC


class Importer(ABC):

    @classmethod
    def import_data(file: str):
        raise NotImplementedError
