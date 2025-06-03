from Core.Components import Parsers as p

RESOURCE_NAME = 'Resources/data/data.xlsx'

class Initializer:
    def __init__(self, core):
        self.core = core
        self.geography_parser = p.GeographyParser(self.core)
        self.lighting_parser = p.LightingParser(self.core)
        self.initialize()

    def initialize(self):
        self.core.data = {}
        self.geography_parser(RESOURCE_NAME)
        self.lighting_parser(RESOURCE_NAME)
        self.core.data.update({
            # 'geography': {
            #     'index': (
            #         ('type1', 'type2', 'type3'),
            #         ('type1', 'type2')
            #     ),
            #     'data': {
            #         'type1': {
            #             'type1': 15,
            #             'type2': 250
            #         },
            #         'type2': {
            #             'type1': 20,
            #             'type2': 300
            #         },
            #         'type3': {
            #             'type1': 25,
            #             'type2': 350
            #         }
            #     }
            # },
            # 'lighting': {
            #     'standard': {
            #         'type1': {
            #             'S': 6.6,
            #             'E1': 50,
            #             'E2': 10
            #         },
            #         'type2': {
            #             'S': 5.7,
            #             'E1': 40,
            #             'E2': 20
            #         }
            #     },  
            #     'artificial_coeff': {
            #         'Лампы нак. 110, 120, 127 В': {
            #             '<100': 2.4,
            #             '>100': 3.2
            #         },
            #         'Лампы накаливания 220 В': {
            #             '<100': 2.0,
            #             '>100': 2.5
            #         },
            #         'Люменесцентные лампы': {
            #             '<100': 6.5,
            #             '>100': 8.0
            #         }
            #     }
            # },
            'manure': {
                'animal1': {
                    'summ_of_manure': 100,
                    'summ_of_trash': 50,
                }
            },
            'air_conditioning': {
                'CO2_types': {
                    'type1': {
                        'max_temperature': 24,
                        'CO2': 0.25,
                        'NH3': 20,
                        'H2S': 10
                    }
                },
                'room_types': {
                    'type1': {
                        'humidity_max': 85,
                        'humidity_min': 70,
                        'temperature': 25
                    }
                },
                'animal_category': {
                    'category1': {
                        'K-H2O': {
                            -10: 1,
                            -5: 1,
                            0: 0.83,
                            5: 0.92,
                            10: 1,
                            15: 1.12,
                            20: 1.43,
                            25: 1.93,
                            30: 1
                        },
                        'K-CO2': {
                            -10: 1,
                            -5: 1,
                            0: 0.83,
                            5: 0.92,
                            10: 1,
                            15: 1.12,
                            20: 1.43,
                            25: 1.93,
                            30: 1
                        },
                    }
                },
                'animals': {
                    'animal1': {
                        'CO2': 86,
                        'H2O': 305,
                    }
                },
                'cities': {
                    'city1': {
                        'temperature': {
                            'cold': -22,
                            'hot': 22.5,
                            'warm': -7.6
                        },
                        'humidity': { 
                            'cold': 74,
                            'hot': 54,
                            'warm': 78
                        }
                    }
                },
                'coeff': {
                    -25.0: 0.54,
                    -25.1: 0.53,
                    -25.2: 0.53,
                    -25.3: 0.53,
                    -25.4: 0.52,
                    -25.5: 0.51
                }
            }
        })