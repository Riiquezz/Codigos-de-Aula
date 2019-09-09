# Binary Heap (Classe)
# Implementacao baseada em:
#   https://visualgo.net/en/heap
#   http://btechsmartclass.com/DS/U3_T7.html

class Nodo:
    def __init__(self, dado, prioridade):
        self.dado = dado
        self.prioridade = prioridade

    ## quando item1 < item2
    def __lt__(self, other):
        # implementar comparar prioridade e depois dado
        if self.prioridade == other.prioridade:
            return self.dado > other.dado
        else:
            return self.prioridade < other.prioridade



    ## quando item1 > item2
    def __gt__(self, other):
        # implementar comparar prioridade e depois dado
        if self.prioridade == other.prioridade:
            return self.dado < other.dado
        else:
            return self.prioridade > other.prioridade

    def __str__(self):
        return str(self.dado)

    def __repr__(self):
        return str(self.dado) + "(" + str(self.prioridade) + ")"

class BinaryHeap:
    def __init__(self):
        self._vet = []
        self._size = 0

    def __str__(self):
        return "{}".format(self._vet)

    def _swap(self, item_index1, item_index2):
        aux = self._vet[item_index1]
        self._vet[item_index1] = self._vet[item_index2]
        self._vet[item_index2] = aux

        # retorna o novo indice do ultimo item inserido
        return item_index2

    def _parent_index(self, item_index):
        return int(item_index/2)

    def _parent_value(self, item_index):
        parent_value = self._vet[self._parent_index(item_index)]
        return parent_value if parent_value is not None else None

    def _left_child_tuple(self, item_index):
        if 2*item_index >= self._size:
            return None

        # filho esquerda
        left_child = self._vet[2*item_index]

        return (2*item_index, left_child)

    def _right_child_tuple(self, item_index):
        if 2*item_index+1 >= self._size:
            return None

        # filho direita
        right_child = self._vet[2*item_index+1]
        return (2*item_index+1, right_child)

    def _after_delete(self, i):
        if self._left_child_tuple(i) is not None:
            left_child_index = self._left_child_tuple(i)[0]
            left_child_value = self._left_child_tuple(i)[1]

            if self._vet[i] < left_child_value:
                if left_child_index+1 < self._size:
                    right_sibling_value = self._vet[left_child_index+1]
                    if left_child_value > right_sibling_value:
                        # troca
                        self._swap(i, left_child_index)
                        # repete processo
                        self._after_delete(left_child_index)
                    else:
                        # troca
                        self._swap(i, left_child_index+1)
                        # repete processo
                        self._after_delete(left_child_index+1)
            else:
                if self._right_child_tuple(i) is not None:
                    right_child_index = self._right_child_tuple(i)[0]
                    right_child_value = self._right_child_tuple(i)[1]
                    if self._vet[i] < right_child_value:
                        # troca
                        self._swap(i, right_child_index)
                        # repete processo
                        self._after_delete(right_child_index)
                else:
                    # quando atinge a condicao de parada
                    # parar o processo
                    return

    def put(self, item):
        if self._size == 0:
            self._vet.append(None)
            self._vet.append(item)
            self._size = 2
        else:
            # insere novo item no final da lista
            self._vet.append(item)
            self._size += 1

            item_index = self._size - 1

            while self._parent_value(item_index) != None and self._parent_value(item_index).__lt__(item):
                item_index = self._swap(item_index, self._parent_index(item_index))


            # implementar insercao
            # enquanto existir valor de raiz e este valor for menor que o item a ser inserido
            # efetuar a troca dos itens

    def get(self):
        # obtem o elemento raiz
        root = self._vet[1]

        # muda raiz para o ultimo item na lista
        self._vet[1] = self._vet.pop()
        self._size -= 1

        # reorganiza os elementos
        self._after_delete(1)

        return root

## TESTES
valores = [Nodo(1, 0), Nodo(2, 0), Nodo(3, 0), Nodo(4, 1), Nodo(5, 1)]

heap = BinaryHeap()
for item in valores:
    heap.put(item)
print("Fila: ")
print(heap)

# retorna o primeiro da fila
print("\nPróxima senha é: ")
print(heap.get())
print("\n")


senhacomum = 0
senhapriorit = 0
senha = 0
vetorcham = []
vetam = []

while(True):
    print("--------Console------_"
    "\n1 - Senha prioritária "
    "\n2 - Senha normal"
    "\n3 - Chamar senha"
    "\n4 - Últimas senhas"
    "\n5 - Sair")
    print("\n"
          "")

    senha = (input("Opção: "))

    if senha == "1":
        senhapriorit +=1
        print("Senha é " + str(senhapriorit) + " com prioridade alta")
        print("\n")
        item = Nodo(senhapriorit, 1)
        heap.put(item)

    elif senha == "2":
        senhacomum +=1
        print("Senha é: " + str(senhacomum) + " com prioridade comum")
        item = Nodo(senhacomum, 0)
        heap.put(item)

    elif senha == "3":
        item = heap.get()
        try:
            print("Senha chamada: " + str(item) + " e a prioridade é: " + str(item.prioridade))
            vetorcham.append(item)
            vetam += 1
            if vetam > 5:
                vetorcham.pop(0)
                vetam -= 1
                print(vetorcham)
            else:
                print(vetorcham)
        except:
            print("Não tem valor")

    elif senha == "4":
        if len(vetorcham) is 6:
            vetorcham.pop(0)
        for x in vetorcham:
            print(x)


    elif senha == "5":
        break
