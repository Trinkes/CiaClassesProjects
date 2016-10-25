# -*- coding: latin-1 -*-
'''
Controlo de aprendizagem por reforço
'''

# _______________________________________________________________________________
from src.AgenteProspector.controlo import Controlo


class ControloAprendRef(Controlo):
    def __init__(self):
        raise NotImplementedError

    def processar(self, percepcao):
        raise NotImplementedError
