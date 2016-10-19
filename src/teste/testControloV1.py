import psa

from src.AgenteProspector.agenteProspector import AgenteProspector
from src.algorithmImp.avoid_obstacle_v1 import AvoidObstacle
from src.algorithmImp.move_to_target_v1 import MoveToTargetV1
from src.controllerImp.controloV1 import ControloV1

psa.iniciar("../amb/amb2.das")

agente = AgenteProspector(ControloV1([AvoidObstacle(), MoveToTargetV1()]))
psa.executar(agente)
