# Autor: Carlos Bordin (20-05-2026, 18:50)
# esse método utiliza listas encadeadas para criar as queues - é mais complexo de implementar, por ser necessário construir uma estrutura mais "amarrada"

class node:
    def __init__(self, value: any, next_node: 'node' | None):
        self.value: any = value
        self.next: 'node' = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next


class queue:
    def __init__(self, max_size=None):
        self.max_size: int = max_size
        self.current_size: int = 0
        self.first: 'node' | None = None
        self.last: 'node' | None = None
    
    def enqueue(self, element):
        if self.current_size == 0:
            self.first = element
        self.last = element
        self.current_size += 1
    
    def dequeue(self):
        self.first = self.first.get_next()
        self.current_size -= 1

    def get_first(self):
        return self.first
    
    def get_last(self):
        return self.last
    
    # def peek(self):
    #     print('x')
    
    # def is_empty(self):
    #     print('x')
    
    # def is_full(self):
    #     print('x')
    
    # def size(self):
    #     print('x')
    
    # def clear(self):
    #     print('x')
        

pessoa_a: str = 'Guilherme Rosa'
pessoa_b: str = 'Amanda Oliveira'
pessoa_c: str = 'Matheus Pfeffer'

exemplo: 'queue' = queue(4)

exemplo.enqueue(pessoa_a)
exemplo.enqueue(pessoa_b)
exemplo.enqueue(pessoa_c)

print(f"Primeiro: {exemplo.get_first()}\nÚltimo: {exemplo.get_last()}")