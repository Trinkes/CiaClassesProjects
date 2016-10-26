from src.AgenteProspector.controlo import Controlo

DIR1 = -0.7853981633974483

ESQ1 = 0.7853981633974483

FRT1 = 0


class ControloV1(Controlo):
    def __init__(self, algorithms):
        self.algorithms = algorithms

    def processar(self, per):

        for algorithm in self.algorithms:
            act = algorithm.nextMove(per)
            if act is not None:
                return act
