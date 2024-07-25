
class veiculo:
    def __init__(self,tipo,chasi,marca,modelo,ano):
        self.tipo=tipo
        self.chasi=chasi
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
class motocicleta(veiculo):#herda do veiculo
    def __init__(self,tipo,chasi,marca,modelo,ano,cc):
        super().__init__(tipo,chasi,marca,modelo,ano) #adicionar uma coisa a + controi no inicializzador e internamnte constroi o veiculo e adiciona a cc da motocicleta
        self.ciclindrada=cc

