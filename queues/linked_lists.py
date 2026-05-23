# Autor: Carlos Bordin (20-05-2026, 18:50)
# esse método utiliza listas encadeadas para criar as queues - é mais complexo de implementar, por ser necessário construir uma estrutura mais "amarrada"

class Node:
    """Instancia uma Node. (Uso interno da classe Queue)"""
    def __init__(self, value):
        self.value = value
        self._next_node = None

class Queue:
    """Instancia a Queue com um limite opcional de elementos (ou Nodes)"""
    def __init__(self, max_size=None):
        self._max_size = max_size
        self._current_size = 0
        self._first = None
        self._last = None
    
    def enqueue(self, element):
        """Instancia uma nova Node e a adiciona ao final da Queue. Se a Queue estiver no limite de elementos, causa um OverflowError."""
        if self._current_size == self._max_size: raise OverflowError(f"Elemento '{element}' não foi adicionado à Queue - Limite de elementos atigindo ({self._max_size}).")

        corresponding_node = Node(element)

        if self._current_size == 0:
            self._first = corresponding_node
            self._last = corresponding_node
        else:
            self._last._next_node = corresponding_node
            self._last = corresponding_node
            
        self._current_size += 1

    def dequeue(self):
        """Remove a primeira Node da lista e retorna o valor armazenado. Se a Queue já estiver vazia, causa um IndexError."""
        if self._current_size == 0 : raise IndexError("A queue já está vazia, nenhuma node foi removida")

        removal_target = self._first.value
        self._first = self._first._next_node
        self._current_size -= 1

        if self._current_size == 0:
            self._last = None

        return removal_target
    
    def peek(self):
        """Retorna o valor da primeira Node da Queue sem remove-la. Se a Queue estiver vazia, causa uma Exception."""
        if self._current_size == 0: raise IndexError("A queue está vazia, nenhum elemento foi retornado")
        return self._first.value
    
    def is_empty(self):
        """Retorna True se a Queue estiver vazia, Retorna False se a Queue tiver 1 ou mais Nodes."""
        return self._current_size == 0
    
    def is_full(self):
        """Retorna True se a Queue estiver no limite de Nodes. Senão, retorna False"""
        return self._current_size == self._max_size
    
    def size(self):
        """Retorna o tamanho da Queue em int."""
        return self._current_size
    
    def clear(self):
        """Limpa a Queue."""
        self._first = None
        self._last = None
        self._current_size = 0
    
    def __repr__(self):
        """Retorna uma string formatada do tamanho da Queue, e os valores de cada Node em sequência"""
        if self._current_size == 0: return "A Queue está vazia."
        msg = f"Queue ({self._current_size}):\n"
        node_to_visit = self._first

        for i in range(self._current_size):
            msg += f"{node_to_visit.value}\n"
            node_to_visit = node_to_visit._next_node

        return msg



if __name__ == "__main__":
    pessoa_a: str = 'Guilherme Rosa'
    pessoa_b: str = 'Amanda Oliveira'
    pessoa_c: str = 'Matheus Pfeffer'
    pessoa_d: str = 'Carlos Bordin'
    pessoa_e: str = 'Luis Claudio'
    pessoa_f: str = 'Leandro Bona'

    # instancia a Queue, tamanho máximo de 4 Nodes
    exemplo = Queue(4)

    # valida se a Queue está vazia
    print(f"A Queue está vazia?: {exemplo.is_empty()}")

    # tenta remover um elemento da Queue vazia
    try:
        exemplo.dequeue()
    except IndexError as erro_capturado:
        print(f"Erro: {erro_capturado}")

    # adiciona 4 elementos novos
    exemplo.enqueue(pessoa_a)
    exemplo.enqueue(pessoa_b)
    exemplo.enqueue(pessoa_c)
    exemplo.enqueue(pessoa_d)

    # tenta adicionar um quinto elemento, mas causa erro de overflow.
    try:
        exemplo.enqueue(pessoa_e)
    except OverflowError as erro_capturado:
        print(f"Erro: {erro_capturado}")

    # valida se a Queue está cheia
    print(f"A Queue está cheia?: {exemplo.is_full()}")

    # remove dois elementos da lista encadeada, e adiciona mais dois em seguida.
    exemplo.dequeue()
    exemplo.dequeue()
    exemplo.enqueue(pessoa_e)
    exemplo.enqueue(pessoa_f)

    # traz o VALOR do primeiro elemento da Queue, e o tamanho da Queue
    print(f"Valor do primeiro Node: {exemplo.peek()}")
    print(f"Tamanho atual da lista: {exemplo.size()}")

    # mostra a Queue (__repr__)
    print(exemplo)

    # limpa a queue inteira
    exemplo.clear()

    # mostra a Queue (__repr__), mas agora está vazia
    print(exemplo)