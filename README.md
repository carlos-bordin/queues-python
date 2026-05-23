# Implementação de uma classe Queue em Python
Este repositório tem com objetivo documentar minha tentativa de criar um algoritmo de Queues implementadas do zero em Python - Atividade proposta pelo prof. Luis Claudio Leite Pereira, na disciplina de Estrutura de Dados.

O código foi desenvolvido sem a utilização de arrays ou collections como parte do desafio.

## Utilização e Métodos

Abaixo estão os exemplos de como utilizar os métodos da classe `Queue`.

#### Criar a fila
Você pode instanciar a fila definindo um limite máximo ou deixá-la sem limite.
```python
# Fila com limite de 4 elementos
lista_pessoas = Queue(4)

# Fila ilimitada
fila_infinita = Queue()
```

#### Adicionar elementos (Enqueue)
Adiciona um novo item ao final da fila. Causa `OverflowError` se a fila estiver cheia.
```python
lista_pessoas.enqueue("Carlos")
lista_pessoas.enqueue("Amanda")
```

#### Remover elementos (Dequeue)
Remove e retorna o primeiro item da fila. Causa `IndexError` se a fila estiver vazia.
```python
removido = lista_pessoas.dequeue()
```

#### Visualizar o primeiro elemento (Peek)
Retorna o valor do primeiro item sem removê-lo da fila. Causa `IndexError` se estiver vazia.
```python
proximo = lista_pessoas.peek()
```

#### Verificadores de Estado
Métodos úteis para checar a situação atual da fila.
```python
tamanho_atual = lista_pessoas.size()      # Retorna a quantidade de itens (int)
esta_vazia = lista_pessoas.is_empty()     # Retorna True ou False
esta_cheia = lista_pessoas.is_full()      # Retorna True ou False
```

#### Limpar a fila (Clear)
Remove todos os elementos e reseta o tamanho da fila.
```python
lista_pessoas.clear()
```


## Roadmap

- Possibilidade de passar uma array de elementos como argumento em `Queue.enqueue([...])`


## Links

[> Link da Atividade no Google Classroom](https://classroom.google.com/c/ODI1MjIzMzA5OTEx/a/ODY1MTUyOTE2OTAy/)

