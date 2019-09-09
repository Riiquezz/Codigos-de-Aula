class Conjunto:

    def __init__(self):
        # inicializa lista simulando um vetor
        self._colisoes = 0
        self._tamanho = 0
        self._vet = []
        for x in range(0,26,1):
            self._vet.append('')

    def __calcula_indice(self, palavra):
        return ord(palavra.lower()[0]) % 26

    def __normaliza(self, palavra):
        return palavra.lower()

    def __verifica_colisao(self, indice):
        return self._vet[indice] != ''

    def inserir(self, palavra):
        palavra = self.__normaliza(palavra)        
        indice = self.__calcula_indice(palavra)
        
        if self.__verifica_colisao(indice):
            print('[!!] Colisao ao inserir {}'.format(palavra))
            self._colisoes += 1
            ## garantir que a lista tenha apenas item unicos
            try:
                self._vet[indice].index(palavra)
            except ValueError:
                # se nao esta na lista
                self._vet[indice].append(palavra)
                self._tamanho += 1
        else:            
            self._vet[indice] = [palavra]
            self._tamanho += 1

    def remover(self, palavra):
        palavra = self.__normaliza(palavra)
        indice = self.__calcula_indice(palavra)
        try:
            indice_item = self._vet[indice].index(palavra)
            self._vet[indice].pop(indice_item)
            self._tamanho -= 1
        except ValueError:
            pass
        
    # retorna boolean
    def contem(self, palavra):
        palavra = self.__normaliza(palavra)
        indice = self.__calcula_indice(palavra)
        return True if palavra in self._vet[indice] else False

    # retorna int
    def tamanho(self):
        return self._tamanho

    def palavras(self):
        for item in self._vet:            
            if item != '':
                indice = self._vet.index(item)
                print("[{}] = {}".format(indice, item))

    def total_colisoes(self):
        return self._colisoes
        
conjunto = Conjunto()
conjunto.inserir('andre')
conjunto.inserir('joao')
conjunto.inserir('josiel')
conjunto.inserir('ronaldo')
conjunto.inserir('josiel')
conjunto.inserir('josiel')
conjunto.inserir('josiel')
conjunto.inserir('roberto')
conjunto.inserir('rosa')
conjunto.inserir('eduardo')
conjunto.inserir('edinaldo')
conjunto.palavras()
print('Qtde elementos: {}'.format(conjunto.tamanho()))
print('Total colisões: {}'.format(conjunto.total_colisoes()))