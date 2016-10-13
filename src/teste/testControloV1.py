import psa

from src.AgenteProspector.agenteProspector import AgenteProspector
from src.controllerImp.controloV1 import ControloV1
from src.controllerImp.moveToTargetV1 import MoveToTargetV1

psa.iniciar("../amb/amb2.das")

agente = AgenteProspector(ControloV1(MoveToTargetV1()))
psa.executar(agente)