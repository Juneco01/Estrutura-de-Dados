class Celula:

    # Construtor da celula
    # Como preferi percorrer a cobra de trás pra frente (já que é mais facil controlar as partes da cobra)
    # criei uma referencia para o membro anterior. podendo assim percorrer a partir do ultimo membro até o primeiro
    # O construtor também recebe dois dados, que são as cordenadas (x,y), a posição do pedaço da cobra no mapa.
    def __init__(self,x,y):
        self.dado = [x,y]        
        self.ant = None
        self.prox = None

