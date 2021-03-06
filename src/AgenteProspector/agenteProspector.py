from psa.agente import Agente


class AgenteProspector(Agente):
    
    
    def __init__(self, controller):
        # type: (object) -> object

        self.controlo = controller

    def executar(self):

        # Percepcionar
        per = self.sensor_multiplo.detectar()

        # Processar
        accao = self.controlo.processar(per)
        # Actuar
        if accao is not None:
            self.actuador.actuar(accao)

#interface Controlo