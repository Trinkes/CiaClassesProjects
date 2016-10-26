import psa

from src.AgenteProspector.agenteProspector import AgenteProspector
from src.AgenteProspector.controlo_aprend.controlo_aprend_ref import ControloAprendRef

psa.iniciar("../amb/amb3b.das", alvo_ini=True)

psa.executar(AgenteProspector(ControloAprendRef()))
