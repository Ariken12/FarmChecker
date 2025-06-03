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