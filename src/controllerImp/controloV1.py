from psa.actuador import ESQ
from psa.actuador import DIR
from psa.actuador import FRT
from src.AgenteProspector.controlo import Controlo

DIR1 = -0.7853981633974483

ESQ1 = 0.7853981633974483

FRT1 = 0

class ControloV1(Controlo):

    def processar(self, per):
        if per.colisao == False:
            act = compare(per[FRT].pot_alvo,per[ESQ].pot_alvo,per[DIR].pot_alvo)
            acesso = (1,act)
        else:
            acesso = (1,DIR1)

        return acesso


def compare(frt, esq, dir):

        xval = 0.0
        xtype = [frt, esq, dir]

        xtype.sort()

        if xtype[2] == frt:
            return FRT1
        elif xtype[2] == esq:
            return ESQ1
        else:
            return DIR1




