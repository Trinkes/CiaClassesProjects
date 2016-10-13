from src.AgenteProspector.controlo import Controlo

DIR1 = -0.7853981633974483

ESQ1 = 0.7853981633974483

FRT1 = 0


class ControloV1(Controlo):
    def __init__(self, move_to_target, avoid_obstacle):
        self.avoidObstacle = avoid_obstacle
        self.moveToTarget = move_to_target

    def processar(self, per):
        act = self.avoidObstacle.nextMove(per)
        if act is None:
            move = (1, self.moveToTarget.nextMove(per))
        else:
            move = (1, act)
        return move
