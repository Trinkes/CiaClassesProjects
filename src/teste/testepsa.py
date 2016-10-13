# -*- config: latin-1 -*-
import psa
from psa.agente import Agente
class AgenteTeste(Agente):
    def executar(self):
        acesso = (1,0)
        self.actuador.actuar(acesso)
        self.actuador.orientar(100)

psa.iniciar("../amb/amb1.das")

agente = AgenteTeste()
psa.executar(agente)

