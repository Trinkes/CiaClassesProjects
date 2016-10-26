from src.AgenteProspector.algorithm import Algorithm
from src.controllerImp.controloV1 import ESQ1, FRT1, DIR1

# contant
START_DISTANCE = 3


class AvoidObstacleV2(Algorithm):
    def nextMove(self, per):
        # indexWithMinDist = self.checkIfMove(per.per_dir)
        # min_dist = per.per_dir[indexWithMinDist]

        move = self.checkIfMove(per.per_dir)
        if move == None:
            return None
        else:
            return 1, move
        # if per.colisao == True:
        #     return ESQ1
        # else:
        #     return None

    def checkIfMove(self, per_periferia):
        indexWithMinDistance = None
        minDistance = 0
        if per_periferia[FRT1].obstaculo and START_DISTANCE >= per_periferia[FRT1].distancia:
            for index in [ESQ1, DIR1, FRT1]:
                if per_periferia[index].obstaculo and per_periferia[index].distancia > minDistance:
                    minDistance = per_periferia[index].distancia
                    indexWithMinDistance = index
        return indexWithMinDistance
