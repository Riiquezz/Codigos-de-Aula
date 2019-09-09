# -- Nodo duplo  + Prioridade --
class Dnodo:
    def __init__(self, dado, prioridade = -1):
        self.dado = dado
        self.prioridade = prioridade
        self.prev = None
        self.next = None

    def __str__(self):
        return ("A prioridade é: " + str(self.prioridade)+ "\n" + "E o dado é: " + str(self.dado)+"\n")

    # Métodos de comparacao do Python, aqui deixamos claros de que forma um objeto Dnodo sera comparado
    def __lt__(self, other):
        return self.prioridade < other.prioridade

    def __le__(self, other):
        return self.prioridade <= other.prioridade

    def __eq__(self, other):
        if other.prioridade is None:
            if self is other:
                return True
            else:
                return False
        if (self.prioridade == other.prioridade):
            return True
        else:
            return False

    def __ne__(self, other):
        if other.prioridade is None:
            if self is not other:
                return True
            else:
                return False
        if (self.prioridade != other.prioridade):
            return True
        else:
            return False

    def __gt__(self, other):
        return self.prioridade > other.prioridade

    def __ge__(self, other):
        return self.prioridade >= other.prioridade


# -- Lista Duplamente Encadeada --
class LDE_Prioridades:
    def __init__(self):
        self.header = Dnodo(None)
        self.trailer = Dnodo(None)
        self.tam = 0

    def vazia(self):
        if self.tam == 0:
            return True

        return False

    def inserir(self, item):
        self.inserirInicio(item)

    #REMOVER O ITEM COM MAIOR PRIORIDADE
    def remover(self):
        maior_item = self.maior()
        self._remover(maior_item)
        return maior_item

    def inserirInicio(self, item):
        if self.vazia():
            item.next = self.trailer
            self.trailer.prev = item

            item.prev = self.header
            self.header.next = item

        else:
            primeiro = self.header.next
            self.header.next = item
            item.prev = self.header
            item.next = primeiro
            primeiro.prev = item

        self.tam += 1

    def inserirFim(self, item):
        if self.vazia():
            item.next = self.trailer
            self.trailer.prev = item

            item.prev = self.header
            self.header.next = item
        else:
            ultimo = self.trailer.prev
            self.trailer.prev = item
            item.next = self.trailer
            item.prev = ultimo
            ultimo.next = item

        self.tam += 1

    def inserirApos(self, alvo, item):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            busca = self.buscar(alvo)
            if(busca.next == self.trailer):
                self.inserirFim(item)
            else:
                atual = busca.next
                busca.next = item
                item.prev = busca
                item.next = atual
                atual.prev = item

            self.tam += 1

    def removerInicio(self):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            removido = self.header.next
            proximo = removido.next
            self.header.next = proximo
            proximo.prev = self.header

            self.tam -= 1
        return removido

    def removerFim(self):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            removido = self.trailer.prev
            penultimo = removido.prev
            penultimo.next = self.trailer
            self.trailer.prev = removido.prev
            self.tam -= 1
        return removido

    def _remover(self, item):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            busca = self.buscar(item)
            if(not busca):
                print("[Valor inexistente]")
                return
            else:
                removido = busca
                if (self.tam == 1):
                    busca.prev = busca.next
                    busca.next.prev = busca.prev.next
                else:
                    if (busca.prev != self.header or busca.next != self.trailer):
                        busca.prev.next = busca.next
                        busca.next.prev = busca.prev
                self.tam -= 1

            return removido

    def substituir(self, item, novoItem):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            busca = self.buscar(item)
            if(not busca):
                print("[Valor inexistente]")
            else:
                busca.dado = novoItem

    def imprimir(self):
        if not self.vazia():
            item = self.header.next

            while item != self.trailer:
                print(item)
                item = item.next

    def buscar(self, alvo):
        if not self.vazia():
            item = self.header.next

            while item != self.trailer:
                if str(alvo) == str(item):
                    return item

                item = item.next
        else:
            print("[Lista Vazia]")
            return

# -- Outras funcoes --
    def menor(self, comeco = None):
        if not comeco:
            comeco = self.header.next;
        else:
            comeco = comeco.next; # começa sempre do proximo item relativo ao cursor

        if not self.vazia():
            item = comeco;
            menor = item;
            while item != self.trailer:
                if item < menor:
                    menor = item;
                item = item.next;
            return menor;

    def maior(self, comeco = None):
        if not comeco:
            comeco = self.header.next;
        else:
            comeco = comeco.next; # começa sempre do proximo item relativo ao cursor

        if not self.vazia():
            item = comeco;
            maior = item;
            while item != self.trailer:
                if item > maior:
                    maior = item;
                item = item.next;
            return maior;

    def selectionSort(self, ordem):
        cursor = self.header.next;
        qt = 0;
        while cursor != self.trailer.prev:
            if qt == 0: # primeira vez
                menor = self.menor(cursor) if ordem =='asc' else self.maior(cursor)
                minimo = self.remover(menor)
                self.inserirInicio(minimo)
            else:
                menor = self.menor(cursor) if ordem =='asc' else self.maior(cursor)
                minimo = self.remover(menor)
                self.inserirApos(cursor, minimo);
                cursor = minimo;
                qt += 1;


fila = LDE_Prioridades()
print("\n")
print("As que você tem, são: ")
print("\n")
fila.inserir(Dnodo("abc", 100))
fila.inserir(Dnodo("ddd", 0))
fila.inserir(Dnodo("fff", 150))
fila.inserir(Dnodo("ggg", 25))
fila.inserir(Dnodo("hhh", 70))
fila.imprimir()
print("\n")
print("As removidas foram: ")
print("\n")
print(fila.remover())
print("\n")
print("As que você ainda tem, são: ")
print("\n")
fila.imprimir()
