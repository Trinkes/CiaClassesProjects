from psa.actuador import DIR
from psa.actuador import ESQ
from psa.actuador import FRT

from src.AgenteProspector.algorithm import Algorithm
from src.controllerImp.controloV1 import FRT1, ESQ1, DIR1


class MoveToTargetV1(Algorithm):
    def nextMove(self, per):
        frt = per[FRT].pot_alvo
        esq = per[ESQ].pot_alvo
        xtype = [frt, esq, per[DIR].pot_alvo]

        xtype.sort()

        if xtype[2] == frt:
            return 1, FRT1
        elif xtype[2] == esq:
            return 1, ESQ1
        else:
            return 1, DIR1
