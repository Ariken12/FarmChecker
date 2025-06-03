from Core.Components.Parsers.Parser import Parser, opxl
from openpyxl import load_workbook
from kivy.logger import Logger
import json


DATA_ROWS = (4, 65)
DATA_COLS = 'GIJ'
IGNORED_CELLS = (16, 21, 28, 34, 45, 63)
ARTIFICIAL_COEFF = {
    'artificial_coeff': {
        'Лампы нак. 110, 120, 127 В': {
            '<100': 2.4,
            '>100': 3.2
        },
        'Лампы накаливания 220 В': {
            '<100': 2.0,
            '>100': 2.5
        },
        'Люменесцентные лампы': {
            '<100': 6.5,
            '>100': 8.0
        }
    }
    }


class LightingParser(Parser):
    def __init__(self, core):
        super().__init__(core)

    def __call__(self, file_xlsx):
        workbook = load_workbook(file_xlsx)
        worksheet = workbook['1']
        data = {}
        type1 = ''
        type2 = ''
        for irow in range(*DATA_ROWS):
            type1 = worksheet[f'A{irow}'].value if worksheet[f'A{irow}'].value != None else type1 
            type2 = worksheet[f'B{irow}'].value if worksheet[f'B{irow}'].value != None else type1 
            if irow in IGNORED_CELLS:
                continue
            index = str(type1) + ' ' + str(type2)
            data[index] = {}
            data[index]['S'] = self.normalize_number(worksheet[f'G{irow}'].value)
            data[index]['E1'] = self.normalize_number(worksheet[f'I{irow}'].value)
            data[index]['E2'] = self.normalize_number(worksheet[f'J{irow}'].value)
        self.core.data['lighting'] = {}
        self.core.data['lighting'].update(ARTIFICIAL_COEFF)
        self.core.data['lighting']['standard'] = data.copy()
        Logger.debug(json.dumps(self.core.data['lighting'], ensure_ascii=False, indent=4))

    def normalize_number(self, nmbr):
        if type(nmbr) is str:
            if ' ' in nmbr:
                nmbr = nmbr[:nmbr.index(' ')]
            if '-' in nmbr:
                nmbr = nmbr[:nmbr.index('-')]
            if nmbr == 'нет':
                nmbr = '0'
            nmbr = float(nmbr.replace(',', '.'))
        elif nmbr is None:
            nmbr = 0
        elif type(nmbr) is int:
            nmbr = float(nmbr)
        else:
            Logger.debug(type(nmbr))
        return nmbr