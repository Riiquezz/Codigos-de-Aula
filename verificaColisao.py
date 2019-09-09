class Conjunto:

    def __init__(self):
        self._vet = []

    def __calcula_indice(self, palavra):
        return ord(palavra.lower()[0]) % 26

    def __normaliza(self, palavra):
        return palavra.lower()

    def __verifica_colisao(self, indice):
        item = self._vet[indice]
        return item != None


    def inserir(self, palavra):
        palavra = self.__normaliza(palavra)
        indice = self.__calcula_indice(palavra)
        if self.__verifica_colisao(indice):
            ## Garantir que a lista tenha apenas item unicos
            if self._vet[indice].index(palavra) == -1:
                self._vet[indice].append(palavra)
            else:
                return
        else:
            self._vet[indice].append([palavra])

    def remover(self, palavra):
        palavra = self.__normaliza(palavra)
        indice = self.__calcula_indice(palavra)
        self._vet.pop(indice)


    # Retorna boolean
    def contem(self, palavra):
        palavra = self.__normaliza(palavra)

    # Retorna int
    def tamanho(self):
        pass