# Avaliacao_Python
Atividade avaliativa de Implementação de uma classe Queue em Python!

Implementei uma fila FIFO em Python.

- queue.py - Classe Queue
- test.py - testes

## Como testar o código ou rodar!
Ter o Python 3 instalado.

Para rodar o teste, abra o terminal na pasta e digitar
```
python test.py
```

Se estiver tudo certo aparece "Todos os testes passaram!".

## Metodos da classe

- dequeue() - tira e retorna o primeiro item
- enqueue(item) - coloca um item no final da fila
- clear() - esvazia a fila
- is_empty() - diz se a fila esta vazia
- is_full() - diz se a fila esta cheia
- size() - quantos itens tem
- peek() - mostra o primeiro item sem tirar

Se tentar tirar de uma fila vazia da erro (IndexError).
Se tentar colocar numa fila cheia da erro (OverflowError).

## Repositorio

Link do GitHub: https://github.com/andrebarbosa-eng/Avaliacao_Python/
