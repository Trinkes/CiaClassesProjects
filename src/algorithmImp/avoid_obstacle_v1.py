from src.AgenteProspector.algorithm import Algorithm
from src.controllerImp.controloV1 import ESQ1


class AvoidObstacle(Algorithm):
    def nextMove(self, per):
        accao_ = per.periferia[per.dir_accao][0][0]

        # if self.checkIfMove(per.periferia, accao_) or self.checkIfMove(per.periferia,
        #                                                                 accao_ + 1) or self.checkIfMove(
            # per.periferia, accao_ + 2):
            # directionToMove = ESQ1
        # else:
        #     directionToMove = None

        # return directionToMove
        if per.colisao == True:
            return ESQ1
        else:
            return None

    def checkIfMove(self, list, index):
        if index < len(list) - 1 and index >= 0:
            return list[index] == 'obst'
        else:
            return False
