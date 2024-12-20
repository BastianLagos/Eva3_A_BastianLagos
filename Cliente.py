class Cliente:
    __idCliente = 0
    __nomCliente = ""
    __apeCliente = ""
    __nroSexCliente = 0
    __nomSexCliente = ""
    __salCliente = 0
    __sitCliente = 0

    def __init__(self):
        pass

    def getIdCliente(self):
        return self.__idCliente

    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente

    def getNomCliente(self):
        return self.__nomCliente

    def setNomCliente(self, nomCliente):
        self.__nomCliente = nomCliente

    def getApeCliente(self):
        return self.__apeCliente

    def setApeCliente(self, apeCliente):
        self.__apeCliente = apeCliente

    def getNroSexCliente(self):
        return self.__nroSexCliente

    def setNroSexCliente(self, nroSexCliente):
        self.__nroSexCliente = nroSexCliente

    def getNomSexCliente(self):
        return self.__nomSexCliente

    def setNomSexCliente(self, nomSexCliente):
        self.__nomSexCliente = nomSexCliente

    def getSalCliente(self):
        return self.__salCliente

    def setSalCliente(self, salCliente):
        self.__salCliente = salCliente

    def getSitCliente(self):
        return self.__sitCliente

    def setSitCliente(self, sitCliente):
        self.__sitCliente = sitCliente