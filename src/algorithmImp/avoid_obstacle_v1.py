from src.AgenteProspector.algorithm import Algorithm
from src.controllerImp.controloV1 import ESQ1


class AvoidObstacleV1(Algorithm):
    def nextMove(self, per):
        if per.colisao == True:
            return 1, ESQ1
        else:
            return None