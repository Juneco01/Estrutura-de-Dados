class Pilha:

    #Classe nó, criei também um ponteiro para o elemento anterior
    #Como preciso desenhar os elementos de cada pilha, a cada iteração
    #É necessario percorrer a pilha como uma lista encadeada para desenhar todos os elementos na tela
    #Porém ainda são mantidas as operações de pilha, e a complexidade Remoção/Inserção continua o(1)
    def __init__(self,dado):
        self.dado = dado
        self.prox = None
        self.ant = None