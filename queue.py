# FIFO = o primeiro que entra e o primeiro que sai

class Queue:

    # Cria a pilha vazia
    # max_size e opcional: 
    #None = pilha sem limite
    def __init__(self, max_size=None):
        self.dados = []          # lista que guarda os itens
        self.max_size = max_size  # limite maximo (ou None)

    # Mostra a pilha quando usamos print()
    def __repr__(self):
        return str(self.dados)

    # Adiciona um item no final da pilha
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("A pilha esta cheia")
        self.dados.append(item)

    # Remove e retorna o primeiro item da pilha
    def dequeue(self):
        if self.is_empty():
            raise IndexError("A pilha esta vazia")
        return self.dados.pop(0)

    # Retorna o primeiro item sem remover
    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha esta vazia")
        return self.dados[0]

    # Retorna True se a pilha estiver vazia
    def is_empty(self):
        return len(self.dados) == 0

    # Retorna True se a pilha estiver cheia
    def is_full(self):
        if self.max_size is None: return False
        return len(self.dados) >= self.max_size

    # Retorna quantos itens tem na pilha
    def size(self):
        return len(self.dados)

    # Limpa a pilha
    def clear(self):
        self.dados = []
