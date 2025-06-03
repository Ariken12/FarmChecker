from Core.Components.Parsers.Parser import Parser, opxl
from openpyxl import load_workbook
from kivy.logger import Logger
import json


DATA_ROWS = (4, 25)
IGNORED_ROWs = (6, 9, 18, 22)
DATA_COLS = 'BCDEFGHIJ'
COLS_WITH_EMPTY_HEADERS = 'BEIJ'


class GeographyParser(Parser):
    def __init__(self, core):
        super().__init__(core)

    def __call__(self, file_xlsx):
        workbook = load_workbook(file_xlsx)
        worksheet = workbook['4']
        types1 = []
        types2 = []
        data = {}
        for row in range(*DATA_ROWS):
            if row in IGNORED_ROWs:
                continue
            type1 = worksheet[f'A{row}'].value
            types1.append(type1)
            data[type1] = {}
            for column in DATA_COLS:
                if column in COLS_WITH_EMPTY_HEADERS:
                    type2 = worksheet[f'{column}2'].value
                else:
                    type2 = worksheet[f'{column}3'].value
                types2.append(type2)
                data[type1][type2] = float(worksheet[f'{column}{row}'].value)
        self.core.data.update({'geography':{}})
        self.core.data['geography']['index'] = (
            tuple(types1), tuple(types2)
        )
        self.core.data['geography']['data'] = data.copy()