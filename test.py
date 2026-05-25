# Testes simples da classe Queue
# Rodar com:  python test_queue.py

from queue import Queue


# Teste 1 - ordem FIFO (primeiro a entrar, primeiro a sair)
def teste_ordem_fifo():
    pilha = Queue()
    pilha.enqueue(1)
    pilha.enqueue(2)
    pilha.enqueue(3)
    pilha.enqueue(4)
    pilha.enqueue(5)
    pilha.enqueue(6)
    assert pilha.dequeue() == 1
    assert pilha.dequeue() == 2
    assert pilha.dequeue() == 3
    assert pilha.dequeue() == 4
    assert pilha.dequeue() == 5
    assert pilha.dequeue() == 6
print("Teste 1 ok / FIFO")


# Teste 2 - dequeue na pilha vazia deve dar erro
def teste_dequeue_vazia():
    pilha = Queue()
    try:
        pilha.dequeue()
        print("Teste 2 FALHOU")
    except IndexError:
        print("Teste 2 ok / erro na pilha vazia")


# Teste 3 - peek mostra o primeiro mas nao remove
def teste_peek():
    pilha = Queue()
    pilha.enqueue("a")
    pilha.enqueue("b")
    assert pilha.peek() == "a"
    assert pilha.size() == 2
    print("Teste 3 ok / peek (nao remove)")


# Teste 4 - pilha cheia deve dar erro no enqueue
def teste_pilha_cheia():
    pilha = Queue(max_size=2)
    pilha.enqueue(10)
    pilha.enqueue(20)
    assert pilha.is_full() == True
    try:
        pilha.enqueue(30)
        print("Teste 4 FALHOU")
    except OverflowError:
        print("Teste 4 ok / erro na pilha cheia")


# Teste 5 - clear esvazia a pilha
def teste_clear():
    pilha = Queue()
    pilha.enqueue(1)
    pilha.enqueue(2)
    pilha.clear()
    assert pilha.is_empty() == True
    assert pilha.size() == 0
    print("Teste 5 ok / clear (limpa)")


if __name__ == "__main__":
    teste_ordem_fifo()
    teste_dequeue_vazia()
    teste_peek()
    teste_pilha_cheia()
    teste_clear()
    print("Tudo Ok!")
