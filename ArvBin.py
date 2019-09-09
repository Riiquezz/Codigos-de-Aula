### Arvore Binaria Não Balanceada

class Nodo:
    """
    Nodo da arvore: filhos da esquerda e direita + dado (que pode ser qualquer objeto)
    """
    def __init__(self, dado):
        self.esq = None
        self.dir = None
        self.dado = dado

    def __str__(self):
        return str(self.dado)

    def inserir(self, dado):
        """
        Insere um novo nodo com dados

        @param dado a ser inserido
        """
        
        ## Insere na sub-arvore da esquerda
        if dado < self.dado:
            if self.esq is None:
                # Cria um novo nodo (que sera a sub-arvore da esquerda)
                self.esq = Nodo(dado)
            else:
                self.esq.inserir(dado)

        ## Insere na sub-arvore da direita
        elif dado > self.dado:
            if self.dir is None:
                # Cria um novo nodo (que sera a sub-arvore da direita)
                self.dir = Nodo(dado)
            else:
                self.dir.inserir(dado)

    def buscar(self, dado, pai=None):
        if dado < self.dado:
            if self.esq is None:
                return None, None
            return self.esq.buscar(dado, self)
        elif dado > self.dado:
            if self.dir is None:
                return None, None
            return self.dir.buscar(dado, self)
        else:
            return self, pai
       
    def hasChild(self, alvo):
        filhos = []

        if alvo.esq is not None:
            filhos.append(alvo.esq)
            
        elif alvo.dir is not None:
            filhos.append(alvo.dir)

        return filhos
    
    def remover(self, pai, alvo):
        # implementar
            
    def imprimirEmOrdem(self):
        """
        Imprime o conteudo da arvore na tela, usando travessia em-ordem (in-order | arv_esq - raiz - arq_dir)
        """
        # Sub-arvore da Esquerda
        if self.esq:            
            self.esq.imprimirEmOrdem()

        # Raiz
        print(self.dado)

        # Sub-arvore da Esquerda
        if self.dir:            
            self.dir.imprimirEmOrdem()

    def imprimirPreOrdem(self):        
        print("[AVISO] imprimirPreOrdem não implementado")    

    def imprimirPosOrdem(self):
        print("[AVISO] imprimirPosOrdem não implementado")

def main():
    # 10, 4, 3, 5, 9, 12
    
    ## Inserindo...
    raiz = Nodo(10)
    nums = [4, 3, 5, 9, 12]
    for n in nums:
        raiz.inserir(n)
    
    ## Pesquisando...
    ## Implementar

    ## Removendo...
    ## Implementar

    
    ## Percorrendo...
    print('Em Ordem  :')
    raiz.imprimirEmOrdem()
    
    print('Pré Ordem :')
    raiz.imprimirPreOrdem()
    
    print('Pós Ordem :')
    raiz.imprimirPosOrdem()
    
if __name__ == "__main__":
    main()