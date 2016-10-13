from src.AgenteProspector.controlo import Controlo

DIR1 = -0.7853981633974483

ESQ1 = 0.7853981633974483

FRT1 = 0


class ControloV1(Controlo):
    def __init__(self, moveToTarget):

        self.moveToTarget = moveToTarget

    def processar(self, per):
        if per.colisao == False:
            act = self.moveToTarget.moveToTarget(per)
            acesso = (1, act)
        else:
            acesso = (1, DIR1)

        return acesso
