# -*- coding: latin-1 -*-
'''
Controlo de aprendizagem por reforço
'''

# _______________________________________________________________________________
from psa.psa5 import dirmov
from psa.psa5.accao import Mover

from src.AgenteProspector.controlo import Controlo
from src.AgenteProspector.controlo_aprend.mec_motiv import MecMotiv
from src.lib.aprend_ref.mec_aprend import MecAprend


class ControloAprendRef(Controlo):
    def __init__(self):
        accoes = [Mover(ang, ang_abs=True) for ang in dirmov()]
        self.mec_motiv = MecMotiv()
        self.mec_aprend = MecAprend(accoes)
        self.s = None
        self.a = None

    def processar(self, percepcao):
        sn = percepcao.posicao
        if self.s is not None:
            a = self.a
            r = self.mec_motiv.gerar_reforco(percepcao)
            self.mec_aprend.aprender(self.s, a, r, sn)
        an = self.mec_aprend.seleccionar_accao(sn)
        self.s = sn
        self.a = an
        return an
